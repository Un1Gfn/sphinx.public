.. include:: include/substitution.txt

============
postmarketOS
============

.. math::

   \mathit{The\ best\ way\ to\ predict\ the\ future\ is\ to\ invent\ it.} - \href{https://www.ted.com/speakers/alan_kay}{\text{Alan Kay}}

| qdl edl firehorse msm8916 postmarketos
| qualcomm boot chain
  |vv| `lineage <https://lineageos.org/engineering/Qualcomm-Firmware/>`__ 
  |vv| `quarkslab <https://blog.quarkslab.com/analysis-of-qualcomm-secure-boot-chains.html>`__
  |vv| `timesys <https://www.timesys.com/security/secure-boot-snapdragon-410/>`__
| `Download Patched Firehose File for 600+ Android Devices <https://www.droidwin.com/patched-firehose-file/>`__
| `andersson/qdl <https://github.com/andersson/qdl>`__
| `bkerler/Loaders <https://github.com/bkerler/Loaders>`__
| `bkerler/edl <https://github.com/bkerler/edl>`__
| `OneLabsTools/Programmers <https://github.com/OneLabsTools/Programmers/>`__
| `list of MSM8916 devices <https://wiki.postmarketos.org/wiki/Qualcomm_Snapdragon_410/412_(MSM8916)>`__
| `vanilla unsigned db410c edl payload <https://matrix.to/#/!zpvMifoucHSiUsVFgl:postmarketos.org/$2r0b_U-yVEidj-uQndqm3fWQ-i0hqMVGBsNMZ87iRyY?via=matrix.org&via=kde.org&via=tchncs.de>`__
| caveat - `they "forgot" to enable secure-boot <https://matrix.to/#/!zpvMifoucHSiUsVFgl:postmarketos.org/$48I-w09LH54XYFviXAzxeYS8xa33foG63GCpa7U_P44?via=matrix.org&via=kde.org&via=tchncs.de>`__
| caveat - short circuit force kick edl test point
| :file:`~/pmos/`
| `redmi2(1/8) redmi2(2/16) redmi2pro(2/16) redmi2prime(2/16) <https://en.wikipedia.org/wiki/Redmi#Redmi_Series>`__
| `<https://wiki.postmarketos.org/wiki/The-big-list-of-who-has-what-device>`__
| msm8916 being the only one with mainline modem
  - `qualcomm <https://wiki.postmarketos.org/wiki/Qualcomm_mainline_porting>`__
  - `all <https://wiki.postmarketos.org/wiki/Mainlining#Supported_SoCs>`__
| :wp:`qualcomm cpu-soc chart <list of Qualcomm Snapdragon processors>`
| :wp:`qualcomm codecs <Qualcomm Hexagon#Hardware_codec_supported>`


EDL/QDL/9008
============

| screws
| ``+`` CR-V + 1.0
| *total: 12*

::

   (hymen ;P)
        |
        v
        +                   +
               CAMERA        
        +             +     +
                             
        +                    
              +           +  
                             
                             
        +                   +
                             
                             
        +                   +

::

   +------------+
   | o          |
   |        o   |
   |            |
   |   o    o   |
   |            |
   +------------+
         o [O] [O]
            ^   ^
            |   |
            +----- QDL test points

1. |:warning:|\ |:zap:| :kbd:`keep tweezer safe & insulated`
#. poweroff, unplug, remove battery, teardown |:warning:|\ |:zap:| :kbd:`keep battery safe & insulated, away from tweezer`
#. put phone to a tilted position with the microUSB side higher than the audioJACK side
#. SSH into a remote PC and execute [|alpha|]
#. connect microUSB port to the remote PC
#. grab the battery with your L hand
#. begin shorting test points with a tweezer and your R hand |:warning:|\ |:zap:| :kbd:`make no contact with anything other than the test points`
#. attach battery with your L hand
#. observe ``05c6:9008 Qualcomm, Inc. Gobi Wireless Modem (QDL mode)`` in SSH
#. wait for 10 seconds
#. lift tweezer |:warning:|\ |:zap:| :kbd:`keep tweezer safe & insulated`
#. keep clear from the remote PC

[|alpha|] ::

   function L_qualcomm {
      P=('|  '
         ' \ '
         '  |'
         ' / ')
      N="${#P[@]}"
      for ((i=0;1;i++)); do
         sleep 0.3
         echo "${P[i%N]} $(lsusb | grep -v \
            -e 1d6b:0003 \
            -e 05c8:0383 \
            -e 138a:003f \
            -e 8087:0a2b \
            -e 1d6b:0002 \
         )"
      done
   }


Boot Modes
==========

.. warning::

   | 1\. Operate at 30%+ battery
   | 2\. |:warning:| **To prevent bootloop, unplug cable before any of the following**
   |    |b| any mode -> any mode (reboot)
   |    |b| S0 -> any mode (poweron)
   |    |b| any mode -> S0 (poweroff)

| :menuselection:`Settings --> About phone --> MIUI version (tap 7 times) --> show developer options`
| :menuselection:`Settings --> Additional settings --> Developer options --> USB debugging (enable)`
| :menuselection:`Settings --> Additional settings --> Developer options --> Fastboot mode (enable)`

| android system, adb not enabled
|    ``2717:ff60 Xiaomi Inc. redmi prime 2``
| android system, adb enabled
|    ``2717:ff68 Xiaomi Inc. Mi-4c``
|    ``676c67a1 device`` :sub:`$ adb devices`
| adb reboot recovery / |beta| |rarr| [recovery]
|    ``18d1:d001 Google Inc. Nexus 4 (fastboot)`` |:warning:| misleading - this is not fastboot
|    ``676c67a1 unauthorized`` :sub:`$ adb devices`
| unplug, :guilabel:`VolUp`\ +\ :guilabel:`PWR` (|beta|)
|    ``05c6:9091 Qualcomm, Inc. Intex Aqua Fish & Jolla C Diagnostic Mode``
|    ``0123456789 device`` :sub:`$ adb devices`
| unplug, :guilabel:`VolDown`\ +\ :guilabel:`PWR`
|    ``18d1:d00d Google Inc. Xiaomi Mi/Redmi 2 (fastboot)``
|    ``676c67a1 fastboot`` :sub:`# fastboot devices`
|  / |beta| |rarr| [Download]
|    ``05c6:9008 Qualcomm, Inc. Gobi Wireless Modem (QDL mode)``
     |:japanese_goblin:|
     |:japanese_ogre:|
     |:skull:|
     |:smiling_imp:|
     |:space_invader:|


Device Info
===========

| adb shell - busybox uname -a
|    ``Linux localhost 3.10.28-gff13db4 #1 SMP PREEMPT Thu Nov 16 00:53:24 CST 2017 armv7l GNU/Linux``

:menuselection:`Settings --> About phone --> Kernel version (tap 5 times) --> CIT --> SW add HW version`

.. table::
   :align: left
   :widths: auto

   ================== ============================
    software version   SW_S88047A1_V061_M22_MP_XM
    hardware version   M22
    PCBA SN            2W60 3W23 0920
    Phone SN           1122 5406 6336 9
    IMEI(1)            8676 2202 8276 650
    IMEI(2)            8676 2202 8276 650
   ================== ============================

:menuselection:`Settings --> About phone --> Kernel version (tap 5 times) --> CIT --> Device View`

.. table::
   :align: left
   :widths: auto

   ================ ===============================
    LCD              otm1285a_otp_720p_video_DEBUG
    TP               Shchao,FT5336,0x7
    Main Camera      ov8865_q8v18a
    Main Camera ID   shunyu
    Sub Camera       ov2680_skuhf
    Battery          10 Sunwoda(2200)
   ================ ===============================

:menuselection:`usb 05c6:9091 --> PCBA Test --> SYSTEM INFO`

.. table::
   :align: left
   :widths: auto

   =========== =======================================================
    SW Ver      SW_S88047 |br| A1_V061_M22_MP_XM
    MIUI Ver    7.11.16
    Modem Ver   MPSS.DPM. |br| 1.0.c7.18-00023-M8916EAAAANUZM-1-all16
    IMEI:       867622028276650
    IMEI2:      867622028276650
    SN:         2W603W230920
    Phone SN    1122540663369
    BoardID     S88047A1
   =========== =======================================================

:menuselection:`usb 05c6:9091 --> Hardware Info`

.. table::
   :align: left
   :widths: auto

   =================== ==============================
    Flash               TYE0HH221657RA-Toshiba
    LCD                 otm1285a_otp_720p_video_EBBG
    TP                  Shchao,FT5336,0x7
    Camera_Main         ov8865_q8v18a
    Camera_Main_modID   shunyu
    Camera_Sub          ov2680_skuhf
    Accleerometer       mpu6881
    Alsps               ltr553
    Gyrocsop            mpu6881
    Magnetometer        yas537
    WIFI                Qualcomm-msm8916
    BT                  Qualcomm-msm8916
    FM                  Qualcomm-msm8916
    GPS                 Qualcomm-msm8916
    Battery             10 Sunwoda(2200)
    Board ID            S88047A1
    gsersor cali
    psensor cali
    gyro sensor cali
   =================== ==============================

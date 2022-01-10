.. include:: include/substitution.txt
.. highlight:: text

============
postmarketOS
============

.. math::

   \mathit{The\ best\ way\ to\ predict\ the\ future\ is\ to\ invent\ it.} - \href{https://www.ted.com/speakers/alan_kay}{\text{Alan Kay}}

.. note:: Todo

   | inspect mountpoint of each partition in both recovery and system
   |    adb shell busybox cat /proc/mounts


Misc
====

blobs at ``~/pmos``

| pmOS wiki
|    `User:Un1Gfn <https://wiki.postmarketos.org/wiki/User:Un1Gfn>`__
|    `wt88047 <https://wiki.postmarketos.org/wiki/Xiaomi_Redmi_2_(xiaomi-wt88047)>`__
|    `MSM8916 <https://wiki.postmarketos.org/wiki/Qualcomm_Snapdragon_410/412_(MSM8916)>`__

| :abbr:`PBL (Primary Boot Loader, in SoC ROM)` in Qualcomm :abbr:`MSM (Mobile Station Modem)` implements :abbr:`EDL (Emergency Download Mode)` mode
| EDL mode implements the Qualcomm Sahara Protocol
| Sahara Protocol accepts an OEM-digitally-signed programmer (\*.mbn file) over USB
| the programmer implements Firehose Protocol
| host PC sends commands over Firehose Protocol to write into the onboard storage (eMMC, UFS)

qualcomm/`Secure Boot and Image Authentication <https://www.qualcomm.com/media/documents/files/secure-boot-and-image-authentication-technical-overview-v2-0.pdf>`__
lineage/`Qualcomm’s Chain of Trust <https://lineageos.org/engineering/Qualcomm-Firmware/>`__
quarkslab/`Analysis of Qualcomm Secure Boot Chains <https://blog.quarkslab.com/analysis-of-qualcomm-secure-boot-chains.html>`__


QDL
Sahara/fireho(r)se sahadra msm8916 postmarketos

| alephsecurity/`firehorse <https://github.com/alephsecurity/firehorse>`__
| qualcomm boot chain
  |vv| `lineage <https://lineageos.org/engineering/Qualcomm-Firmware/>`__ 
  |vv| `quarkslab <https://blog.quarkslab.com/analysis-of-qualcomm-secure-boot-chains.html>`__
  |vv| `timesys <https://www.timesys.com/security/secure-boot-snapdragon-410/>`__
| `Download Patched Firehose File for 600+ Android Devices <https://www.droidwin.com/patched-firehose-file/>`__
| `andersson/qdl <https://github.com/andersson/qdl>`__
| `bkerler/Loaders <https://github.com/bkerler/Loaders>`__
| `bkerler/edl <https://github.com/bkerler/edl>`__
| `OneLabsTools/Programmers <https://github.com/OneLabsTools/Programmers/>`__
| :mt:`vanilla unsigned db410c edl payload <#main:postmarketos.org/$2r0b_U-yVEidj-uQndqm3fWQ-i0hqMVGBsNMZ87iRyY>`
|    `linux-board-support-package-r1034.2.1.zip <https://releases.linaro.org/96boards/dragonboard410c/qualcomm/firmware/linux-board-support-package-r1034.2.1.zip>`__//linux-board-support-package-r1034.2.1/loaders/prog_emmc_firehose_8916.mbn
|    sha1 9fbfc85368a3def9b936a17662d848b4769dc131
| caveat - :mt:`they "forgot" to enable secure-boot <#main:postmarketos.org/$lIMqnR5BXu8zjQKhJhwvK44VFGuPLtSYihjYsATfOsc>`
| caveat - short circuit force kick edl test point
| :file:`~/pmos/`
| `redmi2(1/8) redmi2(2/16) redmi2pro(2/16) redmi2prime(2/16) <https://en.wikipedia.org/wiki/Redmi#Redmi_Series>`__
| `<https://wiki.postmarketos.org/wiki/The-big-list-of-who-has-what-device>`__
| msm8916 being the only one with mainline modem
  - `qualcomm <https://wiki.postmarketos.org/wiki/Qualcomm_mainline_porting>`__
  - `all <https://wiki.postmarketos.org/wiki/Mainlining#Supported_SoCs>`__
| :wp:`qualcomm cpu-soc chart <list of Qualcomm Snapdragon processors>`
| :wp:`qualcomm codecs <Qualcomm Hexagon#Hardware_codec_supported>`

Contacts
========

| main:postmarketos.org
|    travmurav
|    minecrell


EDL/QDL
=======

| screws
| ``+`` CR-V + 1.0
| *total: 12*

::

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
#. SSH into a remote PC and execute /home/darren/pmos/lsusb.sh
#. connect microUSB port to the remote PC
#. grab the battery with your L hand
#. begin shorting test points with a tweezer and your R hand |:warning:|\ |:zap:| :kbd:`make no contact with anything other than the test points`
#. attach battery with your L hand
#. observe ``05c6:9008 Qualcomm, Inc. Gobi Wireless Modem (QDL mode)`` in SSH
#. wait for 10 seconds
#. lift tweezer |:warning:|\ |:zap:| :kbd:`keep tweezer safe & insulated`
#. keep clear from the remote PC


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
| unplug, :guilabel:`VolUp`\ +\ :guilabel:`VolDown`\ +\ :guilabel:`PWR` / adb reboot recovery / |beta| |rarr| [recovery]
|    ``18d1:d001 Google Inc. Nexus 4 (fastboot)`` |:warning:| misleading - this is not fastboot
|    ``676c67a1 unauthorized`` :sub:`$ adb devices`
| unplug, :guilabel:`VolUp`\ +\ :guilabel:`PWR` (|beta|)
|    ``05c6:9091 Qualcomm, Inc. Intex Aqua Fish & Jolla C Diagnostic Mode``
|    ``0123456789 device`` :sub:`$ adb devices`
| unplug, :guilabel:`VolDown`\ +\ :guilabel:`PWR`
|    ``18d1:d00d Google Inc. Xiaomi Mi/Redmi 2 (fastboot)``
|    ``676c67a1 fastboot`` :sub:`# fastboot devices`
| tweezer / |beta| |rarr| [Download]
|    ``05c6:9008 Qualcomm, Inc. Gobi Wireless Modem (QDL mode)``
     |:japanese_goblin:|
     |:japanese_ogre:|
     |:skull:|
     |:smiling_imp:|
     |:space_invader:|


Spec/Device Info
================

system.bin//`build.prop <https://pocketnow.com/build-prop-tweaks>`__ ::

   ?

| adb shell - busybox uname -a
|    ``Linux localhost 3.10.28-gff13db4 #1 SMP PREEMPT Thu Nov 16 00:53:24 CST 2017 armv7l GNU/Linux``

fastbot getvar

:menuselection:`Settings --> About phone`

.. table::
   :align: left
   :widths: auto

   ============================== =================================================
    Device name                    Redmi
    Model number                   2014811
    Android version                4.4.4 KTU84P
    Android security patch level   2016-10-01
    MIUI version                   MIUI 9.7.11.16 | Beta
    CPU                            Quad-core Max 1.2 GHz
    RAM                            2.00GB
    Internal storage               11.75GB available 16.00 GB total
    Baseband version               MPSS.DPM.1.0.c7.18-00023-M8916EAAAANUZM-1-all16
    Kernel version                 3.10.28-gff13db4
   ============================== =================================================

:menuselection:`Settings --> About phone --> Status`

.. table::
   :align: left
   :widths: auto

   =================== ========================
    IMEI                8676220282766650
    IMEI SV             08
    WLAN MAC address    20\:82\:c0\:c6\:de\:cb
    Bluetooth address   20\:82\:C0\:C6\:DE\:CA
    Serial number       676c67a1
   =================== ========================

:menuselection:`Settings --> About phone --> Kernel version (tap 5 times) --> CIT --> SW add HW version`

.. table::
   :align: left
   :widths: auto

   ================== ============================
    software version   SW_S88047A1_V061_M22_MP_XM
    hardware version   M22
    PCBA SN            2W603W230920
    Phone SN           1122540663369
    IMEI(1)            867622028276650
    IMEI(2)            867622028276650
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

| :command:`edl printgpt`
| AOSP doc - `partitions <https://source.android.com/devices/bootloader/partitions>`__
| *total: 30*

:raw-html:`<details open><summary>short a-z</summary>`

::

   aboot
   abootbak
   boot
   cache
   config
   DDR
   fsc
   fsg
   hyp
   hypbak
   keystore
   misc
   modem
   modemst1
   modemst2
   oem
   pad
   persist
   recovery
   rpm
   rpmbak
   sbl1
   sbl1bak
   sec
   splash
   ssd
   system
   tz
   tzbak
   userdata

:raw-html:`</details>`

:raw-html:`<details><summary>full</summary>`

::

   Qualcomm Sahara / Firehose Client V3.53 (c) B.Kerler 2018-2021.
   main - Trying with no loader given ...
   main - Waiting for the device
   main - Device detected :)
   main - Mode detected: firehose
   firehose_client
   firehose_client - [LIB]: No --memory option set, we assume "eMMC" as default ..., if it fails, try using "--memory" with "UFS","NAND" or "spinor" instead !
   firehose - TargetName=MSM8916
   firehose - MemoryName=eMMC
   firehose - Version=1
   firehose_client - Supported functions:
   -----------------

   Parsing Lun 0:

   GPT Table:
   -------------
   modem:               Offset 0x0000000004000000, Length 0x0000000004000000, Flags 0x1000000000000000, UUID 0198b9fe-60eb-e7fa-bd89-d65fb5fa3952, Type EFI_BASIC_DATA
   sbl1:                Offset 0x0000000008000000, Length 0x0000000000080000, Flags         0x00000000, UUID 1c2d2a12-bf4a-366b-8022-212a77c2e65f, Type 0xdea0ba2c
   sbl1bak:             Offset 0x0000000008080000, Length 0x0000000000080000, Flags         0x00000000, UUID 37011c91-6d94-e9b7-8382-6fd5543c1019, Type EFI_BASIC_DATA
   aboot:               Offset 0x0000000008100000, Length 0x0000000000100000, Flags         0x00000000, UUID 349f9d39-ce88-5ed8-0019-9eca6a759b1b, Type 0x400ffdcd
   abootbak:            Offset 0x0000000008200000, Length 0x0000000000100000, Flags         0x00000000, UUID b2e21aed-6e86-0d2e-5865-1e3e3a34a32f, Type EFI_BASIC_DATA
   rpm:                 Offset 0x0000000008300000, Length 0x0000000000080000, Flags         0x00000000, UUID e6e2b0b2-5aba-3a1b-0b63-bb57c54ff292, Type 0x98df793
   rpmbak:              Offset 0x0000000008380000, Length 0x0000000000080000, Flags         0x00000000, UUID 880efbd1-c626-115f-c2f2-c694659f5a2e, Type EFI_BASIC_DATA
   tz:                  Offset 0x0000000008400000, Length 0x0000000000080000, Flags         0x00000000, UUID e16cfecd-0dda-8a7e-dc63-b8a2935b7209, Type 0xa053aa7f
   tzbak:               Offset 0x0000000008480000, Length 0x0000000000080000, Flags         0x00000000, UUID 83fc0ab6-bad0-1e9b-f141-134b059305d8, Type EFI_BASIC_DATA
   hyp:                 Offset 0x0000000008500000, Length 0x0000000000080000, Flags         0x00000000, UUID 34ffcdbd-9741-eb71-4c43-cdccd0a32263, Type 0xe1a6a689
   hypbak:              Offset 0x0000000008580000, Length 0x0000000000080000, Flags         0x00000000, UUID 86981a8c-6223-a3ec-ee79-65ebf71e6283, Type EFI_BASIC_DATA
   pad:                 Offset 0x0000000008600000, Length 0x0000000000100000, Flags         0x00000000, UUID 369ac60c-78ed-0171-6fac-de32fc135fe9, Type EFI_BASIC_DATA
   modemst1:            Offset 0x0000000008700000, Length 0x0000000000180000, Flags         0x00000000, UUID 38937cf1-ded8-184f-ee1b-3e39243e9343, Type 0xebbeadaf
   modemst2:            Offset 0x0000000008880000, Length 0x0000000000180000, Flags         0x00000000, UUID 6f99e571-3e80-e29a-1629-4c8f2d0b6fa2, Type 0xa288b1f
   misc:                Offset 0x0000000008a00000, Length 0x0000000000100000, Flags         0x00000000, UUID 08240ee5-a91d-25bd-91a0-7b1e671a981e, Type 0x20117f86
   fsc:                 Offset 0x0000000008b00000, Length 0x0000000000000400, Flags         0x00000000, UUID a0e0e088-8660-6090-b480-5ad85476e3b9, Type 0x57b90a16
   ssd:                 Offset 0x0000000008b00400, Length 0x0000000000002000, Flags         0x00000000, UUID ad4fe898-d886-7b78-6482-709419c2e5f1, Type 0x2c86e742
   splash:              Offset 0x0000000008b02400, Length 0x0000000000a00000, Flags         0x00000000, UUID 618366ad-7ebb-b23e-d156-5b8d1145cbf2, Type 0x20117f86
   DDR:                 Offset 0x000000000c000000, Length 0x0000000000008000, Flags 0x1000000000000000, UUID 55b9b2f2-7e53-09d2-cfe4-1bf89b5f2de1, Type 0x20a0c19c
   fsg:                 Offset 0x000000000c008000, Length 0x0000000000180000, Flags 0x1000000000000000, UUID bf6ae34e-6657-ae3d-ab8b-263133e07714, Type 0x638ff8e2
   sec:                 Offset 0x000000000c188000, Length 0x0000000000004000, Flags 0x1000000000000000, UUID 685601a2-b7b2-a249-7212-06d883c0c434, Type 0x303e6ac3
   boot:                Offset 0x000000000c18c000, Length 0x0000000002000000, Flags 0x1000000000000000, UUID 94459b6e-b964-7fbf-ead5-c69d9c4a84d3, Type 0x20117f86
   system:              Offset 0x000000000e18c000, Length 0x0000000040000000, Flags 0x1000000000000000, UUID 6a983232-087b-72fb-c073-b1209e7082c0, Type EFI_BASIC_DATA
   cache:               Offset 0x000000004e18c000, Length 0x0000000014000000, Flags 0x1000000000000000, UUID 99bf6a49-b5c2-9cd3-37ce-f1570e24aa9a, Type EFI_BASIC_DATA
   persist:             Offset 0x000000006218c000, Length 0x0000000002000000, Flags 0x1000000000000000, UUID 9a88e4d7-1fae-ef99-c66c-4471908c423d, Type EFI_BASIC_DATA
   recovery:            Offset 0x000000006418c000, Length 0x0000000002000000, Flags 0x1000000000000000, UUID a76ecf95-9dc4-656a-9970-19c11a44c11a, Type 0x20117f86
   keystore:            Offset 0x0000000068000000, Length 0x0000000000080000, Flags         0x00000000, UUID 823da879-cdc1-4c6e-891d-873377e59190, Type 0xde7d4029
   config:              Offset 0x0000000068080000, Length 0x0000000000008000, Flags         0x00000000, UUID 8abadafa-7588-ad86-d829-b4f50756b6b6, Type 0x91b72d4d
   oem:                 Offset 0x0000000068088000, Length 0x0000000004000000, Flags         0x00000000, UUID f31e8f71-eef7-240f-c2f4-0389c205a45e, Type 0x7db6ac55
   userdata:            Offset 0x0000000070000000, Length 0x000000033b3fbe00, Flags 0x1000000000000000, UUID 521979fe-1576-040b-34e8-b438c3c066e0, Type EFI_BASIC_DATA

   Total disk size:0x00000003ab400000, sectors:0x0000000001d5a000

:raw-html:`</details>`


Backup
======

.. include:: include/escalate.txt

.. highlight:: bash

execute **step by step** ::

   mkdir -pv /home/darren/pmos/bak{1,2}

   # cd /home/darren/pmos/bak1
   cd /home/darren/pmos/bak2 && {

      # /home/darren/pmos/prog_emmc_firehose_8916.mbn

      exa -alT

      alias EDL='edl --loader=/home/darren/pmos/prog_emmc_firehose_8916.mbn --memory=eMMC'

      # send programmer (*.mbn)
      EDL
      # Terminate with ^C when the following message appears - "Done |---| 0.0% Read (Sector 0x0 of 0x2) 0.00 MB/s"

      # inspect
      # EDL getstorageinfo # firehose - [LIB]: GetStorageInfo command isn't supported.
      edl secureboot
      EDL printgpt

      # small
      # EDL pbl pbl.img # IndexError: list index out of range
      edl qfp qfp.img
      mkdir gpt; EDL gpt gpt/ --genxml

      # large
      mkdir rl; EDL rl rl/ --skip=userdata --genxml # userdata isn't skipped

      # large
      EDL rf flash.bin

   }

.. note::

   | 1\. Reboot PC
   | 2\. Download 410c mbn programmer
   | 3\. Backup again with 410c programmer to :kbd:`/home/darren/pmos/bak2`
   | 4\. Compare

::

   # make accessible
   sudo chown -Rv darren:darren /home/darren/pmos

   # verify each dump
   diff -u <(cd /home/darren/pmos/bak1; tree -aC) <(cd /home/darren/pmos/bak2; tree -aC)
   # cd /home/darren/pmos/bak1; find . -type f \( -not -name "sha1sum.txt" \) -exec sha1sum {} \; | tee -a sha1sum.txt; echo
   # cd /home/darren/pmos/bak2; find . -type f \( -not -name "sha1sum.txt" \) -exec sha1sum {} \; | tee -a sha1sum.txt; echo
   cd /home/darren/pmos/bak1; sha1sum -c sha1sum.txt --strict -w; echo
   cd /home/darren/pmos/bak2; sha1sum -c sha1sum.txt --strict -w; echo

   # difference between two dumps
   diff -u /home/darren/pmos/bak{1,2}/sha1sum.txt

   # file type
   cd /home/darren/pmos/bak1
   file * | sort -t: -k2 | less -RM +F # -S

   # android boot img
   # unpack_bootimg --boot_img /home/darren/pmos/bak1/rl/boot.bin --out OUT --format info
   # boot.bin:        Android bootimg, kernel, ramdisk, page size: 2048, cmdline (ramoops_memreserve=2M androidboot.hardware=qcom user_debug=31 msm_rtb.filter=0x3F ehci-hcd.park=3 androidboot.bootdevice=782490)
   # recovery.bin:    Android bootimg, kernel, ramdisk, page size: 2048, cmdline (ramoops_memreserve=2M androidboot.hardware=qcom user_debug=31 msm_rtb.filter=0x3F ehci-hcd.park=3 androidboot.bootdevice=782490)

   # interactively inspect fs image
   # sudo mount -v -o ro /home/darren/pmos/bak1/rl/userdata.bin /mnt; sh; sudo umount -v /mnt
   # inspect /mnt; then exit sh
   # modem.bin:       ... FAT (16 bit)
   # cache.bin:       ... ext4 ...
   # system.bin:      ... ext4 ...
   # persist.bin:     ... ext4 ...
   # userdata.bin:    ... ext4 ...

   # inspect emmc dump
   # sudo losetup -f --show -P -r /home/darren/pmos/bak1/flash.bin
   # lsblk -f
   # sudo mount -v -o ro /dev/loop0p1 /mnt; sudo exa -alT /mnt; sudo umount -v /mnt
   # sudo losetup -D; sudo losetup -l

`should back up userdata as well <https://github.com/bkerler/edl/issues/217#issuecomment-1009069582>`__

.. warning::

   | |:no_entry_sign:| :pr:`edl reset` |:no_entry_sign:|
   | To avoid rebooting to android:
   | 1\. :guilabel:`VolUp`\ +\ :guilabel:`PWR` into 05c6\:9091 mode
   | 2\. Detach cable
   | 3\. Click :guilabel:`Power Off`

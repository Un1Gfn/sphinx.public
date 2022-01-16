.. include:: include/substitution.txt
.. highlight:: text

============
postmarketOS
============

.. math::

   \mathit{The\ best\ way\ to\ predict\ the\ future\ is\ to\ invent\ it.} - \href{https://www.ted.com/speakers/alan_kay}{\text{Alan Kay}}


Contacts
========

| :mt:`#main:postmarketos.org`
|    travmurav UTC+5 RU :wp:`YEKT <Yekaterinburg Time>`
|    minecrell (UTC+0)
|    caleb
|    aka\_ UTC+1 PL CET
| :mt:`#lowlevel:postmarketos.org`
|    swiftgeek


Misc
====

| |:dart:| |:dart:| |:dart:|
| :mt:`initramfs with debug shell <#main:postmarketos.org/$R7GeB19FQN28ko33IaGgMS8ok5ZhyFW_NOkhxjhKQ54>`
| :pmos:`SSH`

``~/pmos``

| postmarketOS wiki
| :pmos:`the-big-list-of-who-has-what-device`
| :pmos:`contributing` to pmos
| :pmos:`applications by category`
|    `portfolio-file-manager <https://flathub.org/apps/details/dev.tchx84.Portfolio>`__
|    nemo |larr| :mt:`nncwmonx <#main:postmarketos.org/$L45lsgKLQ7jc3IriQXTtkUnViwcCmmD1E8IZ2tsGaG0>`
|    oFono/ModemManager
|    :wp:`maliit` (virtual keyboard)
|    

| `<https://postmarketos.org/source-code/>`__
| postmarketos 21.12 wt88047 :download:`images <https://images.postmarketos.org/bpo/v21.12/xiaomi-wt88047/>`
| mirror
  |vv| `ustc <https://mirrors.ustc.edu.cn/postmarketos/>`__
  |vv| `tuna <https://mirrors.tuna.tsinghua.edu.cn/postmarketOS/>`__
  |vv| `aliyun <https://mirrors.aliyun.com/postmarketOS/>`__

`redmi2(1/8) redmi2(2/16) redmi2pro(2/16) redmi2prime(2/16) <https://en.wikipedia.org/wiki/Redmi#Redmi_Series>`__

| only msm8916 has mainline modem
| :pmos:`Qualcomm mainline porting`
| :pmos:`Mainlining#Supported_SoCs`
| :wp:`Qualcomm CPU-SoC chart <list of Qualcomm Snapdragon processors>`
| :wp:`Qualcomm codecs <Qualcomm Hexagon#Hardware_codec_supported>`

`DeepSec 2010: All your baseband are belong to us by Ralf Philipp Weinmann <https://www.youtube.com/watch?v=fQqv0v14KKY>`__

| official MIUI rom
| `<https://c.mi.com/global/miuidownload/>`__
| `<https://c.mi.com/forum.php?mod=viewthread&tid=829348&extra=page%3D1>`__

| fastboot `documentation <https://android.googlesource.com/platform/system/core/+/master/fastboot/README.md>`__
| `fastbootd <https://source.android.com/devices/bootloader/fastbootd>`__

| `walleye edl <https://www.reddit.com/r/GooglePixel/comments/pfpmaj>`__
| cable issue?
| try build a smaller twrp.img to fit in boot partition?
| `A/B <https://source.android.com/devices/tech/ota/ab>`__

msdn - `sensor-orientation <https://docs.microsoft.com/en-us/windows/uwp/devices-sensors/sensor-orientation>`__

| EDL equivalents
| samsung exynos `exynos-usbdl <https://github.com/frederic/exynos-usbdl>`__
| mediatek mtk
|    `SP-Flash-Tool-source <https://github.com/ave4/SP-Flash-Tool-source>`__
|    `MTK-bypass <https://github.com/MTK-bypass/>`__ (`tutorial <https://www.xda-developers.com/bypass-mediatek-sp-flash-tool-authentication-requirement/>`__)
|    bkerler/`mtkclient <https://github.com/bkerler/mtkclient>`__

repacck boot.img `cpio+mkbootimg <https://www.whitewinterwolf.com/posts/2016/08/11/how-to-unpack-and-edit-android-boot-img/#rebuild-to-get-the-new-new-bootimg-file>`__

| `phosh <https://puri.sm/posts/phosh-overview/>`__
| `plasma mobile <https://plasma-mobile.org/2021/12/07/plasma-mobile-gear-21-12/>`__

unofficial wayland `protocols explorer <https://wayland.app/protocols/>`__

| nexus 6p angler EDL programmer
| `xda <https://forum.xda-developers.com/t/howtos-debrick-nexus-6p-stuck-in-edl-9008-mode.3552838/page-7>`__
  |rarr| `"turkish" <https://www.androidbrick.com/download/unbrick-nexus-6p-angler/>`__
  |rarr| `maganz <https://mega.nz/file/V19nDbaa#rFuNiTU-W0ChHyf-zqpljktV2wZZy3ndd4oihvfeLZY>`__
  |rarr| ``7z x``
  |rarr| prog_emmc_firehose.mbn
| sha256 `30758B3E0D2E47B19EBCAC1F0A66B545960784AD6D428A2FE3C70E3934C29C7A <https://alephsecurity.com/2018/01/22/qualcomm-edl-1/#:~:text=30758B3E0D2E47B19EBCAC1F0A66B545960784AD6D428A2FE3C70E3934C29C7A>`__
| `accessing EDL mode <https://blog.quarkslab.com/analysis-of-qualcomm-secure-boot-chains.html#accessing-edl-mode>`__

| qcdt or not?
| or, get device tree :mt:`from /sys/firmware/fdt <#main:postmarketos.org/$jWc9LQ0iz4-_VsLfIAcv7zMfJ6WuDJJlXm0muVvpxBs>`


bak.specs
=========

`build.prop <https://pocketnow.com/build-prop-tweaks>`__

:raw-html:`<details><summary>system.bin//build.prop</summary>`

.. literalinclude:: ../pmos/system__build_prop
   :language: text

:raw-html:`</details>`

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


bak.boot_modes
==============

.. warning::

   | 1\. Operate at 30%+ battery
   | 2\. |:warning:| **To prevent bootloop, unplug cable before any power state change**

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
| tweezer / |beta| |rarr| [Download] / ``fastboot oem edl`` / ``fastboot reboot-edl`` / ``fastboot reboot edl``
|    ``05c6:9008 Qualcomm, Inc. Gobi Wireless Modem (QDL mode)``
     |:japanese_goblin:|
     |:japanese_ogre:|
     |:skull:|
     |:smiling_imp:|
     |:space_invader:|


bak.EDL
=======

| :abbr:`PBL (Primary Boot Loader, in SoC ROM)` in Qualcomm :abbr:`MSM (Mobile Station Modem)` implements :abbr:`EDL (Emergency DownLoad mode)`
| EDL implements Sahara Protocol
| Sahara accepts OEM-digitally-signed *programmer* (\*.mbn file) over USB
| *programmer* implements Firehose Protocol
| PC <-> Firehose <-> eMMC/UFS

| alephsecurity/`firehorse <https://github.com/alephsecurity/firehorse>`__
| `Download Patched Firehose File for 600+ Android Devices <https://www.droidwin.com/patched-firehose-file/>`__
| andersson/`qdl <https://github.com/andersson/qdl>`__
| alephsecurity/`firehorse <https://github.com/alephsecurity/firehorse>`__
| bkerler/`edl <https://github.com/bkerler/edl>`__
| bkerler/`Loaders <https://github.com/bkerler/Loaders>`__
| OneLabsTools/`Programmers <https://github.com/OneLabsTools/Programmers/>`__
| :mt:`vanilla unsigned db410c edl programmer <#main:postmarketos.org/$2r0b_U-yVEidj-uQndqm3fWQ-i0hqMVGBsNMZ87iRyY>`
|    `linux-board-support-package-r1034.2.1.zip <https://releases.linaro.org/96boards/dragonboard410c/qualcomm/firmware/linux-board-support-package-r1034.2.1.zip>`__//linux-board-support-package-r1034.2.1/loaders/prog_emmc_firehose_8916.mbn
|    sha1 9fbfc85368a3def9b936a17662d848b4769dc131 [#dragonBL]_
| caveat - :mt:`they "forgot" to enable secure-boot <#main:postmarketos.org/$lIMqnR5BXu8zjQKhJhwvK44VFGuPLtSYihjYsATfOsc>`

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


bak.backup
==========

.. include:: include/escalate.txt

execute **step by step** ::

   mkdir -pv /home/darren/pmos/bak{1,2}
   # cd /home/darren/pmos/bak1
   cd /home/darren/pmos/bak2 && {

      exa -alT

      alias EDL='edl --loader=/home/darren/pmos/prog_emmc_firehose_8916.mbn --memory=eMMC'

      # send programmer
      EDL

      # inspect
      edl secureboot
      EDL printgpt

      # small
      # EDL pbl pbl.img # IndexError: list index out of range
      edl qfp qfp.img
      mkdir gpt; EDL gpt gpt/ --genxml

      # large
      # mkdir rl; EDL rl rl/ --skip=userdata --genxml # userdata isn't skipped
      mkdir rl; EDL rl rl/ --genxml
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


Chain
=====

| :abbr:`RPMB (Rollback Protection Memory Block)` [#RPMB]_
| |b| write protected region on eMMC/UFS
| |b| for storing counters for detecting replay attacks
| |b| once initialized, can only be accessed by trusted apps in
      :abbr:`QTEE (Qualcomm Trusted Execution Environment STOR)` through
      :abbr:`QTEE (Qualcomm Trusted Execution Environment STOR)`
      :abbr:`RPMB (Rollback Protection Memory Block)` driver

| timesys/`Secure Boot and Encrypted Data Storage - FIT, encryption and firmware upgrade <https://timesys.com/security/secure-boot-encrypted-data-storage/>`__
| timesys/`Secure boot on Snapdragon 410 <https://www.timesys.com/security/secure-boot-snapdragon-410/>`__
| `raelize <https://raelize.com/blog/qualcomm-ipq40xx-analysis-of-critical-qsee-vulnerabilities/>`__
| :wp:`booting process of Android devices`
| qualcomm/`Secure Boot and Image Authentication <https://www.qualcomm.com/media/documents/files/secure-boot-and-image-authentication-technical-overview-v2-0.pdf>`__
| lineage/`Qualcomm’s Chain of Trust <https://lineageos.org/engineering/Qualcomm-Firmware/>`__
| quarkslab/`Analysis of Qualcomm Secure Boot Chains <https://blog.quarkslab.com/analysis-of-qualcomm-secure-boot-chains.html>`__
|    Qualcomm, Secure Boot and Image Authentication Technical Overview
     `1.0 <https://www.qualcomm.com/media/documents/files/secure-boot-and-image-authentication-technical-overview-v1-0.pdf>`__
     (`archive <http://web.archive.org/web/20220116085800/https://www.qualcomm.com/media/documents/files/secure-boot-and-image-authentication-technical-overview-v1-0.pdf>`__)
     `2.0 <https://www.qualcomm.com/media/documents/files/secure-boot-and-image-authentication-technical-overview-v2-0.pdf>`__
     (`archive <http://web.archive.org/web/20220116091146/https://www.qualcomm.com/media/documents/files/secure-boot-and-image-authentication-technical-overview-v2-0.pdf>`__)

| **cryp**\ tographically
| attestation /a·tuh·**stay**·shn/
| readonly :abbr:`RFS (root filesystem)` with dm-verity, or rw RFS with dm-crypt/dm-integrity
| Signature + Root Certificate + Attestation Certificate

sectools from Arrow Electronics or Qualcomm blows the fuse bits

1. :abbr:`PBL (Primary Boot Loader (bootROM))` initializes Cortex-A53's SRAM and loads the 1\ :sup:`st` segment of :abbr:`sbl1 (1st stage Secondary Boot Loader)`/:abbr:`xbl (eXtended Boot Loader)` to it [|alpha|]
#. PBL loads the 2\ :sup:`nd` segment of sbl1 to :abbr:`RPM (Resource Power Manager)` memory [|beta|]
#. [|alpha|] initializes DDR, authenticates tz (:abbr:`QSEE (Qualcomm Secure Execution Environment)`/:abbr:`QTEE (Qualcomm Trusted Execution Environment)`) and hyp (:abbr:`QHEE (Qualcomm Hypervisor Execution Environment )`), partitions DDR into Secure :abbr:`TEE (Trusted Execution Environment)` and Non-secure :abbr:`REE (Rich Execution Environment)`
#. [|beta|]  loads rpm to RPM memory
#. [|alpha|] loads aboot (:abbr:`ABL/APPSBL (Android Boot Loader / Application Boot Loader, the first open source component in the boot stack, LK/U-Boot/UEFI based)`), which implements the :wp:`fastboot` interface
#. [|alpha|]'s job finishes, tz and hyp take over, RPM released from reset [#flow]_ [#ndec]_

| `chart <https://github.com/msm8916-mainline/qhypstub#boot-flow>`__
| replace phy with `qhypstub <https://github.com/msm8916-mainline/qhypstub>`__+`qtestsign <https://github.com/msm8916-mainline/qtestsign>`__

| replace hyp and tz?
| `<https://wiki.postmarketos.org/wiki/Huawei_Ascend_G7_(huawei-g7)>`__
| `<https://wiki.postmarketos.org/wiki/Huawei_Y635_(huawei-y635)>`__

| typical :abbr:`EL (Exception Level)` usage model

.. |EL3| replace:: :raw-html:`<span style="color:brown;  ">EL3</span>`
.. |EL2| replace:: :raw-html:`<span style="color:magenta;">EL2</span>`
.. |EL1| replace:: :raw-html:`<span style="color:black;  ">EL1</span>`
.. |EL0| replace:: EL0

.. table::
   :align: left
   :widths: auto

   ======= ========================= ============================ =====================================  ====================== ====================================================================================================
    \       hardware implementation   AArch32                      AArch64                                what runs    
   ======= ========================= ============================ =====================================  ====================== ====================================================================================================
    |EL0|   mandatory                 |:heavy_check_mark:|         only when |EL1|\ |br|\ uses AArch64    Applications           Unprivileged Execution, the lowest software execution privilege)      
    |EL1|   mandatory                 |:heavy_check_mark:|         only when |EL2|\ |br|\ uses AArch64    (Rich) OS kernel          
    |EL2|   optional                  |:heavy_check_mark:|         |:heavy_check_mark:|                   Hypervisor             processor virtualization        
    |EL3|   optional                  |:heavy_multiplication_x:|   |:heavy_check_mark:|                   Secure Monitor (SMC)    the only level where security state associated with the execution can be changed (tz?) (firmware?)        
   ======= ========================= ============================ =====================================  ====================== ====================================================================================================

|    EL0/EL1 share the same MMU configuration
|    each EL has its own :abbr:`AArch64 and AArch32 (execution states)`
| exception
|    on taking an exception, EL remains the same or increases
|    on returning from an exception, EL remains the same or decreases
| exception has a :abbr:`target EL (the EL that the execution changes to, or remains in, on taking an exception)`
|    the target EL is *either* implicit in the nature of the exception, *or* defined by configuration bits in the *System Registers*
|    it cannot be EL0, i.e. an exception cannot target the EL0 Exception level

| Secure state and Non-secure state, each with an associated memory address space
| in Secure state, the processor can access
|    |b| *both* states' memory address space
|    |b| *all* the system control resources (when executing at EL3)
| in Non-secure state, the processor can access
|    |b| *only* the Non-secure memory address space.
|    |b| *no* system control resources


Inspect Images
==============

PabloCastellano/`extract-dtb <https://github.com/PabloCastellano/extract-dtb>`__

(fsimg) inspect interactively in throwaway shell ::

   sudo mount -vo ro /home/darren/pmos/bak1/rl/system.bin /mnt; bash --init-file <(echo 'PS1="(\W)\$ "; cd /mnt; pwd'); sudo umount -v /mnt;

mount \:\: system.bin//etc/vold.fstab ::

   dev_mount sdcard /storage/sdcard1 auto /devices/msm_sdcc.2/mmc_host
   # MTP
   #dev_mount sdcard2 /mnt/sdcard/external_sd auto /devices/platform/msm_sdcc.3/mmc_host

mount \:\: hardcoded in rc \:\: boot.img ::

   mkdir -pv /tmp/BOOT
   unpackbootimg -i ~/pmos/bak1/rl/boot.bin -o $_
   lsinitcpio /tmp/BOOT/boot.bin-ramdisk
   mkdir -v /tmp/BOOT/CPIO && cd $_ && lsinitcpio -x /tmp/BOOT/boot.bin-ramdisk

Android init language
|vv| `dev.to <https://dev.to/larsonzhong/android-system-init-process-startup-and-init-rc-full-analysis-22hi>`__
|vv| `halolinux <https://www.halolinux.us/kernel-reference/mounting-the-root-filesystem.html>`__
|vv| `googlesource <https://android.googlesource.com/platform/system/core/+/master/init/README.md>`__

|nbsp| - grep --binary-files=binary -nr 'mount' CPIO/ ::

   init.qcom.rc:776:              mount none /mnt/shell/emulated/0 /storage/emulated/legacy bind
   init.qcom.syspart_fixup.sh:78: mount -o ro,remount,barrier=1 /system
   init.rc:153:                   mount rootfs rootfs / ro remount
   init.rc:155:                   mount rootfs rootfs / shared rec
   init.recovery.hardware.rc:22:  #mount ext4 /dev/block/platform/msm_sdcc.1/by-name/system /system wait rw barrier=1
   init.target.rc:123:            mount ext4 /dev/block/bootdevice/by-name/system /system ro barrier=1
   init.target.rc:42:             mount_all fstab.qcom
   init.target.rc:49:             mount ext4 /dev/block/bootdevice/by-name/cache /cache check nosuid nodev barrier=1
   init.target.rc:52:             mount ext4 /dev/block/bootdevice/by-name/persist /persist nosuid nodev barrier=1
   init.target.rc:55:             mount vfat /dev/block/bootdevice/by-name/modem /firmware ro shortname=lower,uid=1000,gid=1000,dmask=227,fmask=337

|nbsp| - cat CPIO/fstab.qcom ::

   # Android fstab file.
   # The filesystem that contains the filesystem checker binary (typically /system) cannot
   # specify MF_CHECK, and must come before any filesystems that do specify MF_CHECK

   #TODO: Add 'check' as fs_mgr_flags with data partition.
   # Currently we dont have e2fsck compiled. So fs check would failed.

   #<src>                                                <mnt_point>  <type>  <mnt_flags and options>                     <fs_mgr_flags>
   /dev/block/bootdevice/by-name/system         /system      ext4    ro,barrier=1,discard                                wait
   /dev/block/bootdevice/by-name/userdata       /data        ext4    nosuid,nodev,barrier=1,noauto_da_alloc,discard      wait,check,resize,encryptable=footer
   /devices/soc.0/7864900.sdhci/mmc_host        /storage/sdcard1   vfat    nosuid,nodev         wait,voldmanaged=sdcard1:auto
   /devices/platform/msm_hsusb                  /storage/usbotg    vfat    nosuid,nodev         wait,voldmanaged=usbotg:auto

mount \:\: hardcoded in rc \:\: recovery.img ::

   ?

|    aur/`*bootimg* <https://aur.archlinux.org/packages/?K=bootimg>`__
|    ggrandou/`abootimg <https://github.com/ggrandou/abootimg>`__ |larr| :mt:`mighty17 <#main:postmarketos.org/$sEn8pZncVGMgs1EMrtpVWU9tPpj6M_Av8Z7Non7xJVo>`
|    osm0sis/`mkbootimg <https://github.com/osm0sis/mkbootimg>`__ |larr| :mt:`Tooniis <#main:postmarketos.org/$IdCQBs2sH7ivzqkHDKRYDlv0DhbnBqhr0xiaIAPV6oE>`

| persist.bin//WCNSS_qcom_wlan_nv.bin sha1 7a0005d79045d5b3ff74535c2a7f438e5b79cb70
| `firmware-xiaomi-wt88047-wcnss-nv <http://pkgs.postmarketos.org/package/master/postmarketos/aarch64/firmware-xiaomi-wt88047-wcnss-nv>`__
| `wcnss-wlan.txt <https://android.googlesource.com/kernel/msm/+/android-10.0.0_r0.66/Documentation/devicetree/bindings/wcnss/wcnss-wlan.txt>`__ [#r066]_

| ``gdisk -l ~/pmos/bak1/flash.bin``
| ``sudo losetup -f --show -P -r /home/darren/pmos/bak1/flash.bin; ls -l /dev/disk/by-partlabel/; sudo losetup -D`` 

| AOSP doc - `partitions <https://source.android.com/devices/bootloader/partitions>`__
| *total: 30*

| xda/`[INFO] Android device partitions and filesystems <https://forum.xda-developers.com/t/info-android-device-partitions-and-filesystems.3586565/>`__
| config - saves state of Factory Reset Protection (FRP), "Allow bootloader (OEM) unlocking" . (Developer Options), asks already associated account info. This partition is erased/reset if Factory Reset done from Settings.
| fsc - modem FileSystem Cookies
| DDR - Double Data Rate RAM
| ssd - Secure Software Download, a memory based file system for secure storage, stores some encrypted RSA keys
| sec - contains fuse settings, mainly for secure boot (signing bootloaders for chain of trust) and oem setting
| oem - like VENDOR, it incorporates OEM (Original Equipment Manufacturer i.e. hardware manufacturer or Mobile Phone brand) small customization (modifications) to original Android (AOSP) during OTA updates such as customized system properties values etc.
| pad - related to OEM
| fsg - FileSystem Golden copy
| modem - the phone's radio...
| modemst1 - modem firmware files.
| modemst2 - modem firmware files.

:raw-html:`<details><summary>edl printgpt (full)</summary>`

.. literalinclude:: ../pmos/edl_printgpt.txt
   :language: text

:raw-html:`</details>`

misc partition `used by recovery <https://source.android.com/devices/bootloader/partitions>`__ ::

   $ hexdump -C misc.bin
   00000000  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
   *
   00001000  62 6f 6f 74 2d 73 79 73  74 65 6d 30 00 00 00 00  |boot-system0....|
   00001010  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
   *
   00100000

(recovery) grep --binary-files=binary -hr 'mount' CPIO/ ::

   #mount ext4 /dev/block/platform/msm_sdcc.1/by-name/system /system wait rw barrier=1
   mount tmpfs tmpfs /tmp
   mount functionfs adb /dev/usb-ffs/adb uid=2000,gid=2000
   # remount system as read-write.
   mount -o rw,remount,barrier=1 /system

recovery.bin//CPIO//fstab.qcom ::

   /dev/block/bootdevice/by-name/system         /system      ext4    ro,barrier=1,discard                                wait
   /dev/block/bootdevice/by-name/userdata       /data        ext4    nosuid,nodev,barrier=1,noauto_da_alloc,discard      wait,check,resize,encryptable=footer
   /devices/soc.0/7864900.sdhci/mmc_host        /storage/sdcard1   vfat    nosuid,nodev         wait,voldmanaged=sdcard1:auto
   /devices/platform/msm_hsusb                  /storage/usbotg    vfat    nosuid,nodev         wait,voldmanaged=usbotg:auto

recovery.bin//CPIO//etc/recovery.fstab ::

   # bug_288790,huyonggang.wt,20140930, userdata decrease 20480(20Kb)
   # in order to protect encryption footer size(<=16Kb),
   # should map to BOARD_USERDATAIMAGE_PARTITION_SIZE config at BoardConfig.mk
   /dev/block/bootdevice/by-name/system       /system         ext4    ro,barrier=1                                                    wait
   /dev/block/bootdevice/by-name/cache        /cache          ext4    noatime,nosuid,nodev,barrier=1,data=ordered,discard                     wait,check
   /dev/block/bootdevice/by-name/userdata     /data           ext4    noatime,nosuid,nodev,barrier=1,data=ordered,noauto_da_alloc,discard      wait,check,length=-20480
   /dev/block/mmcblk1p1                       /sdcard         vfat    nosuid,nodev,barrier=1,data=ordered,nodelalloc                  wait
   /dev/block/bootdevice/by-name/boot         /boot           emmc    defaults                                                        defaults
   /dev/block/bootdevice/by-name/recovery     /recovery       emmc    defaults                                                        defaults
   /dev/block/bootdevice/by-name/misc         /misc           emmc    defaults                                                        defaults
   #splash.img dupeiyu.wt add 20141018
   /dev/block/bootdevice/by-name/splash       /splash         emmc    defaults                                                        defaults


Footnotes
=========

.. [#r066] this txt file exists in android-10.0.0_r0.66 tag but becomes absent in android-10.0.0_r0.67

.. [#RPMB]
           `gydwtqsmp.pdf <https://www.qualcomm.com/media/documents/files/guard-your-data-with-the-qualcomm-snapdragon-mobile-platform.pdf>`__
           (`archived <http://web.archive.org/web/20211029173830/https://www.qualcomm.com/media/documents/files/guard-your-data-with-the-qualcomm-snapdragon-mobile-platform.pdf>`__)

.. [#flow] :mt:`#main:postmarketos.org/$INEHhmLuwKuDVRUzpXLfSspsAK45hAp4Q6J4q3WVqLw`

.. [#dragonBL] 
               | `APQ8016E <https://developer.qualcomm.com/hardware/apq-8016e/tools>`__
                 |rarr| DragonBoard 410c (DB410c)
                 |rarr| Schematics/BOM/Assembly Files
               | `Android Downloads for DragonBoard-410c <https://www.96boards.org/documentation/consumer/dragonboard/dragonboard410c/downloads/android.md.html>`__ |rarr| Fastboot files
               |    |rarr| Bootloader |rarr| Download
               |    |rarr| Extras |rarr| Build Folder |rarr| .. |rarr| .. |rarr| firmware |rarr| linux-board-support-package-\*.zip

.. [#ndec] `ndec <https://discuss.96boards.org/t/documentation-on-db410c-bootloader-files/2124/2>`__

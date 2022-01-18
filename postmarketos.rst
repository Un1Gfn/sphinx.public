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

| `<https://postmarketos.org/source-code/>`__
| postmarketos 21.12 wt88047 :download:`images <https://images.postmarketos.org/bpo/v21.12/xiaomi-wt88047/>`
| :pmos:`mirrors`
  |vv| `mirrors.py <https://gitlab.com/postmarketOS/postmarketos.org/-/blob/master/config/mirrors.py>`__

.. \|vv| `ustc <https://mirrors.ustc.edu.cn/postmarketos/>`__
.. \|vv| `tuna <https://mirrors.tuna.tsinghua.edu.cn/postmarketOS/>`__
.. \|vv| `aliyun <https://mirrors.aliyun.com/postmarketOS/>`__

:wp:`redmi2(1/8) redmi2(2/16) redmi2pro(2/16) redmi2prime(2/16) <Redmi#Redmi_Series>`

| only msm8916 has mainline modem
| :pmos:`Qualcomm mainline porting`
| :pmos:`Mainlining#Supported_SoCs`
| :wp:`Qualcomm CPU-SoC chart <list of Qualcomm Snapdragon processors>`
| :wp:`Qualcomm codecs <Qualcomm Hexagon#Hardware_codec_supported>`

`DeepSec 2010: All your baseband are belong to us by Ralf Philipp Weinmann <https://www.youtube.com/watch?v=fQqv0v14KKY>`__

| fastboot `documentation <https://android.googlesource.com/platform/system/core/+/master/fastboot/README.md>`__
| `fastbootd <https://source.android.com/devices/bootloader/fastbootd>`__

| :r:`walleye edl <GooglePixel/comments/pfpmaj>`
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

:abbr:`ACK (Android Common Kernel)`
:abbr:`GKI (Generic Kernel Image)`
:abbr:`KMI (Kernel Module Interface)`
[#GKI]_

:abbr:`V4L (Video4Linux)`
:abbr:`msm-uartdm (Qualcomm UART Data Mover mode)`
:abbr:`qmi (Qualcomm Modem Interface. The internal interface inside Qualcomm SoCs that connect the modem and the application processor.)`
:abbr:`slpi (Sensor Low Power Interface. The interface that connect sensors like the accelerometer to the application processor in Qualcomm SoCs)`
[#Glossary]_

`One Year of postmarketOS: Mainline Calling! <https://postmarketos.org/blog/2018/06/09/one-year/>`__

`Alpine_Linux:Glossary <https://wiki.alpinelinux.org/wiki/Alpine_Linux:Glossary>`__

| :pmos:`making good photos`
| :pmos:`preparing videos for blog posts`

| artwork
| `latex beamer (slides) template <https://gitlab.com/postmarketOS/artwork/-/tree/c8b7378e8a71147c0579848754a21a9c65e3d0a9/presentation/latex>`__
| `midi <https://gitlab.com/postmarketOS/artwork/-/tree/7f0fe16c77f674725d2860157393bcc465610bff/tones>`__
| `wallpaper <https://gitlab.com/postmarketOS/artwork/-/tree/2b39e6081c7a676ae1be3fc036ccbfef3052072c/wallpapers>`__
| `blender3d <https://gitlab.com/postmarketOS/artwork/-/tree/028b40914c75c17c084cf6b2358e56948df12a85/src>`__
| `svg <https://gitlab.com/postmarketOS/artwork/-/tree/028b40914c75c17c084cf6b2358e56948df12a85/logo>`__

`GNSS Share <https://gitlab.com/postmarketOS/gnss-share>`__

`Breaking updates in edge <https://postmarketos.org/edge/>`__


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

adb shell busybox mount | sort -t' ' -k5 | column -tl6 ::

   none                                    on  /dev/cpuctl             type  cgroup      (rw,relatime,cpu)
   none                                    on  /acct                   type  cgroup      (rw,relatime,cpuacct)
   none                                    on  /dev/cpuset             type  cgroup      (rw,relatime,cpuset,noprefix,release_agent=/sbin/cpuset_release_agent)
   none                                    on  /sys/fs/cgroup/freezer  type  cgroup      (rw,relatime,freezer)
   debugfs                                 on  /sys/kernel/debug       type  debugfs     (rw,relatime)
   devpts                                  on  /dev/pts                type  devpts      (rw,seclabel,relatime,mode=600)
   /dev/block/bootdevice/by-name/system    on  /system                 type  ext4        (ro,seclabel,relatime,discard,data=ordered)
   /dev/block/bootdevice/by-name/cache     on  /cache                  type  ext4        (rw,seclabel,nosuid,nodev,relatime,data=ordered)
   /dev/block/bootdevice/by-name/persist   on  /persist                type  ext4        (rw,seclabel,nosuid,nodev,relatime,data=ordered)
   /dev/block/bootdevice/by-name/userdata  on  /data                   type  ext4        (rw,seclabel,nosuid,nodev,relatime,discard,noauto_da_alloc,data=ordered)
   adb                                     on  /dev/usb-ffs/adb        type  functionfs  (rw,relatime)
   /dev/fuse                               on  /mnt/shell/emulated/0   type  fuse        (rw,nosuid,nodev,noexec,relatime,user_id=1023,group_id=1023,default_permissions,allow_other)
   /dev/fuse                               on  /mnt/shell/emulated     type  fuse        (rw,nosuid,nodev,noexec,relatime,user_id=1023,group_id=1023,default_permissions,allow_other)
   /dev/fuse                               on  /storage/uicc0          type  fuse        (rw,nosuid,nodev,noexec,relatime,user_id=1023,group_id=1023,default_permissions,allow_other)
   proc                                    on  /proc                   type  proc        (rw,relatime)
   rootfs                                  on  /                       type  rootfs      (ro,relatime)
   selinuxfs                               on  /sys/fs/selinux         type  selinuxfs   (rw,relatime)
   sysfs                                   on  /sys                    type  sysfs       (rw,seclabel,relatime)
   tmpfs                                   on  /dev                    type  tmpfs       (rw,seclabel,nosuid,relatime,size=968392k,nr_inodes=154469,mode=755)
   none                                    on  /sys/fs/cgroup          type  tmpfs       (rw,seclabel,relatime,size=968392k,nr_inodes=154469,mode=750,gid=1000)
   none                                    on  /sys/fs/cgroup          type  tmpfs       (rw,seclabel,relatime,size=968392k,nr_inodes=154469,mode=750,gid=1000)
   tmpfs                                   on  /mnt/asec               type  tmpfs       (rw,seclabel,relatime,size=968392k,nr_inodes=154469,mode=755,gid=1000)
   tmpfs                                   on  /mnt/obb                type  tmpfs       (rw,seclabel,relatime,size=968392k,nr_inodes=154469,mode=755,gid=1000)
   none                                    on  /var                    type  tmpfs       (rw,seclabel,relatime,size=968392k,nr_inodes=154469,mode=770,gid=1000)
   /dev/block/bootdevice/by-name/modem     on  /firmware               type  vfat        (ro,context=u:object_r:firmware_file:s0,relatime,uid=1000,gid=1000,fmask=0337,dmask=0227,codepage=437,iocharset=iso8859-1,shortname=lower,errors=remount-ro)


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
| :guilabel:`PWR` |rarr| :strong:`viberate` *don't release PWR* |rarr| :guilabel:`VolDown` [#lk2ndUsage]_
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

   mkdir /home/darren/pmos/bak3 && cd /home/darren/pmos/bak3 && {

      tmux attach || tmux

      exa -alT

      alias EDL='/usr/bin/edl --loader=/home/darren/pmos/prog_emmc_firehose_8916.mbn --memory=eMMC'

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

   # check for missing files
   meld <(cd /home/darren/pmos/bak1; find | sort) <(cd /home/darren/pmos/bak3; find | sort)

   # compute checksum (overwritten!)
   # cd /home/darren/pmos/bak3; find . -type f \( -not -name "sha1sum.txt" \) -exec sha1sum {} \; | tee -a sha1sum.txt; echo

   # verify checksum
   cd /home/darren/pmos/bak3; sha1sum -c sha1sum.txt --strict -w; echo

   # difference between two dumps
   meld /home/darren/pmos/bak{1,2,3}/sha1sum.txt

   # ?
   # meld \
   #    <(tune2fs -l /home/darren/pmos/bak1/rl/persist.bin) \
   #    <(tune2fs -l /home/darren/pmos/bak2/rl/persist.bin) \
   #    <(tune2fs -l /home/darren/pmos/bak3/rl/persist.bin)

   # file type
   cd /home/darren/pmos/bak3
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

:aw:`optical disc drive#Making_an_ISO_image_from_existing_files_on_hard_disk` ::

   # execute step-by-step!
   cd /home/darren/pmos/bak1
   sha1sum -c sha1sum.txt --strict -w; echo
   # mkisofs(8) - /^\s+(-[VoJR]( |$)|-iso-level)
   mkisofs \
      -iso-level 3 \
      -J \
      -o ../WT88047_EDL_BAK1.ISO \
      -R \
      -V "WT88047_EDL_BAK1" \
      .
   iso-info -i ~/pmos/WT88047_EDL_BAK1.ISO -l
   isoinfo  -i ~/pmos/WT88047_EDL_BAK1.ISO -l
   sudo mount -vo ro ~/pmos/WT88047_EDL_BAK1.ISO /mnt; bash --init-file <(echo 'echo; PS1="(\W)\$ "; cd /mnt; pwd; df -h; echo; exa -alT; echo'); sudo umount -v /mnt;
      sha1sum -c sha1sum.txt --strict -w; echo
      exit
   touch ~/pmos/WT88047_EDL_BAK1.ISO.sha1."$(sha1sum ~/pmos/WT88047_EDL_BAK1.ISO | cut -d' ' -f1)"


inspect.chain
=============

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
| `Huawei Ascend G7 (huawei-g7)>`
| `Huawei Y635 (huawei-y635)>`

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


inspect.img
===========

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


install.0.updateFW
==================

| `<https://c.mi.com/global/miuidownload/>`__
| `<https://c.mi.com/forum.php?mod=viewthread&tid=829348&extra=page%3D1>`__
| `<https://wiki.lineageos.org/devices/wt88047/install#updating-firmware>`__

inspect firmwares ::

   cd ~/pmos/

   meld \
      <(cd \[C.MI\]_4.4; find | sort) \
      <(cd \[C.MI\]_5.1; find | sort)
   # result: differences in flash scripts and a dummy text dev.img

   meld \
      <(gdisk -l bak1/gpt/gpt_main0.bin) \
      <(gdisk -l \[C.MI\]_5.1/images/gpt_both0.bin)
   # result: userdata partition being the only difference

   meld \
      <(cd \[C.MI\]_5.1/images;             sha1sum emmc_appsboot.mbn hyp.mbn NON-HLOS.bin rpm.mbn sbl1.mbn tz.mbn) \
      <(cd \[LINEAGE\]_fw/firmware-update/; sha1sum emmc_appsboot.mbn hyp.mbn NON-HLOS.bin rpm.mbn sbl1.mbn tz.mbn) \
      <(cd \[C.MI\]_4.4/images;             sha1sum emmc_appsboot.mbn hyp.mbn NON-HLOS.bin rpm.mbn sbl1.mbn tz.mbn) \
      ;
   # result: lineage firmware are taken from 5.1 but not 4.4

:raw-html:`<details><summary>upstream gpt utterly broken, fixing attempt fails, use bak1</summary>`

::

   # execute STEP-BY-STEP!!!
   cd "/home/darren/pmos/[C.MI]_5.1/images"
   rm -v gpt_main0_copygrow.bin gpt_main0_modified.bin gpt_main0_modified_tailed.bin # don't use dangerous glob "*"!!!
   cat <(head -c$((16#200)) /dev/zero) gpt_main0.bin >gpt_main0_copygrow.bin
   cp -v gpt_main0.bin gpt_main0_copygrow.bin
   truncate -cs $((16#3ab400000)) gpt_main0_copygrow.bin
   ls -alh gpt_main0*

   # parted gpt_main0_copygrow.bin
   gdisk gpt_main0_copygrow.bin
   x
   s
   128
   m
   d
   30
   n
   30
   3670016
   30777310
   0700
   c
   30
   userdata
   b
   gpt_main0_modified.bin
   q
   ls -lh gpt_main0*
   hexdump -C gpt_main0.bin
   tail -c +$((16#200)) gpt_main0_modified.bin >|gpt_main0_modified_tailed.bin

:raw-html:`</details>`

minimum requirements for a warking fastboot ::

   A=()
   A+=(
     config
     DDR
     fsc
     fsg
     keystore
     misc
     modemst1
     modemst2
     oem
     pad
     ssd
   )
   A+=(
     sbl1
     aboot
     hyp
     rpm
     tz
     splash
   )

   EDL="--loader=/home/darren/pmos/prog_emmc_firehose_8916.mbn --memory=eMMC"

   edl $EDL # load programmer

   /bin/edl w gpt '/home/darren/pmos/bak1/gpt/gpt_main0.bin' $EDL
   # /bin/edl w gpt '/home/darren/pmos/[C.MI]_5.1/images/gpt_main0.bin' $EDL # boot fail, EDL loop

   for i in "${A[@]}"; do
     file "/home/darren/pmos/bak1/rl/$i.bin" || break
   done
   echo "${#A[@]}"

   echo; for i in "${A[@]}"; do
     read -rp ": write $i? "
     /bin/edl w "$i" "/home/darren/pmos/bak1/rl/$i.bin" $EDL
     echo
   done

   edl reset


install.1.boot
==============

:pmos:`QCDT`

.. table::
   :align: left
   :widths: auto

   +------------------------------------+
   |              bootimg               |
   +-------------------+----------+-----+
   |         zImage    |          |     |
   +-------------+-----+ initcpio | dtb |
   | selfextract | elf |          |     |
   +-------------+-----+----------+-----+

non-QCDT

.. table::
   :align: left
   :widths: auto

   +------------------------------------+
   |                     bootimg        |
   +-------------------------+----------+
   |         zImage          |          |
   +-------------+-----+-----+ initcpio |
   | selfextract | elf | dtb |          |
   +-------------+-----+-----+----------+

| have a taste of all three GUI shells in :pmos:`QEMU <QEMU amd64 (qemu-amd64)>` before writing to emmc /system /userdata
| size:
  `plasma-mobile <https://images.postmarketos.org/bpo/v21.12/xiaomi-wt88047/plasma-mobile/20220112-1123/>`__
  \>
  `phosh         <https://images.postmarketos.org/bpo/v21.12/xiaomi-wt88047/phosh/20220112-1116/>`__
  \>
  `sxmo-de-sway  <https://images.postmarketos.org/bpo/v21.12/xiaomi-wt88047/sxmo-de-sway/20220112-1133/>`__

| install lk2nd
  |vv| :pmos:`pmoswiki <Qualcomm Snapdragon 410/412 (MSM8916)#Installation>`
  |vv| `github <https://github.com/msm8916-mainline/lk2nd#installation>`__
| check for new lk2nd releases before upgrading kernel (already on github watchlist)
| `get log file <https://github.com/msm8916-mainline/lk2nd#troubleshooting>`__ from lk2nd

| :pmos:`pmbootstrap`
| :pkg:`AUR/pmbootstrap` |vv| :pkg:`AUR/pmbootstrap-git`
| :pkg:`community/python-argcomplete` ``sudo activate-global-python-argcomplete``
| :pmos:`deviceinfo_flash_methods`

pmbootstrap `usage <https://gitlab.com/postmarketOS/pmbootstrap#basics>`__

.. danger::

   | |:radioactive:| Make sure there are no mount points in it before removing the work path |:radioactive:|
   | \
     ``pmbootstrap shutdown``
     ``sudo mount | grep -i -e home -e market # check for dangling mount points``
   | ``sudo find /home/darren/.local/var/pmbootstrap # sanity``
   | ``sudo find /home/darren/.local/var/pmbootstrap -type l -exec file {} \; # check for escaping links``
   | ``pmbootstrap zap -hc -d -p -m -o -r``

list of v21.12 aarch64 `initramfs hooks <http://pkgs.postmarketos.org/packages?name=postmarketos-mkinitfs-hook*&branch=v21.12&repo=postmarketos&arch=aarch64>`__
(hover on package name for description)

build
:pmos:`customized installation <Qualcomm Snapdragon 410/412 (MSM8916)#Installation_using_pmbootstrap>`
with pmbootstrap
(initfs only)

::

   # execute step-by-step and selectively!!!

   tmux attach || tmux

   source ~/proxy.bashrc

   # pmbootstrap <COMMAND> -h

   pmbootstrap --version

   pmbootstrap init
   # Work path: [/home/darren/.local/var/pmbootstrap]
   # Config:    [~/.config/pmbootstrap.cfg]
   # mirror:    https://mirrors.tuna.tsinghua.edu.cn/postmarketOS/
   # Locale:    en_US.UTF-8
   # Hostname:  wt88047
   # CopySSH:   y
   # BuildPkg:  n

   # execute in another terminal
   alacrittytitle.sh "(pmbootstrap) log"; pmbootstrap log

   pmbootstrap config work
   pmbootstrap status --details
   pmbootstrap pull

   proxy_off

   # assemble bootimg with debug shell
   pmbootstrap initfs hook_add debug-shell
   pmbootstrap initfs hook_add verbose-initfs
   pmbootstrap initfs hook_ls
   pmbootstrap initfs build # force rebuild
   sudo exa -alT /home/darren/.local/var/pmbootstrap/chroot_rootfs_xiaomi-wt88047/boot/
   file /home/darren/.local/var/pmbootstrap/chroot_rootfs_xiaomi-wt88047/boot/boot.img
   pmbootstrap bootimg_analyze /home/darren/.local/var/pmbootstrap/chroot_rootfs_xiaomi-wt88047/boot/boot.img
   pmbootstrap shutdown # safety measure in case of dangling mounts

try debug shell without installing anything to emmc ::

   : manually enter vendor fastboot

   # vendor fastboot -> lk2nd
   fastboot boot ~/pmos/lk2nd-msm8916_0.11.0_sha1_030aff45c70905fbf3ec069bdb8cbef7a0170719.img

   # lk2nd -> initcpio
   fastboot boot /home/darren/.local/var/pmbootstrap/chroot_rootfs_xiaomi-wt88047/boot/boot.img

   : wait with patience

| :pmos:`boot process`
| :pmos:`partition layout <Partition Layout>`

.. tip::

   Wait patiently after ``fastboot boot`` completes.

| :pmos:`USB Network`
| :pmos:`debug shell <inspecting the initramfs>`
| :pmos:`SSH`
| :pmos:`netboot`

.. table::
   :align: left
   :widths: auto

   ============================= ==================== ============= ===============
    default account [#SSHpass]_   address              username      password
    \                             :kbd:`172.16.42.1`   :kbd:`user`   :kbd:`147147`
   ============================= ==================== ============= ===============

play ::

   echo
   ip l
   echo
   sudo ip link set enp0s20f0u2 up
   sudo ip addr flush dev enp0s20f0u2
   sudo ip addr add 172.16.42.223/8 dev enp0s20f0u2
   sudo ip addr show dev enp0s20f0u2
   echo

   ping 172.16.42.1
   telnet 172.16.42.1

   # ...

   # nohup
   # 1>/dev/null prevents nohup.out file
   # ( busybox nohup busybox ash -c "rm -f /garbage; busybox sleep 5; echo sldjflwkjelfjlsjdklfjslkd >/garbage" 1>/dev/null & )

   # ps -o help
   # ps | head -2
   # pid 1 (init) is "{init} /bin/sh /init PMOS_NO_OUTPUT_REDIRECT"
   # therefore we have to "Force" (don't go through init)
   ( busybox nohup busybox ash -c "busybox poweroff -d 7 -f" 1>/dev/null & )
   : detatch microUSB immediately

| :pmos:`troubleshooting:boot`
| :pmos:`troubleshooting:display`
| :pmos:`troubleshooting:boot:initfshooks`


install.2.rootfs
================

\...


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

.. [#GKI] `Generic Kernel Image | Android Open Source Project <https://source.android.com/devices/architecture/kernel/generic-kernel-image>`__

.. [#Glossary] :pmos:`Glossary`

.. [#SSHpass] :pmos:`SSH`

.. [#lk2ndUsage] lk2nd `usage <https://github.com/msm8916-mainline/lk2nd#usage>`__

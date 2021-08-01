.. include:: substitution.txt

================
|ico| `U-Boot`__
================

.. __: https://www.denx.de/wiki/U-Boot

Misc
====


`Title Capitalization Tool <https://capitalizemytitle.com/>`__

| `GitLab Instance repo <https://source.denx.de/u-boot/u-boot>`__ |:snail:|
| `GitHub mirror <https://github.com/u-boot/u-boot>`__ |:zap:|\ |:zap:|\ |:zap:|

:el:`U-Boot stages <Panda How_to_MLO_&_u-boot#Introduction>`

.. table::

   ================ ================= ============
    File             `Use Case`__      `Header`__
   ================ ================= ============
    u-boot-spl.bin   peripheral boot   520 bytes
    MLO\ [#]_        `MMC loader`__
   ================ ================= ============

.. __: https://e2e.ti.com/support/processors/f/processors-forum/367260/what-is-the-difference-between-mlo-and-spl
.. __: https://stackoverflow.com/a/60880147
.. __: https://stackoverflow.com/a/34805466

| Gmail `search operators`__
| |b| `filter archived mails`__ with ``in:archive``
| |b| Search `lists.denx.de`__
|     |b2| `with Google`__
|     |b2| `with MARC`__

.. __: https://support.google.com/mail/answer/7190
.. __: https://webapps.stackexchange.com/questions/1168/can-i-see-only-mail-i-have-archived-in-gmail
.. __: https://lists.denx.de/listinfo
.. __: https://www.google.com/search?q=site:lists.denx.de
.. __: https://marc.info/?l=u-boot

.. :prlink:`history <https://github.com/u-boot/u-boot/commits/master/configs/am335x_boneblack_vboot_defconfig>\ `\ :pr:`of configs/am335x_boneblack_vboot_defconfig`

no need for verified boot, use ``configs/am335x_evm_defconfig`` instead\ [#]_

.. table::

   ========================================== ============= ================ ============
    config                                     version       u-boot-spl.bin   u-boot.img 
   ========================================== ============= ================ ============
    :pr:`configs/am335x_evm_defconfig`         `history`__
    configs/am335x_boneblack_vboot_defconfig   v2021.04      |O|              |O|
   ========================================== ============= ================ ============

.. __: https://github.com/u-boot/u-boot/commits/master/configs/am335x_boneblack_vboot_defconfig

make `FIT image <https://elinux.org/images/f/f4/Elc2013_Fernandes.pdf>`__
with :pkg:`community/uboot-tools` :manpage:`mkimage(1)`

| `README <https://github.com/u-boot>`__
  - *Building the Software:*
| AM335X/`README <https://github.com/u-boot/u-boot/tree/master/board/ti/am335x>`__

`DULG Introduction <https://www.denx.de/wiki/view/DULG/Introduction>`__
~ 2.3. Availability
~ `PDF manual <http://www.denx.de/wiki/publish/DULG/DULG-canyonlands.pdf>`__

`U-Boot on AM335x`_

| Guides on building u-boot
| |b| `TI <https://web.archive.org/web/20210114145232/https://processors.wiki.ti.com/index.php/AM335x_U-Boot_User's_Guide>`__
| |b| `PKGBUILD for other SoC <https://aur.archlinux.org/packages/?O=0&SeB=nd&K=u-boot&outdated=&SB=n&SO=a&PP=50&do_Search=Go>`__
| |b| `Buildroot <https://git.busybox.net/buildroot/tree/board/beaglebone/readme.txt>`__

.. Pentester Academy TV .. Embedded Linux Booting Process (Multi-Stage Bootloaders, Kernel, Filesystem)
.. youtube:: DV5S_ZSdK0s
   :height: 80
   :width: 100%

|

Get U-Boot
==========

|alpha|. from `ALARM`__ [R]_
----------------------------

.. __: https://archlinuxarm.org/platforms/armv7/ti/beaglebone-green-wireless

download :pkg:`alarm-armv7h/uboot-beaglebone`

::

   pacman -Qqlp uboot-beaglebone-2017.07-1-armv7h.pkg.tar.xz

.. | :manpage:`tar(1)` emits ``tar: Ignoring unknown extended header keyword 'SCHILY.fflags'``
.. | use :manpage:`bsdtar(1)`\ [#]_

extract with :manpage:`bsdtar(1)`
instead of :manpage:`tar(1)`
in case of ``tar: Ignoring unknown extended header keyword 'SCHILY.fflags'``\
[#]_

::

   # sha1sum -c ArchLinuxARM-am33x-latest.tar.gz.sha1sum
   # tar -x -v --no-xattrs --strip-components 1 -f ArchLinuxARM-am33x-latest.tar.gz "./boot"
   rm -rfv alarm_boot
   mkdir -pv alarm_boot
   bsdtar -x \
      -C "./alarm_boot" \
      -f uboot-beaglebone-2017.07-1-armv7h.pkg.tar.xz \
      --no-xattrs \
      --strip-components 1 \
      -v
   # tar -x \
   #    -v \
   #    --no-xattrs \
   #    --strip-components 1 \
   #    -f uboot-beaglebone-2017.07-1-armv7h.pkg.tar.xz \
   #    -C "./alarm_boot"

``MLO``
|rarr| `strip 520-byte header <https://e2e.ti.com/support/processors/f/processors-forum/321500/serial-boot-on-am3359-mlo-does-not-give-prompt>`__ |rarr|
u-boot-spl.bin

::

   # dd if=MLO of=u-boot-spl.bin bs=1 skip=520
   { [ -f alarm_boot/u-boot-spl.bin ] && echo error; } \
      || tail -c +521 alarm_boot/MLO >alarm_boot/u-boot-spl.bin
   diff -u10 \
      <(xxd -c 8 -u alarm_boot/MLO            | cut -d':' -f2-) \
      <(xxd -c 8 -u alarm_boot/u-boot-spl.bin | cut -d':' -f2-)

shortcut for minicom

::

   echo; \
      ls -Al alarm_boot; echo; \
      sudo rm -fv /root/MINICOM_RES; \
      sudo ln -sv "$(realpath alarm_boot)" "$_"; echo; \
      sudo ls -Al /root/MINICOM_RES/; echo

|beta|. build w/ buildroot
--------------------------

| bump :pkg:`AUR/buildroot-meta` according to latest `requirements <https://buildroot.org/downloads/manual/manual.html>`__
| install :pkg:`AUR/buildroot-meta`

| `download <https://buildroot.org/download.html>`__ buildroot
| it builds u-boot version ``boot/uboot/Config.in:BR2_TARGET_UBOOT_VERSION``
  (`git <https://git.busybox.net/buildroot/tree/boot/uboot/Config.in>`__)

get key\ [#gpgSR]_

::

   gpg --search-key --keyserver-options "http-proxy=http://127.0.0.1:8080" AB07D806D2CE741FB886EE50B025BA8B59C36319
   gpg --recv-keys  --keyserver-options "http-proxy=http://127.0.0.1:8080" AB07D806D2CE741FB886EE50B025BA8B59C36319

verify clear signed message of checksum\ [#gpgV]_

::

   gpg --verify buildroot-202?.??.?.tar.bz2.sign

verify tarball with checksum

::

   grep tar buildroot-202?.??.?.tar.bz2.sign
   md5sum buildroot-202?.??.?.tar.bz2
   sha1sum buildroot-202?.??.?.tar.bz2

| configure buildroot
| |b| `01 = little endian <https://serverfault.com/a/749469>`__
| |b| NEON\ |tm| `SIMD Coprocessor <https://www.ti.com/document-viewer/AM3358/datasheet/features-sprs7179524#sprs7179524>`__
| |b| NEON\ |:tm:| `SIMD Coprocessor <https://www.ti.com/document-viewer/AM3358/datasheet/features-sprs7179524#sprs7179524>`__

::

   $ hexdump -s 5 -n 1 -C ~/beaglebone/ArchLinuxARM_boot/initramfs-linux/bin/busybox
   00000005  01                                                |.|
   00000006

::

   Target options
      Target Architecture = ARM (little endian)
      Target Architecture Variant = cortex-A8
      Target ABI = EABIhf
      Floating point strategy = NEON
      ...

\...

|gamma|. build Manually
-----------------------

`contributing <https://archlinuxarm.org/wiki/Contributing>`__
- send PR to archlinuxarm/PKGBUILDs/\ `alarm/uboot-beaglebone <https://github.com/archlinuxarm/PKGBUILDs/tree/master/alarm/uboot-beaglebone>`__

| Docs » Build U-Boot » `Building with GCC <https://u-boot.readthedocs.io/en/latest/build/gcc.html>`__
| :el:`eLinux <Building_for_BeagleBone>`
| TI/`Create a Network Bootable U-Boot Image <https://web.archive.org/web/https://processors.wiki.ti.com/index.php/Sitara_Linux_Program_the_eMMC_on_Beaglebone_Black#Create_a_Network_Bootable_U-Boot_Image>`__

| :pkg:`AUR/distccd-alarm-armv7h`
| |b| :aw:`arch wiki <Distcc_Cross-Compiling>`
| |b| `alarm wiki <https://archlinuxarm.org/wiki/Distcc_Cross-Compiling>`__

.. table:: u-boot tarball

   =================== ========== =========
    Source              Name       GPG sig
   =================== ========== =========
    `nginx`__            202?.??   |O|
    `GitLab`__          v202?.?? 
    `GitHub mirror`__   v202?.?? 
   =================== ========== =========

.. __: https://ftp.denx.de/pub/u-boot/
.. __: https://source.denx.de/u-boot/u-boot/-/tags
.. __: https://github.com/u-boot/u-boot/tags

get key\ [#gpgSR]_

::

    gpg --search-key --keyserver-options "http-proxy=http://127.0.0.1:8080" 1A3C7F70E08FAB1707809BBF147C39FF9634B72C
    gpg --recv-keys  --keyserver-options "http-proxy=http://127.0.0.1:8080" 1A3C7F70E08FAB1707809BBF147C39FF9634B72C

verify tarball wigh signature\ [#gpgV]_

::

    gpg --verify u-boot-202?.??.tar.bz2.sig u-boot-202?.??.tar.bz2


`kbuild <https://www.kernel.org/doc/html/latest/kbuild/kconfig.html#menuconfig-color>`__

::

   make MENUCONFIG_COLOR=mono menuconfig

| :pkg:`core/linux-headers`/usr/lib/modules/$(uname -r)/build/scripts/
| |b| `diffconfig`__ - compare two .config files
| |b| `config`__ - manipulate options in a .config file

.. __: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/scripts/config
.. __: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/scripts/diffconfig

::

   cd ~/beaglebone
   source ~/beaglebone/u-boot.bashrc
   tar xf ~/beaglebone/u-boot-v2021.04.tar.bz2
   cd u-boot-*/
   make -j4 am335x_evm_defconfig
   make -j4 xconfig

Manually apply the following changes

.. code:: text

   Boot options - Autoboot options - Autoboot - ☐

.. code:: text

   # Command line interface - Device access commands - poweroff - ✓ # lib/efi_loader/efi_runtime.c:217: undefined reference to `do_poweroff'
   Command line interface - Device access commands - gpio     - ✓ # Command 'gpio' failed: Error -19

.. code:: text

   Environment - Environment is not stored          - ✓
   Environment - Environment is in a FAT filesystem - ☐

.. code:: text

   # Device Drivers - USB support - EHCI HCD (USB 2.0) support - ✓ # asm/arch/ehci.h not found
   #
   # CONFIG_USB_GADGET_VBUS_DRAW undeclared
   # Device Drivers - USB support - MUSB host mode support - ☐
   # Device Drivers - USB support - MUSB gadget mode support - ☐
   # Device Drivers - USB support - Enable TI OTG USB controller - ☐
   # Device Drivers - USB support - USB Gadget Support - ☐
   #
   # ASIX
   Device Drivers - USB support - USB to Ethernet Controller Drivers - ✓
   Device Drivers - USB support - USB to Ethernet Controller Drivers - ASIX AX8817X (USB 2.0) support - ✓
   Device Drivers - USB support - USB to Ethernet Controller Drivers - ASIX AX88179 (USB 3.0) support - ✓
   # Save

build

::

   make -j4 all && \
   ls -l O/{spl/u-boot-spl.bin,MLO,u-boot.img} && \
   sudo rm -rfv /root/MINICOM_RES && \
   sudo mkdir /root/MINICOM_RES && \
   for DEST in {spl/u-boot-spl.bin,u-boot.img}; do
     sudo ln -sv "$(realpath O)/$DEST" -t /root/MINICOM_RES/
   done

.. subsection
.. ~~~~~~~~~~

Make eMMC image
===============

|alpha|. with `genimage`__ [R]_
-------------------------------

.. __: https://github.com/pengutronix/genimage

| :pkg:`AUR/genimage`
| `genimage <https://git.busybox.net/buildroot/tree/package/genimage>`__\
  :superscript:`buildroot`

...

|beta|. manually
----------------

escalate

::

   $ su -
   #

zerofill (e.g. 1MiB)

::

   cd /tmp
   dd if=/dev/zero of=emmc.img bs=1 count=$((1024*1024))
   fdisk -l emmc.img

loop device

::

   losetup -l -a
   losetup -f --show -L -P -v emmc.img
   losetup -l -a
   fdisk -l /dev/loop0

partition

::

   fdisk /dev/loop0
   o
   n p 1 1 2047
   t 1 a
   w

format

::

   lsblk -f
   mkfs.fat -v /dev/loop0p1

write

::

   mkdir  /tmp/mnt
   mount -v /dev/loop0p1 /tmp/mnt
   cp -v ~/MLO /tmp/mnt
   sync
   cp -v ~/u-boot.img /tmp/mnt
   sync
   umount -v /tmp/mnt
   rmdir -v /tmp/mnt

cleanup

::

   losetup -l -a
   losetup -D
   losetup -l -a
   mv -v emmc.img ~/

Connect Serial Debug Port
=========================

Serial Send
===========

Write eMMC
==========

`ALARM <https://archlinuxarm.org/packages/armv7h/uboot-beaglebone/files/uboot-beaglebone.install>`__
- `boot.txt <https://archlinuxarm.org/packages/armv7h/uboot-beaglebone/files/boot.txt>`__

Power Off
=========

Footnotes
=========

.. [R]      Recommended

.. [#]      MLO = **M**\ MC **lo**\ ader
.. [#]      https://lists.denx.de/pipermail/u-boot/2021-May/449518.html
.. [#]      http://lifeonubuntu.com/tar-errors-ignoring-unknown-extended-header-keyword/
.. [#gpgSR] https://wiki.archlinux.org/title/GnuPG#Searching_and_receiving_keys
.. [#gpgV]  https://wiki.archlinux.org/title/GnuPG#Verify_a_signature

.. include:: link.txt

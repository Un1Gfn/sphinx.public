.. include:: substitution.txt

================
|ico| `U-Boot`__
================

.. __: https://www.denx.de/wiki/U-Boot

Misc
====

`Title Capitalization Tool <https://capitalizemytitle.com/>`__

| misterious article
| `<http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.set.boards/index.html>`__

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
  - *Monitor Commands - Overview:*
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

download :pkg:`alarm-armv7h/uboot-beaglebone` ::

   pacman -Qqlp uboot-beaglebone-2017.07-1-armv7h.pkg.tar.xz

.. | :manpage:`tar(1)` emits ``tar: Ignoring unknown extended header keyword 'SCHILY.fflags'``
.. | use :manpage:`bsdtar(1)`\ [#]_

extract with :manpage:`bsdtar(1)`
instead of :manpage:`tar(1)`
in case of ``tar: Ignoring unknown extended header keyword 'SCHILY.fflags'``\
[#]_\ ::

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
u-boot-spl.bin ::

   # dd if=MLO of=u-boot-spl.bin bs=1 skip=520
   { [ -f alarm_boot/u-boot-spl.bin ] && echo error; } \
      || tail -c +521 alarm_boot/MLO >alarm_boot/u-boot-spl.bin
   diff -u10 \
      <(xxd -c 8 -u alarm_boot/MLO            | cut -d':' -f2-) \
      <(xxd -c 8 -u alarm_boot/u-boot-spl.bin | cut -d':' -f2-)

shortcut for minicom::

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

get key\ [#gpgSR]_ ::

   gpg --search-key --keyserver-options "http-proxy=http://127.0.0.1:8080" AB07D806D2CE741FB886EE50B025BA8B59C36319
   gpg --recv-keys  --keyserver-options "http-proxy=http://127.0.0.1:8080" AB07D806D2CE741FB886EE50B025BA8B59C36319

verify clear signed message of checksum\ [#gpgV]_ ::

   gpg --verify buildroot-202?.??.?.tar.bz2.sign

verify tarball with checksum ::

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

.. https://docs.readthedocs.io/en/stable/guides/cross-referencing-with-sphinx.html
.. _reference_label_u-boot_build_manually:

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

get key\ [#gpgSR]_ ::

    gpg --search-key --keyserver-options "http-proxy=http://127.0.0.1:8080" 1A3C7F70E08FAB1707809BBF147C39FF9634B72C
    gpg --recv-keys  --keyserver-options "http-proxy=http://127.0.0.1:8080" 1A3C7F70E08FAB1707809BBF147C39FF9634B72C

verify tarball wigh signature\ [#gpgV]_ ::

    gpg --verify u-boot-202?.??.tar.bz2.sig u-boot-202?.??.tar.bz2

`kbuild <https://www.kernel.org/doc/html/latest/kbuild/kconfig.html#menuconfig-color>`__ ::

   make MENUCONFIG_COLOR=mono menuconfig

| :pkg:`core/linux-headers`/usr/lib/modules/$(uname -r)/build/scripts/
| |b| `diffconfig`__ - compare two .config files
| |b| `config`__ - manipulate options in a .config file

.. __: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/scripts/config
.. __: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/scripts/diffconfig

tools/`genboardscfg.py <https://github.com/u-boot/u-boot/blob/master/tools/genboardscfg.py>`__

::

   cd ~/beaglebone
   source ~/beaglebone/u-boot.bashrc
   tar xf ~/beaglebone/u-boot-v2021.04.tar.bz2
   cd u-boot-*/
   make -j4 am335x_evm_defconfig
   make -j4 xconfig

Manually apply the following changes

``Boot options -``

.. code:: text

   - Autoboot options - Autoboot - ☐

``Command line interface -``

.. code:: text

   # - Device access commands - poweroff - ✓ # lib/efi_loader/efi_runtime.c:217: undefined reference to `do_poweroff'
   - Device access commands - gpio     - ✓ # Command 'gpio' failed: Error -19

``Environment -``

.. code:: text

   - Environment is not stored          - ✓
   - Environment is in a FAT filesystem - ☐

``Device Drivers - USB support -``

.. code:: text

   # - EHCI HCD (USB 2.0) support - ✓ # asm/arch/ehci.h not found
   #
   # CONFIG_USB_GADGET_VBUS_DRAW undeclared
   # - MUSB host mode support - ☐
   # - MUSB gadget mode support - ☐
   # - Enable TI OTG USB controller - ☐
   # - USB Gadget Support - ☐
   #
   # ASIX
   - USB to Ethernet Controller Drivers - ✓
   - USB to Ethernet Controller Drivers - ASIX AX8817X (USB 2.0) support - ✓
   - USB to Ethernet Controller Drivers - ASIX AX88179 (USB 3.0) support - ✓
   # Save

build::

   make -j4 all && \
   ls -l O/{spl/u-boot-spl.bin,MLO,u-boot.img} && \
   sudo rm -rfv /root/MINICOM_RES && \
   sudo mkdir /root/MINICOM_RES && \
   for DEST in {spl/u-boot-spl.bin,u-boot.img}; do
     sudo ln -sv "$(realpath O)/$DEST" -t /root/MINICOM_RES/
   done

check output ::

   git check-ignore * | xargs file
   file * spl/* | grep -v -F -e ASCII -e directory | less -S
   find . -type f -a \( \
        -iname GARBAGE"       \
     -o -iname "*bin"         \
     -o -iname "*dtb"         \
     -o -iname "*img"         \
     -o -iname "*spl"         \
     -o -iname "*spl*bin*"    \
     -o -iname "*spl*dtb*"    \
     -o -iname "*spl*img*"    \
     -o -iname "*u-boot"      \
     -o -iname "*u-boot*bin*" \
     -o -iname "*u-boot*dtb*" \
     -o -iname "*u-boot*img*" \
     -o -iname "mlo*"         \
   \)



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

escalate::

   $ su -
   #

zerofill (e.g. 1MiB)::

   cd /tmp
   dd if=/dev/zero of=emmc.img bs=1 count=$((1024*1024))
   fdisk -l emmc.img

loop device::

   losetup -l -a
   losetup -f --show -L -P -v emmc.img
   losetup -l -a
   fdisk -l /dev/loop0

partition::

   fdisk /dev/loop0
   o
   n p 1 1 2047
   t 1 a
   w

format::

   lsblk -f
   mkfs.fat -v /dev/loop0p1

write::

   mkdir  /tmp/mnt
   mount -v /dev/loop0p1 /tmp/mnt
   cp -v ~/MLO /tmp/mnt
   sync
   cp -v ~/u-boot.img /tmp/mnt
   sync
   umount -v /tmp/mnt
   rmdir -v /tmp/mnt

cleanup::

   losetup -l -a
   losetup -D
   losetup -l -a
   mv -v emmc.img ~/

Connect Serial Debug Port
=========================

:el:`BB serial port <BeagleBone/Serial_Port>`

| lsusb\
| |b| `067b:2303 <https://linux-hardware.org/?id=usb:067b-2303>`__
| |b| ``Prolific Technology, Inc. PL2303 Serial Port / Mobile Action MA-8910P``

`The acme of foolishness <https://dave.cheney.net/2013/09/22/two-point-five-ways-to-access-the-serial-console-on-your-beaglebone-black>`__ ::

> the red wire, this carries +5v from the USB port and can blow the arse out of your BBB
> you must leave it unconnected
> Do not connect the red lead to anything!

:el:`eLinux <Beagleboard:BeagleBone_Black_Serial>` ::

> an extra RED wire on this cable that supplies 5V @ 500mA
> which could power the board if connected to one of the VDD_5V pins (P9_05, P9_06)
> Just leave it unconnected.

.. warning::

   | Don't supply any power to BBGW yet.
   | Don't connect PL2303 USB-A to PC yet.

.. https://docutils.sourceforge.io/docs/ref/rst/directives.html#table
.. table:: pinout
   :align: left
   :widths: auto

   ======== ================== ==== ==== ===== ================== ====
    \        1                  2    3    4     5                  6
   ======== ================== ==== ==== ===== ================== ====
    BBGW     GND                NC   NC   RX    TX                 NC
    PL2303   |:black_circle:|   NC   NC   |O|   |:white_circle:|   NC
   ======== ================== ==== ==== ===== ================== ====

1. Double check the connection
2. Connect PL2303 USB-A to PC
3. Hold :kbd:`USER`
4. Supply 5v :stlink:`?A <https://electronics.stackexchange.com/questions/563406/which-wall-charger-for-beaglebone-green-wireless>`
   power through Micro-USB
5. Wait for 5 seconds
6. Release :kbd:`USER`
7. Make sure ``lsusb | grep -i prolific`` reveals ``PL2303``


Serial Send
===========

`SystemSetup < DULG < DENX <http://www.denx.de/wiki/view/DULG/SystemSetup#Section_4.3>`__

lists.denx.de `minicom+kermit <https://lists.denx.de/pipermail/u-boot/2003-June/001527.html>`__

`DULG <https://www.denx.de/wiki/view/DULG/SystemSetup>`__
- :aw:`ArchWiki <Working_with_the_serial_console>`
- :el:`eLinux <Beagleboard:BeagleBone_Black_Accessories#Serial_Debug_Cables>`

.. https://docutils.sourceforge.io/docs/ref/rst/directives.html#table
.. table:: parameters
   :align: left
   :widths: auto

   =========== =========
   =========== =========
    Baud        115,200
    Bits        8
    Parity      N
    Stop Bits   1
    Handshake   None
   =========== =========

..  Fastbit Embedded Brain Academy .. Beaglebone Black Serial booting procedure ( UART BOOT )
.. youtube:: 3y1LMNPoaJI
   :height: 80
   :width: 100%

|

.. warning::
   Make sure :pkg:`community/lrzsz` is installed.

escalate ::

   su -

run minicom ::

   # --metakey
   minicom \
     -c off \
     -b 115200 \
     -8 \
     --device /dev/ttyUSB0

Wait for at most 30 seconds until ``CCC...`` appears in minicom console

:kbd:`<CTRL+A>` |rarr| :kbd:`<S>` |rarr| xmodem |rarr| ``[MINICOM_RES]``

.. warning::

   | Don't use ``MLO``.
   | ``MLO`` is for booting from eMMC.
   | Use ``u-boot-spl.bin``.

locate ``u-boot-spl.bin`` and send (xmodem)

locate ``u-boot.img`` and send (either xmodem or ymodem)

press :kbd:`<SPACE>`

check U-Boot version ::

   => version

Write eMMC
==========

`ALARM <https://archlinuxarm.org/packages/armv7h/uboot-beaglebone/files/uboot-beaglebone.install>`__
- `boot.txt <https://archlinuxarm.org/packages/armv7h/uboot-beaglebone/files/boot.txt>`__

`mmc <https://www.denx.de/wiki/view/DULG/UBootCmdGroupMMC>`__

.. code:: text

   mmc list
   mmc dev 1
   mmc info
   mmc part

erase

.. tip::
   | eMMC block size is ``512B``\ :superscript:`citation needed`
   | ``0x5000blk * 512B/blk = 20480blk * 512B/blk`` (=10485760B=10*1024*1024B=\ **10MiB**\ )
   | Therefore the following are roughly equivalent
   | |b| mmc erase 0 0x5000
   | |b| dd if=/dev/zero of=/dev/mmcblk0 bs=512 count=20480

.. code:: text

   mmc erase 0 0x5000
   mmc rescan
   mmc part

| zerofill 1MiB RAM, starting from 0x82000000
| |b| `cmp`__.b - compare byte
| |b| `mw`__.b - memory write byte

.. __: https://www.denx.de/wiki/view/DULG/UBootCmdGroupMemory#Section_5.9.2.3.
.. __: https://www.denx.de/wiki/view/DULG/UBootCmdGroupMemory#Section_5.9.2.8.

.. tip::
   | RAM block size is ``1B``
   | ``0x100000blk * 1B/blk = 0x100000B = 1048576B = 1024 * 1024B = 1MiB``

.. code:: text

   cmp.b   0x100000 0x82000000 0x100000
   mw.b  0x82000000          0 0x100000
   cmp.b   0x100000 0x82000000 0x100000

| xmodem send eMMC image to RAM
| md.b - memory display byte

.. code:: text

   loadx 0x82000000 115200
   md.b  0x82000000 0x4

dump eMMC image from RAM to eMMC
- `mmc <https://www.denx.de/wiki/view/DULG/UBootCmdGroupMMC>`__

.. tip::
   ``0x800 * 512B = 2048 * 512B = 1048576B = 1024 * 1024B = 1MiB``

.. code:: text

   mmc list
   mmc dev 1
   mmc info
   mmc part
   mmc write 0x82000000 0 0x800
      MMC write: dev # 1, block # 0, count 2048 ... 2048 blocks written: OK

verify partition layout

.. code:: text

   mmc part
      Partition Map for MMC device 1  --   Partition Type: DOS

      Part    Start Sector    Num Sectors     UUID            Type
        1     1               2047            01d0a302-01     01
   mmc rescan
   mmc part
      # Should be the same as prevous one

view installed MLO

.. warning::

   | There shouldn't be ``u-boot-spl.bin`` here.
   | Expect ``MLO``.

.. code:: text

   fatls mmc 1

Power Off
=========

1. Unplug PL2303 USB-A from PC
2. Press and hold :kbd:`POWER` button
3. When LED ``PWR`` goes off (approx 8s)
   `release POWER button immediately <https://github.com/beagleboard/beaglebone-black/wiki/System-Reference-Manual#power-button>`__
4. Clean up

::

   lsusb | grep -i prolific
   ./usbreset /dev/bus/usb/...
   lsusb | grep -i prolific

Footnotes
=========

.. [R]      Recommended

.. [#]      MLO = **M**\ MC **lo**\ ader
.. [#]      https://lists.denx.de/pipermail/u-boot/2021-May/449518.html
.. [#]      http://lifeonubuntu.com/tar-errors-ignoring-unknown-extended-header-keyword/
.. [#gpgSR] https://wiki.archlinux.org/title/GnuPG#Searching_and_receiving_keys
.. [#gpgV]  https://wiki.archlinux.org/title/GnuPG#Verify_a_signature

.. include:: link.txt

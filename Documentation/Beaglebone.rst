.. `x <y>`_  Named hyperlink reference
.. `x <y>`__ Anonymous hyperlink reference

========================================================
`Beaglebone <http://www.github.com/Un1Gfn/beaglebone>`__
========================================================

`AM3358 <https://www.ti.com/product/AM3358>`__ =
`Cortex-A8 <https://en.wikipedia.org/wiki/ARM_Cortex-A8>`__ =
`ARMv7-A <https://en.wikipedia.org/wiki/Comparison_of_ARMv7-A_cores>`__ =
32-bit w/ FPU =
`gnueabihf <https://wiki.debian.org/Multiarch/Tuples#armhf>`__

| `Allwinner V5 eMMC Support List <http://files.lindeni.org/lindenis-v5/documents/support_list/Allwinner%C2%A0V5%20eMMC%C2%A0Support%C2%A0List.pdf>`__
| |b| MTFC8GAKAJCN-1M WT / `Micron MTFC4GACAJCN-1M WT <https://www.micron.com/products/managed-nand/emmc/part-catalog/mtfc8gakajcn-1m-wt>`__ (possibly 6FA27-JY976)

Prog.World - `eMMC 5.0 sequential write 90MB/s <https://prog.world/nvme-vs-ufs-3-1-the-battle-of-smartphone-memory-types-parsing/>`__

`BBGW schematics <https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green_Wireless/master/resources/BeagleBone_Green%20Wireless_V1.0_SCH_20160314.pdf>`__

`Arch Linux ARM <https://archlinuxarm.org/platforms/armv7/ti/beaglebone-green-wireless>`__

`eLinux/Toolchains <https://elinux.org/Toolchains>`__

Distro
======

| `Void Linux <https://voidlinux.org/>`__
| |b| `packages <https://voidlinux.org/packages/>`__
| |b| `void-beaglebone-musl-\*.img.xz <https://a-hel-fi.m.voidlinux.org/live/current/>`__ extract |asymp| 2000 MiB sparse live image
| |b| `void-beaglebone-musl-\*.tar.xz <https://a-hel-fi.m.voidlinux.org/live/current/>`__ extract |asymp| 400 MiB rootfs tarball `howto <https://wiki.voidlinux.org/Beaglebone>`__

| `Buildroot <https://buildroot.org/>`__ (build images on CircleCI)
| |b| `packages <https://git.busybox.net/buildroot/tree/package>`__

| `yocto <https://www.yoctoproject.org/>`__ (build images on CircleCI)
| |b| `packages <https://layers.openembedded.org/layerindex/branch/master/recipes/>`__

Communications
==============

.. role:: raw-html(raw)

    :format: html

.. |br| replace:: :raw-html:`<br />`

.. |r| replace:: `recovery guide <https://elinux.org/AM335x_recovery>`__

.. table:: Tutorials

  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  |                 |                                                  |          Build          |           |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  | Tutorial        | [#u]_    | `TFTP`_ | `BOOTP`_ | Serial | Mass    | Boot   | Kernel | User- | NFS | SSH |
  |                 | |br|     |         |          |        | |br|    | |br|   |        | |br|  |     |     |
  |                 | `RNDIS`_ |         |          |        | Storage | Loader |        | space |     |     |
  +=================+==========+=========+==========+========+=========+========+========+=======+=====+=====+
  | `techniq`_      | |O|      |         |          | |O|    | |O|     |        |        |       |     |     |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  | `BBBlfs`_       | |O|      |         |          |        |         | |O|    | |O|    | |O|   |     |     |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  | [#p]_ [#b]_     | |O|      | |O|     | |O|      |        |         | |O|    |        |       |     |     |
  | |br| |r|        |          |         |          |        |         |        |        |       |     |     |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  | `U-boot \       | |O|      | |O|     |          | |O|    |         | |O|    |        |       | |O| |     |
  | on AM335x`_     |          |         |          |        |         |        |        |       |     |     |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  | `terminal \     |          |         |          | |O|    |         |        |        |       |     | |O| |
  | shells`_        |          |         |          |        |         |        |        |       |     |     |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  | `Android \      | |O|      |         |          |        |         |        |        |       |     | |O| |
  | USB SSH`_       |          |         |          |        |         |        |        |       |     |     |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  | [#g_ether]_     | |O|      |         |          |        |         |        |        |       |     |     |
  | |br| `deleted   |          |         |          |        |         |        |        |       |     |     |
  | SU question`_   |          |         |          |        |         |        |        |       |     |     |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  | `RidgeRun`_     | |O|      |         |          |        |         |        |        |       | |O| |     |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  | `eLinux image`_ |          |         |          |        |         | |O|    | |O|    | |O|   |     |     |
  | (obselete)      |          |         |          |        |         |        |        |       |     |     |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  | eLinux |br|     |          |         |          | |O|    |         | |O|    | |O|    |       |     |     |
  | `beagleboard`_  |          |         |          |        |         |        |        |       |     |     |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  | `nfs-\          |          | |O|     |          |        |         |        |        |       | |O| |     |
  | kernel-\        |          |         |          |        |         |        |        |       |     |     |
  | server`_        |          |         |          |        |         |        |        |       |     |     |
  |                 |          |         |          |        |         |        |        |       |     |     |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+

Device
======

| eLinux wiki
| |b| `BB generations brief <https://elinux.org/BeagleBone_Community>`__
| |b| `BB <https://elinux.org/BeagleBoard_Community>`__
| |b| `BBB <https://elinux.org/Beagleboard:BeagleBoneBlack>`__
| |b| `BBBW <https://elinux.org/Beagleboard:BeagleBoneBlackWireless>`__

| Official wiki
| |b| `BBB <https://github.com/beagleboard/beaglebone-black/wiki/System-Reference-Manual>`__
| |b| `BBGW <http://wiki.seeedstudio.com/BeagleBone_Green_Wireless/#specification>`__

| Serial port
| |b| eLinux [#bbs]_ [#tssc]_
| |b| `unix stackexchange <https://unix.stackexchange.com/questions/22545/how-to-connect-to-a-serial-port-as-simple-as-using-ssh>`__
| |b| nixCraft [#folspws]_ [#cmdsc]_
| |b| `dummies <https://www.dummies.com/computers/beaglebone/how-to-connect-the-beaglebone-black-via-serial-over-usb/>`__
| |b| `rpi stackexchange <https://raspberrypi.stackexchange.com/a/15825/71791>`__
| |b| `askubuntu <https://askubuntu.com/a/474560/634976>`__

| UART
| |b| `YouTube <https://www.youtube.com/watch?v=3y1LMNPoaJI>`__
| |b| `TI <https://web.archive.org/web/20210114145232/https://processors.wiki.ti.com/index.php/AM335x_U-Boot_User's_Guide#Boot_Over_UART>`__

CPU
===

`Sitara AM3358 <http://www.ti.com/product/AM3358>`__ ~
`Arm Cortex-A8 <https://en.wikipedia.org/wiki/ARM_Cortex-A8>`__ ~
32-bit `armhf <https://wiki.debian.org/ArmHardFloatPort#Supported_devices>`__
`ArmEabiPort <https://wiki.debian.org/ArmEabiPort>`__
`arm-linux-gnueabihf- <https://wiki.debian.org/ArmHardFloatPort#Rationale>`__
[#preq]_

| `Functional Block Diagram <http://www.ti.com/data-sheets/diagram.tsp?genericPartNumber=AM3358&diagramId=SPRS717K>`__
| Docs `latest rev <http://www.ti.com/product/AM3358/technicaldocuments>`__
| |b| Datasheet ~ AM335x Sitara™ Processors datasheet `trunc rev <http://www.ti.com/lit/gpn/am3358>`__
|     |b| "Functional Block Diagram" ~ Page 5 (1.4)
| |b| User guides ~ AM335x and AMIC110 Sitara™ Processors Technical Reference Manual `trunc rev <http://www.ti.com/lit/pdf/spruh73>`__
|     |b| "Memery Map" ~ Page 117 (2.1)
|     |b| "Public ROM Code Architecture" (xmodem) ~ Page 5019 (26.1.2) (Figure 26-1)
| `Boot process <https://processors.wiki.ti.com/index.php/AM335x_board_bringup_tips>`__
| `U-Boot on AM335x`

.. https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#transitions

`U-boot <https://www.denx.de/wiki/U-Boot>`__
============================================

Pentester Academy - `Embedded Linux Booting Process <https://www.youtube.com/watch?v=DV5S_ZSdK0s>`__

`FIT image <https://elinux.org/images/f/f4/Elc2013_Fernandes.pdf>`__

| repo `README <https://github.com/u-boot>`__ (GitHub mirror)
| |b| "Building the Software:"
| |b| AM335X `README <https://github.com/u-boot/u-boot/tree/master/board/ti/am335x>`__

`DULG Introduction <https://www.denx.de/wiki/view/DULG/Introduction>`__ ~ 2.3. Availability ~ `manual in PDF <http://www.denx.de/wiki/publish/DULG/DULG-canyonlands.pdf>`__

`U-Boot on AM335x`_

| guides on building u-boot
| |b| `Texus Instruments <https://web.archive.org/web/https://processors.wiki.ti.com/index.php/AM335x_U-Boot_User's_Guide>`__
| |b| `PKGBUILD for other SoC <https://aur.archlinux.org/packages/?O=0&SeB=nd&K=u-boot&outdated=&SB=n&SO=a&PP=50&do_Search=Go>`__
| |b| `Buildroot <https://git.busybox.net/buildroot/tree/board/beaglebone/readme.txt>`__

Toolchain
=========

.. https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#character-level-inline-markup-1

| arm-linux-gnueabi\ **hf**\ -gcc
  (`AUR <https://aur.archlinux.org/packages/arm-linux-gnueabihf-gcc/>`__)
| `Arago TI-SDK <http://arago-project.org/wiki/index.php/Setting_Up_Build_Environment>`__ [#preq]_

`BusyBox <https://www.busybox.net/>`__
======================================

`udhcpc <https://en.wikipedia.org/wiki/Udhcpc>`__

| ip & mask
| |b| `NexGenT <https://www.youtube.com/watch?v=ddM9AcreVqY&list=PLl9NdZbdtA0wK8OIgttkScKRxcMkvoev_>`__
| |b| `Eli the Computer Guy <https://www.youtube.com/watch?v=EkNq4TrHP_U>`__

libc
====

| |b| `musl/uClibc/dietlibc/glibc <http://www.etalabs.net/compare_libcs.html>`__
| |b| `uClibc->musl <https://elinux.org/images/e/eb/Transitioning_From_uclibc_to_musl_for_Embedded_Development.pdf>`__


QEMU
===============

| |b| `U&L <https://unix.stackexchange.com/questions/41889/how-can-i-chroot-into-a-filesystem-with-a-different-architechture>`__
| |b| `AUR <https://aur.archlinux.org/packages/?O=0&K=qemu+static>`__
| |b| `binfmt <https://en.wikipedia.org/wiki/Binfmt_misc>`__
| |b| `Gentoo wiki <https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Compiling_with_qemu_user_chroot>`__
| |b| `Debian wiki <https://wiki.debian.org/QemuUserEmulation>`__

----

.. [#u] https://en.wikipedia.org/wiki/Ethernet_over_USB
.. [#p] https://www.pengutronix.de/en/software/barebox.html
.. [#b] https://www.barebox.org/
.. [#g_ether] https://github.com/techniq/wiki/wiki/Linux-USB-Gadget-API#network-g_ether
.. [#bbs] https://elinux.org/Beagleboard:BeagleBone_Black_Serial
.. [#tssc] https://elinux.org/Beagleboard:Terminal_Shells#Serial_Connect
.. [#folspws] https://www.cyberciti.biz/faq/find-out-linux-serial-ports-with-setserial
.. [#cmdsc] https://www.cyberciti.biz/hardware/5-linux-unix-commands-for-connecting-to-the-serial-console
.. [#preq] https://web.archive.org/web/20210114145232/https://processors.wiki.ti.com/index.php/AM335x_U-Boot_User's_Guide#Prerequisite

.. _Android USB SSH: https://stackoverflow.com/questions/44926644/control-beaglebone-black-linux-with-android-smartphone-through-usb-cable
.. _BBBlfs: https://github.com/ungureanuvladvictor/BBBlfs>
.. _BOOTP: https://en.wikipedia.org/wiki/Bootstrap_Protocol
.. _RNDIS: https://en.wikipedia.org/wiki/RNDIS
.. _RidgeRun: https://developer.ridgerun.com/wiki/index.php/How_to_use_USB_device_networking
.. _TFTP: https://en.wikipedia.org/wiki/Trivial_File_Transfer_Protocol
.. _U-Boot on AM335x: https://web.archive.org/web/20210114145232/https://processors.wiki.ti.com/index.php/AM335x_U-Boot_User's_Guide
.. _beagleboard: https://elinux.org/BeagleBoard_Community
.. _deleted SU question: https://superuser.com/questions/1529130/linux-tethering-ethernet-over-usb-network-device-usb0-not-exposed-after-loading
.. _eLinux image: https://elinux.org/Beagleboard:BeagleBoneBlack_Rebuilding_Software_Image
.. _nfs-kernel-server: https://bootlin.com/blog/tftp-nfs-booting-beagle-bone-black-wireless-pocket-beagle
.. _techniq: https://github.com/techniq/wiki/wiki/Linux-USB-Gadget-API
.. _terminal shells: https://elinux.org/Beagleboard:Terminal_Shells

.. https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#transitions

----

.. include:: unicode.rst

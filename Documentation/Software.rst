==============
|ico| Software
==============

`BusyBox <https://www.busybox.net/>`__
======================================

`udhcpc <https://en.wikipedia.org/wiki/Udhcpc>`__

| ip & mask
| |b| `NexGenT <https://www.youtube.com/watch?v=ddM9AcreVqY&list=PLl9NdZbdtA0wK8OIgttkScKRxcMkvoev_>`__
| |b| `Eli the Computer Guy <https://www.youtube.com/watch?v=EkNq4TrHP_U>`__

Distro
======

`Arch Linux ARM <https://archlinuxarm.org/platforms/armv7/ti/beaglebone-green-wireless>`__

| `Void Linux <https://voidlinux.org/>`__
| |b| `packages <https://voidlinux.org/packages/>`__
| |b| `void-beaglebone-musl-\*.img.xz <https://a-hel-fi.m.voidlinux.org/live/current/>`__ extract |asymp| 2000 MiB sparse live image
| |b| `void-beaglebone-musl-\*.tar.xz <https://a-hel-fi.m.voidlinux.org/live/current/>`__ extract |asymp| 400 MiB rootfs tarball `howto <https://wiki.voidlinux.org/Beaglebone>`__

| `Buildroot <https://buildroot.org/>`__ (build images on CircleCI)
| |b| `packages <https://git.busybox.net/buildroot/tree/package>`__

| `yocto <https://www.yoctoproject.org/>`__ (build images on CircleCI)
| |b| `packages <https://layers.openembedded.org/layerindex/branch/master/recipes/>`__

libc
====

| |b| `musl/uClibc/dietlibc/glibc <http://www.etalabs.net/compare_libcs.html>`__
| |b| `uClibc->musl <https://elinux.org/images/e/eb/Transitioning_From_uclibc_to_musl_for_Embedded_Development.pdf>`__

QEMU
====

| |b| `U&L <https://unix.stackexchange.com/questions/41889/how-can-i-chroot-into-a-filesystem-with-a-different-architechture>`__
| |b| `AUR <https://aur.archlinux.org/packages/?O=0&K=qemu+static>`__
| |b| `binfmt <https://en.wikipedia.org/wiki/Binfmt_misc>`__
| |b| `Gentoo wiki <https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Compiling_with_qemu_user_chroot>`__
| |b| `Debian wiki <https://wiki.debian.org/QemuUserEmulation>`__

Toolchain
=========

`eLinux/Toolchains <https://elinux.org/Toolchains>`__

.. https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#character-level-inline-markup-1

| arm-linux-gnueabi\ **hf**\ -gcc
  (`AUR <https://aur.archlinux.org/packages/arm-linux-gnueabihf-gcc/>`__)
| `Arago TI-SDK <http://arago-project.org/wiki/index.php/Setting_Up_Build_Environment>`__ [#w]_

`U-Boot <https://www.denx.de/wiki/U-Boot>`__
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

.. https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#transitions

----

.. Footnotes

.. [#w] https://web.archive.org/web/20210114145232/https://processors.wiki.ti.com/index.php/AM335x_U-Boot_User's_Guide#Prerequisite

.. include:: link.rst

.. include:: substitution.rst

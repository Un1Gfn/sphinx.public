.. include:: substitution.txt

==============
|ico| Software
==============

Toolchain
=========

eLinux/:el:`Toolchains`

.. https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#character-level-inline-markup-1
.. arm-linux-gnueabi\ **hf**\ -gcc

:pkg:`AUR/arm-linux-gnueabihf-gcc`

`Arago TI-SDK <http://arago-project.org/wiki/index.php/Setting_Up_Build_Environment>`__\ [#w]_

`BusyBox`__
===========

.. __: https://www.busybox.net/

| busybox :wp:`udhcpc <Udhcpc>`
| busybox `ip <https://web.archive.org/web/https://www.busybox.net/downloads/BusyBox.html#ip>`__

.. Eli the Computer Guy .. TCP/IP and Subnet Masking
.. youtube:: EkNq4TrHP_U
   :width: 100%
   :height: 80

|

`IPv4 Addressing - A Comprehensive Lesson <https://www.youtube.com/playlist?list=PLl9NdZbdtA0wK8OIgttkScKRxcMkvoev_>`__

.. NexGenT .. IPv4 Addressing Lesson 1: Binary and the IP Address MADE EASY
.. youtube:: ddM9AcreVqY
   :width: 100%
   :height: 80

|

libc
====

| |b| `musl/uClibc/dietlibc/glibc <http://www.etalabs.net/compare_libcs.html>`__
| |b| :el:`uClibc->musl <images/e/eb/Transitioning_From_uclibc_to_musl_for_Embedded_Development.pdf>`

Other Distros
=============

| https://beagleboard.org/latest-images
| |b| Debian
| |b| Ångström (at the bottom of the page) (:wp:`Wikipedia <Ångström_distribution>`) (:el:`eLinux <BeagleBoardAngstrom>`)

| `Void Linux <https://voidlinux.org/>`__
| |b| `packages <https://voidlinux.org/packages/>`__
| |b| `void-beaglebone-musl-\*.img.xz`__ extract |asymp| 2000 MiB sparse live image
| |b| `void-beaglebone-musl-\*.tar.xz`__ extract |asymp| 400 MiB rootfs tarball `howto <https://wiki.voidlinux.org/Beaglebone>`__

.. __: https://a-hel-fi.m.voidlinux.org/live/current/
.. __: https://a-hel-fi.m.voidlinux.org/live/current/

| `Buildroot <https://buildroot.org/>`__ (build images on CircleCI)
| |b| `packages <https://git.busybox.net/buildroot/tree/package>`__

| `yocto <https://www.yoctoproject.org/>`__ (build images on CircleCI)
| |b| `packages <https://layers.openembedded.org/layerindex/branch/master/recipes/>`__

QEMU
====

| `chroot + qemu-arm-static <https://unix.stackexchange.com/questions/41889/how-can-i-chroot-into-a-filesystem-with-a-different-architechture>`__
| |b| AUR/`qemu+static <https://aur.archlinux.org/packages/?O=0&K=qemu+static>`__
| |b| :wp:`binfmt <Binfmt_misc>`
| |b| :gw:`Gentoo Wiki <Embedded_Handbook/General/Compiling_with_qemu_user_chroot>`
| |b| :dw:`Debian Wiki <QemuUserEmulation>`

| `Keys in the character backend multiplexer <https://qemu-project.gitlab.io/qemu/system/mux-chardev.html>`__
| |b| :kbd:`<CTRL-A><X>` to exit emulator

| `try u-boot with qemu <https://dev.to/rulyrudel/how-to-execute-u-boot-on-qemu-system-arm-2b22>`__
| |b| QEMU wiki `Platforms/ARM <https://wiki.qemu.org/Documentation/Platforms/ARM>`__
| |b| :pr:`qemu-system-arm -machine vexpress-a9` vexpress_ca9x4_defconfig vanished
| |b| ``qemu-system-arm -machine virt`` w/ ``make -j4 qemu_arm_defconfig``

.. https://docs.readthedocs.io/en/stable/guides/cross-referencing-with-sphinx.html

:ref:`build u-boot <reference_label_u-boot_build_manually>`

run qemu ::

   qemu-system-arm \
      -machine virt \
      -nographic \
      -no-reboot \
      -kernel ./O/u-boot

----

.. [#w] https://web.archive.org/web/20210114145232/https://processors.wiki.ti.com/index.php/AM335x_U-Boot_User's_Guide#Prerequisite

.. include:: link.txt

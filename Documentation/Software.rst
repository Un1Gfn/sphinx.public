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

Misc
----

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

| 9p
| |b| `9p <https://superuser.com/q/628169>`__
| |b| `9p_fstab <https://unix.stackexchange.com/a/94253>`__
| |b| `virtfs_kvm <http://www.linux-kvm.org/page/VirtFS>`__
| |b| `9p_vs_nfs <https://unix.stackexchange.com/a/240309>`__

standalone app

::

   qemu-arm-static \
     -L ~/beaglebone/alarm_root/ \
     usr/bin/uname -a


`Binfmt`__
----------

.. __: https://en.wikipedia.org/wiki/Binfmt_misc

:gw:`qemu-wrapper.c <Embedded_Handbook/General/Compiling_with_qemu_user_chroot#Setup_chroot>`

abuse binfmt [#gobinfmt]_ [#itbinfmt]_ [#jpbinfmt]_ [#kdocbinfmt]_ [#kdocbinfmtjava]_

`/usr/lib/binfmt.d/mono.conf <https://github.com/archlinux/svntogit-packages/blob/packages/mono/trunk/mono.binfmt.d>`__

.. code:: text

   :CLR:M::MZ::/usr/bin/mono:

.. code:: shell-session

   # cat /proc/sys/fs/binfmt_misc/CLR
   enabled
   interpreter /usr/bin/mono
   flags:
   offset 0
   magic 4d5a

Initramfs
---------

| `initramfs 101 <https://web.archive.org/web/20160730094856/http://wiki.sourcemage.org/HowTo(2f)Initramfs.html>`__
| |b| `summary <https://unix.stackexchange.com/a/126222>`__

inspect

::

   rm -rfv /tmp/initramfs*
   cd /tmp
   unzstd -o initramfs-linux-lts54.cpio /boot/initramfs-linux-lts54.img
   mkdir initramfs
   cd initramfs/
   7z x ../initramfs-linux-lts54.cpio

::

   ss=()
   ss+=("$(printf busybox   | sha1sum | cut -d' ' -f1)")
   ss+=("$(printf fsck.ext4 | sha1sum | cut -d' ' -f1)")
   ss+=("$(printf kmod      | sha1sum | cut -d' ' -f1)")
   for f in usr/bin/*; do
      s="$(sha1sum "$f" | cut -d' ' -f1)"
      for i in ${ss[@]}; do
         [ "$s" == "$i" ] && { rm -v "$f"; break; }
      done
   done

::

   cd /tmp/initramfs
   exa -alT



----

.. [#w] https://web.archive.org/web/20210114145232/https://processors.wiki.ti.com/index.php/AM335x_U-Boot_User's_Guide#Prerequisite

.. [#gobinfmt] https://blog.cloudflare.com/using-go-as-a-scripting-language-in-linux/
.. [#itbinfmt] https://www.linux.it/~rubini/docs/binfmt/binfmt.html
.. [#jpbinfmt] https://www.netfort.gr.jp/~dancer/software/binfmtc.html.en
.. [#kdocbinfmt] https://www.kernel.org/doc/html/latest/admin-guide/binfmt-misc.html
.. [#kdocbinfmtjava] https://www.kernel.org/doc/html/latest/admin-guide/java.html

.. include:: link.txt

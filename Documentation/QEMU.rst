.. include:: substitution.txt

====
QEMU
====

Misc
====

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


`Binfmt`__
===========

.. __: https://en.wikipedia.org/wiki/Binfmt_misc

abuse binfmt [#]_ [#]_ [#]_

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
=========

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

Usermode
========

.. todo::

   1. Move most things from this section to a suitable :file:`ALARM.rst` section
   2. :pr:`U-Boot.rst sha1sum speedrun` (done)
   3. :file:`ALARM.rst`  busybox tftpd
   4. :file:`ALARM.rst`  nfs

.. tip::

   Build AUR packages in ``tmux attach || tmux``.

| QEMU+chroot
| |b| `Unix&Linux <https://unix.stackexchange.com/questions/41889/how-can-i-chroot-into-a-filesystem-with-a-different-architechture>`__
| |b| :aw:`ArchWiki <QEMU#Chrooting_into_arm/arm64_environment_from_x86_64>`
|     |b| :pkg:`AUR/qemu-user-static` :pr:`qemu-arm-static (binary)`
|     |b| :pkg:`AUR/binfmt-qemu-static` :pr:`binfmt-qemu-static-all-arch (too smart)`
|     |b| :pkg:`AUR/armutils-git` (depends on the previous two)
| |b| :dw:`Debian Wiki <QemuUserEmulation>`
| |b| :gw:`Gentoo Wiki <Embedded_Handbook/General/Compiling_with_qemu_user_chroot>`

::

   sudo systemctl restart systemd-binfmt.service

get key of `Arch Linux ARM Build System <https://archlinuxarm.org/about/package-signing#keys>`__ ::

   gpg --search-key --keyserver-options "http-proxy=http://127.0.0.1:8080" 68B3537F39A313B3E574D06777193F152BDBE6A6
   gpg --recv-keys  --keyserver-options "http-proxy=http://127.0.0.1:8080" 68B3537F39A313B3E574D06777193F152BDBE6A6

download from `mirrors <https://archlinuxarm.org/about/mirrors>`__
and verify ::

   cd ~/beaglebone
   source ~/proxy.bashrc
   wget http://mirror.archlinuxarm.org/os/ArchLinuxARM-am33x-latest.tar.gz
   wget http://mirror.archlinuxarm.org/os/ArchLinuxARM-am33x-latest.tar.gz.md5
   wget http://mirror.archlinuxarm.org/os/ArchLinuxARM-am33x-latest.tar.gz.sig
   proxy_off
   md5sum -c ArchLinuxARM-am33x-latest.tar.gz.md5
   gpg --verify ArchLinuxARM-am33x-latest.tar.gz.sig ArchLinuxARM-am33x-latest.tar.gz

extract ::

   cd ~/beaglebone &&
   { sudo umount -v ~/beaglebone/alarm_root; chmod -R u+w alarm_root; rm -rf alarm_root; } &&
   [ ! -e alarm_root ] &&
   mkdir -pv alarm_root &&
   cd $_ &&
   /usr/bin/time --format="\n  wall clock time - %E\n" \
      /usr/bin/bsdtar -x --no-same-permissions -f ../ArchLinuxARM-am33x-latest.tar.gz

:raw-html:`<details><summary>standalone app</summary>`

::

   qemu-arm-static \
     -L ~/beaglebone/alarm_root/ \
     usr/bin/uname -a

:raw-html:`</details>`

:aw:`chroot <QEMU#Chrooting_into_arm/arm64_environment_from_x86_64>` ::

   cp -v ~/proxy.bashrc ~/beaglebone/alarm_root/
   sudo mount --bind ~/beaglebone/alarm_root ~/beaglebone/alarm_root
   sudo arch-chroot ~/beaglebone/alarm_root /bin/bash

.. tip::

   | Remove mouse USB receiver to avoid copying
   | |b| :file:`hid-logitech-dj.ko`
   | |b| :file:`hid-logitech-hidpp.ko`

customize initramfs ::

   # source proxy.bashrc
   MK="mkinitcpio -p linux-am33x"
   mv -iv /boot/initramfs-linux{,-orig}.img
   $MK
   mv -iv /boot/initramfs-linux{,-regen}.img
   # "mii" and "usbnet" are builtin instead of loadable module
   sed \
      -e 's,^MODULES=()$,MODULES=(ax88179_178a),g' \
      -i.orig \
      /etc/mkinitcpio.conf
   diff --color=always -u /etc/mkinitcpio.conf{.orig,}
   $MK
   mv -iv /boot/initramfs-linux{,-usbnet}.img
   unset -v MK

exit ::

   exit

::

   sudo umount -v ~/beaglebone/alarm_root

inspect ::

   for i in orig regen usbnet; do
      rm -rf /tmp/img-${i}
      mkdir -pv /tmp/img-${i}
      cd /tmp/img-${i}
      gunzip -l ~/beaglebone/alarm_root/boot/initramfs-linux-$i.img
      gunzip -c -d -k -S.gz -v ~/beaglebone/alarm_root/boot/initramfs-linux-$i.img >$i.cpio
      # cpio -it -v    <$i.cpio
        cpio -i     -d <$i.cpio
      rm -v $i.cpio
      cd /tmp
   done
   # exa -alT /tmp/img-*

::

   #             -q          -y             -W999       -r                                                 
   # DIFF="diff --brief     --side-by-side --width=999 --recursive --no-dereference --color=always"
     DIFF="diff --unified=1                --width=999 --recursive --no-dereference --color=always"
   cd /tmp/
   echo
   if $DIFF img-{orig,regen}; then
      printf "\e[32m%s\e[0m\n" "identical"
   else
      printf "\e[31m%s\e[0m\n" "mismatch"
   fi
   echo
   $DIFF img-{orig,usbnet}
   echo
   unset -v DIFF

Footnotes
=========

.. [#] https://blog.cloudflare.com/using-go-as-a-scripting-language-in-linux/
.. [#] https://www.linux.it/~rubini/docs/binfmt/binfmt.html
.. [#] https://www.netfort.gr.jp/~dancer/software/binfmtc.html.en

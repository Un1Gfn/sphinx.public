.. include:: substitution.txt

.. |S0| replace:: S\ :subscript:`0`
.. |S1| replace:: S\ :subscript:`1`
.. |S2| replace:: S\ :subscript:`2`


==============
|ico| `ALARM`_
==============

`alarm.md <https://github.com/Un1Gfn/beaglebone/blob/markdown/alarm.md>`__


Contacts
========

| `u-boot@lists.denx.de <mailto:u-boot@lists.denx.de>`__
| :r:`PerfectALARM`
| :r:`BeagleBone`
| ALARM `forum <https://archlinuxarm.org/forum/>`__
| ALARM `GitHub <https://github.com/archlinuxarm>`__


Misc
====

denx - `TFTP+NFS <https://www.denx.de/wiki/view/DULG/LinuxNfsRoot>`__

| to clear minicom screen
| \
  :kbd:`<SPACE>`  |rarr|
  :kbd:`<CTRL+A>` |rarr|
  :kbd:`<C>`      |rarr|
  :kbd:`<CTRL+;>` |rarr|
  :kbd:`<Enter>`

Build Static QEMU
=================

.. tip::

   | It takes hours to build dependency :pkg:`AUR/glib2-static`
   | \
     Use ``tmux attach || tmux``

| install :pkg:`AUR/armutils-git`
| dependencies :pkg:`AUR/qemu-user-static` and :pkg:`AUR/binfmt-qemu-static` will be automatically installed
| :pr:`qemu-arm-static (binary)`
| :pr:`binfmt-qemu-static-all-arch (too smart)`

::

   sudo systemctl restart systemd-binfmt.service


Get ALARM
=========

get the `key <https://archlinuxarm.org/about/package-signing#keys>`__ of ALARM Build System ::

   gpg --search-key --keyserver-options "http-proxy=http://127.0.0.1:8080" 68B3537F39A313B3E574D06777193F152BDBE6A6
   gpg --recv-keys  --keyserver-options "http-proxy=http://127.0.0.1:8080" 68B3537F39A313B3E574D06777193F152BDBE6A6

download from `mirrors <https://archlinuxarm.org/about/mirrors>`__ ::

   cd ~/beaglebone
   source ~/proxy.bashrc
   wget http://mirror.archlinuxarm.org/os/ArchLinuxARM-am33x-latest.tar.gz
   wget http://mirror.archlinuxarm.org/os/ArchLinuxARM-am33x-latest.tar.gz.md5
   wget http://mirror.archlinuxarm.org/os/ArchLinuxARM-am33x-latest.tar.gz.sig
   proxy_off

verify ::

   md5sum -c ArchLinuxARM-am33x-latest.tar.gz.md5
   gpg --verify ArchLinuxARM-am33x-latest.tar.gz{.sig,}

.. include:: escalate.txt

extract

.. warning::

   | Everything from a previous extract will be lost
   | \
     Make sure nfs-related services are
     :ref:`spinned down <reference_label_section_clean_up>` |:dart:|
     before removing

::

   # sudo -u darren /usr/bin/bsdtar -x --no-same-permissions -f ../ArchLinuxARM-am33x-latest.tar.gz
   if [ "No machines." = "$(machinectl)" ] && ! mount | grep beaglebone; then
      cd ~darren/beaglebone &&
         rm -rf ~/beaglebone/alarm_root &&
         mkdir -pv alarm_root &&
         chmod -v 777 alarm_root &&
         cd alarm_root/ &&
         /usr/bin/bsdtar -xpf ../ArchLinuxARM-am33x-latest.tar.gz &&
         cd ~darren/beaglebone
   else
      printf "\n\e[31m  %s\e[0m\n\n" "err"
   fi

proxy for pacman ::

   cp -v ~darren/proxy.bashrc ~darren/beaglebone/alarm_root/

change password ::

   chpasswd -R ~darren/beaglebone/alarm_root <<<"root:root"$'\n'"alarm:alarm"

workaround :aw:`systemd-nspawn#Root_login_fails` ::

   # printf "\npts/0\n\n" >>~darren/beaglebone/alarm_root/usr/share/factory/etc/securetty
     printf "\npts/0\n\n" >>~darren/beaglebone/alarm_root/etc/securetty
     cat ~darren/beaglebone/alarm_root/etc/securetty

| remove fstab
| |b| :aw:`NFS#Mount_using_/etc/fstab`

::

   cd ~darren/beaglebone
   grep -q -e '^[^#]' alarm_root/etc/fstab && printf "\n\e[31m  %s\e[0m\n\n" "err"
   rm -v alarm_root/etc/fstab

:raw-html:`<details><summary><s>GPG timeout workaround by disabling package signature checking (fixed with rngd.service in host)</s></summary>`

:aw:`Pacman/Package_signing#Disabling_signature_checking`

|:warning:| vulnerable ::

   sed -i.pacnew \
      -e 's/SigLevel    = Required DatabaseOptional/SigLevel = Never/g' \
      -e 's/^#Color$/Color/g' \
      -e 's/^#VerbosePkgLists$/VerbosePkgLists/g' \
      alarm_root/etc/pacman.conf
   diff -u --color alarm_root/etc/pacman.conf{.pacnew,}

:raw-html:`</details>`

disable problematic units

::

   # systemctl get-default
   # systemctl set-default multi-user.target
   # systemctl set-default graphical.target
   # systemctl disable haveged.service
   # systemctl disable dhcpcd.service
   # systemctl disable dhcpcd@.service
   # systemctl disable systemd-networkd-wait-online.service
   # systemctl disable systemd-networkd.service
   # systemctl disable systemd-networkd.socket
   if cd ~darren/beaglebone/alarm_root/etc/systemd/system; then
      # Leave sshd.service enabled, for debugging purposes
      rm -v \
         multi-user.target.wants/systemd-networkd.service \
         multi-user.target.wants/systemd-resolved.service \
         network-online.target.wants/systemd-networkd-wait-online.service \
         sockets.target.wants/systemd-networkd.socket \
         sysinit.target.wants/haveged.service \
         sysinit.target.wants/systemd-timesyncd.service
      exa -alT
      cd ~darren/beaglebone/
   fi

Entrophy
========

`myths about /dev/urandom <https://www.2uo.de/myths-about-urandom/>`__

| might take a very long time without much entryphy
| |b| :aw:`pacman-key --init <Pacman/Package_signing#Initializing_the_keyring>`
| |b| :aw:`nfs <NFS#Starting_the_server>`

`820g3 has TPM 1.2 <https://support.hp.com/us-en/document/c04913012#:~:text=Trusted%20Platform%20Module%20(TPM%20)%201.2%20Embedded%20Security%20Chip%20(Common%20Criteria%20EAL4%2B%20Certified)>`__

.. include:: escalate.txt

load tpm drivers ::

   modprobe tpm
   modprobe -a tpm_{infineon,tis,crb}

check hardware random number generator (TRNG) ::

   file /dev/hwrng

| :pkg:`community/rng-tools` (:aw:`ArchWiki <Rng-tools>`)

::

   systemctl start rngd.service # (-B)

wait for approx 7s until harvest rate reaches at least :file:`[ 48KiB/s]`\ [#si]_

::

   pv -prb </dev/random >/dev/null


Modify Initramfs
================

| `gen_initramfs.sh <https://github.com/torvalds/linux/blob/master/usr/gen_initramfs.sh>`__
| kernel doc - `ramfs, rootfs and initramfs <https://www.kernel.org/doc/html/latest/filesystems/ramfs-rootfs-initramfs.html#what-is-rootfs>`__

| QEMU+chroot
| |b| `Unix&Linux <https://unix.stackexchange.com/questions/41889/how-can-i-chroot-into-a-filesystem-with-a-different-architechture>`__
| |b| :aw:`ArchWiki <QEMU#Chrooting_into_arm/arm64_environment_from_x86_64>`
| |b| :dw:`Debian Wiki <QemuUserEmulation>`
| |b| :gw:`Gentoo Wiki <Embedded_Handbook/General/Compiling_with_qemu_user_chroot>`

:aw:`systemd-nspawn` - `chroot on steriods`__

.. __: https://www.youtube.com/watch?v=s7LlUs5D9p4

prepare machine id ``-M alarm``

::

   cd ~/beaglebone/
   sudo rm -fv /var/lib/machines/alarm
   sudo ln -sv "$(realpath alarm_root/)" /var/lib/machines/alarm

:raw-html:`<details><summary><s>bootless container</s></summary>`

::

   # sudo mount --bind alarm_root alarm_root
   # sudo arch-chroot alarm_root /bin/bash
   sudo systemd-nspawn -D alarm_root -M alarm

:raw-html:`</details>`

launch booted container |:rocket:|

::

   P="$(realpath ~/beaglebone/alarm_root/var/cache/pacman/pkg)"
   if [ -z "$(ls -A "$P")" ]; then
      # --link-journal=guest
      sudo systemd-nspawn \
         -b \
         -M alarm \
         --bind-ro=/etc/resolv.conf \
         --bind=/var/cache/pacman/pkg \
   else
      printf "\n\e[31m  %s\e[0m\n\n" "err"
   fi

log in as :file:`root:root`, wait approx 25s (max 60s) for bash prompt

.. tip::

   | |b| :pr:`Run journalctl -M alarm [-f] in host for container journal`
   | |b| Run ``systemctl shutdown`` for peaceful shutdown
   | |b| \
         To force quit, press
         :kbd:`<CTRL+]><CTRL+]><CTRL+]>` or
         :kbd:`<CTRL+5><CTRL+5><CTRL+5>` within one second

make sure no units harmful to nfs are enabled ::

   env SYSTEMD_COLORS=0 systemctl --no-pager --legend=0 list-unit-files \
      | rev \
      | env LC_ALL=C sort -k 2,2 -s \
      | rev \
      | less -SRM +%

backup & regen ::

   mv -iv /boot/initramfs-linux{,-orig}.img
   mkinitcpio -p linux-am33x
   mv -iv /boot/initramfs-linux{,-regen}.img

| |b| :aw:`Mkinitcpio#Using_net`
| |b| :aw:`Diskless_system#NFS_2`
| |b| \
      :pkg:`alarm/mkinitcpio-netconf`
      depends on
      :pkg:`alarm/mkinitcpio-nfs-utils`

| add :file:`ax88179_178a.ko.gz` module
| add :file:`net` hook

.. table::
   :align: left
   :widths: auto

   =========== ===================== =====================
    \           ``\( \)``             ``( )``
   =========== ===================== =====================
       ``-E``   literal parenthesis   substitution group
    no ``-E``   ?                     literal parenthesis
   =========== ===================== =====================

::

   # "mii" and "usbnet" are builtin instead of loadable module
   mv -fv /etc/mkinitcpio.conf{.orig,}
   # -e 's,^HOOKS=\((.*)\)$,HOOKS=(\1 net),g' \
   sed \
      -E \
      -i.orig \
      -e 's,^MODULES=\(\)$,MODULES=(ax88179_178a nfsv4),g' \
      -e 's,^BINARIES=\(\)$,BINARIES=(/usr/bin/mount.nfs4),g' \
      -e 's,^HOOKS=\((.*)\)$,HOOKS=(\1 netnfs4),g' \
      /etc/mkinitcpio.conf
   diff --color=always -u /etc/mkinitcpio.conf{.orig,}

.. table::
   :align: left
   :widths: auto

   =================================== =================== ==========================================
    pkg                                 hooks it provides   kernel cmdline params it parses
   =================================== =================== ==========================================
    :pkg:`alarm/mkinitcpio-netconf`     ``netconf``         ``ip=``
    :pkg:`alarm/mkinitcpio-nfs-utils`   ``net``             ``ip=`` ``nfsaddrs=`` ``nfsroot=``
   =================================== =================== ==========================================

:aw:`import archlinuxarm keys <Offline_installation#Importing_archlinux_keys>` ::

   # We have already started rngd.service in host
   # No /usr/bin/pv available in container
   # Benchmark in container with "dd if=/dev/random of=/dev/null status=progress"
   # Check CPU usage of "gpg-agent" to make sure it ain't blocked
   pacman-key --init
   # Avoid downloading keys again
   #  downloading required keys...
   #  :: Import PGP key 77193F152BDBE6A6, "Arch Linux ARM Build System <builder+xu6@archlinuxarm.org>"? [Y/n] y
   pacman-key --populate archlinux

sysuupgrade & install ::

   source /proxy.bashrc
   pacman -Syu nfs-utils mkinitcpio-nfs-utils # netnfs4 needs mount.nfs4 binary
   # pacman -Ql mkinitcpio-netconf
   pacman -Ql mkinitcpio-nfs-utils
   mkinitcpio -L
   # mkinitcpio -H netconf
   mkinitcpio -H net

| use ``mount.nfs4`` instead of ``nfsmount``
| |b| :pkg:`AUR/mkinitcpio-nfs4-hooks`
| |b| :aw:`Diskless_system#NFS_2`

::

   echo
   sed \
     -e 's/nfsmount/mount.nfs4/g' \
     /usr/lib/initcpio/hooks/net \
     >/usr/lib/initcpio/hooks/netnfs4
   diff -u --color /usr/lib/initcpio/hooks/net*
   echo
   cp -v /usr/lib/initcpio/install/net{,nfs4}
   echo

.. tip::

   | Remove mouse USB receiver to avoid copying
   | |b| :file:`hid-logitech-dj.ko`
   | |b| :file:`hid-logitech-hidpp.ko`

commit

::

   if [ "$(uname -m)" == armv7l ]; then
      mkinitcpio -p linux-am33x
      mv -iv /boot/initramfs-linux{,-net}.img
   else
      printf "\n\e[31m  %s\e[0m\n\n" "err"
   fi

verify ::

   lsinitcpio -a /boot/initramfs-linux-net.img

exit ::

   if [ "$(uname -m)" == armv7l ]; then
      systemctl poweroff
   else
      printf "\n\e[31m  %s\e[0m\n\n" "err"
   fi

::

   sudo rm -rv ~darren/beaglebone/alarm_root/var/log/journal/*
   sudo rm -fv /var/lib/machines/alarm
   # sudo umount -v ~/beaglebone/alarm_root

inspect ::

   for i in orig regen net; do
      rm -rf /tmp/img-${i}
      mkdir -pv /tmp/img-${i}
      cd /tmp/img-${i}
      #
      # gunzip -l ~/beaglebone/alarm_root/boot/initramfs-linux-$i.img
      # gunzip -c -d -k -S.gz -v ~/beaglebone/alarm_root/boot/initramfs-linux-$i.img >$i.cpio
      # # cpio -it -v    <$i.cpio
      #   cpio -i     -d <$i.cpio
      # rm -v $i.cpio
      #
      # lsinitcpio -a ~/beaglebone/alarm_root/boot/initramfs-linux-$i.img
      # lsinitcpio -l ~/beaglebone/alarm_root/boot/initramfs-linux-$i.img
      lsinitcpio -x ~/beaglebone/alarm_root/boot/initramfs-linux-$i.img
      #
      cd /tmp
   done

::

   # exa -alT /tmp/img-*
   #             -q          -y             -W999       -r
   # DIFF="diff --brief     --side-by-side --width=999 --recursive --no-dereference --color=always"
     DIFF="diff --unified=1                --width=999 --recursive --no-dereference --color=always"
   cd /tmp/
   echo
   if $DIFF img-{orig,regen}; then
      printf "\e[32m%s\e[0m\n" "orig regen identical"
   else
      printf "\e[31m%s\e[0m\n" "orig regen mismatch"
   fi
   echo
   $DIFF img-{orig,net}
   echo
   unset -v DIFF

::

   rm -r /tmp/img-{orig,regen,net}


PC TFTP
=======

.. table::
   :align: left
   :widths: auto

   === ====== ================ ======================================
    \   settings
   --- ----------------------- --------------------------------------
    \   a      b                result
   === ====== ================ ======================================
    1   Auto   Auto             |:white_check_mark:| operate at Full
    2   Auto   Half             |:white_check_mark:| operate at Half
    3   Auto   Full\ [#AuFl]_    |:x:|                boom!
    4   Half   Half             |:white_check_mark:| operate at Half
    5   Half   Full             |:x:|                boom!
    6   Full   Full             |:white_check_mark:| operate at Full
   === ====== ================ ======================================

:manpage:`systemd.net-naming-scheme(7)`

.. code:: text

                   [SCREEN]
   enp0s20f0u2 -> [KEYBOARD] <- enp0s20f0u1
                  [TOUCHPAD]

| linux-hardware.org/`0b95-1790 <https://linux-hardware.org/?id=usb:0b95-1790>`__
| ``$ lsusb`` :file:`Bus 00? Device 00?: ID 0b95:1790 ASIX Electronics Corp. AX88179 Gigabit Ethernet`
| ``$ ip addr`` :file:`link/ether 00:0e:c6:d3:2d:5f`
| ``$ usb-devices``\ [#ax8817]_ :file:`Driver=ax88179_178a`

| make `FIT image <https://elinux.org/images/f/f4/Elc2013_Fernandes.pdf>`__
  with :manpage:`mkimage(1)`
  from :pkg:`community/uboot-tools`
| |b| `ELF to uImage <https://www.denx.de/wiki/view/DULG/HowCanICreateAnUImageFromAELFFile>`__
| |b| `Combining a Kernel and a Ramdisk into a Multi-File Image <https://www.denx.de/wiki/view/DULG/CombiningKernelAndRamdisk>`__

| denx - `boot from BOOTP/TFTP <https://www.denx.de/wiki/view/DULG/UBootCmdGroupDownload#Section_5.9.5.1.>`__
| ArchWiki - :aw:`TFTP`

submit to ArchWiki :aw:`BusyBox` and link from :aw:`TFTP#Server`

.. include:: escalate.txt

::

   echo
   ip link    set                dev enp0s31f6 up
   ip address flush              dev enp0s31f6
   ip address add   10.0.0.89/24 dev enp0s31f6
   ip route
   echo
   printf "\033]0;TFTP\007"
   cd ~darren/beaglebone/alarm_root/boot
   sha1sum \
      zImage \
      dtbs/am335x-bonegreen-wireless.dtb \
      initramfs-linux-net.img
   echo
   # busybox udpsvd -Ev -u darren:darren -l 820g3 10.0.0.89 69 tftpd -r -u darren -l .
     busybox udpsvd -Ev                  -l 820g3 10.0.0.89 69 tftpd -r           -l .


PC :wp:`NFS<Network_File_System>`
=================================

| ArchWiki
| |b| :aw:`Diskless_system#Server_configuration`
| |b| :aw:`NFS`

client |rarr| ``mount`` |rarr| server |rarr| ``rpcbind`` |rarr| ``nfsd`` |rarr| ``mountd``

.. warning::

   Use NFSv3 instead of NFSv4

.. include:: escalate.txt

`append to /etc/exports <https://wiki.archlinux.org/title/Diskless_system#NFS>`__ ::

   F=/etc/exports
   BAK=/etc/exports.pacnew

   S="$(sha256sum $F | cut -d' ' -f 1)"
   S0="$(zcat /var/lib/pacman/local/nfs-utils-2.5.4-1/mtree \
      | grep "^\.$F " \
      | cut -d' ' -f5- \
      | cut -d'=' -f2
   )"

   function M {
   # echo | sudo tee -a "$F"
     echo >>"$F"
   # sudo tee -a "$F" <<EOP
     cat  >>"$F" <<EOP
   /srv                               *(rw,no_root_squash,no_subtree_check)
   /home/darren/beaglebone/alarm_root *(rw,no_root_squash,no_subtree_check)
   EOP
   }

   if [ "$S0" == "$S" ]; then
      cp -vi "$F" "$BAK"
      M
      diff -u --color=always "$BAK" "$F"
   else
      echo
      printf "\e[31m  %s\e[0m\n" "err"
      printf "\e[31m  %s\e[0m\n" "$F already modified"
      printf "\e[31m  %s\e[0m\n" "$BAK is a backup"
      echo
   fi

   unset -v F BAK S S0
   unset -f M

:aw:`NFS#Restricting_NFS_to_interfaces/IPs` ::

   # sed -i.pacnew -e 's/^# host=$/host=10.0.0.64/g'

install :pkg:`community/rng-tools`

start nfs ::

   # ln -sfv "$(realpath ~darren/beaglebone/alarm_root)" /srv/alarm
   exportfs -arv
   exportfs -v
   systemctl start rngd.service # (-A)
   systemctl start nfs-idmapd.service # (A)
   systemctl start nfs-mountd.service # (B)
   systemctl start nfs-server.service # (C)

check listening ports ::

   rpcinfo -p | grep nfs
   ss -tlnp | grep -e 111 -e 2049 -e 20048
   ss -ulnp | grep -e 111 -e 2049 -e 20048

check api fs ::

   echo
   for FS in nfsd sunrpc; do
      findmnt "$FS"
      echo
   done

test mounting ::

   echo
   for H in 820g3 10.0.0.89; do
      showmount -e "$H"
      echo
      # mount -v -t nfs -o vers=3 "$H":/home/darren/beaglebone/alarm_root /mnt
        mount -v "$H":/home/darren/beaglebone/alarm_root /mnt
      echo
      findmnt /mnt
      echo
      ls -x /home/darren/beaglebone/alarm_root /mnt
      echo
      umount -v /mnt
      echo
   done


| `ntp server <https://www.denx.de/wiki/view/DULG/UseNTPToSynchronizeSystemTimeAgainstRTC>`__
| |b| :file:`/etc/systemd/timesyncd.conf`

::

   # With -w, client can't sync from us
   # Without -w, systemd-timesyncd.service is interefered
   # printf "\033]0;NTP\007"
   # sudo busybox ntpd \
   #    -dd \
   #    -n \
   #    -w \
   #    -p 0.arch.pool.ntp.org \
   #    -p 1.arch.pool.ntp.org \
   #    -p 2.arch.pool.ntp.org \
   #    -p 3.arch.pool.ntp.org \
   #    -l \
   #    -I enp0s31f6


|S0| TFTP
=========

.. tip::

   When in trouble, ask :pkg:`community/wireshark-qt`

.. tip::

   Verify integrity of received files with u-boot ``sha1sum``

u-boot `drivers/net <https://github.com/u-boot/u-boot/tree/master/drivers/net>`__/e1000

`Net: No ethernet found <https://www.denx.de/wiki/view/DULG/NetNoEthernetFound>`__

| \
  :file:`.dtb` blob file |equiv| FDT (:el:`Flattened Device Tree <Device_Tree_What_It_Is#The_Flattened_Device_Tree_is...>`)
| \
  :file:`.dts` :file:`.dtsi` |rarr| :pkg:`community/dtc` |rarr| FDT |rarr| kernel internal EDT (:el:`Expanded Device Tree <Device_Tree_What_It_Is#Introduction>`)


1/2 :ref:`connect serial <reference_label_section_connect_serial>`

| 2/2 connect ethernet :pr:`box-drawing character`
| BBGW\:\:USB - USB\:\:AX88179\:\:RJ45 - :wp:`Ethernet over twisted pair` - RJ45\:\:820g3

|S0| bring up ethernet

.. code:: text

   usb start

u-boot `variables <https://github.com/u-boot/u-boot/blob/7a4ff7c41bab8b43767eacc0b30ca1573ab6acb1/README#L3314>`__

.. code:: text

   if test $eth4addr = '00:0e:c6:d3:2d:5f'; then
     # ax88179_eth
     setenv ethprime eth4
     setenv ethact eth4
     setenv ethrotate yes
     setenv netretry  no
     echo OK
   else
     echo "FAIL"
   fi
   printenv ethprime ethact ethrotate netretry

.. code:: text

   setenv ipaddr   10.0.0.64
   setenv clientip 10.0.0.64
   setenv serverip 10.0.0.89
   setenv gwip     10.0.0.89
   setenv netmask  255.255.255.0
   setenv hostname alarm
   setenv rootdir  /home/darren/beaglebone/alarm_root
   printenv ipaddr clientip serverip gwip netmask hostname rootdir 

ping

.. code:: text

   ping ${serverip}

check tftp vars

.. code:: text

   if test 0 -eq 0 \
     -a ${bootport}        =  "0:2"            \
     -a ${bootfile}        =  "zImage"         \
     -a ${fdtfile}         =  "undefined"      \
     -a ${console}         =  "ttyO0,115200n8" \
     -a ${kernel_addr_r}  -eq 0x82000000       \
     -a ${fdt_addr_r}     -eq 0x88000000       \
     -a ${ramdisk_addr_r} -eq 0x88080000       \
   ; then
     echo OK
   else
     echo ERR
   fi

set tftp vars

.. code:: text

   setenv tftpdstp 69
   # setenv tftpblocksize
   setenv tftptimeout 5000
   setenv tftptimeoutcountmax 0
   # setenv tftpwindowsize
   printenv tftpdstp tftptimeout tftptimeoutcountmax

| tftp download files
| compare sha1sum against those in ``xdotool windowfocus "$(xdotool search --name TFTP)"``

.. code:: text

   tftpboot ${kernel_addr_r} zImage
   sha1sum  ${kernel_addr_r} ${filesize}

.. code:: text

   tftpboot ${fdt_addr_r} "dtbs/am335x-bonegreen-wireless.dtb"
   sha1sum  ${fdt_addr_r} ${filesize}

.. code:: text

   tftpboot ${ramdisk_addr_r} initramfs-linux-net.img
   sha1sum  ${ramdisk_addr_r} ${filesize}
   setenv     ramdisk_size    ${filesize}


.. \:raw-html:`<strike>S<sub>0</sub> -> S<sub>1</sub></strike>`
.. \======================================================================

|S0|\ [0]_ -> |S1|\ [1]_ -> |S2|\ [2]_
======================================

.. warning::

   Use NFSv3 instead of NFSv4

.. warning::

   Shut down USB in U-Boot before booting Linux [#down]_

ethernet force ``autonegotiation`` [#tcp]_

| ArchWiki - :aw:`Working with the serial console`
| kernal doc - `Linux Serial Console <https://www.kernel.org/doc/html/latest/admin-guide/serial-console.html>`__
| `Remote Serial Console HOWTO <https://tldp.org/HOWTO/Remote-Serial-Console-HOWTO/configure-kernel.html>`__
| |b| tty0 - framebuffer
| |b| ttyS0 - serial console [#noinput]_

.. code:: text

   echo; echo -n "  "; if test "${console}" = "ttyO0,115200n8" -a "${baudrate}" = 115200; then echo ok; else echo err; fi; echo

| kernel doc
  - `cmdline <https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html>`__
  - `NFS <https://www.kernel.org/doc/html/latest/admin-guide/nfs/index.html>`__
  - `nfsroot <https://www.kernel.org/doc/html/latest/admin-guide/nfs/nfsroot.html>`__
  (`txt <https://www.kernel.org/doc/Documentation/filesystems/nfs/nfsroot.txt>`__)
| ArchWiki - `cmdline <https://wiki.archlinux.org/title/Kernel_parameters#Parameter_list>`__
| DULG - `LinuxNfsRoot <https://www.denx.de/wiki/DULG/LinuxNfsRoot>`__


| setenv `bootargs <https://www.denx.de/wiki/view/DULG/LinuxKernelArgs>`__
| |b| ``ramdisk_size=``\ [#rdsz]_
| |b| for ``<nfs-options>`` see :manpage:`nfs(5)`
| |b| ``nfsroot=`` [#tcp]_ [#noNFS4]_
| |b| :prlt:`init=`\ [#shenanigans]_
| |b| :prlt:`rdinit=`\ [#shenanigans]_ [#kdocnfsroot]_

.. code:: text

   # setenv bootargs $bootargs nfsroot=${serverip}:${rootdir},nfsvers=3,proto=tcp,mountproto=tcp

.. code:: text

   setenv bootargs
   setenv bootargs $bootargs console=tty0 console=ttyS0,115200n8
   setenv bootargs $bootargs ip=${clientip}:${serverip}:${gwip}:${netmask}:${hostname}:eth0:none
   setenv bootargs $bootargs nfsroot=${serverip}:${rootdir}
   setenv bootargs $bootargs rw rootwait
   printenv bootargs

.. warning::
   
   | Make sure no container is running
   | ``sudo machinectl list``

.. code:: text

   # iminfo ${kernel_addr_r}
   # bootm ${kernel_addr_r} ${ramdisk_addr_r}:${ramdisk_size} ${fdt_addr_r}
     bootz ${kernel_addr_r} ${ramdisk_addr_r}:${ramdisk_size} ${fdt_addr_r}

::

   cat /proc/cmdline

.. warning::

   Dont execute ``ping`` without specifying number of packets!

::

   busybox ping -4 -c 10 -I eth0      10.0.0.89
   busybox ping -4 -c 10 -I 10.0.0.64 10.0.0.89

| boot
| bootd
| :pr:`bootefi`
| :pr:`bootelf`
| bootm
| :pr:`bootp`
| :pr:`bootvx`
| bootz

`=> fdt <https://www.denx.de/wiki/DULG/UBootCmdFDT>`__

.. tip::

   wireshark?

:aw:`NFS/Troubleshooting`

misc ::

   dmesg -D
   export TERM=xterm-256color

Install
=======

.. warning::

   Check eMMC partition alignment!

| :aw:`Installation guide`
| `alarm wiki <https://archlinuxarm.org/platforms/armv7/ti/beaglebone-green-wireless>`__
  |rarr| ``Installation``


Tune
====

| `UBootCmdGroupExec`__
| |b| ``$ mkinage -T script`` -
      ``=> tftp`` -
      ``=> source`` -
      ``=> bootm``
| |b| `ALARM <https://archlinuxarm.org/packages/armv7h/uboot-beaglebone/files/uboot-beaglebone.install>`__ -
      `boot.txt <https://archlinuxarm.org/packages/armv7h/uboot-beaglebone/files/boot.txt>`__ -
      `mkscr`__

.. __: https://www.denx.de/wiki/DULG/UBootCmdGroupExec
.. __: https://archlinuxarm.org/packages/armv7h/uboot-beaglebone/files/mkscr

`linux dev major minor <https://www.kernel.org/doc/html/latest/admin-guide/devices.html>`__

:aw:`fake-hwclock <System_time#fake-hwclock>`

.. _reference_label_section_clean_up:

Clean up
========

|:dart:|

.. include:: escalate.txt

::

   mv -v /etc/exports.pacnew /etc/exports
   systemctl stop nfs-server.service # (C)
   systemctl stop nfs-mountd.service # (B)
   systemctl stop nfs-idmapd.service # (A)
   systemctl is-enabled rngd.service || systemctl stop rngd.service # (-A)
   systemctl stop rngd.service # (-B)

::

   ip address flush dev enp0s31f6
   ip link    set   dev enp0s31f6 down

Footnotes
=========

..

----

.. [0] |S0| - The state where U-Boot with built-in NIC driver is running

.. [1] |S1| - The state where Linux with only initramfs is running

.. [2] |S2| - The state where a fully functional Linux is running

----

.. [#AuFl] :wp:`Autonegotiation#Duplex_mismatch`

.. [#ax8817] https://unix.stackexchange.com/a/60080
.. [#si] 50 kB/s |asymp| 48.828 KiB/s

.. [#down] https://www.denx.de/wiki/view/U-Boot/DesignPrinciples#2_Keep_it_Fast
.. [#tcp] https://www.denx.de/wiki/view/DULG/EthernetIsUnreliable

.. [#noinput] https://www.denx.de/wiki/view/DULG/NoInputUsingFramebuffer


.. [#rdsz] https://www.denx.de/wiki/view/DULG/RamdiskGreaterThan4MBCausesProblems
.. [#noNFS4] :aw:`NFSv4 is not yet supported <Mkinitcpio#Using_net>`

.. [#shenanigans] https://unix.stackexchange.com/a/430614
.. [#kdocnfsroot] https://www.kernel.org/doc/html/latest/admin-guide/nfs/nfsroot.html


----

.. include:: link.txt

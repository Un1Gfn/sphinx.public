.. include:: include/substitution.txt

.. |S0| replace:: S\ :subscript:`0`
.. |S1| replace:: S\ :subscript:`1`
.. |S2| replace:: S\ :subscript:`2`
.. |S3| replace:: S\ :subscript:`3`

======================
|ico| Install `ALARM`_
======================

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

   cd ~/beaglebone
   md5sum -c ArchLinuxARM-am33x-latest.tar.gz.md5
   gpg --verify ArchLinuxARM-am33x-latest.tar.gz{.sig,}

.. include:: include/escalate.txt

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
         rm -rf alarm_root/ &&
         mkdir -pv alarm_root/ &&
         chmod -v 777 alarm_root &&
         cd alarm_root/ &&
         /usr/bin/bsdtar -xpf ../ArchLinuxARM-am33x-latest.tar.gz &&
         cd ~darren/beaglebone
   else
      printf "\n\e[31m  %s\e[0m\n\n" "err"
   fi

copy tarball for installation ::

   cp -v ~darren/beaglebone/{ArchLinuxARM-am33x-latest.tar.gz,alarm_root/}

proxy for pacman ::

   cp -v ~darren/proxy.bashrc ~darren/beaglebone/alarm_root/

change password ::

   # chpasswd -R ~darren/beaglebone/alarm_root <<<"root:root"$'\n'"alarm:alarm"
   mount -v --bind ~darren/beaglebone/alarm_root ~darren/beaglebone/alarm_root
   arch-chroot ~darren/beaglebone/alarm_root chpasswd <<<"root:root"$'\n'"alarm:alarm"
   umount -v ~darren/beaglebone/alarm_root

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

.. include:: include/escalate.txt

load tpm drivers ::

   modprobe tpm
   modprobe -a tpm_{infineon,tis,crb}

check hardware random number generator (TRNG) ::

   file /dev/hwrng

| :pkg:`community/rng-tools` (:aw:`ArchWiki <Rng-tools>`)

::

   systemctl start rngd.service # (A)

wait for approx 7s until harvest rate reaches at least :file:`[ 48KiB/s]` [#si]_

::

   pv -prb /dev/random >/dev/null


Modify Initramfs
================

| `gen_initramfs.sh <https://github.com/torvalds/linux/blob/master/usr/gen_initramfs.sh>`__
| kernel doc - `ramfs, rootfs and initramfs <https://www.kernel.org/doc/html/latest/filesystems/ramfs-rootfs-initramfs.html#what-is-rootfs>`__

| QEMU+chroot
| |b| `Unix&Linux <https://unix.stackexchange.com/questions/41889/how-can-i-chroot-into-a-filesystem-with-a-different-architechture>`__
| |b| :aw:`ArchWiki <QEMU#Chrooting_into_arm/arm64_environment_from_x86_64>`
| |b| :debian:`Debian Wiki <QemuUserEmulation>`
| |b| :gentoo:`Gentoo Wiki <Embedded_Handbook/General/Compiling_with_qemu_user_chroot>`

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

| our nfs setup relies on vulnerable static network
| make sure no network-related units are enabled

::

   env SYSTEMD_COLORS=0 systemctl --no-pager --legend=0 list-unit-files \
      | rev \
      | env LC_ALL=C sort -k 2,2 -s \
      | rev \
      | less -SRM +%

bench rng ::

   # We have already started rngd.service in host
   # No /usr/bin/pv available in container
   dd if=/dev/random of=/dev/null status=progress

| :aw:`import <Offline_installation#Importing_archlinux_keys>` ALARM keys
| |b| this step is usually done by pacstrap

::

   # Check CPU usage of "gpg-agent" to make sure it ain't blocked
   pacman-key --init

::

   # Avoid downloading keys again
   #  downloading required keys...
   #  :: Import PGP key 77193F152BDBE6A6, "Arch Linux ARM Build System <builder+xu6@archlinuxarm.org>"? [Y/n] y
   pacman-key --populate archlinuxarm

| install packages
| |b| :pkg:`extra/pv`
| |b| :pkg:`extra/parted`
|             /usr/bin/partprobe
| |b| :pkg:`core/nfs-utils`
|             /usr/bin/mount.nfs4
| |b| :pkg:`core/mkinitcpio-nfs-utils`
|             /usr/lib/initcpio/hooks/net
|             /usr/lib/initcpio/install/net
| |b| :aw:`Mkinitcpio#Using_net`
| |b| :aw:`Diskless_system#NFS_2`

.. table::
   :align: left
   :widths: auto

   =================================== =================== ==========================================
    pkg                                 hooks it provide    kernel cmdline params it parses
   =================================== =================== ==========================================
    :pkg:`alarm/mkinitcpio-netconf`     ``netconf``         ``ip=``
    :pkg:`alarm/mkinitcpio-nfs-utils`   ``net``             ``ip=`` ``nfsaddrs=`` ``nfsroot=``
   =================================== =================== ==========================================

::

   source /proxy.bashrc
   pacman -Syu pv parted nfs-utils mkinitcpio-nfs-utils
   pacman -Ql mkinitcpio-nfs-utils
   mkinitcpio -L
   mkinitcpio -H net

| use ``mount.nfs4`` instead of ``nfsmount`` in hook ``net``
| |b| altenatively, install :pkg:`AUR/mkinitcpio-nfs4-hooks`
| |b| :aw:`Diskless_system#NFS_2`

::

   echo
   mv -fv /usr/lib/initcpio/hooks/net{.orig,}
   sed -e 's/nfsmount/mount.nfs4/g' -i.orig /usr/lib/initcpio/hooks/net
   diff -u --color /usr/lib/initcpio/hooks/net{.orig,}
   echo

| modify :file:`mkinitcpio.conf`
| add :file:`ax88179_178a.ko.gz` module
| add ``net`` hook

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
      -e 's,^HOOKS=\((.*)\)$,HOOKS=(\1 net),g' \
      /etc/mkinitcpio.conf
   diff --color=always -u /etc/mkinitcpio.conf{.orig,}

.. tip::

   | hide from autodetect
   | |b| remove mouse USB receiver ( :file:`hid-logitech-dj.ko` :file:`hid-logitech-hidpp.ko` )
   | |b| remove PL2303
   | |b| remove ...

mkinitcpio ::

   if [ "$(uname -m)" == armv7l ]; then
      mkinitcpio -p linux-am33x
   else
      printf "\n\e[31m  %s\e[0m\n\n" "err"
   fi

inspect initramfs ::

   lsinitcpio -a /boot/initramfs-linux.img

| stop gpg-agent
| workaround
| ``systemctl poweroff`` stuck after ``Finished Generate shutdown-ramfs``

::

   ps aux | grep qemu-arm-static | grep gpg
   # kill <N>

exit ::

   if [ "$(uname -m)" == armv7l ]; then
      printf "\n\e[32m  %s\e[0m\n\n" "ok"
   else
      printf "\n\e[31m  %s\e[0m\n\n" "err"
   fi

::

   systemctl poweroff

::

   sudo rm -fv /var/lib/machines/alarm
   # sudo rm -rfv ~darren/beaglebone/alarm_root/var/log/journal/*
   # sudo umount -v ~/beaglebone/alarm_root


PC TFTP
=======

:manpage:`systemd.net-naming-scheme(7)`

| :wp:`autonegotiation`
| :wp:`duplex (telecommunications)#Half_duplex`
| :wp:`duplex (telecommunications)#Full_duplex`
| :wp:`duplex mismatch`

.. table::
   :align: left
   :widths: auto

   +---+-----------+---------------------------------------------+
   | # | port conf | result                                      |
   +===+===+=======+=============================================+
   | 1 | A | A     | |:white_check_mark:| operate at full duplex |
   +---+---+-------+---------------------------------------------+
   | 2 | A | H     | |:white_check_mark:| operate at half duplex |
   +---+---+-------+---------------------------------------------+
   | 3 | A | F     | |:x:|                boom  [#AuFl]_         |
   +---+---+-------+---------------------------------------------+
   | 4 | H | H     | |:white_check_mark:| operate at half duplex |
   +---+---+-------+---------------------------------------------+
   | 5 | H | F     | |:x:|                boom                   |
   +---+---+-------+---------------------------------------------+
   | 6 | F | F     | |:white_check_mark:| operate at full duplex |
   +---+---+-------+---------------------------------------------+

| `0b95:1790 <https://linux-hardware.org/?id=usb:0b95-1790>`__
| `OUI Lookup Tool <https://www.wireshark.org/tools/oui-lookup.html>`__
| 00:0E:C6 - Asix Electronics Corp.

.. code:: text

                   [SCREEN]
   enp0s20f0u2 -> [KEYBOARD] <- enp0s20f0u1
                  [TOUCHPAD]

.. code:: shell-session

  $ lsusb | grep -i ax
  Bus * Device *: ID 0b95:1790 ASIX Electronics Corp. AX88179 Gigabit Ethernet
  $ ip addr
  ... link/ether 00:0e:c6:d3:2d:5f ...
  $ usb-devices
  T:  Bus=* Lev=* Prnt=* Port=* Cnt=* Dev#=  2 Spd=5000 MxCh= 0
  D:  Ver= 3.00 Cls=ff(vend.) Sub=ff Prot=00 MxPS= 9 #Cfgs=  1
  P:  Vendor=0b95 ProdID=1790 Rev=01.00
  S:  Manufacturer=ASIX Elec. Corp.
  S:  Product=AX88179
  S:  SerialNumber=000000000001E9
  C:  #Ifs= 1 Cfg#= 1 Atr=a0 MxPwr=496mA
  I:  If#= 0 Alt= 0 #EPs= 3 Cls=ff(vend.) Sub=ff Prot=00 Driver=ax88179_178a
  E:  Ad=03(O) Atr=02(Bulk) MxPS=1024 Ivl=0ms
  E:  Ad=81(I) Atr=03(Int.) MxPS=   8 Ivl=11ms
  E:  Ad=82(I) Atr=02(Bulk) MxPS=1024 Ivl=0ms

| make :el:`FIT image <images/f/f4/Elc2013_Fernandes.pdf>`
  with :manpage:`mkimage(1)`
  from :pkg:`community/uboot-tools`
| |b| `uImage.FIT/howto.txt <https://github.com/u-boot/u-boot/blob/master/doc/uImage.FIT/howto.txt>`__
| |b| `ELF to uImage <https://www.denx.de/wiki/view/DULG/HowCanICreateAnUImageFromAELFFile>`__
| |b| `Combining a Kernel and a Ramdisk into a Multi-File Image <https://www.denx.de/wiki/view/DULG/CombiningKernelAndRamdisk>`__

`booting ARM linux <https://www.kernel.org/doc/html/latest/arm/booting.html>`__

| denx - `boot from BOOTP/TFTP <https://www.denx.de/wiki/view/DULG/UBootCmdGroupDownload#Section_5.9.5.1.>`__
| ArchWiki - :aw:`TFTP`

submit to ArchWiki :aw:`BusyBox` and link from :aw:`TFTP#Server`

.. include:: include/escalate.txt

::

   # ip link set dev enp0s31f6 down
   # ethtool -s enp0s31f6 mdix on
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
      initramfs-linux.img
   echo
   busybox udpsvd -E -l 820g3 10.0.0.89 69 tftpd -r -l "$PWD"


PC NFS
======

|:link:| postmarketos\:\ :ref:`postmarketos:backup`

| ArchWiki
| |b| :aw:`Diskless_system#Server_configuration`
| |b| :aw:`NFS`

client |rarr| ``mount`` |rarr| server |rarr| ``rpcbind`` |rarr| ``nfsd`` |rarr| ``mountd``

.. include:: include/escalate.txt

:aw:`append to /etc/exports <diskless system#NFS>` ::

   # https://wiki.archlinux.org/title/Diskless_system#NFS

| |:warning:| :aw:`NFS#Restricting_NFS_to_interfaces/IPs`
| :manpage:`rpc.nfsd(8)`

::

   # https://wiki.archlinux.org/title/NFS#Restricting_NFS_to_interfaces/IPs

| make sure kernel ip forwarding is disabled for security
| kernel doc - `ip sysctl <https://www.kernel.org/doc/html/latest/networking/ip-sysctl.html>`__

::

   sudo sysctl -n net.ipv4.ip_forward
   sudo sysctl -n net.ipv6.conf.all.forwarding
   # expect two '0's

start nfs ::

   # start
   sudo exportfs -arv
   # sudo systemctl start rngd.service # (B)
   sudo systemctl start nfs-idmapd.service # (C)
   sudo systemctl start nfs-mountd.service # (D)
   sudo systemctl start nfsv4-server.service # (?)
   sudo systemctl start nfs-server.service # (E)

   # check
   echo
   exportfs -v
   echo
   systemctl --no-pager status \
      rngd.service \
      nfs-idmapd.service \
      nfs-mountd.service \
      nfs-server.service
   echo

check api fs ::

   echo; findmnt nfsd
   echo; findmnt sunrpc
   echo

check listening ports ::

   echo; rpcinfo -p | grep nfs
   echo; ss -tlnp | grep -e 111 -e 2049 -e 20048
   echo; ss -ulnp | grep -e 111 -e 2049 -e 20048
   echo

test mounting ::

   echo
   # for H in 820g3 10.0.0.89; do
     for H in       10.0.0.89; do
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

:raw-html:`<details><summary><s> <a href="https://www.denx.de/wiki/view/DULG/UseNTPToSynchronizeSystemTimeAgainstRTC">ntp server</a> </s></summary>`

:file:`/etc/systemd/timesyncd.conf`

::

   # With -w, client can't sync from us
   # Without -w, systemd-timesyncd.service is interefered
   printf "\033]0;NTP\007"
   sudo busybox ntpd \
      -dd \
      -n \
      -w \
      -p 0.arch.pool.ntp.org \
      -p 1.arch.pool.ntp.org \
      -p 2.arch.pool.ntp.org \
      -p 3.arch.pool.ntp.org \
      -l \
      -I enp0s31f6

:raw-html:`</details>`


|S0|\ [0]_ TFTP
===============

`README.usb <https://github.com/u-boot/u-boot/blob/master/doc/README.usb>`__

u-boot `drivers/net <https://github.com/u-boot/u-boot/tree/master/drivers/net>`__/e1000

`Net: No ethernet found <https://www.denx.de/wiki/view/DULG/NetNoEthernetFound>`__

| \
  :file:`.dtb` blob file |equiv| FDT (:el:`Flattened Device Tree <Device_Tree_What_It_Is#The_Flattened_Device_Tree_is...>`)
| \
  :file:`.dts`/:file:`.dtsi` |rarr| :pkg:`community/dtc` |rarr| FDT |rarr| kernel internal EDT (:el:`Expanded Device Tree <Device_Tree_What_It_Is#Introduction>`)

:ref:`connect serial <reference_label_section_connect_serial>`

| connect ethernet
| BBGW\:\:USB - USB\:\:AX88179\:\:RJ45 - :wp:`ethernet over twisted pair` - RJ45\:\:820g3

u-boot bring up ethernet

.. code:: text

   usb start

.. code:: text

   usb info

net `variables <https://github.com/u-boot/u-boot/blob/7a4ff7c41bab8b43767eacc0b30ca1573ab6acb1/README#L3314>`__

.. code:: text

   if test $eth4addr = '00:0e:c6:d3:2d:5f'; then
      echo
      echo ok
      echo
      # ax88179_eth
      # setenv ethprime usb_ether
      # setenv ethact   usb_ether
      # setenv ethprime eth4
      # setenv ethact   eth4
      setenv ethprime ax88179_eth
      setenv ethact   ax88179_eth
      setenv ethrotate no
      setenv netretry  no
      printenv ethprime ethact ethrotate netretry
      echo
      setenv ipaddr    10.0.0.64
      setenv clientip  10.0.0.64
      setenv serverip  10.0.0.89
      setenv gwip      10.0.0.89
      setenv netmask   255.255.255.0
      setenv hostname  alarm
      setenv rootdir   /home/darren/beaglebone/alarm_root
      printenv ipaddr clientip serverip gwip netmask hostname rootdir
      echo
   else
     echo "err"
     echo
   fi

ping

.. code:: text

   ping ${serverip}

tftp `variables <https://github.com/u-boot/u-boot/blob/7a4ff7c41bab8b43767eacc0b30ca1573ab6acb1/README#L3359>`__

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
     echo
     echo OK
     echo
     setenv tftpdstp 69
     # setenv tftpblocksize
     setenv tftptimeout 5000
     setenv tftptimeoutcountmax 0
     # setenv tftpwindowsize
     printenv tftpdstp tftptimeout tftptimeoutcountmax
     echo
   else
     echo
     echo ERR
     echo
   fi

| tftp download files
| compare sha1sum against those in
|  ``xdotool windowfocus "$(xdotool search --name TFTP)"``

.. code:: text

   if test 0 -eq 0; then
      tftpboot ${kernel_addr_r}  zImage                             ; setenv kernel_size  ${filesize}
      tftpboot ${fdt_addr_r}     dtbs/am335x-bonegreen-wireless.dtb ; setenv fdt_size     ${filesize}
      tftpboot ${ramdisk_addr_r} initramfs-linux.img                ; setenv ramdisk_size ${filesize}
      echo
      sha1sum ${kernel_addr_r}  ${kernel_size}
      sha1sum ${fdt_addr_r}     ${fdt_size}
      sha1sum ${ramdisk_addr_r} ${ramdisk_size}
      echo
   fi

.. tip::

   Debug with :pkg:`community/wireshark-qt`

`fdt <https://www.denx.de/wiki/DULG/UBootCmdFDT>`__ ::

   if true; then
      fdt addr ${fdt_addr_r}
      fdt list /
      fdt print /cpus
   fi


.. \:raw-html:`<strike>S<sub>0</sub> -> S<sub>1</sub></strike>`
.. \======================================================================

|S0|\ [0]_ -> |S1|\ [1]_ -> |S2|\ [2]_
======================================

make sure no container is running ::

   sudo machinectl list
   sudo ps aux | grep qemu
   sudo ps aux | grep systemd-nspawn

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
| ArchWiki - :aw:`cmdline <kernel parameters#Parameter_list>`
| DULG - `LinuxNfsRoot <https://www.denx.de/wiki/DULG/LinuxNfsRoot>`__

| setenv `bootargs <https://www.denx.de/wiki/view/DULG/LinuxKernelArgs>`__
| |b| ``ramdisk_size=``\ [#rdsz]_
| |b| for ``<nfs-options>`` see :manpage:`nfs(5)`
| |b| ``nfsroot=`` [#tcp]_ [#noNFS4]_
| |b| :prlt:`init=`\ [#shenanigans]_
| |b| :prlt:`rdinit=`\ [#shenanigans]_ [#kdocnfsroot]_

.. code:: text

   if true; then
      setenv bootargsapp
      setenv bootargs
      echo
      setenv bootargsapp console=tty0 console=ttyS0,115200n8                                 ; printenv bootargsapp; setenv bootargs $bootargs $bootargsapp
      setenv bootargsapp ip=${clientip}:${serverip}:${gwip}:${netmask}:${hostname}:eth0:none ; printenv bootargsapp; setenv bootargs $bootargs $bootargsapp
    # setenv bootargsapp  nfsroot=${serverip}:${rootdir},nfsvers=3,proto=tcp,mountproto=tcp  ; printenv bootargsapp; setenv bootargs $bootargs $bootargsapp
      setenv bootargsapp nfsroot=${serverip}:${rootdir}                                      ; printenv bootargsapp; setenv bootargs $bootargs $bootargsapp
      setenv bootargsapp rw rootwait                                                         ; printenv bootargsapp; setenv bootargs $bootargs $bootargsapp
      echo
      printenv bootargs
      echo
   fi

shut down USB in U-Boot before booting Linux [#down]_

.. code:: text

   usb stop

| boot
| bootd
| :pr:`bootefi`
| :pr:`bootelf`
| bootm
| :pr:`bootp`
| :pr:`bootvx`
| bootz

.. code:: text

   # iminfo ${kernel_addr_r}
   setenv silent_linux no
   # bootm ${kernel_addr_r} ${ramdisk_addr_r}:${ramdisk_size} ${fdt_addr_r}
     bootz ${kernel_addr_r} ${ramdisk_addr_r}:${ramdisk_size} ${fdt_addr_r}

.. tip::

   | Debug with :pkg:`community/wireshark-qt`
   | :aw:`NFS/Troubleshooting`


|S2|\ [2]_ Install
==================

| :aw:`Installation guide`
| `alarm wiki <https://archlinuxarm.org/platforms/armv7/ti/beaglebone-green-wireless>`__
  |rarr| ``Installation``

::

   dmesg -D
   export TERM=xterm-256color

::

   cat /proc/cmdline

.. warning::

   Dont execute ``ping`` without specifying number of packets!

::

   # busybox ping -4 -c 4 -I eth0      -w 7 10.0.0.89
             ping -4 -c 4 -I eth0      -w 7 10.0.0.89

::

   # busybox ping -4 -c 4 -I 10.0.0.64 -w 7 10.0.0.89
             ping -4 -c 4 -I 10.0.0.64 -w 7 10.0.0.89

why is there an rtc? ::

   find /sys/class/rtc/

show time ::

   systemctl stop systemd-timesyncd.service &&
   timedatectl set-ntp false &&
   rm -fv /etc/adjtime &&
   timedatectl set-timezone Asia/Makassar &&
   timedatectl status

| sync time
| make sure no stray command in minicom
| execute this command outside minicom
| |troll|

::

   # Lag!
   # printf 'timedatectl set-time "%s"\n' "$(date "+%F %T")" | pv -L8 >/dev/ttyUSB0
     printf 'timedatectl set-time "%s"\n' "$(date "+%F %T")"          >/dev/ttyUSB0

check "synced" time ::

   timedatectl status

write rtc ::

   hwclock --systohc &&
   timedatectl status

erase eMMC

.. danger::

   | **All data on the device will be lost forever**
   | **Make sure you are executing on the correct device**

execute one by one, with caution ::

   lsblk
   wipefs -af /dev/mmcblk1p1
   wipefs -af /dev/mmcblk1
   sync; partprobe
   date; blkdiscard -sv /dev/mmcblk1; date
   sync; partprobe
   date; cmp /dev/zero /dev/mmcblk1; date
   # date; pv -prb /dev/zero | cmp - /dev/mmcblk1; date
     date; dd if=/dev/zero of=/dev/stdout status=progress | cmp - /dev/mmcblk1; date
      # Expect EOF

`4k align <https://www.diskgenius.com/how-to/4k-alignment.php>`__ in :manpage:`fdisk(8)`

.. code:: text

   fdisk is able to optimize the disk layout for
   a 4K-sector size and use an alignment offset on modern devices for MBR and GPT. It is always a good idea to follow
   fdisk's defaults as the default values (e.g., first and last partition sectors) and partition sizes specified by the
   +/-<size>{M,G,...} notation are always aligned according to the device properties.

| partitioning
| |b| partition table ``MBR`` :pr:`GPT`
| |b| single partition
|     |b| first sector ``2048``
|     |b| type ``Linux``

::

   fdisk -l
   fdisk /dev/mmcblk1
   # ...

populate filesystem ::

   mke2fs -n -t ext4 -v /dev/mmcblk1p1

::

   mke2fs    -t ext4 -v /dev/mmcblk1p1
   mount -v /dev/mmcblk1p1 /mnt
   date; bsdtar -xpf /ArchLinuxARM-am33x-latest.tar.gz -C /mnt; sync; date

write u-boot in boot sector before the first partition ::

   # head -c $((2048*512)) /dev/mmcblk1 | od
     head -c $((2048*512)) /dev/mmcblk1 | hexdump
   dd if=/mnt/boot/MLO        of=/dev/mmcblk1 count=1 seek=1 conv=notrunc bs=128k
   dd if=/mnt/boot/u-boot.img of=/dev/mmcblk1 count=2 seek=1 conv=notrunc bs=384k
   sync; partprobe
     head -c $((2048*512)) /dev/mmcblk1 | hexdump | head -100

power off ::

   sync
   umount -v /mnt
   systemctl poweroff


.. _reference_label_section_clean_up:

Host Cleanup
============

|:dart:|

.. include:: include/escalate.txt

::

   mv -v /etc/exports.pacnew /etc/exports
   systemctl stop nfs-server.service # (E)
   systemctl stop nfs-mountd.service # (D)
   systemctl stop nfs-idmapd.service # (C)
   systemctl is-enabled rngd.service || systemctl stop rngd.service # (B)
   systemctl stop rngd.service # (A)

::

   ip address flush dev enp0s31f6
   ip link    set   dev enp0s31f6 down


Footnotes
=========

..

----

.. [0] |S0| - The state where U-Boot with built-in NIC driver is running

.. [1] |S1| - The state where Linux with only initramfs is running (both are TFTP'd)

.. [2] |S2| - The state where a fully functional Linux through NFS is running

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

.. include:: include/link.txt

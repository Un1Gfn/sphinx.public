.. include:: include/substitution.txt
.. include:: include/link.txt

==========
|ico| Test
==========

Tmp
===

::

   sudo rm -rf /tmp/alarm_root &&
   # mkdir -pv "$_" &&
   # cd "$_" &&
   # bsdtar -x --no-same-permissions -f ~/beaglebone/ArchLinuxARM-am33x-latest.tar.gz
   sudo mkdir -pv "$_" &&
   cd "$_" &&
   sudo bsdtar -xpf ~/beaglebone/ArchLinuxARM-am33x-latest.tar.gz -p

::

   # error: chroot to '/tmp/alarm_root' failed: (Operation not permitted)
   # PACMAN="fakeroot /usr/bin/pacman --sysroot /tmp/alarm_root"
     PACMAN="sudo /usr/bin/pacman --sysroot /tmp/alarm_root"
   $PACMAN -Q  | tee ~/beaglebone/alarm_pacman_Q
   $PACMAN -Qq | tee ~/beaglebone/alarm_pacman_Qq
   $PACMAN -Rsc --color auto $($PACMAN -Qq)

::

   sudo tree -a -I 'ca-certificates|certs' -F -C





:raw-html:`<br /><br />`

Extension Showcase
==================

| archlinux.py
| |b| :pkg:`core/base`
| |b| :pkg:`AUR/distccd-alarm-armv7h`

| xxlink.py
| |b| `example <https://example.org>`__
| |b| :emlink:`example <https://example.org>`
| |b| :prlink:`example <https://example.org>`
| |b| :stlink:`example <https://example.org>`
| |b| :ltlink:`example <https://example.org>`


| wikilink.py
| |b| :wp:`Wikipedia`
| |b| :aw:`Archiso`
| |b| :el:`Device Tree Reference`
| |b| :dw:`DebianReleases`
| |b| :gw:`Portage`


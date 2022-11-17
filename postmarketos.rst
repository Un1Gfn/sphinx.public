.. include:: include/substitution.txt
.. highlight:: text

============
postmarketOS
============

.. math::

   \mathit{The\ best\ way\ to\ predict\ the\ future\ is\ to\ invent\ it.} - \href{https://www.ted.com/speakers/alan_kay}{\text{Alan Kay}}

:file:`~/wt88047.?`


#contacts#
==========

:alpine:`Alpine Linux:IRC`

| :mt:`#main:postmarketos.org`
|    travmurav UTC+5 :wp:`YEKT <Yekaterinburg Time>`
|    minecrell UTC+0
|    caleb
|    aka\_ UTC+1 PL CET

| :mt:`#lowlevel:postmarketos.org`
|    swiftgeek


#misc#
======

| Alpine Linux `packages <https://pkgs.alpinelinux.org/packages>`__
| postmarketOS `packages <https://pkgs.postmarketos.org/packages>`__

`postmarketos-ui-phosh <http://pkgs.postmarketos.org/package/master/postmarketos/aarch64/postmarketos-ui-phosh>`__

| :pmos:`terminal cheat sheet`
| :alpine:`comparison with other distros`
| :alpine:`Alpine Linux:Glossary`

| postmarketOS wiki
| :pmos:`the-big-list-of-who-has-what-device`
| :pmos:`contributing` to pmos
| :pmos:`applications by category`
|    `portfolio-file-manager <https://flathub.org/apps/details/dev.tchx84.Portfolio>`__
|    nemo
|    oFono/ModemManager
|    :wp:`maliit` (virtual keyboard)

| `<https://postmarketos.org/source-code/>`__
| \
  :pmos:`mirrors` |vv| `mirrors.py <https://gitlab.com/postmarketOS/postmarketos.org/-/blob/master/config/mirrors.py>`__
  |vv| `ustc <https://mirrors.ustc.edu.cn/postmarketos/>`__
  |vv| `tuna <https://mirrors.tuna.tsinghua.edu.cn/postmarketOS/>`__
  |vv| `aliyun <https://mirrors.aliyun.com/postmarketOS/>`__

| `phosh <https://puri.sm/posts/phosh-overview/>`__
| `plasma mobile <https://plasma-mobile.org/2021/12/07/plasma-mobile-gear-21-12/>`__

unofficial wayland `protocols explorer <https://wayland.app/protocols/>`__

| :pmos:`making good photos`
| :pmos:`preparing videos for blog posts`

| artwork
| `latex beamer (slides) template <https://gitlab.com/postmarketOS/artwork/-/tree/c8b7378e8a71147c0579848754a21a9c65e3d0a9/presentation/latex>`__
| `midi <https://gitlab.com/postmarketOS/artwork/-/tree/7f0fe16c77f674725d2860157393bcc465610bff/tones>`__
| `wallpaper <https://gitlab.com/postmarketOS/artwork/-/tree/2b39e6081c7a676ae1be3fc036ccbfef3052072c/wallpapers>`__
| `blender3d <https://gitlab.com/postmarketOS/artwork/-/tree/028b40914c75c17c084cf6b2358e56948df12a85/src>`__
| `svg <https://gitlab.com/postmarketOS/artwork/-/tree/028b40914c75c17c084cf6b2358e56948df12a85/logo>`__

`Breaking updates in edge <https://postmarketos.org/edge/>`__

| `GNU on a Smartphone          <https://cascardo.eti.br/blog/GNU_on_a_Smartphone/>`__
| `GNU on Smartphones (part II) <https://cascardo.eti.br/blog/GNU_on_Smartphones_part_II/>`__

| :wp:`polkit`
| :aw:`polkit#Examples`
| :manpage:`pkaction(1)`
| allow_active
|    linuxcsuf `Understanding-polkit <https://github.com/linuxcsuf/linuxcsuf/wiki/Understanding-polkit>`__
|    :manpage:`polkit(8)`
|    `suse doc <https://documentation.suse.com/sles/15-SP4/single-html/SLES-security/#sec-security-polkit-policies-implicit>`__

:pmos:`tips and tricks`

`alpine user handbook <https://docs.alpinelinux.org/user-handbook/0.1a/index.html>`__

| :pmos:`inspecting the initramfs`
| :pmos:`initramfs development`

:pmos:`audio`

`gdb in qemu <https://qemu-project.gitlab.io/qemu/system/gdb.html>`__


alarm
=====

| `rtcwake <https://askubuntu.com/a/511804/>`__
| aosp/platform/frameworks/base//data/`sounds <https://android.googlesource.com/platform/frameworks/base.git/+/refs/heads/master/data/sounds>`__
  |rarr| `tgz <https://android.googlesource.com/platform/frameworks/base.git/+archive/refs/heads/master/data/sounds.tar.gz>`__
  |rarr| ~/pmos.pinephone/base.git-refs_heads_master-data-sounds.tar.gz
| postmarketos-tweaks//settings/`sound.yml <https://gitlab.com/postmarketOS/postmarketos-tweaks/-/blob/master/settings/sound.yml>`__

::

   find -type f -name '*.wav' -exec stat -c '%s %n' {} \; | sort -rh | less
   scp ~/pmos.pinephone/sounds/ringtones/wav/Themos.wav user@pinephoneusb:/home/user/.local/share/sounds/__custom/alarm-clock-elapsed.wav
   scp ~/pmos.pinephone/sounds/ringtones/wav/Sceptrum.wav user@pinephoneusb:/home/user/.local/share/sounds/__custom/alarm-clock-elapsed.wav


APKBUILD
========

`pmb install with "temporary error" when installing packages <https://gitlab.com/postmarketOS/pmaports/-/issues/1453>`__

| :pmos:`pmbootstrap`
| `gitlab <https://gitlab.com/postmarketOS/pmbootstrap>`__
| :pmos:`installing pmbootstrap`
| :pmos:`build internals#pmbootstrap_vs._abuild`

| `aports <https://gitlab.alpinelinux.org/alpine/aports/>`__ + `pmaports <https://gitlab.com/postmarketOS/pmaports>`__
| :alpine:`development using git`

| :alpine:`creating an Alpine package`
| :alpine:`setting up the build environment <abuild and Helpers#Setting_up_the_build_environment>`
| :alpine:`abuild and Helpers`

| :alpine:`APKBUILD Reference`
| :alpine:`include:Abuild`


| :file:`~/wt88047.pmbootstrap`
| :file:`~/wt88047.pmaports`

:pmos:`troubleshooting#pmbootstrap_and_build_related_errors`

| :pmos:`purge <installing pmbootstrap#Uninstalling_after_installing_manually>`

.. highlight:: bash

| install pmbootstrap with pacman
| clone https://gitlab.com/postmarketOS/pmaports.git to :file:`~/wt88047.pmaports`

keep out of :file:`~/.local/var` ::

   cat <<EOF >~/.config/pmbootstrap.cfg
   [pmbootstrap]
   work = ~/wt88047.pmbootstrap
   aports = ~/wt88047.pmaports
   mirror_alpine = http://mirrors.aliyun.com/alpine/
   mirrors_postmarketos = http://mirrors.aliyun.com/postmarketOS/
   EOF

init ::

   pmbootstrap shutdown
   pmbootstrap zap
   sudo rm -rfv ~/wt88047.pmbootstrap/!(cache_apk*)
   pmbootstrap init
   # keep default options since it is not used anayway

set up chroot ::

   pmbootstrap status
   # pmbootstrap chroot --add meson,alpine-sdk,elogind-dev,meson,networkmanager-dev,networkmanager-wifi -b aarch64
   pmbootstrap chroot --add gcc,make,meson -b aarch64
   # pmbootstrap netboot
   # pmbootstrap install
   # adduser -u 1000 darren

   # execute outside chroot
   # sudo cp -v /etc/resolv.conf /home/darren/wt88047.pmbootstrap/chroot_buildroot_aarch64/etc/resolv.conf

build in chroot ::

   # cd ~/coldspot
   # ./chroot.sh
   # su - darren
   # cd coldspot.bindmount


backup
======

:pmos:`backup and restore your data`

noatime ::

   mount -o remount,rw,noatime /dev/mapper/mmcblk0p30p2

sort packages by size (bash) [#NOPIPEMAP]_ ::

   # readarray is nothing but an alias of mapfile
   {
      NFO="$(/sbin/apk info -e -s \*)"
      unset -v PKG; readarray -t PKG < <(awk NR%3==1 <<<"$NFO" | cut -d ' ' -f 1) # declare -p PKG
      unset -v SIZ; readarray -t SIZ < <(awk NR%3==2 <<<"$NFO" | tr -d ' ')       # declare -p SIZ
      N="${#PKG[@]}"
      echo "$N ${#SIZ[@]} 0~$((N-1))"
      {
         for i in $(seq 0 $((N-1))); do
            busybox printf "%8s %s\n" "${SIZ[$i]}" "${PKG[$i]}"
         done
      } | /usr/bin/sort -bh | uniq >/tmp/pkg.lst
   }
   sed 's/^/|/g' /tmp/pkg.lst | /usr/bin/less -SRM +%

   # pkgcleanup.installer
   rm -v /var/cache/apk/*-*-r*.????????.apk
   # pkgcleanup.package
   # apk del -ir ...


.. nencrypted plain nfs over usbnet (`unudhcpd <https://pkgs.alpinelinux.org/package/v3.16/community/aarch64/unudhcpd>`__)
.. installalarm\:\ :ref:`installalarm:PC NFS`
.. # nfs.client
.. showmount -e 172.16.42.2
.. mount -v 172.16.42.2:/home/darren/pmos.backup /mnt.pmos.backup

nbd.server ::

   # drop runlevel
   # rc-service tinydm stop
   rc-update add sshd boot; openrc boot

   # tmpfs for tmux
   : manually clean up /tmp, move out valuable files
   mount -vt tmpfs tmpfs /tmp
   tmux new -s nbd

   # ro
   echo 3 | tee /proc/sys/vm/drop_caches
   sync
   cd /tmp
   mount -vo remount,ro,noatime /
   findmnt /
   fstrim -v /
   fsck.ext4 -fvn /dev/dm-1; echo '$?='$?
   # fsck.ext4 -Dfv /dev/dm-1; echo '$?='$?

   # nbd
   modprobe -v nbd
   cat <<EOF | sed 's/^\s*//g' | tee /tmp/config
      [generic]
         allowlist = true
         listenaddr = 172.16.42.1
         oldstype = false
      [vuf7p0]
         exportname = /dev/dm-1
         readonly = true
   EOF
   nbd-server -C /tmp/config -d

e2image qcow2 (820g3) (tmux) (superuser) ::

   modprobe -v nbd
   nbd-client 172.16.42.1 -l
   nbd-client 172.16.42.1 /dev/nbd0 -name vuf7p0
   nbd-client -c /dev/nbd0; echo '$?='$?
   file -sL /dev/nbd0; date; e2image -aQ /dev/nbd0 /home/darren/pmos.backup/pmOS_root.e2i.qcow2; date
   file /home/darren/pmos.backup/pmOS_root.e2i.qcow2
   nbd-client -d /dev/nbd0
   rmmod -v nbd



bluetooth
=========

| :wp:`list of Bluetooth protocols#Radio_frequency_communication_(RFCOMM)`
| `rfcomm.rst <https://github.com/bluez/bluez/blob/43f547d7e55ceae1825909b6d50f89320e7d81e8/tools/rfcomm.rst>`__
| `alternatives <https://unix.stackexchange.com/questions/352494/alternative-to-the-now-deprecated-rfcomm-binary-in-bluez>`__
| :pkg:`AUR/bluez-rfcomm`

https://unix.stackexchange.com/questions/92255/how-do-i-connect-and-send-data-to-a-bluetooth-serial-port-on-linux
https://askubuntu.com/questions/248817/how-to-i-connect-a-raw-serial-terminal-to-a-bluetooth-connection
https://blog.habets.se/2022/02/SSH-over-Bluetooth-cleanly.html
https://hacks.mozilla.org/2017/02/headless-raspberry-pi-configuration-over-bluetooth/

camera
======

| `ov8865.c <https://github.com/torvalds/linux/blob/master/drivers/media/i2c/ov8865.c>`__
| `ov2680.c <https://github.com/torvalds/linux/blob/master/drivers/media/i2c/ov2680.c>`__

linux-postmarketos-qcom-msm8916/`config-postmarketos-qcom-msm8916.aarch64 <https://gitlab.com/postmarketOS/pmaports/-/blob/master/device/community/linux-postmarketos-qcom-msm8916/config-postmarketos-qcom-msm8916.aarch64>`__

::

   env XDG_SESSION_TYPE=wayland WAYLAND_DISPLAY=wayland-0 DISPLAY=:0 megapixels

| `linux-xiaomi-wt88047-downstream <http://pkgs.postmarketos.org/package/master/postmarketos/armv7/linux-xiaomi-wt88047-downstream>`__
| `device-xiaomi-wt88047-downstream <http://pkgs.postmarketos.org/package/master/postmarketos/armv7/device-xiaomi-wt88047-downstream>`__


megapixels - `Linux video subsystem <https://gitlab.com/postmarketOS/megapixels/-/tree/1.5.2#linux-video-subsystem>`__


HID
===

:wp:`Human interface device`
:pmos:`troubleshooting:HID_buttons`

hotspot
=======

| `<https://developer-old.gnome.org/NetworkManager/stable/settings-802-11-wireless.html>`__
| `<https://gist.github.com/narate/d3f001c97e1c981a59f94cd76f041140>`__

:manpage:`nmcli(1)` ::

   # marks the device as unavailable for auto-connecting
   # nmcli dev: STATE=disconnected
   nmcli c down HotspotManual

   # without preventing the device from further auto-activation
   # nmcli dev: STATE=unavailable
   # nmcli d down wlan0
   nmcli r wifi off
   nmcli r wwan off

:file:`/usr/local/bin/Hotspot.sh`

C libnm/dbus `examples <https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/blob/main/examples/C>`__

::

   find / | grep -i -e polkit -e policy | grep -i -e network -e nm
   # /usr/share/polkit-1/actions/org.freedesktop.NetworkManager.policy
   # /usr/share/polkit-1/rules.d/01-org.freedesktop.NetworkManager.settings.modify.system.rules

| libnm doc on `gnome <https://developer-old.gnome.org/libnm-glib/stable/>`__
| `transfer <https://gi.readthedocs.io/en/latest/annotations/giannotations.html#memory-and-lifecycle-management>`__ none full ...

| nm_client_get_all_devices() |rarr| nm_device_filter_connections() |rarr| NMConnection
|    |rarr| nm_client_get_connection_by_uuid(nm_connection_get_uuid()) |rarr| NM\ **Remote**\ Connection
| nm_client_wireless_set_enabled(FALSE) |rarr| nm_device_get_available_connections() |rarr| NM\ **Remote**\ Connection

::

   nmcli con show 22b985e1-e00e-4e0a-be92-8d9de9903968 550757c3-3ebc-4451-a61a-f95d36a029d4 | grep -Ee 'connection.(id|uuid|auto)'

| these functions doesn't seem to work in pmOS 22.06 libnm-1.38.2-r1
|    nm_connection_add_setting()
|    nm_setting_connection_get_autoconnect()
|    nm_setting_option_clear_by_name()
|    nm_setting_option_get_all_names()
|    nm_setting_option_set()
|    nm_setting_option_set_boolean()

| toggle mobile data without disabling modem
|    nm_device_disconnect()
|    nm_client_get_active_connections() |rarr| nm_client_deactivate_connection()
|    nm_client_activate_connection_async()


location.GNSS
=============

:wp:`Assisted GNSS` |vv| A-GNSS |vv| AGPS

:pmos:`Qualcomm Snapdragon 410/412 (MSM8916)#GNSS_(GPS)`

`GNSS Share <https://gitlab.com/postmarketOS/gnss-share>`__

::

   qrtr-lookup | grep -iE 'node|loc'
   sudo qmicli -pd qrtr://0:18 --loc-start --client-no-release-cid

   sudo qmicli -pd qrtr://0:18 --client-cid=1 --loc-get-position-report
   sudo qmicli -pd qrtr://0:18 --client-cid=1 --loc-get-gnss-sv-info

   qmicli --help     | sed -E 's/([^ ]) {40}/\1/g' | less -SRM
   qmicli --help-loc | sed -E 's/([^ ]) {48}/\1/g' | less -SRM
   sudo qmicli -pd qrtr://0:18 --client-cid=1 --loc-follow-nmea | gpsd -bnN /dev/stdin


location.GPS
============


modem
=====

| :pmos:`Dual-Sim QMI draft <User:TravMurav/Dual-Sim_QMI_draft>`
| :pmos:`mobile data <modem#Mobile_Data>`

::

   nmcli con add con-name "modem" type "gsm" ifname "wwan0qmi0" apn "3gnet" user "blank" password "blank"

sudo service rmtfs restart [#RMTFS]_


OpenRC
======

| :aw:`OpenRC` - aw
| :gentoo:`OpenRC` - gentoo
| :gentoo:`OpenRC to systemd Cheatsheet`
| :gentoo:`comparison of init systems`
| :alpine:`Writing Init Scripts`

::

   sudo rc-status


SMS
===

::

   $ sqlite3 /home/user/.purple/chatty/db/chatty-history.db '.SCHEMA messages'
   CREATE TABLE messages (
      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      uid TEXT NOT NULL,
      thread_id INTEGER NOT NULL REFERENCES threads(id) ON DELETE CASCADE,
      sender_id INTEGER REFERENCES users(id),
      user_alias TEXT,
      body TEXT NOT NULL,
      body_type INTEGER NOT NULL,
      direction INTEGER NOT NULL,
      time INTEGER NOT NULL,
      status INTEGER,
      encrypted INTEGER DEFAULT 0,
      preview_id INTEGER REFERENCES files(id),
      subject TEXT,
      UNIQUE (
         uid,
         thread_id,
         body,
         time
      )
   );

::

   sqlite3 /home/user/.purple/chatty/db/chatty-history.db 'SELECT * FROM messages'
   sqlite3 /home/user/.purple/chatty/db/chatty-history.db 'SELECT body FROM messages ORDER BY time ASC'


Footnotes
=========

.. [#RMTFS] :mt:`#main:postmarketos.org/$AZBbV9jdhw1u7uRQE_6Yq-XCT0ywmd941mSlrCUXUuU`
.. [#NOPIPEMAP] `cannot pipe into a command which takes a varname as an arg <https://superuser.com/a/1348950/>`__ (readarray/mapfile)

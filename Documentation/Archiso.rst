.. include:: substitution.txt

===========
`Archiso`__
===========

.. __: https://github.com/Un1Gfn/archiso


Misc
====

:aw:`ArchWiki <archiso>`

`GitLab instance <https://gitlab.archlinux.org/archlinux/archiso/>`__

`CHANGELOG.rst <https://gitlab.archlinux.org/archlinux/archiso/-/blob/master/CHANGELOG.rst>`__

`README.profile.rst`_

list files ::

   cd ~/archiso
   exa -T -a -s extension -I '.git|.gitignore|archlive'

sqeeze everything out of readme.sh

:pr:`Cheatsheet - Bash - assertion or error handling - sed ... @ABRTEXIT@ ... @ABRTRET@ ...`

:aw:`Full_system_backup_with_SquashFS`

Check mkfs timestamp of PaaFS (Partition-as-a-Filesystem) (mkfs.ext4 /dev/sdXN) ::

   sudo dumpe2fs /dev/sdXN

Check mkfs timestamp of DaaFS (Drive-as-a-Filesystem) (mksquashfs ... /dev/sdX) ::

   sudo file -sL /dev/sda
   sudo unsquashfs -stat /dev/sdX


Swipe
=====

| /root/.config/filelightrc
| \
  ``sudo filelight`` |rarr|
  :file:`Settings` |rarr|
  :file:`Configure Filelight...` |rarr|
  :file:`Scanning` |rarr|
  :file:`Do not scan these folders:`

::

   source ~/archiso/ignarr.bashrc
   # https://stackoverflow.com/q/53839253
   # builtin printf --help
   builtin printf -v joined '%s,' "${IGNARR_FILELIGHT[@]}"
   SCRIPT="$(printf 's|^skipList.*$|skipList[$e]=%s|g' "${joined%,}")"
   echo "$SCRIPT"
   # sudo sed    -e "$SCRIPT" /root/.config/filelightrc
     sudo sed -i -e "$SCRIPT" /root/.config/filelightrc
   unset -v IGNARR_FILELIGHT SCRIPT

::

   sudo filelight

Prepare
=======

.. warning::

   | Don't escalate yet
   | |:no_entry_sign:| su
   | |:no_entry_sign:| sudo

default umask in :pkg:`core/filesystem`\ `etc/profile`__ is ``022`` [#profilelog]_

.. table::
   :align: left
   :widths: auto

   =========== ========================== ============== ============================================================
    type        permissions w/o mask       mask           permissions w mask
   =========== ========================== ============== ============================================================
    file        :file:`0666 = rwxrwxrwx`   :file:`0022`   :file:`0666 - 0022 = 0644 = rw-r--r--`
    directory   :file:`0777 = rwxrwxrwx`   :file:`0022`   :file:`0777 - 0022 = 0755 = rwxr-xr-x`
   =========== ========================== ============== ============================================================

.. __: https://github.com/archlinux/svntogit-packages/blob/ed2da51a91162eaa0916dc3d9725fb2b574fb901/trunk/profile#L4

upgrade ::

   sudo pacman -Fy; sudo pacman -Syuu

tmux ::

   tmux attach || tmux

check umask ::

   {
     [ "$(umask)" = "0022" ] &&
     [ "$(umask -S)" = "u=rwx,g=rx,o=rx" ];
   } || echo "error"

.. warning::

   Vars will be lost once you leave tmux 

vars ::

   BASELINE="/usr/share/archiso/configs/baseline"
   RELENG="/usr/share/archiso/configs/releng"
   PROJ="$HOME/archiso"
   ARCHLIVE="$PROJ/archlive"
   AIROOTFS="$ARCHLIVE/airootfs"
   BASELINEPKG="$BASELINE/packages.x86_64"
   RELENGPKG="$RELENG/packages.x86_64"
   ARCHLIVEPKG="$ARCHLIVE/packages.x86_64"
   printf "\033]0;archiso\007"


Packages
========

check bootstrap packages [#bootpkg]_ ::

   BOOTPKG=arch-install-scripts$'\n'base$'\n'
   if
      cmp <(echo -n "$BOOTPKG") "$BASELINE/bootstrap_packages.x86_64" &&
      cmp <(echo -n "$BOOTPKG") "$RELENG/bootstrap_packages.x86_64";
   then
      printf "\n\e[32m%s\e[0m\n\n" "  ok"
   else
      printf "\n\e[31m%s\e[0m\n\n" "  err"
   fi
   unset -v BOOTPKG

check if releng and baseline are sorted and newline-terminated ::

   # https://stackoverflow.com/q/38746/how-to-detect-file-ends-in-newline/25749716#25749716
   for CONF in "$BASELINEPKG" "$RELENGPKG"; do
      if [ "$(tail -c1 "$CONF" | wc -l)" -eq 1 ];
      then printf "\n  %s \e[32m%s\e[0m\n\n" "$CONF"  "newline-terminated"
      else printf "\n  %s \e[31m%s\e[0m\n\n" "$CONF"  "not newline-terminated"
      fi
      if cmp "$CONF" <(env LC_ALL=C sort "$CONF");
      then printf "\n  %s \e[32m%s\e[0m\n\n" "$CONF"  "sorted"
      else printf "\n  %s \e[31m%s\e[0m\n\n" "$CONF"  "not sorted"
      fi
   done

make sure baseline is a strict subset of releng ::

   if
      [ -z "$(env LC_ALL=C comm    -2 -3 --check-order "$BASELINEPKG" "$RELENGPKG")" ] &&
      [ -n "$(env LC_ALL=C comm -1    -3 --check-order "$BASELINEPKG" "$RELENGPKG")" ] &&
      cmp "$BASELINEPKG" <(env LC_ALL=C comm -1 -2 --check-order "$BASELINEPKG" "$RELENGPKG");
   then
      printf "\n\e[32m%s\e[0m\n\n" "  ok"
   else
      printf "\n\e[31m%s\e[0m\n\n" "  err"
   fi

.. warning::

   Previous customizations will be lost

copy releng ::

   cd "$PROJ"
   rm -rf "$ARCHLIVE"
   cp -r "$RELENG" "$ARCHLIVE"

write canonicalized package list ::

   source "$PROJ/pkgarr.bashrc"
   printf "%s\n" ${PKGARR[@]} | env LC_ALL=C sort | uniq >"$ARCHLIVEPKG"
   unset -v PKGARR

packages unique to releng (compared to archlive) ::

   echo; env LC_ALL=C comm    -2 -3 "$RELENGPKG" "$ARCHLIVEPKG" | sed -e 's/^/- /g'; echo

packages unique to archlive (compared to releng) ::

   echo; env LC_ALL=C comm -1    -3 "$RELENGPKG" "$ARCHLIVEPKG" | sed -e 's/^/+ /g'; echo


Files
=====

:raw-html:`<details><summary><s>change root password</s></summary>`

| :aw:`Archiso#Users_and_passwords`
| ``openssl passwd -6``

:raw-html:`</details>`

:raw-html:`<details><summary><s>copytoram (loader entry already provided)</s></summary>`

| gitlab/archlinux/archiso             - `README.profile.rst`_  - #efiboot
| gitlab/mkinitcpio/mkinitcpio-archiso - `README.bootparams`__

.. __: https://gitlab.archlinux.org/mkinitcpio/mkinitcpio-archiso/-/blob/master/docs/README.bootparams

copytoram ::

   sed \
     -e 's|^\(title.*\)$|\1 (copytoram)|g' \
     -e 's|^\(options.*\)$|\1 copytoram=y copytoram_size=75%|g' \
      "$ARCHLIVE/efiboot/loader/entries/archiso-x86_64-linux.conf" \
     >"$ARCHLIVE/efiboot/loader/entries/archiso-x86_64-copytoram-linux.conf"

:raw-html:`</details>`

convenience mountpoints ::

   mkdir -v "$AIROOTFS"/mnt.{nvme,usb}

timezone ::

   rm -fv "$AIROOTFS/etc/localtime"
   ln -sfv "/usr/share/zoneinfo/Asia/Makassar" "$_"
   file "$_"

:manpage:`motd(5)` :manpage:`issue(5)` ::

   if [ -e "$AIROOTFS/etc/motd.orig" ]; then
      printf "\n\e[31m%s\e[0m\n\n" "  err"
   else
      cp -v "$AIROOTFS/etc/motd"{,.orig}
      {
         echo "/etc/motd"
         echo
         cat "$AIROOTFS/etc/motd"
      } | sponge "$AIROOTFS/etc/motd"
      echo
      cat "$AIROOTFS/etc/motd"
   fi

:file:`exclude_file` for :file:`mksquashfs.sh` ::

   source "$PROJ/ignarr.bashrc"
   builtin printf '%s\n' "${IGNARR_MKSQUASHFS[@]}" >"$AIROOTFS/exclude_file"
   echo
   cat "$AIROOTFS/exclude_file"
   echo
   unset -v IGNARR_MKSQUASHFS

| :file:`mksquashfs.sh`
| `README.profile.rst <https://gitlab.archlinux.org/archlinux/archiso/-/blob/master/docs/README.profile.rst>`__ - #airootfs
| :manpage:`sed(1)`
| |b| Zero- or One- address commands |rarr| ``a \ text`` |rarr| Append text
| |b| Addresses |rarr| ``/regexp/`` |rarr| Match  lines  matching  the regular expression regexp

::

   echo
   install -m755 -v "$PROJ/mksquashfs.sh" "$AIROOTFS/"
   ln -sfv "/mksquashfs.sh" "$AIROOTFS/usr/local/bin/mksquashfs.sh"
   exa -l "$_"
   echo
   sed -e '/^file_permissions=(/a \ \ ["/mksquashfs.sh"]="0:0:755"' "$RELENG/profiledef.sh" >"$ARCHLIVE/profiledef.sh"
   diff -u --color {"$RELENG","$ARCHLIVE"}/profiledef.sh
   echo

enable gpm ::

   ln -sv "/usr/lib/systemd/system/gpm.service" "$ARCHLIVE/airootfs/etc/systemd/system/multi-user.target.wants/gpm.service"
   exa -l "$_"

no accidental suspend ::

   if   [ -e "$AIROOTFS/etc/systemd/logind.conf" ];
   then printf "\n\e[31m%s\e[0m\n\n" "  err"
   else tee <<EOC >"$AIROOTFS/etc/systemd/logind.conf"
   [Login]
   HandlePowerKey=suspend
   HandleSuspendKey=ignore
   HandleHibernateKey=ignore
   HandleLidSwitch=ignore
   HandleLidSwitchExternalPower=ignore
   HandleLidSwitchDocked=ignore
   HandleRebootKey=ignore
   IdleAction=ignore
   EOC
   fi

**kill da madafakin dhc\***

::

   find "$ARCHLIVE" -iname '*udev*'
   # rm -fv "$ARCHLIVE/airootfs/etc/udev/rules.d/81-dhcpcd.rules"

::

   # env SYSTEMD_COLORS=1 systemctl --root="$AIROOTFS" --no-pager list-unit-files
   echo
   exa -aT "$AIROOTFS/etc/systemd/system"/*.wants
   echo

::

   pushd "$AIROOTFS/etc/systemd/system/"
   rm    -r -v cloud-init.target.wants
   rm       -v multi-user.target.wants/choose-mirror.service
   rm       -v multi-user.target.wants/iwd.service
   rm       -v multi-user.target.wants/livecd-talk.service
   rm       -v multi-user.target.wants/ModemManager.service
   rm       -v multi-user.target.wants/reflector.service
   rm       -v multi-user.target.wants/sshd.service             # Vulnerable
   rm       -v multi-user.target.wants/systemd-networkd.service
   rm    -r -v network-online.target.wants
   popd

::

   # env SYSTEMD_COLORS=1 systemctl --root="$AIROOTFS" --no-pager list-unit-files
   echo
   exa -aT "$AIROOTFS/etc/systemd/system"/*.wants
   echo


Mkarchiso
=========

findmnt snapshot ::

   sudo findmnt -A >/tmp/findmnt.before_mkarchiso

drop caches & discard ::

   free -h
   su -c 'builtin echo 3 >/proc/sys/vm/drop_caches'
   sudo systemctl start fstrim.service
   su -c 'builtin echo 3 >/proc/sys/vm/drop_caches'
   free -h

.. tip::

   Exit Chromium, Firefox and other apps to free up some RAM

.. warning::

   Do not clear screen or scrollback buffer before an ISO is successfully generated

build the ISO as root ::

   sudo \
     /usr/bin/time --format="\n  wall clock time - %E\n" \
     mkarchiso \
      -v \
      -w /tmp/archiso-tmp/ \
      -o "$PROJ" \
      "$ARCHLIVE"
   sudo chown -v darren:darren "$PROJ/archlinux-$(date +%Y.%m.%d)-x86_64.iso"
   file "$PROJ/archlinux-$(date +%Y.%m.%d)-x86_64.iso"

record checksum manually ::

   cd "$PROJ"
   sha256sum "archlinux-$(date +%Y.%m.%d)-x86_64.iso"
   subl "archlinux-$(date +%Y.%m.%d)-x86_64.iso.sha256sum"
   # Paste hash alone, w/o filename, newline-terminated

.. tip::

   | To verify checksum later
   | \
     ``F="archlinux-$(date +%Y.%m.%d)-x86_64.iso"; echo "$(cat "$F.sha256sum")  $F" | sha256sum -c --strict -w; unset -v F``

.. warning::

   Make sure there are no mount binds before removing work directory ::

      if su -c 'diff -u /tmp/findmnt.before_mkarchiso <(findmnt -A)'
      then printf "\n\e[32m%s\e[0m\n\n" "  ok"
      else printf "\n\e[31m%s\e[0m\n\n" "  err"
      fi

remove work directory ::

   sudo rm -r /tmp/archiso-tmp
   sudo sh -c 'echo 3 >/proc/sys/vm/drop_caches'
   free -h

qemu ::

   run_archiso -d -i "$PROJ/archlinux-$(date +%Y.%m.%d)-x86_64.iso" -u

`Transfer`__
============

.. __: https://gitlab.archlinux.org/archlinux/archiso/-/blob/master/docs/README.transfer

Escalate

.. code:: shell-session

   $ su -
   Password:
   #

plug in removable drive ::

   lsusb

.. danger::

   Make sure there are **no valuable data** on the drive before **wiping everything** ::

      lsblk -f

wipefs

.. code:: shell-session

   # wipefs -af /dev/sdXN
   # wipefs -af /dev/sdXN

   # wipefs -af /dev/sdX

zerofill

.. code:: shell-session

   # head -c"$((10*1024*1024))" /dev/zero >/dev/sdX

sync ::

   sync
   partprobe

spin down ::

   udisksctl power-off -b /dev/sdX

reattach ::

   # Detatch
   # Reattach
   lsusb
   lsblk -f

.. tip::

   | What about a health check before writing?
   | :file:`~/archiso/disk_health.bashrc`

write ::

   date
   cat "archlinux-$(date +%Y.%m.%d)-x86_64.iso" >/dev/sdX
   date

sync ::

   sync
   partprobe

inspect ::

   lsblk -f

byte by byte compare

.. code:: shell-session

   # cd ~/archiso
   # D=/dev/sdX
   # F="archlinux-$(date +%Y.%m.%d)-x86_64.iso"

::

   SZ="$(stat -c %s "$F")"
   function err { printf "\n\e[31m%s\e[0m\n\n" "  err"; }
   if   ! [ "$SZ" = "$(wc -c  "$F" | cut -d' '   -f1)" ]; then err
   elif ! [ "$SZ" = "$(du -ab "$F" | cut -d$'\t' -f1)" ]; then err
   elif ! ((SZ%512==0)); then err
   else
      date
      # diff -u --color "$F.sha256sum" <(head -c "$SZ" "$D" | sha256sum | cut -d' ' -f1)
      # cmp -l -n "$SZ" "$F" "$D"
      cmp -l -n "$((SZ+1))" "$F" "$D"
      R="$?"
      date
      if [ 0 -eq "$R" ];
      then printf "\n\e[32m%s\e[0m\n\n" "  ok"
      else err
      fi
   fi
   unset -f err

spin down

.. code:: shell-session

   # udisksctl power-off -b /dev/sdX

detatch


What to Do in ISO
============================

backup ::

   mksquashfs.sh ... ...

turn off screen ::

   vbetool dpms off; read -r; vbetool dpms on


Inspect Backup
==============

rofi -  drun - pcmanfm

::

   # -o ro,gid="$(id -u)",uid="$(id -g)"
   sudo mount -v -t squashfs -o ro /run/media/darren/*/*.sfs /mnt

::

   umount -vR /mnt
   # udisksctl unmount -p ?
   udisksctl unmount -b /dev/sd??
   udisksctl power-off -b /dev/sd??

Footnotes
=========

.. [#profilelog] `history <https://github.com/archlinux/svntogit-packages/commits/packages/filesystem/trunk/profile>`__ of :file:`/etc/profile`
.. [#bootpkg] | `configs/baseline/bootstrap_packages.x86_64`__
              | `configs/releng/bootstrap_packages.x86_64`__
.. __: https://gitlab.archlinux.org/archlinux/archiso/-/blob/0f3a83abf767d0efd409d5563feb13d762c82c7c/configs/baseline/bootstrap_packages.x86_64
.. __: https://gitlab.archlinux.org/archlinux/archiso/-/blob/0f3a83abf767d0efd409d5563feb13d762c82c7c/configs/releng/bootstrap_packages.x86_64

.. links
.. _README.profile.rst: https://gitlab.archlinux.org/archlinux/archiso/-/blob/master/docs/README.profile.rst

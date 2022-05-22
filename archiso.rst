.. include:: include/substitution.txt

=============
:aw:`Archiso`
=============

Misc
====

| gitlab.archlinux.org/archlinux/`archiso <https://gitlab.archlinux.org/archlinux/archiso/>`__
|    `CHANGELOG.rst <https://gitlab.archlinux.org/archlinux/archiso/-/blob/master/CHANGELOG.rst>`__
|    docs/`README.profile.rst <https://gitlab.archlinux.org/archlinux/archiso/-/blob/master/docs/README.profile.rst>`__

list files ::

   cd ~/archiso
   exa -aT -s extension -I '.git|.gitignore|archlive'


check mkfs timestamp of PaaFS (Partition-as-a-Filesystem) (mkfs.ext4 /dev/sdXN) ::

   sudo dumpe2fs /dev/sdXN | head -70

check mkfs timestamp of DaaFS (Drive-as-a-Filesystem) (mksquashfs ... /dev/sdX) ::

   sudo file -sL /dev/sda
   sudo unsquashfs -stat /dev/sdX

default umask in `etc/profile <https://github.com/archlinux/svntogit-packages/blob/ed2da51a91162eaa0916dc3d9725fb2b574fb901/trunk/profile#L4>`__
(:pkg:`core/filesystem`) is ``022`` [#profilelog]_

.. table::
   :align: left
   :widths: auto

   =========== ========================== ============== ============================================================
    type        permissions w/o mask       mask           permissions w/ mask
   =========== ========================== ============== ============================================================
    file        :file:`0666 = rwxrwxrwx`   :file:`0022`   :file:`0666 - 0022 = 0644 = rw-r--r--`
    directory   :file:`0777 = rwxrwxrwx`   :file:`0022`   :file:`0777 - 0022 = 0755 = rwxr-xr-x`
   =========== ========================== ============== ============================================================

modify users ans groups ::

   PASSWORD='SOME_PASSWORD'
   function create_user {
      # Users and passwords
      # QUOTING & HISTORY EXPANSION '!''
      set +H
      # diff -u <(cat $AIROOTFS/etc/shadow) <(sudo grep root /etc/shadow)
      # Groups
      echo "darren:x:1000:"  >>"$AIROOTFS/etc/group"
      echo   "root:!!::root" >>"$AIROOTFS/etc/gshadow"
      echo "darren:!!::"     >>"$AIROOTFS/etc/gshadow"
      # Users
      echo  "darren:x:1000:1000:darren:/home/darren:/usr/bin/zsh"                      >>"$AIROOTFS/etc/passwd"
      sed -i "s|root::14871::::::|root:$(openssl passwd -6 "$PASSWORD"):14871::::::|g"   "$AIROOTFS/etc/shadow"
      echo                     "darren:$(openssl passwd -6 "$PASSWORD"):14871::::::"   >>"$AIROOTFS/etc/shadow"
      #
      diff -uN $AIROOTFS{0,}/etc/group
      diff -uN $AIROOTFS{0,}/etc/gshadow
      diff -uN $AIROOTFS{0,}/etc/passwd
      diff -uN $AIROOTFS{0,}/etc/shadow
   }

syslinux serial ::

   function syslinux_serial {
      # https://wiki.archlinux.org/title/Talk:Archiso#Add_a_section_to_Tips_and_Tricks_to_build_an_ISO_for_installation_entirely_over_a_serial_console
      # https://wiki.archlinux.org/index.php/Working_with_the_serial_console#Installing_Arch_Linux_using_the_serial_console
      # https://wiki.archlinux.org/index.php/Syslinux#Kernel_parameters
      # https://wiki.syslinux.org/wiki/index.php?title=Config#APPEND
      sed -e '/APPEND/ s/$/ console=ttyS0,38400/' /root/archlive/syslinux/archiso_sys.cfg >tmp.cfg
      diff -u /root/archlive/syslinux/archiso_sys.cfg tmp.cfg --color=always
      mv -iv tmp.cfg /root/archlive/syslinux/archiso_sys.cfg # Press 'y' before Enter!
   }


Mkarchiso
=========

**run as unprivileged user**

tmux ::

   tmux new -s archiso

launch ::

   cd ~/archiso
   ./archiso.py

sha1sum

.. table::
   :align: left
   :widths: auto

   ================================= =================================================
    iso                               sha1sum
   ================================= =================================================
    archlinux-2022.01.19-x86_64.iso   :kbd:`744b8d84bc1dae3cfee1427f2a6b9883dae70ad2`
    archlinux-2021.10.09-x86_64.iso   :kbd:`31077a281a062ef51ee3ff3fbf565d05c213a9dc`
   ================================= =================================================

qemu ::

   # function my_run_archiso {
   #   # -display gtk \
   #   # -vga std \
   #   # -vga qxl \
   #   # -machine type=kvm64 \
   #   # -cpu host \
   #   qemu-system-x86_64 \
   #     -accel kvm \
   #     -boot order=d,menu=on,reboot-timeout=5000 \
   #     -m size=3072,slots=0,maxmem=$((3072*1024*1024)) \
   #     -k en \
   #     -name archiso,process=archiso_0 \
   #     -drive file=/home/darren/archlinux-2020.04.30-x86_64.iso,media=cdrom,readonly=on \
   #     -display sdl \
   #     -vga virtio \
   #     -no-reboot \
   #     -no-shutdown \
   #     #
   # }

   run_archiso -d -i "$PROJ/archlinux-$(date +%Y.%m.%d)-x86_64.iso" -u
      # Probing EDD (edd=off to disable)

`Transfer`__
============

.. __: https://gitlab.archlinux.org/archlinux/archiso/-/blob/master/docs/README.transfer

.. include:: include/escalate.txt

plug in removable drive ::

   lsusb

.. danger::

   Make sure there are **no valuable data** on the drive before **wiping everything** ::

      lsblk -f

wipefs

.. code:: shell-session

   # wipefs -af /dev/sdXN
   # wipefs -af /dev/sdXN
   # ...
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

.. warning::

   | If the last bytes don't fill up a 512B sector
   | :command:`dd` might zero out the rest
   | :command:`cat` doesn't

write ::

   cd ~darren/archiso
   date
   # Change "null" to the correct device
   # dd if=archlinux-$(date +%Y.%m.%d)-$(uname -m).iso of=/dev/null status=progress

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
      cmp -l -n "$((SZ-1))" "$F" "$D"
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

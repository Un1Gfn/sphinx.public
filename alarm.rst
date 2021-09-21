.. include:: include/substitution.txt

===============
|ico| `ALARM`__
===============

.. __: https://archlinuxarm.org/


Misc
====

.. warning::

   Install/remove packages in either tmux or minicom
   ssh might bring pacman down

:aw:`Post-Installation <installation_guide#Post-installation>`

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

log in as root

there should be no rtc at all ::

   find /sys/class/rtc/

| sntp time with internet
| |b| :aw:`system time`
| |b| :aw:`systemd-timesyncd`
| |b| kernel doc - `timers <https://www.kernel.org/doc/html/latest/timers/index.html>`__

::

   export SYSTEMD_COLORS=1
   systemctl enable systemd-timesyncd.service
   systemctl start  systemd-timesyncd.service
   timedatectl set-ntp false
   timedatectl set-time '1989-06-04 00:00:00'
   timedatectl set-ntp true
   echo
   timedatectl show
   echo
   timedatectl status
   echo
   hwclock --show
   echo
   timedatectl show-timesync -a
   echo
   timedatectl timesync-status
   echo

:pkg:`AUR/fake-hwclock-git`

::

   # git clone https://aur.archlinux.org/fake-hwclock-git.git
   # makepkg -si

::

   systemctl enable fake-hwclock.service

locale ::

   sed -i.pacnew 's/^#en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/g' /etc/locale.gen
   diff --color=always -u /etc/locale.gen{.pacnew,}
   locale-gen


Network & Time
==============

| :aw:`wireless#Manual/automatic_setup`
| |b| :aw:`network managers <network configuration#Network_managers>` (:aw:`category <category:Network_managers>`)
| |b| :aw:`iw vs wireless_tools <network configuration/Wireless#iw_and_wireless_tools_comparison>`
| |b| :aw:`iproute2 vs net-tools <network_configuration#net-tools>`
| |b| \
      |:ballot_box_with_check:| - pre-installed in tarball

.. table::
   :align: left
   :widths: auto

   +------------+---------------------------------------------------------------------------+---------------------------------------+
   | high-level | :pr:`networkmanager`                                                                                              |
   |            +---------------------------------------------------------------------------+---------------------------------------+
   |            | :pr:`wicd`                                                                                                        |
   |            +---------------------------------------------------------------------------+---------------------------------------+
   |            | :aw:`connman` (intel)                                                     | :manpage:`connman-service.config(5)`  |
   |            +---------------------------------------------------------------------------+---------------------------------------+
   |            | :aw:`iwd` (intel)                                                                                                 |
   |            +---------------------------------------------------------------------------+---------------------------------------+
   |            | :aw:`netctl` (arch) |:ballot_box_with_check:|                             | :manpage:`netctl.profile(5)`          |
   |            +---------------------------------------------------------------------------+---------------------------------------+
   |            | :aw:`systemd-networkd` |:ballot_box_with_check:|                                                                  |
   +------------+---------------------------------------------------------------------------+---------------------------------------+
   | low-level  | :aw:`iproute2 <network_configuration#iproute2>` |:ballot_box_with_check:| | :manpage:`ifstat(8)` |br|             |
   |            |                                                                           | :manpage:`ip(8)`     |br|             |
   |            |                                                                           | :manpage:`ss(8)`     |br|             |
   |            |                                                                           | :manpage:`tc(8)`     |br|             |
   |            +---------------------------------------------------------------------------+---------------------------------------+
   |            | :aw:`iw <network configuration/Wireless#iw>` |:ballot_box_with_check:|    | :manpage:`iw(8)`                      |
   |            +---------------------------------------------------------------------------+---------------------------------------+
   |            | :pkg:`core/net-tools` |:ballot_box_with_check:|                           | :manpage:`arp(8)`      |br|           |
   |            |                                                                           | :manpage:`ifconfig(8)` |br|           |
   |            |                                                                           | :manpage:`netstat(8)`  |br|           |
   |            |                                                                           | :manpage:`route(8)`    |br|           |
   |            +---------------------------------------------------------------------------+---------------------------------------+
   |            | :pkg:`core/wireless_tools` |:ballot_box_with_check:|                      | :manpage:`ifrename(8)` |br|           |
   |            |                                                                           | :manpage:`iwconfig(8)` |br|           |
   |            |                                                                           | :manpage:`iwlist(8)`   |br|           |
   |            +---------------------------------------------------------------------------+---------------------------------------+
   |            | :aw:`wpa_supplicant` |:ballot_box_with_check:|                                                                    |
   +------------+---------------------------------------------------------------------------+---------------------------------------+

.. warning::

   Manually set an approximate time before doing anything at all

:raw-html:`<details><summary><span class="problematic">manual time</span></summary>`

manual time (1/2) ::

   timedatectl set-ntp false
   systemctl stop systemd-timesyncd.service
   rm -fv /etc/adjtime
   timedatectl set-timezone Asia/Makassar

(PC) manual time (2/2) ::

   ssh root@bbgw sh -c "timedatectl set-time \"$(date "+%F %T")\""

:raw-html:`</details>`

connection status ::

   for i in $(cd /sys/class/net/; echo w*); do iw dev $i link; done

auto connect ::

   function f {
      iface="$(cd /sys/class/net/; echo w*)"
      if [[ $iface =~ ^w[a-z0-9]+$ ]]; then
         rm -iv /etc/wpa_supplicant/*
         wpa_passphrase "$1" "$2" >/etc/wpa_supplicant/wpa_supplicant-$iface.conf
         systemctl enable --now wpa_supplicant@$iface.service
         systemctl enable --now dhcpcd@$iface.service
         systemctl enable --now systemd-resolved.service
      else
         echo err
      fi
   }

::

   f <MYSSID> <passphrase>
   unset -v f

test ::

   resolvectl flush-caches
   resolvectl query example.org.
   ping -c4 example.org
   curl https://www.example.org/

test again after cold reboot (poweroff, detatch power, reattach power, boot)

log ::

   journalctl --no-pager -b -u wpa_supplicant@\*.service
   journalctl --no-pager -b -u dhcpcd@\*.service

:aw:`force renew DHCP lease <hcpcd#Remove_old_DHCP_lease>` ::

   # (1)
   systemctl stop dhcpcd@\*.service
   pgrep dhcpcd
   rm -fv /var/lib/dhcpcd/*.lease
   systemctl poweroff
   # (2) (PC) Reboot router from web UI
   # (3) Manually boot BBGW

ntp ::

   timedatectl set-ntp true
   systemctl enable --now systemd-timesyncd.service
   timedatectl status

permissive sshd ::

   sed -i.pacnew 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
   diff $_{.pacnew,}
   systemctl restart sshd.service

(PC) ssh-copy-id ::

   ssh-copy-id -i ~/.ssh/id_rsa.pub alarm@bbgw
   ssh-copy-id -i ~/.ssh/id_rsa.pub root@bbgw

(PC) resolve me ::

   ME="$(ip -4 addr show "$(cd /sys/class/net;echo w*)" | awk '/inet / {print $2}' | cut -d/ -f1)"
   cat <<EOF | ssh bbgw bash
   cp -vn /etc/hosts{,.pacnew}

   cat <<EOF2 >>/etc/hosts

   ::1       localhost
   127.0.0.1 localhost

   $ME 820g3.localdomain 820g3
   EOF2

   diff --color=always -u /etc/hosts{.pacnew,}

   EOF

(PC) share proxy ::

   sed -e 's/127.0.0.1/820g3/g' ~/proxy.bashrc >/tmp/proxy.bashrc
   scp /tmp/proxy.bashrc alarm@bbgw:~/proxy.bashrc
   rm -fv /tmp/proxy.bashrc

add `mirrors <https://archlinuxarm.org/about/mirrors>`__
|vv| `ustc <https://mirrors.ustc.edu.cn/help/archlinuxarm.html>`__
|vv| `tuna <https://mirrors.tuna.tsinghua.edu.cn/help/archlinuxarm/>`__
to :file:`/etc/pacman.d/mirrorlist`

::

   cp -vn /etc/pacman.d/mirrorlist{,.pacnew}
   {
      echo '# https://mirrors.ustc.edu.cn/help/archlinuxarm.html'
      echo 'Server = https://mirrors.ustc.edu.cn/archlinuxarm/$arch/$repo'
      echo
      echo '# https://mirrors.tuna.tsinghua.edu.cn/help/archlinuxarm/'
      echo 'Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxarm/$arch/$repo'
      echo
      cat /etc/pacman.d/mirrorlist.pacnew
   } \
      | tee /etc/pacman.d/mirrorlist

install, install, install (no tmux yet, execute in minicom) ::

   pacman-key --init
   pacman-key --populate archlinuxarm
   pacman Fy; pacman -Syuu --needed base-devel git sudo tmux vim

| reboot
| check if time is synced again

::

   timedatectl status

:aw:`fake-hwclock<system time#fake-hwclock>` (minicom) ::

   source ~alarm/proxy.bashrc
   pacman -Syu --needed fake-hwclock
   systemctl enable --now fake-hwclock.service
   systemctl enable       fake-hwclock-save.timer

:raw-html:`<details><summary><s>AUR/fake-hwclock-git (minicom)</s></summary>`

::

   su -c '
      mkdir -pv ~/.cache/paru/clone/
      cd $_
      source ~/proxy.bashrc
      PKG=fake-hwclock-git
      if [ -e "$PKG" ]; then
         cd $PKG
         git pull
      else
         git clone https://aur.archlinux.org/$PKG.git
         cd $PKG
      fi
      rm -rfv src pkg *.pkg.*
      makepkg -si
   ' alarm
   systemctl enable --now fake-hwclock.service

:raw-html:`</details>`


GPIO
====

kernel doc - `gpio <https://www.kernel.org/doc/html/v5.11/driver-api/gpio/index.html>`__

`bbb-pin-utils <https://github.com/mvduin/bbb-pin-utils>`__ (showpins)
`iobb <https://github.com/shabaz123/iobb>`__

`mmap() on gpio <http://vabi-robotics.blogspot.com/2013/10/register-access-to-gpios-of-beaglebone.html>`__

| `bb.org-overlays <https://github.com/beagleboard/bb.org-overlays>`__
| |b| `tools/beaglebone-universal-io/config-pin <https://github.com/beagleboard/bb.org-overlays/blob/master/tools/beaglebone-universal-io/config-pin>`__
| |b| `tools/pmunts_muntsos/config-pin.c <https://github.com/beagleboard/bb.org-overlays/blob/master/tools/pmunts_muntsos/config-pin.c>`__

| BBGW <-> X200 pinout
| `<https://libreboot.org/docs/install/spi.html#hardware-configuration>`__
| `<https://www.coreboot.org/Board:lenovo/x200#Dumping_the_original_firmware>`__


`Flashrom`__
============

.. __: https://www.flashrom.org/Flashrom

:wp:`wp <Flashrom>`

::

   pacman -Syu --needed dmidecode flashrom

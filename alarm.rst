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


:wp:`GPIO`/:wp:`SPI <Serial Peripheral Interface>`
==================================================

.. attention::

   | SPIDEV0/**SPI0 won't work** - not exposed on P8 P9 expansion headers at all!
   | SPIDEV1/**SPI1 won't work** - conflicts
   |    :menuselection:`AM3358BZCZ100.A13/SPI1_SCLK --> SPI1_SCLK --> TXS0108E_U.B1`
   |    :menuselection:`AM3358BZCZ100.B13/SPI1_D0   --> SPI1_D0   --> TXS0108E_U.B2`
   |    :menuselection:`AM3358BZCZ100.D12/SPI1_D1   --> SPI1_D1   --> TXS0108E_U.B3`

:abbr:`bit banging (data transmission with software instead of dedicated hardware)`
(:wp:`wikipedia <bit banging>`)

| :wp:`pull-up resistor`
| :wp:`open collector`
| :wp:`push-pull output`
| :wp:`push-pull converter`
| https://forum.allaboutcircuits.com/threads/on-the-8051-what-is-a-quasi-bi-directional-port.102601/
| https://www.electrodragon.com/w/IO

`bbb-pin-utils <https://github.com/mvduin/bbb-pin-utils>`__ (showpins)
`iobb <https://github.com/shabaz123/iobb>`__

`mmap() on gpio <http://vabi-robotics.blogspot.com/2013/10/register-access-to-gpios-of-beaglebone.html>`__

| `bb.org-overlays <https://github.com/beagleboard/bb.org-overlays>`__
| |b| `tools/beaglebone-universal-io/config-pin <https://github.com/beagleboard/bb.org-overlays/blob/master/tools/beaglebone-universal-io/config-pin>`__
| |b| `tools/pmunts_muntsos/config-pin.c <https://github.com/beagleboard/bb.org-overlays/blob/master/tools/pmunts_muntsos/config-pin.c>`__

| u-boot
| |b| `fdt <https://www.denx.de/wiki/DULG/UBootCmdFDT>`__
| |b| `device tree overlays <https://u-boot.readthedocs.io/en/latest/usage/fdt_overlays.html>`__

| e2e forum
| |b| `name_overlays <https://e2e.ti.com/support/processors-group/processors/f/processors-forum/1006886/am6548-how-do-we-use-dtbo-in-uenv-txt>`__
| |b| `fdt apply <https://e2e.ti.com/support/processors-group/processors/f/processors-forum/1016579/tda4vm-overlay-dtb-files-in-u-boot>`__

| kernel doc html
| `gpio <https://www.kernel.org/doc/html/v5.11/driver-api/gpio/index.html>`__

| kernel doc txt
| `spidev <https://www.kernel.org/doc/Documentation/spi/spidev>`__
| `gpio sysfs deprecated <https://www.kernel.org/doc/Documentation/gpio/sysfs.txt>`__

| alarm wiki - `bbgw <https://archlinuxarm.org/platforms/armv7/ti/beaglebone-green-wireless>`__ - installation
| :pkg:`alarm/uboot-beaglebone`

`/proc/device-tree <https://unix.stackexchange.com/questions/265890>`__

`linux and the devicetree <https://www.kernel.org/doc/html/latest/devicetree/usage-model.html>`__

:prlink:`capemgr <https://elinux.org/Capemgr>` obselete?

flashrom - `BBB <https://www.flashrom.org/BBB>`__

`BBB gpio pinout <https://www.element14.com/community/community/designcenter/single-board-computers/next-genbeaglebone/blog/2019/08/15/beaglebone-black-bbb-io-gpio-spi-and-i2c-library-for-c-2019-edition>`__

(PC) `compile dts files to dtb <https://github.com/beagleboard/bb.org-overlays/issues/216#issuecomment-851028406>`__ ::

   cd ~/beaglebone
   source ~/proxy.bashrc
   git clone https://github.com/beagleboard/bb.org-overlays
   cd bb.org-overlays && {
      git clean -dfx
      PATH="$PATH:/opt/x-tools7h/arm-unknown-linux-gnueabihf/bin/"
      hash -r
      make -j4 ARCH=arm CROSS_COMPILE=armv7l-unknown-linux-gnueabihf- # V=1
      file src/arm/BB-SPIDEV0-00A0*
      scp src/arm/BB-SPIDEV0-00A0.dtbo bbgw:/boot/BB-SPIDEV0-00A0.dtbo
      # scp src/arm/BB-SPIDEV1-00A0.dtbo bbgw:/boot/BB-SPIDEV1-00A0.dtbo
   }

::

   0x82000000 kernel_addr_r
              5961976 (0x5af8f8) bytes read
   0x825af8f7 kernel_end
   0x825af8f8

   0x88000000 fdt_addr_r
              88862 (0x15b1e) bytes read
   0x88015b1d fdt_end
   0x88015b1e

   0x88070000 overlayaddr
              1515 (0x5eb) bytes read
   0x880705ea overlayaddr_end
   0x880705eb

   0x88080000 ramdisk_addr_r

:manpage:`kernel-command-line(7)` - systemd.mask

::

   if test 0 -eq 0 \
      -a  kernel_addr_r -eq 0x82000000 \
      -a     fdt_addr_r -eq 0x88000000 \
      -a ramdisk_addr_r -eq 0x88080000;
   then

      # setenv disable_uboot_overlay_emmc     1
      # setenv disable_uboot_overlay_video    1
      # setenv disable_uboot_overlay_audio    1
      # setenv disable_uboot_overlay_wireless 1
      # setenv disable_uboot_overlay_adc      1

      load mmc 1:1 ${kernel_addr_r}  /boot/zImage

      # /boot/dtbs/am335x-bone.dtb
      # /boot/dtbs/am335x-boneblack-uboot.dtb
      # /boot/dtbs/am335x-boneblack-wireless.dtb
      # /boot/dtbs/am335x-boneblack.dtb
      # /boot/dtbs/am335x-boneblue.dtb
      # /boot/dtbs/am335x-bonegreen-gateway.dtb
      # /boot/dtbs/am335x-bonegreen-wireless.dtb
      # /boot/dtbs/am335x-bonegreen.dtb
      load mmc 1:1 ${fdt_addr_r}     /boot/dtbs/am335x-bonegreen.dtb
      fdt addr $fdt_addr_r

      # /boot/BB-SPIDEV0-00A0.dtbo
      # /boot/BB-SPIDEV1-00A0.dtbo
      setenv overlayaddr 0x88070000
      load mmc 1:1 ${overlayaddr}    /boot/BB-SPIDEV1-00A0.dtbo
      fdt resize 102400
      fdt apply ${overlayaddr}

      load mmc 1:1 ${ramdisk_addr_r} /boot/initramfs-linux.img
      setenv ramdisk_size ${filesize}

      part uuid mmc 1:1 uuid
      setenv bootargs "console=tty0 console=${console} root=PARTUUID=${uuid} rw rootwait"
      setenv bootargs $bootargs systemd.mask=wpa_supplicant@wlan0.service systemd.mask=dhcpcd@wlan0.service
      bootz ${kernel_addr_r} ${ramdisk_addr_r}:${ramdisk_size} ${fdt_addr_r}

   fi

page 9/11 P9 expansion headers ::

                         P9
                       +-----+
             DGND [BK] |01 02| [BK] DGND
         VDD_3V3B [RD] |03 04| [RD] VDD_3V3B
       (x) VDD_5V      |05 06|      VDD_5V (x)
       (x) SYS_5V      |07 08|      SYS_5V (x)
                       |.. ..|
                       |   28| [BU] SPI1_CS0
   (MISO) SPI1_D0 [WH] |29 30| [GN] SPI1_D1 (MOSI)
        SPI1_SCLK [YE] |31 32|      VDD_ADC
                       |.. 34|      GDNA_ADC
                       |.. ..|
             DGND [BK] |43 44| [BK] DGND
             DGND [BK] |45 46| [BK] DGND
                       +-----+

::

   modprobe spidev

bb.org-overlays `#221 <https://github.com/beagleboard/bb.org-overlays/issues/221>`__

::

   cd ~/beaglebone
   # wget https://mirrors.kernel.org/pub/linux/kernel/v5.x/linux-5.11.2.tar.sign
   gunzip -k linux-5.11.2.tar.gz
   gpg --verify linux-5.11.2.tar{.sign,}
   tar -xf linux-5.11.2.tar
   cd linux-5.11.2/arch/arm/boot/dts/ && {
      rm -v !(am33*bone*)

      grep -nri \
         -e P9_22 -e spi0_sclk \
         -e P9_21 -e spi0_d0 \
         -e P9_18 -e spi0_d1 \
         -e P9_17 -e spi0_cs0 \
         -e spi0

      grep -nri \
         -e P9_31 -e spi1_sclk \
         -e P9_29 -e spi1_d0 \
         -e P9_30 -e spi1_d1 \
         -e P9_28 -e spi1_cs0 \
         -e spi1

   }


`pinctrl/am33xx.h <https://github.com/torvalds/linux/blob/v5.11/include/dt-bindings/pinctrl/am33xx.h>`__

BBG\ :pr:`W`\ +SPIDEV1 ok

.. code:: console

   # dmesg | grep -i pin
   [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 129666
   [    0.073109] pinctrl core: initialized pinctrl subsystem
   [    2.959422] pinctrl-single 44e10800.pinmux: 142 pins, size 568

   # flashrom -p linux_spi:dev=/dev/spidev1.0
   flashrom v1.2 on Linux 5.11.2-1-ARCH (armv7l)
   flashrom is free software, get the source code at https://flashrom.org

   Using clock_gettime for delay loops (clk_id: 1, resolution: 1ns).
   Using default 2000kHz clock. Use 'spispeed' parameter to override.
   No EEPROM/flash device found.
   Note: flashrom can never write if the flash chip isn't found automatically.

   # flashrom -p linux_spi:dev=/dev/spidev1.1
   flashrom v1.2 on Linux 5.11.2-1-ARCH (armv7l)
   flashrom is free software, get the source code at https://flashrom.org

   Using clock_gettime for delay loops (clk_id: 1, resolution: 1ns).
   Using default 2000kHz clock. Use 'spispeed' parameter to override.
   No EEPROM/flash device found.
   Note: flashrom can never write if the flash chip isn't found automatically.

`<https://groups.google.com/g/beagleboard/c/LbqaSGJjvnw>`__

| `<https://electronics.stackexchange.com/questions/258112/reflection-on-spi-clock-signal-termination-or-stub-issue>`__
| `<https://www.avrfreaks.net/forum/reflection-spi-bus>`__
| `<https://electronics.stackexchange.com/questions/33372/spi-bus-termination-considerations>`__
| `<https://www.mail-archive.com/search?l=flashrom@flashrom.org&q=subject:%22%5C%5Bflashrom%5C%5D+Failure+using+flashrom+and+BusPirate+to+flash+Macronix+MX25L3206E+bios+chip%22&o=newest&f=1>`__
| `<https://groups.google.com/g/beagleboard/c/LbqaSGJjvnw>`__


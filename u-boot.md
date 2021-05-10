<!-- u-boot.md -->

---

**&#9656; u-boot.md**\
&bullet; [readme.md](https://github.com/Un1Gfn/beaglebone)

---

## &AElig; - Misc

`mkimage` from community/uboot-tools

[U-Boot stages](https://elinux.org/Panda_How_to_MLO_%26_u-boot#Introduction)

[Gmail search operators](https://support.google.com/mail/answer/7190) - 
[filter archived mails `in:archive`](https://webapps.stackexchange.com/questions/1168/can-i-see-only-mail-i-have-archived-in-gmail)\
[Search lists.denx.de with Google](https://www.google.com/search?q=site:lists.denx.de)

am335x_evm_defconfig

|version|u-boot-spl.bin|u-boot.img|
|-|:-:|:-:|
|v2021.07-rc1|?|?|
|v2021.04|OK|OK|
|v2021.01|OK|OK|
|v2020.10|OK|OK|

am335x_boneblack_vboot_defconfig

|version|u-boot-spl.bin|u-boot.img|
|-|:-:|:-:|
|v2021.07-rc1|hang|-|
|v2021.04|hang|-|
|v2021.01|hang|-|
|v2020.10|OK|OK|
|v2020.07|?|?|
|v2020.04|?|?|
|v2020.01 <sup>&alpha;</sup>|OK|OK|
<!-- ||||| -->

<sup>(&alpha;) Fix build error by adding `extern` before `YYLTYPE yylloc;` in `u-boot-v2020.01/scripts/dtc/dtc-lexer.l`</sup>

[history of `configs/am335x_boneblack_vboot_defconfig`](https://source.denx.de/u-boot/u-boot/-/commits/master/configs/am335x_boneblack_vboot_defconfig)

<details><summary>minicom output - 2017.07-1 - ArchLinuxARM</summary>

```plain

U-Boot SPL 2017.07-1 (Sep 02 2017 - 21:04:29)
Trying to boot from UART

CxyzModem - CRC mode, 2886(SOH)/0(STX)/0(CAN) packets, 5 retries
Loaded 369200 bytes


U-Boot 2017.07-1 (Sep 02 2017 - 21:04:29 +0000) Arch Linux ARM

CPU  : AM335X-GP rev 2.1
I2C:   ready
DRAM:  512 MiB
No match for driver 'omap_hsmmc'
No match for driver 'omap_hsmmc'
Some drivers were not found
MMC:   OMAP SD/MMC: 0, OMAP SD/MMC: 1
Using default environment

<ethaddr> not set. Validating first E-fuse MAC
Net:   Could not get PHY for cpsw: addr 0
cpsw, usb_ether
Press SPACE to abort autoboot in 2 seconds
=> version

U-Boot 2017.07-1 (Sep 02 2017 - 21:04:29 +0000) Arch Linux ARM
gcc (GCC) 7.1.1 20170630
GNU ld (GNU Binutils) 2.28.0.20170506
```

</details>

<details><summary>minicom output - v2020.10 - distccd-alarm-armv7h</summary>

```plain
Welcome to minicom 2.8

OPTIONS: I18n
Compiled on Jan  9 2021, 12:42:45.
Port /dev/ttyUSB0, 01:59:52

Press CTRL-A Z for help on special keys

CCCCCCCC
U-Boot SPL 2020.10 (May 07 2021 - 02:06:21 +0800)
WDT:   Not found!
Trying to boot from UART
CCxyzModem - CRC mode, 4057(SOH)/0(STX)/0(CAN) packets, 9 retries
Loaded 519045 bytes


U-Boot 2020.10 (May 07 2021 - 02:06:21 +0800)

CPU  : AM335X-GP rev 2.1
Model: TI AM335x BeagleBone Black
DRAM:  512 MiB
MMC:   OMAP SD/MMC: 0, OMAP SD/MMC: 1
Loading Environment from FAT... MMC: no card present
Loading Environment from MMC... *** Warning - bad CRC, using default environment

<ethaddr> not set. Validating first E-fuse MAC
Net:   Could not get PHY for ethernet@4a100000: addr 0
eth2: ethernet@4a100000, eth3: usb_ether
Press SPACE to abort autoboot in 2 seconds
=> version
U-Boot 2020.10 (May 07 2021 - 02:06:21 +0800)

armv7l-unknown-linux-gnueabihf-gcc (crosstool-NG 1.23.0.418-d590) 10.2.0
GNU ld (crosstool-NG 1.23.0.418-d590) 2.35
```

</details>

## A - Get U-Boot

[Docs » Build U-Boot » Building with GCC](https://u-boot.readthedocs.io/en/latest/build/gcc.html)

[eLinux](https://elinux.org/Building_for_BeagleBone)

[Sitara Linux Program the eMMC on Beaglebone Black](https://web.archive.org/web/https://processors.wiki.ti.com/index.php/Sitara_Linux_Program_the_eMMC_on_Beaglebone_Black)

|File|[Use Case](https://e2e.ti.com/support/processors/f/processors-forum/367260/what-is-the-difference-between-mlo-and-spl)|[Header](https://stackoverflow.com/a/60880147)|
|:-:|:-:|:-:|
|u-boot-spl.bin|peripheral boot|520 bytes|
|MLO           |[**M**MC **lo**ader](https://stackoverflow.com/a/34805466)|no|

### A1/3 - From Arch Linux ARM

[Write MLO and u-boot.img to the beginning of /dev/mmcblk0](https://archlinuxarm.org/packages/armv7h/uboot-beaglebone/files/uboot-beaglebone.install)

[boot.txt](https://archlinuxarm.org/packages/armv7h/uboot-beaglebone/files/boot.txt)

<details><summary><a href="https://archlinuxarm.org/packages/armv7h/uboot-beaglebone">alarm/uboot-beaglebone 2017.07-1</a></summary>

---

[Arch Linux ARM](https://archlinuxarm.org/platforms/armv7/ti/beaglebone-green-wireless)

    rm -rfv ArchLinuxARM_boot
    sha1sum -c ArchLinuxARM-am33x-latest.tar.gz.sha1sum

Extract

    tar -x -v --no-xattrs --strip-components 1 -f ArchLinuxARM-am33x-latest.tar.gz "./boot"
    mv -v {,ArchLinuxARM_}boot

u-boot-spl.bin - [strip 520-byte header](https://e2e.ti.com/support/processors/f/processors-forum/321500/serial-boot-on-am3359-mlo-does-not-give-prompt)

    # dd if=MLO of=u-boot-spl.bin bs=1 skip=520
    { [ -e ArchLinuxARM_boot/u-boot-spl.bin ] && echo error; } || tail -c +521 ArchLinuxARM_boot/MLO >ArchLinuxARM_boot/u-boot-spl.bin

Verify

    echo; ls -Al ArchLinuxARM_boot; echo
    sudo rm -fv /root/MINICOM_RES; sudo ln -sfv "$(realpath "$PWD/ArchLinuxARM_boot")" "$_"

---

</details>

### A2/3 - With buildroot

<details><summary>&nbsp;</summary>

[BR2_TARGET_UBOOT_VERSION "2021.04"](https://git.busybox.net/buildroot/tree/boot/uboot/Config.in)

[Searching and receiving keys](https://wiki.archlinux.org/title/GnuPG#Searching_and_receiving_keys)

    gpg --search-key --keyserver-options "http-proxy=http://127.0.0.1:8080" AB07D806D2CE741FB886EE50B025BA8B59C36319
    gpg --recv-keys --keyserver-options "http-proxy=http://127.0.0.1:8080" AB07D806D2CE741FB886EE50B025BA8B59C36319

Verify clearsigned message

    gpg --verify buildroot-202?.??.?.tar.bz2.sign

Verify checksum

    grep tar buildroot-202?.??.?.tar.bz2.sign
    md5sum buildroot-202?.??.?.tar.bz2
    sha1sum buildroot-202?.??.?.tar.bz2

[01 little endian](https://serverfault.com/a/749469)

    $ hexdump -s 5 -n 1 -C ~/beaglebone/ArchLinuxARM_boot/initramfs-linux/bin/busybox
    00000005  01                                                |.|
    00000006

[NEON™ SIMD Coprocessor](https://www.ti.com/document-viewer/AM3358/datasheet/features-sprs7179524#sprs7179524)

```
Target options
  Target Architecture = ARM (little endian)
  Target Architecture Variant = cortex-A8
  Target ABI = EABIhf
  Floating point strategy = NEON
  ...
```

</details>

### A3/3 - Build manually

<!-- [eewiki](https://www.digikey.com/eewiki/display/linuxonarm/BeagleBone+Black#BeagleBoneBlack-Bootloader:U-Boot) -->
<details><summary><a href="https://www.digikey.com/eewiki/display/linuxonarm/BeagleBone+Black#BeagleBoneBlack-Bootloader:U-Boot">eewiki</a></summary>

```bash
wget https://gitlab.denx.de/u-boot/u-boot/-/archive/v2019.04/u-boot-v2019.04.tar.bz2
md5 10218bf500cd36894722df95aeb15c91

patch --verbose -p1 < ../0001-am335x_evm-uEnv.txt-bootz-n-fixes.patch
patch --verbose -p1 < ../0002-U-Boot-BeagleBone-Cape-Manager.patch
export CROSS_COMPILE='arm-linux-gnueabihf-'
export KBUILD_OUTPUT='O'
make -j3 am335x_evm_defconfig
make -j3 all
```

</details>

1&period; Prepare toolchain

(&alpha;) [AUR/distccd-alarm-armv7h](https://aur.archlinux.org/packages/distccd-alarm-armv7h)\
&bullet; [ArchLinuxARM Wiki](https://archlinuxarm.org/wiki/Distcc_Cross-Compiling)\
&bullet; [Arch Wiki](https://wiki.archlinux.org/title/Distcc#Volunteers_2)

(&beta;) [community/arm-none-eabi-gcc](https://archlinux.org/packages/community/x86_64/arm-none-eabi-gcc)\
&bullet; [`-linux-` vs `-none-`](https://stackoverflow.com/questions/33586100/why-arm-linux-gnueabi-gcc-and-not-arm-none-eabi-gcc-when-compiling-linux-kernel#comment54949190_33586100)\

<!-- https://superuser.com/questions/360966/how-do-i-use-a-bash-variable-string-containing-quotes-in-a-command -->
(&gamma;) [AUR/arm-linux-gnueabihf-gcc](https://aur.archlinux.org/packages/arm-linux-gnueabihf-gcc)\
0&period; `YAY="yay -Syu --gpg '$(realpath ./gpg_proxy.sh)'"`\
1&period; eval "$YAY" arm-linux-gnueabihf-gcc-stage1\
2&period; eval "$YAY" arm-linux-gnueabihf-glibc-headers\
3&period; eval "$YAY" arm-linux-gnueabihf-gcc-stage2\
4&period; eval "$YAY" arm-linux-gnueabihf-glibc\
5&period; eval "$YAY" arm-linux-gnueabihf-gcc

2&period; Download tarball\
&bullet; [nginx](https://ftp.denx.de/pub/u-boot/) - 202?.?? - PGP sig\
&bullet; [GitLab](https://source.denx.de/u-boot/u-boot/-/tags) - **v**202?.?? - no PGP sig

[Searching and receiving keys](https://wiki.archlinux.org/title/GnuPG#Searching_and_receiving_keys)

    gpg --search-key --keyserver-options "http-proxy=http://127.0.0.1:8080" 1A3C7F70E08FAB1707809BBF147C39FF9634B72C
    gpg --recv-keys --keyserver-options "http-proxy=http://127.0.0.1:8080" 1A3C7F70E08FAB1707809BBF147C39FF9634B72C

[Verify a signature](https://wiki.archlinux.org/title/GnuPG#Verify_a_signature)

    gpg --verify u-boot-202?.??.tar.bz2.sig u-boot-202?.??.tar.bz2

3&period; Build

<!--
Do NOT use aarch64-linux-gnu-gcc
aarch64-linux-gnu-gcc  -mabi=ilp32           test.c # skipping incompatible ... cannot find -l...
aarch64-linux-gnu-gcc -march=armv7-a         test.c # cc1: error: unknown value 'armv7-a' for '-march'
aarch64-linux-gnu-gcc -mtune=generic-armv7-a test.c # cc1: error: unknown value 'generic-armv7-a' for '-mtune'
-->

<!--
$ file ~/beaglebone/u-boot-202?.??/O/cmd/boot.o
O/cmd/boot.o: ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), with debug_info, not stripped
$ mkdir ~/beaglebone/ArchLinuxARM_boot/initramfs-linux; cd "$_"
$ zcat ../initramfs-linux.img | cpio -idmv # https://access.redhat.com/solutions/24029
$ file bin/busybox
bin/busybox: ELF 32-bit LSB pie executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux-armhf.so.3, BuildID[sha1]=4d5ffd0f3a95ec0808d4f4b0e939368db6e0cf63, for GNU/Linux 3.2.0, stripped
-->

<!--
Requirements for "make check"
python-pytest
-->

<!--
comm \
  -1 -2 -3 \
  <(sort u-boot-v2020.10.config) \
  <(sort u-boot-v2021.01.config) \
  | wc -l
-->

<!--
https://www.kernel.org/doc/html/latest/kbuild/kconfig.html
make MENUCONFIG_COLOR=mono menuconfig
-->

<!--
https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/scripts/diffconfig
https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/scripts/diffconfig
-->

    source ~/beaglebone/u-boot.bashrc
    # Follow the hints

## B - Prepare U-Boot eMMC image

### B1/2 - with genimage

?

### B2/2 - manually

<details><summary></summary>

Escalate

```
$ su -
#
```

Zero fill (e.g. 1MiB)

    cd /tmp
    dd if=/dev/zero of=emmc.img bs=1 count=$((1024*1024))
    fdisk -l emmc.img

Loop

    losetup -l -a
    losetup -f --show -L -P -v emmc.img
    losetup -l -a
    fdisk -l /dev/loop0

Partition

    fdisk /dev/loop0
    o
    n p 1 1 2047
    t 1 a
    w

Format
<!-- <div></div> -->

    lsblk -f
    mkfs.fat -v /dev/loop0p1

Write

    mkdir  /tmp/mnt
    mount -v /dev/loop0p1 /tmp/mnt
    cp -v ~/MLO /tmp/mnt
    sync
    cp -v ~/u-boot.img /tmp/mnt
    sync
    umount -v /tmp/mnt
    rmdir -v /tmp/mnt

Cleanup

    losetup -l -a
    losetup -D
    losetup -l -a
    mv -v emmc.img ~/

</details>

## C - Hook up serial port and boot BBGW

[serial port](https://elinux.org/BeagleBone/Serial_Port)

lsusb\
[067b:2303](https://linux-hardware.org/?id=usb:067b-2303) `Prolific Technology, Inc. PL2303 Serial Port / Mobile Action MA-8910P`


[The acme of foolishness](https://dave.cheney.net/2013/09/22/two-point-five-ways-to-access-the-serial-console-on-your-beaglebone-black)
>the red wire, this carries +5v from the USB port and can blow the arse out of your BBB\
>you must leave it unconnected\
>Do not connect the red lead to anything!

[eLinux](https://elinux.org/Beagleboard:BeagleBone_Black_Serial)
>an extra RED wire on this cable that supplies 5V @ 500mA\
>which could power the board if connected to one of the VDD_5V pins (P9_05, P9_06)\
>Just leave it unconnected.

**Do NOT power BBGW**\
**Do NOT connect PL2303 USB-A to PC**

1&period; Connect BBGW serial port to PL2303

<!--
|PL2303 |<div style="font-weight:bold;background:gray;color:black;">black</div>|  |  |<div style="font-weight:bold;background:gray;color:green;">green</div>|<div style="font-weight:bold;background:gray;color:white;">white</div>|  |
-->

||1|2|3|4|5|6|
|-|-|-|-|-|-|-|
|BBGW   |GND  |NC|NC|RX   |TX   |NC|
|PL2303 |black|  |  |green|white|  |

2&period; Double check the connection\
3&period; Connect PL2303 USB-A to PC\
4&period; Hold <kbd>USER</kbd>\
5&period; Supply 5v [**?A**](https://electronics.stackexchange.com/questions/563406/which-wall-charger-for-beaglebone-green-wireless) power through Micro-USB\
6&period; Wait for 5 seconds\
7&period; Release <kbd>USER</kbd>\
8&period; Make sure `lsusb | grep -i prolific` reveals PL2303

## D - Send U-Boot via serial debug port

[SystemSetup &lt; DULG &lt; DENX](https://www.denx.de/wiki/view/DULG/SystemSetup)

[ArchWiki](https://wiki.archlinux.org/title/Working_with_the_serial_console)

[parameters](https://web.archive.org/web/https://elinux.org/Beagleboard:BeagleBone_Black_Accessories#Serial_Debug_Cables)

|||
|-|-|
|Baud         |115,200|
|Bits         |8      |
|Parity       |N      |
|**Stop Bits**|1      |
|**Handshake**|None   |

### D1/2 - with minicom (recommended)

[minicom+kermit](https://lists.denx.de/pipermail/u-boot/2003-June/001527.html)

[YouTube - Fastbit Embedded Brain Academy](https://youtu.be/3y1LMNPoaJI)

**Make sure lrzsz is installed**

Escalate

    su -

Run minicom

    # --metakey
    minicom \
      -c off \
      -b 115200 \
      -8 \
      --device /dev/ttyUSB0

Wait for at most 30 seconds until `CCC...` appears in minicom console

<kbd>CTRL</kbd>+<kbd>a</kbd>, <kbd>s</kbd>, xmodem, `[MINICOM_RES]`

Locate `u-boot-spl.bin` (**not `MLO`**) and send

Locate `u-boot.img` and send (xmodem, the same)

Press <kbd>SPACE</kbd>

Check U-Boot version

    => version

### D2/2 - with stty+sx+cu

<details><summary></summary>

Escalate

    $ su -
    # 

stty

    echo '
    115200
    -clocal
    ignbrk ignpar
    -icrnl -ixon -opost -isig -icanon -iexten -echo
    ' | xargs stty -F /dev/ttyUSB0

Verify

    cat /dev/ttyUSB0
    [WAIT FOR 25 SECONDS]
    SSS...

[XMODEM](http://e2e.ti.com/support/processors/f/791/t/803163?Linux-AM3358-Serial-transfer-of-files)

    sx --xmodem -k -vv </dev/ttyUSB0 >/dev/ttyUSB0 /home/darren/beaglebone/u-boot-v202?.??/O/spl/u-boot-spl.bin
    sx --xmodem -k -vv </dev/ttyUSB0 >/dev/ttyUSB0 /home/darren/beaglebone/u-boot-v202?.??/O/u-boot.img

cu ([redhat](https://access.redhat.com/solutions/209663)) ([resize](https://wiki.archlinux.org/index.php/Working_with_the_serial_console#Troubleshooting))

    cu -l /dev/ttyUSB0 -s 115200
    [RUN STTY AGAIN]

    => 

U-Boot

    => help
    => version
    => bdinfo
    => mmcinfo
    => usb info
    => reset

Exit cu

```
=> ~.

```

</details>

## E F G H I J K L M N O P Q R S T U V W X

From here on we will be interacting with the volatile U-Boot code in RAM

## Y - Write U-Boot eMMC image to eMMC

Check eMMC - [mmc](https://www.denx.de/wiki/view/DULG/UBootCmdGroupMMC)

    mmc list
    mmc dev 1
    mmc info
    mmc part

<div></div>

Erase eMMC (dd if=/dev/zero of=/dev/mmcblk0 bs=512 count=20480)
<!-- >0x800\*512=2048\*512=1048576=1024\*1024=1Mi -->
>0x5000blk\*512B/blk=20480blk\*512B/blk=10485760B=10\*1024\*1024B=10MiB

    mmc erase 0 0x5000
    mmc rescan
    mmc part

Zero fill DRAM starting from 0x82000000 -
[cmp](https://www.denx.de/wiki/view/DULG/UBootCmdGroupMemory#Section_5.9.2.3.) -
[mw](https://www.denx.de/wiki/view/DULG/UBootCmdGroupMemory#Section_5.9.2.8.)
>0x100000B\*1B/blk=1048576B=1024\*1024B=1MiB

    cmp.b 0x100000 0x82000000 0x100000 # compare byte
    mw.b 0x82000000 0 0x100000         # fill    byte
    cmp.b 0x100000 0x82000000 0x100000 # compare byte

Send eMMC image to RAM with xmodem

    loadx 0x82000000 115200
    md.b 0x82000000 0x4                # memory display byte

Dump eMMC image from RAM to eMMC - [mmc](https://www.denx.de/wiki/view/DULG/UBootCmdGroupMMC)

```
mmc list
mmc dev 1
mmc info
mmc part

mmc write 0x82000000 0 0x800

MMC write: dev # 1, block # 0, count 2048 ... 2048 blocks written: OK

mmc part

Partition Map for MMC device 1  --   Partition Type: DOS

Part    Start Sector    Num Sectors     UUID            Type
  1     1               2047            01d0a302-01     01

fatls mmc 1

mmc rescan
mmc part
```

## Z - Disonnect and poweroff BBGW

1&period; Unplug PL2303 USB-A from PC\
[2&period; Press and hold <kbd>POWER</kbd> button\
3&period; When LED `PWR` goes off (approx 8s) **release <kbd>POWER</kbd> immediately**](https://github.com/beagleboard/beaglebone-black/wiki/System-Reference-Manual#power-button)\
4&period; Clean up

    lsusb | grep -i prolific
    ./usbreset /dev/bus/usb/...
    lsusb | grep -i prolific

<!-- https://en.wikipedia.org/wiki/List_of_Latin-script_letters -->
## &Zcaron; - What now?

[net](https://source.denx.de/u-boot/u-boot/-/tree/master/drivers/net)/e1000\* \
[Net: No ethernet found](https://www.denx.de/wiki/view/DULG/NetNoEthernetFound)\
[boot from BOOTP/TFTP](https://www.denx.de/wiki/view/DULG/UBootCmdGroupDownload#Section_5.9.5.1.) - [ArchWiki](https://wiki.archlinux.org/title/TFTP)

[boot from USB](https://stackoverflow.com/questions/30488942/how-to-boot-linux-kernel-from-u-boot)

[TFTP+NFS](https://www.denx.de/wiki/view/DULG/LinuxNfsRoot)

Generate Arch Linux ARM root ext4 image, chop into 256MiB pieces and receive with U-Boot via USB ethernet adapter?\
PC<->BBGW direct with twisted pair RJ45?

<details><summary>hidden</summary>

Example serial port setup that works

stty -aF /dev/ttyUSB0
```
speed 115200 baud; rows 0; columns 0; line = 0;
intr = ^C; quit = ^\; erase = ^?; kill = ^U; eof = ^D; eol = <undef>; eol2 = <undef>; swtch = <undef>; start = ^Q; stop = ^S;
susp = ^Z; rprnt = ^R; werase = ^W; lnext = ^V; discard = ^O; min = 1; time = 0;
-parenb -parodd -cmspar cs8 hupcl -cstopb cread -clocal -crtscts
ignbrk -brkint ignpar -parmrk -inpck -istrip -inlcr -igncr -icrnl -ixon -ixoff -iuclc -ixany -imaxbel -iutf8
-opost -olcuc -ocrnl onlcr -onocr -onlret -ofill -ofdel nl0 cr0 tab0 bs0 vt0 ff0
-isig -icanon -iexten -echo echoe echok -echonl -noflsh -xcase -tostop -echoprt echoctl echoke -flusho -extproc
```

Run u-boot on BeagleBone [(kermit)](http://www.kermitproject.org/) [<sup>O</sup>](https://www.denx.de/wiki/view/DULG/SystemSetup#Section_4.3.)

* Launch ckermit

```
$ su -
# ckermit
C-Kermit>set port /dev/ttyUSB0
C-Kermit>set speed 115200
C-Kermit>set handshake none
C-Kermit>set flow-control none
C-Kermit>set serial 8n1
C-Kermit>connect
[Wait for CCC]
<Ctrl-\> <C>
```

* Send `u-boot-spl.bin` and `u-boot.img`

```
C-Kermit>set protocol xmodem
C-Kermit>set send timeout 90 fixed
C-Kermit>set retry 0
C-Kermit>send /home/darren/beaglebone/u-boot-v202?.??/O/spl/u-boot-spl.bin
C-Kermit>send /home/darren/beaglebone/u-boot-v202?.??/O/u-boot.img
C-Kermit>connect

=> 
```

Misc

```
https://gitlab.denx.de/u-boot/u-boot
Building the Software:
======================

http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.set.boards/index.html
./tools/genboardscfg.py -j 3

gitclear

make -j3 vexpress_ca9x4_defconfig

git check-ignore * | xargs file
file * spl/* | grep -v -F -e ASCII -e directory | less -S

find .                      \
-type  f                 -a \
\(                          \
  -iname \*dtb           -o \
  -iname \*bin           -o \
  -iname \*img           -o \
  -iname \*spl           -o \
  -iname \*spl\*bin\*    -o \
  -iname \*spl\*dtb\*    -o \
  -iname \*spl\*img\*    -o \
  -iname \*u-boot        -o \
  -iname \*u-boot\*bin\* -o \
  -iname \*u-boot\*dtb\* -o \
  -iname \*u-boot\*img\* -o \
  -iname mlo\*              \
\)

https://dev.to/rulyrudel/how-to-execute-u-boot-on-qemu-system-arm-2b22
k=./O/u-boot
qemu-system-arm \
  -machine vexpress-a9 \
  -nographic \
  -no-reboot \
  -kernel "$k"

Monitor Commands - Overview:
============================


https://www.qemu.org/docs/master/qemu-doc.html#index-Ctrl_002da-x
Ctrl-a x


https://wiki.archlinux.org/index.php/Working_with_the_serial_console

https://stackoverflow.com/questions/38279621/how-to-send-boot-files-over-uart

http://www.denx.de/wiki/view/DULG/SystemSetup#Section_4.3

http://www.kermitproject.org/onlinebooks/usingckermit3e.pdf
Page 64(74)
8 data bits, No parity, 1 stop bit (8N1)
"SET SERIAL 8N1" == "SET PARITY NONE, SET STOP-BITS 1, SET TERM BYTE 8"


set line /dev/ttyUSB0
set carrier-watch off


robust
set file type bin
set file name lit
set rec pack 1000
set send pack 1000
set window 5


RNDIS

IP & mask

sudo cat /proc/tty/driver/serial

cu \
  --line /dev/ttyUSB0 \
  --parity=none \
  --speed=115200 \
  --debug all \
```

</details>

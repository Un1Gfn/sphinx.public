<!-- u-boot.md -->

---

**&#9656; u-boot.md**\
&bullet; [readme.md](https://github.com/Un1Gfn/beaglebone)

---

## &AElig; - Misc

[U-Boot stages](https://elinux.org/Panda_How_to_MLO_%26_u-boot#Introduction)

## A - Get U-Boot

[eLinux](https://elinux.org/Building_for_BeagleBone)

[Sitara Linux Program the eMMC on Beaglebone Black](https://web.archive.org/web/https://processors.wiki.ti.com/index.php/Sitara_Linux_Program_the_eMMC_on_Beaglebone_Black)

||[use case](https://e2e.ti.com/support/processors/f/processors-forum/367260/what-is-the-difference-between-mlo-and-spl)|[520-byte header](https://stackoverflow.com/a/60880147)|
|-|-|-|
|u-boot-spl.bin|peripheral boot|X|
|MLO           |[**M**MC **lo**ader](https://stackoverflow.com/a/34805466)|O|

### A1/3 - From Arch Linux ARM

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

### A2/3 - With buildroot

?

### A3/3 - With AUR toolchain

<details><summary>latest</summary>

1&period; Toolchain [arm-linux-gnueabihf-gcc](https://aur.archlinux.org/packages/arm-linux-gnueabihf-gcc/)\

    cd ~/beaglebone
    source ~/proxy.bashrc
    yay -Syu --gpg "$(realpath gpg_proxy.sh)" arm-linux-gnueabihf-glibc-headers
    yay -Syu --gpg "$(realpath gpg_proxy.sh)" arm-linux-gnueabihf-gcc-stage2
    yay -Syu --gpg "$(realpath gpg_proxy.sh)" arm-linux-gnueabihf-gcc

2&period; Download tarball from [nginx](https://ftp.denx.de/pub/u-boot/) or [GitLab tags](https://source.denx.de/u-boot/u-boot/-/tags)

[Verify a signature](https://wiki.archlinux.org/title/GnuPG#Verify_a_signature)

    gpg --verify u-boot-202?.??.tar.bz2.sig u-boot-202?.??.tar.bz2

[Searching and receiving keys](https://wiki.archlinux.org/title/GnuPG#Searching_and_receiving_keys)

    gpg --search-key --keyserver-options "http-proxy=http://127.0.0.1:8080" 1A3C7F70E08FAB1707809BBF147C39FF9634B72C
    gpg --recv-keys --keyserver-options "http-proxy=http://127.0.0.1:8080" 1A3C7F70E08FAB1707809BBF147C39FF9634B72C

3&period; Extract to `u-boot-v202?.??/`\
4&period; Build

    cd u-boot-v202?.??/
    export CROSS_COMPILE='arm-linux-gnueabihf-'
    export KBUILD_OUTPUT='O'
    make -j3 am335x_boneblack_vboot_defconfig
    make -j3 all
    sudo cp -v O/MLO O/u-boot.img O/spl/u-boot-spl.bin ~root/

Output dir `u-boot-v202?.??/O/`

</details>

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
**Do NOT power PL2303**

1&period; Connect BBGW serial port to PL2303

||||||||
|-|-|-|-|-|-|-|
|PL2303 |<div style="font-weight:bold;background:gray;color:black;">black</div>|  |  |<div style="font-weight:bold;background:gray;color:green;">green</div>|<div style="font-weight:bold;background:gray;color:white;">white</div>|  |
|BBGW   |GND  |NC|NC|RX   |TX   |NC|

    BBGW  PL2303
    ----  ------
    GND   black
    NC
    NC
    RX    green
    TX    white
    NC
          red (NC)

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

1&period; **Make sure lrzsz is installed** \
2&period; Escalate

    su -

3&period; Run minicom

    # --metakey
    minicom \
      -c off \
      -b 115200 \
      -8 \
      --device /dev/ttyUSB0

4&period; send `MINICOM_RES/u-boot-spl.bin` with xmodem\
5&period; send `MINICOM_RES/u-boot.img` with xmodem

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

Erase (wipefs -af /dev/mmcblk0\*) - [mmc](https://www.denx.de/wiki/view/DULG/UBootCmdGroupMMC)
>0x800\*512=2048\*512=1048576=1024\*1024=1Mi

    mmc dev 1
    mmc part
    mmc erase 0 0x800
    mmc rescan
    mmc part

Zero fill (cat /dev/zero >/dev/mmcblk0) -
[cmp](https://www.denx.de/wiki/view/DULG/UBootCmdGroupMemory#Section_5.9.2.3.) -
[mw](https://www.denx.de/wiki/view/DULG/UBootCmdGroupMemory#Section_5.9.2.8.)
>0x100000=1048576=1024\*1024=1Mi

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
2&period; [Press and hold <kbd>POWER</kbd> button for 8+ seconds untill `PWR` LED turns off](https://github.com/beagleboard/beaglebone-black/wiki/System-Reference-Manual#power-button)\
3&period; Clean up

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

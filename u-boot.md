<!-- u-boot.md -->

---

**&#9656; u-boot.md**\
&bullet; [readme.md](https://github.com/Un1Gfn/beaglebone)

---

## &AElig; - Misc

[U-Boot stages](https://elinux.org/Panda_How_to_MLO_%26_u-boot#Introduction)

## A - Build U-Boot

[Sitara Linux Program the eMMC on Beaglebone Black](https://web.archive.org/web/https://processors.wiki.ti.com/index.php/Sitara_Linux_Program_the_eMMC_on_Beaglebone_Black)

1&#46; Toolchain [arm-linux-gnueabihf-gcc](https://aur.archlinux.org/packages/arm-linux-gnueabihf-gcc/)\
2&#46; Download tarball from [nginx](https://ftp.denx.de/pub/u-boot/) or [GitLab tags](https://source.denx.de/u-boot/u-boot/-/tags)\
3&#46; Extract to `u-boot-v202?.??/`\
4&#46; Build

```bash
cd u-boot-v202?.??/
export CROSS_COMPILE='arm-linux-gnueabihf-'
export KBUILD_OUTPUT='O'
make -j3 am335x_boneblack_vboot_defconfig
make -j3 all
sudo cp -v O/MLO O/u-boot.img O/spl/u-boot-spl.bin ~root/
```

Output dir `u-boot-v202?.??/O/`

[eewiki](https://www.digikey.com/eewiki/display/linuxonarm/BeagleBone+Black#BeagleBoneBlack-Bootloader:U-Boot)

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

## B - Prepare U-Boot eMMC image

### B1/2 - genimage (recommended)

?

### B2/2 - manually

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

lsusb - [067b:2303](https://linux-hardware.org/?id=usb:067b-2303) `Prolific Technology, Inc. PL2303 Serial Port / Mobile Action MA-8910P`

**Connect BBGW to PL2303 and double check, before connecting PL2303 to PC**\
**Do NOT connect BBGW to a powered PL2303**

[The acme of foolishness](https://dave.cheney.net/2013/09/22/two-point-five-ways-to-access-the-serial-console-on-your-beaglebone-black)
>the red wire, this carries +5v from the USB port and can blow the arse out of your BBB\
>you must leave it unconnected\
>Do not connect the red lead to anything!

[eLinux](https://elinux.org/Beagleboard:BeagleBone_Black_Serial)
>an extra RED wire on this cable that supplies 5V @ 500mA\
>which could power the board if connected to one of the VDD_5V pins (P9_05, P9_06)\
>Just leave it unconnected.

1&#46; Connect BBGW serial port to PL2303

    BBGW  PL2303
    ----  ------
    GND   black
    NC
    NC
    RX    green
    TX    white
    NC
          red (NC)

2&#46; Double check the connection\
3&#46; Connect PL2303 USB-A to PC\
4&#46; Hold <kbd>USER</kbd>\
5&#46; Supply 5v **?A** power through Micro-USB\
6&#46; Wait for 5 seconds\
7&#46; Release <kbd>USER</kbd>\
8&#46; Make sure `lsusb | grep -i prolific` reveals PL2303

## D - Send stage2 MLO and stage3 u-boot.img to BBGW RAM

[SystemSetup &lt; DULG &lt; DENX](https://www.denx.de/wiki/view/DULG/SystemSetup)

[ArchWiki](https://wiki.archlinux.org/title/Working_with_the_serial_console)

### D1/2 - minicom (recommended)

[YouTube - Fastbit Embedded Brain Academy](https://youtu.be/3y1LMNPoaJI)

```bash
# --metakey
minicom                 \
  --color=off           \
  --baudrate 115200     \
  --device /dev/ttyUSB0
```

### D2/2 - stty+sx+cu

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

* Unplug PL2303 from PC
* Hold BeagleBone POWER button till it's off
* Clean up

``` bash
lsusb | grep -i prolific
./usbreset /dev/bus/usb/...
```

<!-- https://en.wikipedia.org/wiki/List_of_Latin-script_letters -->
## &Zcaron; - Hidden

<details><summary>&nbsp;</summary>

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

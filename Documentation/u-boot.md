## &AElig; - Misc

## A - Get U-Boot

### A1/3 - From Arch Linux ARM

### A2/3 - With buildroot

### A3/3 - Build manually

## B - Prepare U-Boot eMMC image

### B1/2 - with genimage

### B2/2 - manually

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

Locate `u-boot.img` and send (xmodem or ymodem)

Press <kbd>SPACE</kbd>

Check U-Boot version

    => version

### D2/2 - with stty+sx+cu

(REMOVED)

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

(REMOVED)

Run u-boot on BeagleBone [(kermit)](http://www.kermitproject.org/) [<sup>O</sup>](https://www.denx.de/wiki/view/DULG/SystemSetup#Section_4.3.)

(REMOVED)

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

C-Kermit>

(REMOVED)

sudo cat /proc/tty/driver/serial

cu

(REMOVED)
```

</details>

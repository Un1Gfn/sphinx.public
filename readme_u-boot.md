```
https://elinux.org/Building_for_BeagleBone
https://git.busybox.net/buildroot/tree/board/beaglebone
https://elinux.org/BeagleBone/Serial_Port
https://processors.wiki.ti.com/index.php/AM335x_U-Boot_User's_Guide
https://www.digikey.com/eewiki/display/linuxonarm/BeagleBone+Black
https://www.linux4sam.org/bin/view/Linux4SAM/U-Boot
http://www.armadeus.org/wiki/index.php?title=Serial_Transfer
https://lists.denx.de/pipermail/u-boot/2003-June/001527.html
https://processors.wiki.ti.com/index.php/Sitara_Linux_Program_the_eMMC_on_Beaglebone_Black
https://wiki.debian.org/FreedomBox/Hardware/BeagleBone
https://wiki.debian.org/InstallingDebianOn/TI/BeagleBone
https://elinux.org/Beagleboard:Updating_The_Software
https://beagleboard.org/latest-images
http://lists.busybox.net/pipermail/buildroot/2016-April/160030.html
https://www.busybox.net/use_less_ram.html
https://github.com/pengutronix/genimage
https://github.com/Un1Gfn/beaglebone/blob/master/readme_u-boot.md
```

###### Build u-boot for BeagleBone

* Toolchain: [arm-linux-gnueabihf-gcc](https://aur.archlinux.org/packages/arm-linux-gnueabihf-gcc/)
* Download [u-boot-v2020.01.tar.bz2](https://gitlab.denx.de/u-boot/u-boot/-/archive/v2020.01/u-boot-v2020.01.tar.bz2) from [releases](https://gitlab.denx.de/u-boot/u-boot/-/tags)
* Extract to `u-boot-v2020.01/`
* Build
```bash
cd u-boot-v2020.01/
export CROSS_COMPILE='arm-linux-gnueabihf-'
export KBUILD_OUTPUT='O'
make -j3 am335x_boneblack_vboot_defconfig
make -j3 all
sudo cp -v O/MLO O/u-boot.img O/spl/u-boot-spl.bin ~root/
```
* Binaries in `u-boot-v2020.01/O/`

###### Write u-boot to eMMC
* Escalate
```
$ su -
#
```
* Fill
```bash
cd /tmp
dd if=/dev/zero of=emmc.img bs=1 count=$((1024*1024))
fdisk -l emmc.img
```
* Loop
```bash
losetup -l -a
losetup -f --show -L -P -v emmc.img
losetup -l -a
fdisk -l /dev/loop0
```
* Format
```bash
fdisk /dev/loop0
o
n
p
1
1
2047
t
1
a
w
lsblk
mkfs.fat -v /dev/loop0p1
```
* Write
```bash
mkdir  /tmp/mnt
mount -v /dev/loop0p1 /tmp/mnt
cp -v ~/MLO /tmp/mnt
sync
cp -v ~/u-boot.img /tmp/mnt
sync
umount -v /tmp/mnt
rmdir -v /tmp/mnt
```
* Cleanup
```bash
losetup -l -a
losetup -D
losetup -l -a
mv -v emmc.img ~/
```
* Run Run u-boot on BeagleBone (stty)
> Mi=1024\*1024=1048576
> Mi=2048\*512=0x800\*512
```
mmc dev 1
mmc part
mmc erase 0 0x800
mmc rescan
mmc part

cmp.b 0x100000 0x82000000 0x100000
mw.b 0x82000000 0 0x100000
cmp.b 0x100000 0x82000000 0x100000

loadx 0x82000000 115200
md.b 0x82000000 0x4

```
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

###### Run u-boot on BeagleBone (minicom)

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

```bash
# --metakey
minicom                 \
  --color=off           \
  --baudrate 115200     \
  --device /dev/ttyUSB0
```

###### Run u-boot on BeagleBone (stty) [<sup>O</sup>](https://www.denx.de/wiki/view/DULG/SystemSetup#Section_4.2.)

* Connect `BeagleBone ~ PL2303 ~ PC`
```
BeagleBone  PL2303
------------------
  Black      GND
  Green      RX
  White      TX
```
* Hold BeagleBone USER button
* Supply power to BeagleBone
* Wait for 5 seconds
* Release BeagleBone USER button
* Check `lsusb | grep -i prolific`
* **Escalate**
```
$ su -
# 
```
* stty
```bash
echo '
115200
-clocal
ignbrk ignpar
-icrnl -ixon -opost -isig -icanon -iexten -echo
' | xargs stty -F /dev/ttyUSB0
```
* Verify
```
cat /dev/ttyUSB0
[WAIT FOR 25 SECONDS]
SSS...
```
* [XMODEM](http://e2e.ti.com/support/processors/f/791/t/803163?Linux-AM3358-Serial-transfer-of-files)
```bash
sx --xmodem -k -vv </dev/ttyUSB0 >/dev/ttyUSB0 /home/darren/beaglebone/u-boot-v2020.01/O/spl/u-boot-spl.bin
sx --xmodem -k -vv </dev/ttyUSB0 >/dev/ttyUSB0 /home/darren/beaglebone/u-boot-v2020.01/O/u-boot.img
```
* cu [<sup>O</sup>](https://access.redhat.com/solutions/209663) [(resize)](https://wiki.archlinux.org/index.php/Working_with_the_serial_console#Troubleshooting)
```
cu -l /dev/ttyUSB0 -s 115200
[RUN STTY AGAIN]

=> 
```
* u-boot
```?
=> help
=> version
=> bdinfo
=> mmcinfo
=> usb info
=> reset
```
* exit cu
```
=> ~.

```
* Unplug PL2303 from PC
* Hold BeagleBone POWER button till it's off
* Clean up
``` bash
lsusb | grep -i prolific
./usbreset /dev/bus/usb/...
```

###### Hidden

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
C-Kermit>send /home/darren/beaglebone/u-boot-v2020.01/O/spl/u-boot-spl.bin
C-Kermit>send /home/darren/beaglebone/u-boot-v2020.01/O/u-boot.img
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

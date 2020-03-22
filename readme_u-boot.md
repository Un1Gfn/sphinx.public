###### Build u-boot for BeagleBone

* Toolchain: [arm-linux-gnueabihf-gcc](https://aur.archlinux.org/packages/arm-linux-gnueabihf-gcc/)
* Download [u-boot-v2020.01.tar.bz2](https://gitlab.denx.de/u-boot/u-boot/-/archive/v2020.01/u-boot-v2020.01.tar.bz2) from [releases](https://gitlab.denx.de/u-boot/u-boot/-/tags)
* Extract to `u-boot-v2020.01/`
* Build
```
$ cd u-boot-v2020.01/
$ export CROSS_COMPILE='arm-linux-gnueabihf-'
$ export KBUILD_OUTPUT='O'
$ make -j3 am335x_boneblack_vboot_defconfig
$ make -j3 all
```
* Binaries in `u-boot-v2020.01/O/`

###### Run u-boot on BeagleBone (stty)

```
speed 115200 baud; rows 0; columns 0; line = 0;
intr = ^C; quit = ^\; erase = ^?; kill = ^U; eof = ^D; eol = <undef>; eol2 = <undef>; swtch = <undef>; start = ^Q; stop = ^S;
susp = ^Z; rprnt = ^R; werase = ^W; lnext = ^V; discard = ^O; min = 1; time = 0;
-parenb -parodd -cmspar cs8 hupcl -cstopb cread -clocal -crtscts
ignbrk -brkint ignpar -parmrk -inpck -istrip -inlcr -igncr -icrnl -ixon -ixoff -iuclc -ixany -imaxbel -iutf8
-opost -olcuc -ocrnl onlcr -onocr -onlret -ofill -ofdel nl0 cr0 tab0 bs0 vt0 ff0
-isig -icanon -iexten -echo echoe echok -echonl -noflsh -xcase -tostop -echoprt echoctl echoke -flusho -extproc
```

###### Run u-boot on BeagleBone

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
```
* Try out u-boot
```
=> ?
=> help
=> version
=> bdinfo
=> mmcinfo
=> usb info
=> reset
<Ctrl-\> <C>
C-Kermit>exit
```
* Unplug PL2303 from PC
* Hold BeagleBone POWER button till it's off
* Clean up
```
# lsusb | grep -i prolific
# ./usbreset /dev/bus/usb/...
```

###### Hidden

<details><summary>&nbsp;</summary>

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

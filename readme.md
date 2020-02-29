
<details><summary><i>hidden</i></summary>

```
txt -> md
pacman -Qttq | grep python | sudo pacman -Rc -
https://pip.pypa.io/en/stable/installing/
https://pypi.org/project/PySocks/#history
https://github.com/joeyespo/grip
https://github.com/github/cmark-gfm

f='readme.md'
cat "$f" | cmark-gfm -t html >readme.html

echo "$f" | entr -cnp ""

tail--follow

Libreboot
‌‌‎sop8 clip 燒錄夾 (+ch341a)

GitHub Flavored Markdown html entity whitelist
https://github.com/jch/html-pipeline/blob/master/lib/html/pipeline/sanitization_filter.rb#L67

grab telegram saved messages
```
</details>

[Render md on GitHub Wiki](https://github.com/Un1Gfn/empty/wiki/_new)  
[HTML entities](http://www.amp-what.com/)  

###### Distro
* [Void Linux](https://voidlinux.org/)
  * [packages](https://voidlinux.org/packages/)
  * [void-beaglebone-musl-\*.img.xz](https://a-hel-fi.m.voidlinux.org/live/current/) extract &asymp; 2000 MiB live image
  * [void-beaglebone-musl-\*.tar.xz](https://a-hel-fi.m.voidlinux.org/live/current/) extract &asymp; 400 MiB rootfs tarball [howto](https://wiki.voidlinux.org/Beaglebone)
* [Buildroot](https://buildroot.org/) (build images on CircleCI)
  * [packages](https://git.busybox.net/buildroot/tree/package)
* [yocto](https://www.yoctoproject.org/) (build images on CircleCI)
  * [packages](https://layers.openembedded.org/layerindex/branch/master/recipes/)

###### Communication
<!-- Guide RNDIS TFTP BOOTP Serial Mass bootloader kernel userspace NFS SSH-->
|Guide|[RNDIS](https://en.wikipedia.org/wiki/RNDIS) [<sup>O</sup>](https://en.wikipedia.org/wiki/Ethernet_over_USB)<br>network|[TFTP](https://en.wikipedia.org/wiki/Trivial_File_Transfer_Protocol)|[BOOTP](https://en.wikipedia.org/wiki/Bootstrap_Protocol)|Serial|Mass<br>Storage|bootloader<br>build|kernel<br>build|userspace<br>build|NFS|SSH|
|-|-|-|-|-|-|-|-|-|-|-|
|[techniq](https://github.com/techniq/wiki/wiki/Linux-USB-Gadget-API)|O|||O|O||||||
|[BBBlfs](https://github.com/ungureanuvladvictor/BBBlfs)|O|||||O|O|O|||
|[eLinux recovery guide](https://elinux.org/AM335x_recovery) w/ [barebox](https://www.barebox.org/) [<sup>O</sup>](https://www.pengutronix.de/en/software/barebox.html)|O|O|O|||O|||||
|[U-boot on AM335x](https://processors.wiki.ti.com/index.php/AM335x_U-Boot_User's_Guide)|O|O||O||O|||O||
|[eLinux](https://elinux.org/Beagleboard:Terminal_Shells)||||O||||||O|
|[Android USB SSH](https://stackoverflow.com/questions/44926644/control-beaglebone-black-linux-with-android-smartphone-through-usb-cable)|O|||||||||O|
|[deleted superuser question](https://superuser.com/questions/1529130/linux-tethering-ethernet-over-usb-network-device-usb0-not-exposed-after-loading) [<sup>O</sup>](https://github.com/techniq/wiki/wiki/Linux-USB-Gadget-API#network-g_ether)|O||||||||||
<!-- |||||||||||| -->
[nfs-kernel-server](https://bootlin.com/blog/tftp-nfs-booting-beagle-bone-black-wireless-pocket-beagle)  

###### Hareware
* Beaglebone Green Wireless (BBGW) Wiki on [Seeed](http://wiki.seeedstudio.com/BeagleBone_Green_Wireless/#specification)
* Beaglebone Black (BBB) Reference Manual on [GitHub](https://github.com/beagleboard/beaglebone-black/wiki/System-Reference-Manual)
* [Texus Instruments Sitara AM3358](http://www.ti.com/product/AM3358) [Arm Cortex-A8](https://en.wikipedia.org/wiki/ARM_Cortex-A8)
  * 32-bit [armhf](https://wiki.debian.org/ArmHardFloatPort#Supported_devices) [<sup>O</sup>](https://wiki.debian.org/ArmEabiPort)
  * [Diagram](http://www.ti.com/data-sheets/diagram.tsp?genericPartNumber=AM3358&diagramId=SPRS717K)
  * [docs](http://www.ti.com/product/AM3358/technicaldocuments) --- User guides --- AM335x and AMIC110 Sitara™ Processors Technical Reference Manual
    * "Memery Map" --- Page 117 (2.1)
  * [Boot process](https://processors.wiki.ti.com/index.php/AM335x_board_bringup_tips)
  * [U-boot on AM3358](https://processors.wiki.ti.com/index.php/AM335x_U-Boot_User's_Guide)
* Serial port
  * eLinux [<sup>O</sup>](https://elinux.org/Beagleboard:BeagleBone_Black_Serial) [<sup>O</sup>](https://elinux.org/Beagleboard:Terminal_Shells#Serial_Connect)
  * [unix stackexchange](https://unix.stackexchange.com/questions/22545/how-to-connect-to-a-serial-port-as-simple-as-using-ssh)
  * nixCraft [<sup>O</sup>](https://www.cyberciti.biz/faq/find-out-linux-serial-ports-with-setserial/) [<sup>O</sup>](https://www.cyberciti.biz/hardware/5-linux-unix-commands-for-connecting-to-the-serial-console/)
  * [dummies](https://www.dummies.com/computers/beaglebone/how-to-connect-the-beaglebone-black-via-serial-over-usb/)
  * [rpi stackexchange](https://raspberrypi.stackexchange.com/a/15825/71791)
  * [askubuntu](https://askubuntu.com/a/474560/634976)
  * [YouTube](https://www.youtube.com/watch?v=3y1LMNPoaJI)

###### [U-boot](https://www.denx.de/wiki/U-Boot)
* [GitLab repo](https://gitlab.denx.de/u-boot)
* [U-boot on AM3358](https://processors.wiki.ti.com/index.php/AM335x_U-Boot_User's_Guide)
* [AM335X readme](https://gitlab.denx.de/u-boot/u-boot/tree/master/board/ti/am335x)
* [DULG Introduction](https://www.denx.de/wiki/view/DULG/Introduction) &rarr; 2.3. Availability  &rarr; [manual in PDF](http://www.denx.de/wiki/publish/DULG/DULG-canyonlands.pdf)
* build
  * [guide from beagleboard.org](http://beagleboard.org/project/U-Boot+%28V1%29/)
  * [u-boot for other SoC on AUR](https://aur.archlinux.org/packages/?O=0&SeB=nd&K=u-boot&outdated=&SB=n&SO=a&PP=50&do_Search=Go)

###### [BusyBox](https://www.busybox.net/)
* [udhcpc](https://en.wikipedia.org/wiki/Udhcpc)



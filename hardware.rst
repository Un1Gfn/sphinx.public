.. include:: include/substitution.txt

==============
|ico| Hardware
==============

Specs
=====

.. https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#anonymous-hyperlinks

| GitHub
| |b| `BBGW schematics`__
| |b| `BBB manual`__

.. __: https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green_Wireless/master/resources/BeagleBone_Green%20Wireless_V1.0_SCH_20160314.pdf
.. __: https://github.com/beagleboard/beaglebone-black/wiki/System-Reference-Manual

| eLinux wiki
| |b| :el:`BB generations brief <BeagleBone_Community>`
| |b| :el:`BeagleBoard <BeagleBoard_Community>`
| |b| :el:`BBB <Beagleboard:BeagleBoneBlack>`
| |b| :el:`BBBW <Beagleboard:BeagleBoneBlackWireless>`

| Seeed wiki
| |b| `BBGW <http://wiki.seeedstudio.com/BeagleBone_Green_Wireless/#specification>`__

| ALARM
| |b| `BBGW <https://archlinuxarm.org/platforms/armv7/ti/beaglebone-green-wireless>`__


Communication Tutorials
=======================

.. |r| replace:: :el:`recovery guide <AM335x_recovery>`

.. table:: Tutorials
   :align: left
   :widths: auto

   +------------------+-----------+---------+----------+--------+---------+--------+--------+-------+-----+-------+
   |                  | Connect                                           |          Build          | Communicate |
   +------------------+-----------+---------+----------+--------+---------+--------+--------+-------+-----+-------+
   | Tutorial         | `RNDIS`_\ | `TFTP`_ | `BOOTP`_ | Serial | Mass    | Boot   | Kernel | User- | NFS | SSH   |
   |                  | [#u]_     |         |          |        | |br|    | |br|   |        | |br|  |     |       |
   |                  |           |         |          |        | Storage | Loader |        | space |     |       |
   +==================+===========+=========+==========+========+=========+========+========+=======+=====+=======+
   | `techniq`_       | |O|       |         |          | |O|    | |O|     |        |        |       |     |       |
   +------------------+-----------+---------+----------+--------+---------+--------+--------+-------+-----+-------+
   | `BBBlfs`_        | |O|       |         |          |        |         | |O|    | |O|    | |O|   |     |       |
   +------------------+-----------+---------+----------+--------+---------+--------+--------+-------+-----+-------+
   | [#p]_ [#b]_\ |r| | |O|       | |O|     | |O|      |        |         | |O|    |        |       |     |       |
   |                  |           |         |          |        |         |        |        |       |     |       |
   +------------------+-----------+---------+----------+--------+---------+--------+--------+-------+-----+-------+
   | `U-boot \        | |O|       | |O|     |          | |O|    |         | |O|    |        |       | |O| |       |
   | on AM335x`_      |           |         |          |        |         |        |        |       |     |       |
   +------------------+-----------+---------+----------+--------+---------+--------+--------+-------+-----+-------+
   | `terminal \      |           |         |          | |O|    |         |        |        |       |     | |O|   |
   | shells`_         |           |         |          |        |         |        |        |       |     |       |
   +------------------+-----------+---------+----------+--------+---------+--------+--------+-------+-----+-------+
   | `Android \       | |O|       |         |          |        |         |        |        |       |     | |O|   |
   | USB SSH`_        |           |         |          |        |         |        |        |       |     |       |
   +------------------+-----------+---------+----------+--------+---------+--------+--------+-------+-----+-------+
   | [#g_ether]_      | |O|       |         |          |        |         |        |        |       |     |       |
   | |br| `deleted    |           |         |          |        |         |        |        |       |     |       |
   | SU question`_    |           |         |          |        |         |        |        |       |     |       |
   +------------------+-----------+---------+----------+--------+---------+--------+--------+-------+-----+-------+
   | `RidgeRun`_      | |O|       |         |          |        |         |        |        |       | |O| |       |
   +------------------+-----------+---------+----------+--------+---------+--------+--------+-------+-----+-------+
   | `eLinux image`_  |           |         |          |        |         | |O|    | |O|    | |O|   |     |       |
   | (obselete)       |           |         |          |        |         |        |        |       |     |       |
   +------------------+-----------+---------+----------+--------+---------+--------+--------+-------+-----+-------+
   | eLinux |br|      |           |         |          | |O|    |         | |O|    | |O|    |       |     |       |
   | `beagleboard`_   |           |         |          |        |         |        |        |       |     |       |
   +------------------+-----------+---------+----------+--------+---------+--------+--------+-------+-----+-------+
   | `nfs-\           |           | |O|     |          |        |         |        |        |       | |O| |       |
   | kernel-\         |           |         |          |        |         |        |        |       |     |       |
   | server`_         |           |         |          |        |         |        |        |       |     |       |
   |                  |           |         |          |        |         |        |        |       |     |       |
   +------------------+-----------+---------+----------+--------+---------+--------+--------+-------+-----+-------+


CPU
===

`45nm <https://www.ti.com/lit/ug/tidua96/tidua96.pdf>`__

.. code:: console

   $ lscpu
   Architecture:           armv7l
     Byte Order:           Little Endian
   CPU(s):                 1
     On-line CPU(s) list:  0
   Vendor ID:              ARM
     Model name:           Cortex-A8
       Model:              2
       Thread(s) per core: 1
       Core(s) per socket: 1
       Socket(s):          1
       Stepping:           r3p2
       CPU max MHz:        1000.0000
       CPU min MHz:        300.0000
       BogoMIPS:           995.32
       Flags:              half thumb fastmult vfp edsp thumbee neon vfpv3 tls vfpd
                           32

.. code:: console

   $ cat /proc/cpuinfo
   processor       : 0
   model name      : ARMv7 Processor rev 2 (v7l)
   BogoMIPS        : 995.32
   Features        : half thumb fastmult vfp edsp thumbee neon vfpv3 tls vfpd32
   CPU implementer : 0x41
   CPU architecture: 7
   CPU variant     : 0x3
   CPU part        : 0xc08
   CPU revision    : 2

   Hardware        : Generic AM33XX (Flattened Device Tree)
   Revision        : 0000
   Serial          : 0000000000000000


`AM3358 <https://www.ti.com/product/AM3358>`__ =
:wp:`ARM Cortex-A8` =
:wp:`ARMv7-A <comparison of ARMv7-A cores>` =
32-bit w/ FPU =
:debian:`gnueabihf <Multiarch/Tuples#armhf>`

`Sitara AM3358 <http://www.ti.com/product/AM3358>`__ ~
:wp:`Arm Cortex-A8` ~
32-bit :debian:`armhf <ArmHardFloatPort#Supported_devices>` ~
:debian:`ArmEabiPort <ArmEabiPort>` ~
:debian:`arm-linux-gnueabihf- <ArmHardFloatPort#Rationale>`\ [#w]_

| `Functional Block Diagram <http://www.ti.com/data-sheets/diagram.tsp?genericPartNumber=AM3358&diagramId=SPRS717K>`__
| Docs `latest rev <http://www.ti.com/product/AM3358/technicaldocuments>`__
| |b| Datasheet ~ AM335x Sitara™ Processors datasheet `trunc rev <http://www.ti.com/lit/gpn/am3358>`__
|     |b2| "Functional Block Diagram" ~ Page 5 (1.4)
| |b| User guides ~ AM335x and AMIC110 Sitara™ Processors Technical Reference Manual `trunc rev <http://www.ti.com/lit/pdf/spruh73>`__
|     |b2| "Memery Map" ~ Page 117 (2.1)
|     |b2| "Public ROM Code Architecture" (xmodem) ~ Page 5019 (26.1.2) (Figure 26-1)
| `Boot process <https://processors.wiki.ti.com/index.php/AM335x_board_bringup_tips>`__
| `U-Boot on AM335x`_


eMMC
====

Prog.World - `eMMC 5.0 sequential write 90MB/s <https://prog.world/nvme-vs-ufs-3-1-the-battle-of-smartphone-memory-types-parsing/>`__

| 6FA27-JY976
| `Allwinner V5 eMMC Support List <http://files.lindeni.org/lindenis-v5/documents/support_list/Allwinner%C2%A0V5%20eMMC%C2%A0Support%C2%A0List.pdf>`__
| Micron MTFC8GAKAJCN-1M WT / MTFC4GACAJCN-1M WT
| (both on the same
  `datasheet <https://www.micron.com/products/managed-nand/emmc/part-catalog/mtfc8gakajcn-1m-wt>`__)


RTC
===

| :file:`/sys/class/rtc/rtc0`
| :file:`/sys/devices/platform/ocp/44c00000.interconnect/44c00000.interconnect:segment@200000/44e3e074.target-module/44e3e000.rtc/rtc/rtc0`

| rtc is dummy
| time survives across ``systemctl reboot``
| but gets lost right after ``systemctl reboot`` even if the power is still attached

| (a) rtc nonexist in /sys
| (b) rtc dummy, zero on boot unless set by system |:ballot_box_with_check:|
| (c) rtc static, non-volative but frozen
| (d) rtc active, goes forward when system is off


Serial
======

| |b| eLinux [#el_s]_ [#el_ts_s]_ [#bb_sp]_
| |b| `unix stackexchange <https://unix.stackexchange.com/questions/22545/how-to-connect-to-a-serial-port-as-simple-as-using-ssh>`__
| |b| nixCraft [#c_f_s]_ [#c_h_s]_
| |b| `dummies <https://www.dummies.com/computers/beaglebone/how-to-connect-the-beaglebone-black-via-serial-over-usb/>`__
| |b| `rpi stackexchange <https://raspberrypi.stackexchange.com/a/15825/71791>`__
| |b| `askubuntu <https://askubuntu.com/a/474560/634976>`__


UART
====

`TI <https://web.archive.org/web/20210114145232/https://processors.wiki.ti.com/index.php/AM335x_U-Boot_User's_Guide#Boot_Over_UART>`__

:yt:`Fastbit Embedded Brain Academy .. Beaglebone Black Serial booting procedure ( UART BOOT ) <3y1LMNPoaJI>`


USB
===

| `<http://wiki.seeedstudio.com/BeagleBone_Green_Wireless/#step2-install-drivers>`__
| |b| ``~/beaglebone/mkudevrule.sh``


Wi-Fi
=====

`schematics`__ page 10 - `WL1835MOD`__

.. __: https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green_Wireless/master/resources/BeagleBone_Green%20Wireless_V1.0_SCH_20160314.pdf
.. __: https://www.ti.com/product/WL1835MOD

| connector - :wp:`RF connectors <list of RF connector types>`\
  /:wp:`micro-sized <list of RF connector types#Micro-sized>`\
| |b| :wp:`Hirose_U.FL`

| `mouser <https://www.mouser.com/>`__\
  /Products\
  /Passive Components\
  /`Antennas <https://www.mouser.com/Passive-Components/Antennas/_/N-8w0fa>`__\
  /Termination Style\
  /
| |b| :file:`IPEX*`
| |b| :file:`MHF / U.FL Plug`
| |b| :file:`u.FL`
| |b| :file:`U.FL*`

| :pkg:`alarm/firmware-beaglebone`
| |b| `rcn-ee <https://github.com/rcn-ee/repos>`__
| |b| `latest-images <https://github.com/beagleboard/Latest-Images>`__
  |larr| `wl18xx_fw <https://git.ti.com/cgit/wilink8-wlan/wl18xx_fw/>`__
  |larr| `WiLink™ 8 Wi-Fi Driver for Linux OS <https://www.ti.com/tool/WILINK8-WIFI-NLCP>`__

`existing Linux Wireless drivers <https://wireless.wiki.kernel.org/en/users/drivers>`__
- `wl18xx <https://wireless.wiki.kernel.org/en/users/drivers/wl18xx>`__


----

.. Footnotes

.. [#u] :wp:`Ethernet over USB`
.. [#p] https://www.pengutronix.de/en/software/barebox.html
.. [#b] https://www.barebox.org/
.. [#g_ether] https://github.com/techniq/wiki/wiki/Linux-USB-Gadget-API#network-g_ether
.. [#w] https://web.archive.org/web/20210114145232/https://processors.wiki.ti.com/index.php/AM335x_U-Boot_User's_Guide#Prerequisite
.. [#el_s] :el:`Beagleboard:BeagleBone_Black_Serial`
.. [#el_ts_s] :el:`Beagleboard:Terminal_Shells#Serial_Connect`
.. [#bb_sp] :el:`BeagleBone/Serial_Port`
.. [#c_f_s] https://www.cyberciti.biz/faq/find-out-linux-serial-ports-with-setserial
.. [#c_h_s] https://www.cyberciti.biz/hardware/5-linux-unix-commands-for-connecting-to-the-serial-console

.. include:: include/link.txt

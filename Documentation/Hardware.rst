==============
|ico| Hardware
==============

Board
=====

.. https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#anonymous-hyperlinks

| GitHub
| |b| `BBGW schematics`__
| |b| `BBB manual`__

.. __: https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green_Wireless/master/resources/BeagleBone_Green%20Wireless_V1.0_SCH_20160314.pdf
.. __: https://github.com/beagleboard/beaglebone-black/wiki/System-Reference-Manual

| eLinux wiki
| |b| `BB generations brief`__
| |b| `BB`__
| |b| `BBB`__
| |b| `BBBW`__

.. __: https://elinux.org/BeagleBone_Community
.. __: https://elinux.org/BeagleBoard_Community
.. __: https://elinux.org/Beagleboard:BeagleBoneBlack
.. __: https://elinux.org/Beagleboard:BeagleBoneBlackWireless

| Seeed wiki
| |b| `BBGW <http://wiki.seeedstudio.com/BeagleBone_Green_Wireless/#specification>`__

Communication Tutorials
=======================

.. |r| replace:: `recovery guide <https://elinux.org/AM335x_recovery>`__

.. table:: Tutorials

  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  |                 |                                                  |          Build          |           |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  | Tutorial        | [#u]_    | `TFTP`_ | `BOOTP`_ | Serial | Mass    | Boot   | Kernel | User- | NFS | SSH |
  |                 | |br|     |         |          |        | |br|    | |br|   |        | |br|  |     |     |
  |                 | `RNDIS`_ |         |          |        | Storage | Loader |        | space |     |     |
  +=================+==========+=========+==========+========+=========+========+========+=======+=====+=====+
  | `techniq`_      | |O|      |         |          | |O|    | |O|     |        |        |       |     |     |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  | `BBBlfs`_       | |O|      |         |          |        |         | |O|    | |O|    | |O|   |     |     |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  | [#p]_ [#b]_     | |O|      | |O|     | |O|      |        |         | |O|    |        |       |     |     |
  | |br| |r|        |          |         |          |        |         |        |        |       |     |     |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  | `U-boot \       | |O|      | |O|     |          | |O|    |         | |O|    |        |       | |O| |     |
  | on AM335x`_     |          |         |          |        |         |        |        |       |     |     |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  | `terminal \     |          |         |          | |O|    |         |        |        |       |     | |O| |
  | shells`_        |          |         |          |        |         |        |        |       |     |     |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  | `Android \      | |O|      |         |          |        |         |        |        |       |     | |O| |
  | USB SSH`_       |          |         |          |        |         |        |        |       |     |     |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  | [#g_ether]_     | |O|      |         |          |        |         |        |        |       |     |     |
  | |br| `deleted   |          |         |          |        |         |        |        |       |     |     |
  | SU question`_   |          |         |          |        |         |        |        |       |     |     |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  | `RidgeRun`_     | |O|      |         |          |        |         |        |        |       | |O| |     |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  | `eLinux image`_ |          |         |          |        |         | |O|    | |O|    | |O|   |     |     |
  | (obselete)      |          |         |          |        |         |        |        |       |     |     |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  | eLinux |br|     |          |         |          | |O|    |         | |O|    | |O|    |       |     |     |
  | `beagleboard`_  |          |         |          |        |         |        |        |       |     |     |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+
  | `nfs-\          |          | |O|     |          |        |         |        |        |       | |O| |     |
  | kernel-\        |          |         |          |        |         |        |        |       |     |     |
  | server`_        |          |         |          |        |         |        |        |       |     |     |
  |                 |          |         |          |        |         |        |        |       |     |     |
  +-----------------+----------+---------+----------+--------+---------+--------+--------+-------+-----+-----+

CPU
===

`AM3358 <https://www.ti.com/product/AM3358>`__ =
`Cortex-A8 <https://en.wikipedia.org/wiki/ARM_Cortex-A8>`__ =
`ARMv7-A <https://en.wikipedia.org/wiki/Comparison_of_ARMv7-A_cores>`__ =
32-bit w/ FPU =
`gnueabihf <https://wiki.debian.org/Multiarch/Tuples#armhf>`__

`Sitara AM3358 <http://www.ti.com/product/AM3358>`__ ~
`Arm Cortex-A8 <https://en.wikipedia.org/wiki/ARM_Cortex-A8>`__ ~
32-bit `armhf <https://wiki.debian.org/ArmHardFloatPort#Supported_devices>`__
`ArmEabiPort <https://wiki.debian.org/ArmEabiPort>`__
`arm-linux-gnueabihf- <https://wiki.debian.org/ArmHardFloatPort#Rationale>`__
[#w]_

| `Functional Block Diagram <http://www.ti.com/data-sheets/diagram.tsp?genericPartNumber=AM3358&diagramId=SPRS717K>`__
| Docs `latest rev <http://www.ti.com/product/AM3358/technicaldocuments>`__
| |b| Datasheet ~ AM335x Sitara™ Processors datasheet `trunc rev <http://www.ti.com/lit/gpn/am3358>`__
|     |b| "Functional Block Diagram" ~ Page 5 (1.4)
| |b| User guides ~ AM335x and AMIC110 Sitara™ Processors Technical Reference Manual `trunc rev <http://www.ti.com/lit/pdf/spruh73>`__
|     |b| "Memery Map" ~ Page 117 (2.1)
|     |b| "Public ROM Code Architecture" (xmodem) ~ Page 5019 (26.1.2) (Figure 26-1)
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

Serial
======

| |b| eLinux [#el_s]_ [#el_ts_s]_
| |b| `unix stackexchange <https://unix.stackexchange.com/questions/22545/how-to-connect-to-a-serial-port-as-simple-as-using-ssh>`__
| |b| nixCraft [#c_f_s]_ [#c_h_s]_
| |b| `dummies <https://www.dummies.com/computers/beaglebone/how-to-connect-the-beaglebone-black-via-serial-over-usb/>`__
| |b| `rpi stackexchange <https://raspberrypi.stackexchange.com/a/15825/71791>`__
| |b| `askubuntu <https://askubuntu.com/a/474560/634976>`__

UART
====

| |b| `YouTube <https://www.youtube.com/watch?v=3y1LMNPoaJI>`__
| |b| `TI <https://web.archive.org/web/20210114145232/https://processors.wiki.ti.com/index.php/AM335x_U-Boot_User's_Guide#Boot_Over_UART>`__

.. https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#transitions

----

.. Footnotes

.. [#u] https://en.wikipedia.org/wiki/Ethernet_over_USB
.. [#p] https://www.pengutronix.de/en/software/barebox.html
.. [#b] https://www.barebox.org/
.. [#g_ether] https://github.com/techniq/wiki/wiki/Linux-USB-Gadget-API#network-g_ether
.. [#w] https://web.archive.org/web/20210114145232/https://processors.wiki.ti.com/index.php/AM335x_U-Boot_User's_Guide#Prerequisite
.. [#el_s] https://elinux.org/Beagleboard:BeagleBone_Black_Serial
.. [#el_ts_s] https://elinux.org/Beagleboard:Terminal_Shells#Serial_Connect
.. [#c_f_s] https://www.cyberciti.biz/faq/find-out-linux-serial-ports-with-setserial
.. [#c_h_s] https://www.cyberciti.biz/hardware/5-linux-unix-commands-for-connecting-to-the-serial-console

.. include:: link.txt

.. include:: substitution.txt

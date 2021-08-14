.. include:: substitution.txt

==============
|ico| `ALARM`_
==============

`alarm.md <https://github.com/Un1Gfn/beaglebone/blob/markdown/alarm.md>`__

Misc
====

.. warning::

   `Shut down USB <https://www.denx.de/wiki/view/U-Boot/DesignPrinciples#2_Keep_it_Fast>`__
   before booting Linux.

ALARM/`BBGW <https://archlinuxarm.org/platforms/armv7/ti/beaglebone-green-wireless>`__

`boot from USB <https://stackoverflow.com/questions/30488942/how-to-boot-linux-kernel-from-u-boot>`__

denx `TFTP+NFS <https://www.denx.de/wiki/view/DULG/LinuxNfsRoot>`__

| Install ALARM with only U-Boot
|  generate ALARM root ext4 image
|  :manpage:`split(1)` into 256MiB pieces
|  for each piece
|   send via `TFTP`_\ (UDP)
|   u-boot `sha1sum`__\ [#]_

.. __: https://github.com/u-boot/u-boot/blob/master/cmd/sha1sum.c

ArchWiki/:aw:`Working with the serial console`

| make `FIT image <https://elinux.org/images/f/f4/Elc2013_Fernandes.pdf>`__
  with :pkg:`community/uboot-tools` :manpage:`mkimage(1)`
| |b| `ELF to uImage <https://www.denx.de/wiki/view/DULG/HowCanICreateAnUImageFromAELFFile>`__

.. code:: text

                   [SCREEN]
   enp0s20f0u2 -> [KEYBOARD] <- enp0s20f0u1
                  [TOUCHPAD]

| linux-hardware.org/`0b95-1790 <https://linux-hardware.org/?id=usb:0b95-1790>`__
| |b| ``$ lsusb`` :file:`Bus 00? Device 00?: ID 0b95:1790 ASIX Electronics Corp. AX88179 Gigabit Ethernet`
| |b| ``$ ip addr`` :file:`link/ether 00:0e:c6:d3:2d:5f`
| |b| ``$ usb-devices``\ [#]_ :file:`Driver=ax88179_178a`

``proto=tcp`` and force ``autonegotiation`` [#]_

use :ltlink:`busybox rx <https://www.busybox.net/downloads/BusyBox.html#rx>` instead of ``cat`` for :file:`ax88179_178a.ko.gz` ?

`ALARM <https://archlinuxarm.org/packages/armv7h/uboot-beaglebone/files/uboot-beaglebone.install>`__
- `boot.txt <https://archlinuxarm.org/packages/armv7h/uboot-beaglebone/files/boot.txt>`__

PC Set up NIC
=============

*S0*\ [0]_ Set up NIC
=====================

u-boot `drivers/net <https://github.com/u-boot/u-boot/tree/master/drivers/net>`__/e1000

`Net: No ethernet found <https://www.denx.de/wiki/view/DULG/NetNoEthernetFound>`__

NIC.TFTP Send zImage+initramfs
==============================

| denx `boot from BOOTP/TFTP <https://www.denx.de/wiki/view/DULG/UBootCmdGroupDownload#Section_5.9.5.1.>`__
| ArchWiki :aw:`TFTP`

*S0*\ [0]_ -> **S1**\ [1]_
==========================

Serial Send NIC driver
======================

.. [#]_

PC Set up NFS
=============

**S1**\ [1]_ -> **S2**\ [2]_
============================

| ``root=/dev/nfs``
| ``nfsroot=[<server-ip>:]<root-dir>[,<nfs-options>]``\ [#]_

.. warning::
   
   Check eMMC partition alignment!

Footnotes
=========

.. [#]   `sh1sum.c <https://github.com/u-boot/u-boot/blob/master/cmd/sha1sum.c>`__:\
         ``do_sha1sum`` |larr|
         `hash.c <https://github.com/u-boot/u-boot/blob/master/common/hash.c>`__:\
         ``hash_command()``

.. [#]   https://unix.stackexchange.com/a/60080

.. [#]   https://www.denx.de/wiki/view/DULG/EthernetIsUnreliable


.. [0]   **S0:** U-Boot with built-in NIC driver
.. [1]   **S1:** Linux and initramfs as rootfs (busybox?), lacking kernel module for NIC
.. [2]   **S2:** Linux and NFS as rootfs, fully functional

.. [#]   https://www.kernel.org/doc/Documentation/filesystems/nfs/nfsroot.txt

.. \[#]   ???

.. include:: link.txt

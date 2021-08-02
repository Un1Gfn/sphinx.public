.. include:: substitution.txt

==============
|ico| `ALARM`_
==============

Misc
====

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

Footnotes
=========

.. [#] `sh1sum.c <https://github.com/u-boot/u-boot/blob/master/cmd/sha1sum.c>`__:\
       ``do_sha1sum`` |larr|
       `hash.c <https://github.com/u-boot/u-boot/blob/master/common/hash.c>`__:\
       ``hash_command()``

.. [0] **S0:** U-Boot with built-in NIC driver
.. [1] **S1:** Linux and initramfs as rootfs (busybox?), lacking kernel module for NIC
.. [2] **S2:** Linux and NFS as rootfs, fully functional

.. [#] https://www.kernel.org/doc/Documentation/filesystems/nfs/nfsroot.txt

.. \[#] ???

.. include:: link.txt

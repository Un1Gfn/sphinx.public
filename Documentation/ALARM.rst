.. include:: substitution.txt

==============
|ico| `ALARM`_
==============

Misc
====

ALARM/`BBGW <https://archlinuxarm.org/platforms/armv7/ti/beaglebone-green-wireless>`__

PC Set up NIC
=============

*S0*\ [0]_ Set up NIC
=====================

NIC.TFTP Send zImage+initramfs
==============================

*S0*\ [0]_ -> **S1**\ [1]_
==========================

Serial.Minicom Send NIC ko
==========================

.. [#]_

PC Set up NFS
=============

**S1**\ [1]_ -> **S2**\ [2]_
============================

Footnotes
=========

.. [0] **S0:** U-Boot with built-in NIC driver
.. [1] **S1:** Linux and initramfs as rootfs (busybox?), lacking kernel module for NIC
.. [2] **S2:** Linux and NFS as rootfs, fully functional


.. \[#] ???

.. include:: link.txt

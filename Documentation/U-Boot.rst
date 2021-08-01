.. include:: substitution.txt

================
|ico| `U-Boot`__
================

.. __: https://www.denx.de/wiki/U-Boot

Misc
====

`Title Capitalization Tool <https://capitalizemytitle.com/>`__

| `GitLab Instance repo <https://source.denx.de/u-boot/u-boot>`__ |:snail:|
| `GitHub mirror <https://github.com/u-boot/u-boot>`__ |:zap:|\ |:zap:|\ |:zap:|

:el:`U-Boot stages <Panda How_to_MLO_&_u-boot#Introduction>`

| Gmail `search operators`__
| |b| `filter archived mails`__ with ``in:archive``
| |b| Search `lists.denx.de`__
|     |b2| `with Google`__
|     |b2| `with MARC`__

.. __: https://support.google.com/mail/answer/7190
.. __: https://webapps.stackexchange.com/questions/1168/can-i-see-only-mail-i-have-archived-in-gmail
.. __: https://lists.denx.de/listinfo
.. __: https://www.google.com/search?q=site:lists.denx.de
.. __: https://marc.info/?l=u-boot

.. :prlink:`history <https://github.com/u-boot/u-boot/commits/master/configs/am335x_boneblack_vboot_defconfig>\ `\ :pr:`of configs/am335x_boneblack_vboot_defconfig`

no need for verified boot, use ``configs/am335x_evm_defconfig`` instead\ [#]_

========================================== ============= ================ ============
 config                                     version       u-boot-spl.bin   u-boot.img 
========================================== ============= ================ ============
 :pr:`configs/am335x_evm_defconfig`         `history`__
 configs/am335x_boneblack_vboot_defconfig   v2021.04      |O|              |O|
========================================== ============= ================ ============

.. __: https://github.com/u-boot/u-boot/commits/master/configs/am335x_boneblack_vboot_defconfig

make `FIT image <https://elinux.org/images/f/f4/Elc2013_Fernandes.pdf>`__
with :pkg:`community/uboot-tools` :manpage:`mkimage(1)`

| `README <https://github.com/u-boot>`__
  - *Building the Software:*
| AM335X/`README <https://github.com/u-boot/u-boot/tree/master/board/ti/am335x>`__

`DULG Introduction <https://www.denx.de/wiki/view/DULG/Introduction>`__
~ 2.3. Availability
~ `PDF manual <http://www.denx.de/wiki/publish/DULG/DULG-canyonlands.pdf>`__

`U-Boot on AM335x`_

| Guides on building u-boot
| |b| `TI <https://web.archive.org/web/20210114145232/https://processors.wiki.ti.com/index.php/AM335x_U-Boot_User's_Guide>`__
| |b| `PKGBUILD for other SoC <https://aur.archlinux.org/packages/?O=0&SeB=nd&K=u-boot&outdated=&SB=n&SO=a&PP=50&do_Search=Go>`__
| |b| `Buildroot <https://git.busybox.net/buildroot/tree/board/beaglebone/readme.txt>`__

.. Pentester Academy TV .. Embedded Linux Booting Process (Multi-Stage Bootloaders, Kernel, Filesystem)
.. youtube:: DV5S_ZSdK0s
   :height: 80
   :width: 100%

|

Get U-Boot
==========

|alpha| Get from ALARM [*]_
---------------------------

Make U-Boot eMMC image
======================

Connect Serial Debug Port
=========================

Serial Send U-Boot
==================

Write U-Boot to eMMC
====================

Power Off
=========

Footnotes
=========

.. [*] Recommended
.. [#] https://lists.denx.de/pipermail/u-boot/2021-May/449518.html

.. include:: link.txt

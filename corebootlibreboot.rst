.. include:: include/substitution.txt

==========================
coreboot/Libreboot
==========================

| `<https://thinkpads.com/forum/viewtopic.php?f=43&p=845241>`__
| `<https://www.thinkpads.com/forum/viewtopic.php?t=132686>`__

| *dmidecode*
| :file:`~/x200/7VET83WW.dmidecode\*`

.. table:: BIOS settings page
   :align: left
   :widths: auto

   ======= ============================== ======================================
    \       BIOS Version                   3.13 (7VET83WW)
    \       BIOS Date                      2010-03-12
    \       Embedded Controller Version    1.06
    \       System-unit serial number      745533ALV0039R
    \       System board serial number     1ZGMD28DFB6
    \       CPU Type                       Intel(R) Core(TM)2 Duo CPU P8600
    \       CPU Speed                      2.40GHz
    \       Installed Memory               8192MB
    \       UUID                           95e196a0-0b28-11dd-806e-c93a11fb16fb
    \       MAC Address (Internal LAN)     88 88 88 88 87 88
   ------- ------------------------------ --------------------------------------
   ------- ------------------------------ --------------------------------------
    AMT     Active Management Technology
    FSP     Firmware Support Package
    ME      Management Engine
    vBIOS   Video BIOS
   ======= ============================== ======================================

:raw-html:`<details><summary>[IMG_0146.JPG] photograph of BIOS settings page</summary>`

.. image:: ../x200/IMG_0146.JPG 
   :alt: [IMG_0146.JPG]

:raw-html:`</details>`

| `coreboot <https://www.coreboot.org/>`__
  - :wp:`wp:coreboot <coreboot>`
  - `r/coreboot <https://www.reddit.com/r/coreboot/>`__
  - `aur/\*coreboot\* <https://aur.archlinux.org/packages/?O=0&SeB=nd&K=coreboot>`__
| |b| `payloads <https://doc.coreboot.org/payloads.html>`__
| |b| `releases <https://doc.coreboot.org/releases/index.html>`__
| |b| `flashing firmware tutorial <https://doc.coreboot.org/flash_tutorial/index.html>`__

| `Libreboot <https://libreboot.org/>`__
  - :wp:`wp:Libreboot <Libreboot>`
  - `r/libreboot <https://www.reddit.com/r/libreboot/>`__
  - `aur/\*libreboot\* <https://aur.archlinux.org/packages/?O=0&SeB=nd&K=libreboot>`__
| |b| `version history <https://libreboot.org/news/>`__
| |b| `downloads <https://libreboot.org/download.html>`__ - `roms <https://mirrors.mit.edu/libreboot/testing/20210522/roms/>`__
| |b| `x200 <https://libreboot.org/docs/hardware/x200.html>`__

`FSP <https://www.intel.com/content/www/us/en/intelligent-systems/intel-firmware-support-package/intel-fsp-overview.html>`__
(`archive <http://web.archive.org/web/*/https://www.intel.com/content/www/us/en/intelligent-systems/intel-firmware-support-package/intel-fsp-overview.html>`__)
- `github/FSP <https://github.com/intel/FSP>`__
- `github/BCT <https://github.com/intel/BCT>`__

| extract bin/rom from exe
| |b| `<https://www.youtube.com/watch?v=0dr7uq27sTA>`__
| |b| `<https://www.youtube.com/watch?v=7qESTVi_DVg>`__
| |b| `<https://www.youtube.com/watch?v=FWGs_ivzFxs>`__
| |b| `<https://www.youtube.com/watch?v=L9nFUCimaF8>`__
| |b| `<https://www.youtube.com/watch?v=kVXk28c59hM>`__
| |b| `<https://www.youtube.com/watch?v=qdNrp8IBfoU>`__

`pureboot <https://docs.puri.sm/PureBoot.html>`__

Intel FSP reverse engineering: finding the real entry point! (latest
`archive <http://web.archive.org/web/20180421130721/https://puri.sm/posts/intel-fsp-reverse-engineering-finding-the-real-entry-point/>`__
before removal)

`a primer guide to reverse engineering <https://puri.sm/posts/primer-to-reverse-engineering/>`__

| `ich9fdgbe_8m.bin <https://github.com/m4rc0linux/thinkpad-x200-coreboot>`__ (8MiB)
| `x200 7457.rar <https://badcaps.net/forum/showthread.php?t=57533>`__ (8MiB)

`<https://stafwag.github.io/blog/blog/2019/02/10/how-to-install-libreboot-on-a-thinkspad-w500/>`__

::

   F=x200_4mb/seabios_grubfirst_x200_4mb_libgfxinit_corebootfb_esqwerty.rom
   hexdump "$F" | grep -B1 -e '^\*$' -A1 | less -SRM +%
   hexdump "$F" | grep 'ffff ffff ffff ffff ffff ffff ffff ffff' | less -SRM +%
   hexdump "$F" | grep '0000 0000 0000 0000 0000 0000 0000 0000' | less -SRM +%
   hexdump "$F" | grep 
   hexdump "$F" | less -SRM +%
   '00f5fa0'


BMP
===

multithreading (divide into 4 parts)

| :pr:`mmap()`
| :menuselection:`read rom buffer from file --> open bmp buffer --> fill bmp buffer --> write bmp buffer to file`

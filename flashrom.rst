.. include:: include/substitution.txt
.. highlight:: text

================
Flashrom |:zap:|
================

| `<https://en.wikipedia.org/wiki/Chipset>`__
| `<https://en.wikipedia.org/wiki/I/O_Controller_Hub>`__
| `<https://en.wikipedia.org/wiki/Northbridge_(computing)>`__
| `<https://en.wikipedia.org/wiki/Platform_Controller_Hub>`__
| `<https://en.wikipedia.org/wiki/Southbridge_(computing)>`__


Misc
====

.. note::

   | |:shopping_cart:|\ |:shopping:|
   | |b| :pr:`stranded` solid :pr:`duplex` copper wire (單股銅線)
   | |b| 47 ohm resistor, at least 4 pcs
   | |b| :wp:`helping hand <helping hand (tool)>` / :wp:`jig <jig (tool)>` / :zh:`夾具`
   | |b| USB tester
   | |b| :wp:`jumpers <jumper (computing)>`
   | |b| :wp:`magnifying glass`
         - `33038367511 <https://www.aliexpress.com/i/33038367511.html>`__
         - :tmall:`619962129533`
   | |b| female header (keep spare jumper wires neat)

squeeze and discard
|vv| `bios.md <https://github.com/Un1Gfn/x200/blob/master/bios.md>`__
|vv| `readme.md <https://github.com/Un1Gfn/x200/blob/master/readme.md>`__

::

   ERROR
   0271: Check date and time settings
   ERROR
   0251: System CMOS checksum bad - Default configuration used

:raw-html:`<details><summary>CH341A devices overview (photograph)</summary>`

.. image:: https://1.bp.blogspot.com/-RFzfABqVamg/WlEZ-s0FkxI/AAAAAAAAIqg/3L0JBCCQN9sNm4e7ST9Csczwwu7tO1OzgCLcBGAs/s1600/ch341a_products.png
   :target: https://github.com/boseji/CH341-Store
   :alt: [CH341-Store]

:raw-html:`</details>`


DKMS
====

.. warning::

   | Unable to test
   | See flashrom\:\ :ref:`CH341A MiniProgrammer <flashrom:CH341A\\ \|br\|\\ MiniProgrammer>`

:aw:`DKMS`
- :manpage:`dkms(8)`
- :aw:`package guidelines <DKMS package guidelines>`

AUR - `\*ch34\* <https://aur.archlinux.org/packages/?O=0&K=ch34>`__

:pkg:`AUR/spi-ch341-usb-dkms`

| :pkg:`AUR/ch341-i2c-spi-gpio-dkms-git` (`frank-zago/ch341-i2c-spi-gpio <https://github.com/frank-zago/ch341-i2c-spi-gpio>`__)
| :file:`/usr/src/ch341-i2c-spi-gpio-*/` - installed source
| :file:`/var/lib/dkms/ch341-i2c-spi-gpio/` - generated module

::

   flashrom -p linux_spi:dev=/dev/spidev0.0 ...
   flashrom -p linux_spi:dev=/dev/spidev0.0 ...


W25Q32BVSIG
===========

`official datasheet <https://www.winbond.com/resource-files/w25q32bv_revi_100413_wo_automotive.pdf>`__
(`archive <http://web.archive.org/web/*/https://www.winbond.com/resource-files/w25q32bv_revi_100413_wo_automotive.pdf>`__)

| connect to SOIC 208-mil W25Q32BVSIG
| IEC 60757 `2-letter color code <https://www.kollmorgen.com/en-us/developer-network/wire-color-coding/>`__
| :file:`~/x200/W25Q32BV.pdf` - p10 - *4.2 Serial Data Input, Output and IOs (DI, DO and IO0, IO1, IO2, IO3)*
|     DI (input) ...  to serially write instructions, addresses or data to the device
|     DO (output) ... to read data or status from the device

::

                                    O---------------+
                               [BU] |1 /CS     VCC 8| [RD] (connect everything else, check again, then connect VCC)
                        (MISO) [WH] |2  DO   /HOLD 7| [RD] (aL, H=don't hold?) <???>
   <???> (aL, L=writeprotect?) [BK] |3 /WP     CLK 6| [YE]
                               [BK] |4 GND      DI 5| [GN] (MOSI)
                                    +---------------+


CH341A\ |br|\ MiniProgrammer
============================

:wp:`ZIF <zero insertion force>` socket

::

   front
   +----------+---------+
   | 5 6 7 8  |         |
   |          |         |
   |          |         |
   | 4 3 2 1  |         |
   +----------+---------+

   back
   +----------+---------+
   | 5 6 7 8  |         |   MISO  5v  ⚡
   |  25 SPI  | 24 I2C  |   MOSI  5v  ⚡
   |   BIOS  (  EEPROM (    VCC  3.3v .
   | 4 3 2 1  |         |
   +----------+---------+

.. hint::
   | 5V data might be necessary, clues:
   | |b| ``Found Winbond flash chip "W25Q32.V" (4096 kB, SPI) on ch341a_spi.`` not showing up on the first flashrom attempt
   | |b| ``Block protection could not be disabled!`` every now and then
   | |b| \
         `ISP <https://www.flashrom.org/ISP>`__ -
         `interference from other on-board circuits that are connected to W25Q32BVSIG as well <http://www.diybcq.com/thread-145078-1-1.html>`__
   | Better desolder W25Q32BVSIG and use SMT test socket!


:pr:`CH341A`\ |br|\ :pr:`LC-Technology`
=======================================

.. error::

   | CH341A.LC-Technology does NOT work even if /WP grounded and /HOLD pulled HIGH
   | Dump differs each time
   | 5v MOSI/MISO along with 3.3v VCC turns out to be necessary
   | Try desoldered offline programming instead of `ISP <https://flashrom.org/ISP>`__

.. _ref_ch341:

| `CH341 <http://www.wch.cn/products/CH341.html>`__
  with 3 :wp:`jumpers <jumper (computing)>`
  |:dart:|
| :taobao:`584926806782` (`img <https://gd1.alicdn.com/imgextra/i1/44390641/O1CN017SjtRI1GbcMnRjeuf_!!44390641.jpg>`__)
| :taobao:`595835010606` (`img <https://gd4.alicdn.com/imgextra/i4/4112832130/O1CN01Got6Sd1Rba9YqMnSO_!!4112832130.jpg>`__)
| :taobao:`616744148415` (`img <https://gd1.alicdn.com/imgextra/i1/2658592015/O1CN01Q53EjM1QkufS4F2K6_!!2658592015.jpg>`__)

::

   (SPI)  +---+---+   (TTL)
   (I2C)  | O   O | O (UART)                      +-----+
   (GPIO) +---+---+                      VCC [RD] |01 ..| NC
              +---------+  +----------+  GND [BK] |02 ..| NC
   --------+  | AMS1117 |  |WCH CH341A|  CS0 [BU] |03 ..| NC
      USB-A|  |3.3 2129C|  |202386A40 |  CS1      |04 ..| NC
   --------+  +---------+  +----------+  CS2      |05 ..| NC
              +---+---+                  SCK [YE] |06 ..| NC
            O | O   O |                 MOSI [GN] |07 ..| NC
              +---+---+                 MISO [WH] |08 ..| NC
            O | O   O |                           +-----+
              +---+---+
          (5v)     (3v3)

.. warning::

   | Check
   |  (1) clip pinout
   |  (2) connection between clip and CH341A
   | before plugging CH341A to PC

.. danger::

   | For online voltage test
   |  |b| Plug CH341A to a USB wall adapter instead of a PC
   |  |b| **VCC and GND pins on SPI side are too close, be cautious not shorting them** |:skull:|
   | Attach female-female jump wires and perform test on the other side of the wires


Other\ |br|\ programmers
========================

| `FT2232SPI_Programmer <https://flashrom.org/FT2232SPI_Programmer>`__
| |b| `C232HM-DDHSL (3.3V) <https://ftdichip.com/products/c232hm-ddhsl-0-2/>`__
      :prlink:`C232HM-EDHSL (5V) <https://ftdichip.com/products/c232hm-edhsl-0/>`
| |b| `FT2232H Mini-Module <https://ftdichip.com/products/ft2232h-mini-module/>`__

| `serprog <https://www.flashrom.org/Serprog>`__
| |b| `Urja Rannikko <https://www.flashrom.org/Arduino_flasher_3.3v>`__

Flashrom
========

:raw-html:`<details><summary>ch341prog</summary>`

:pkg:`AUR/ch341prog-git`

::

   for i in 1; do
      cd ~darren/x200 || break
      FILE="$(date +%4Y%m%d-%H:%M:%S.rom)"
      echo "$FILE"
      echo
      printf "\n\e[7m  %s  \e[0m\n\n" "$(date)"
      ch341prog -r "$(date +%4Y%m%d-%H:%M:%S.rom)" || break
      printf "\n\e[7m  %s  \e[0m\n\n" "$(date)"
      echo
      id darren &>/dev/null || break
      chown darren:darren "$FILE"
   done

::

   Device reported its revision [4.03]
   Manufacturer ID: ef
   Memory Type: 4016
   No CFI structure found, trying to get capacity from device ID. Set manually if detection fails.
   Capacity: 16
   Chip capacity is 4194304 bytes
   Read started!

:raw-html:`</details>`

`flashrom <https://www.flashrom.org/Flashrom>`__
|vv| `Common_problems <https://www.flashrom.org/Common_problems>`__
|vv| `FAQ <https://www.flashrom.org/FAQ>`__
|vv| `Board_Testing_HOWTO (-p internal) <https://www.flashrom.org/Board_Testing_HOWTO>`__


.. code:: console

   # flashrom --flash-name -p ch341a_spi
   Using clock_gettime for delay loops (clk_id: 1, resolution: 1ns).
   Found Winbond flash chip "W25Q32.V" (4096 kB, SPI) on ch341a_spi.
   vendor="Winbond" name="W25Q32.V"

   # flashrom --flash-size -p ch341a_spi
   Using clock_gettime for delay loops (clk_id: 1, resolution: 1ns).
   Found Winbond flash chip "W25Q32.V" (4096 kB, SPI) on ch341a_spi.
   4194304 (4*1024*1024)

::

   # "$(date +%4Y%m%d-%H:%M:%S.bios)"
   # "$(date +%4Y%m%d-%H:%M:%S.fd)"
   # "$(date +%4Y%m%d-%H:%M:%S.gbe)"
   # "$(date +%4Y%m%d-%H:%M:%S.me)"
   # "$(date +%4Y%m%d-%H:%M:%S.pd)"
   # "$(date +%4Y%m%d-%H:%M:%S.rom)"
   echo; cd ~darren/x200 && {
      FILE="$(date +%4Y%m%d-%H:%M:%S.rom)"
      echo "$FILE"
      echo
      printf "\n\e[7m  %s  \e[0m\n\n" "$(date)"
      flashrom -r "$FILE" -p ch341a_spi
      printf "\n\e[7m  %s  \e[0m\n\n" "$(date)"
      echo
      id darren &>/dev/null && chown darren:darren "$FILE"
   }

::

   Using clock_gettime for delay loops (clk_id: 1, resolution: 1ns).
   Found Winbond flash chip "W25Q32.V" (4096 kB, SPI) on ch341a_spi.
   Block protection could not be disabled!
   Reading flash... done.

verify ::

   FILE=""
   flashrom -v "$FILE" -p ch341a_spi

| `<https://libreboot.org/docs/install/spi.html#hardware-configuration>`__
| `<https://www.coreboot.org/Board:lenovo/x200#Dumping_the_original_firmware>`__

| `drivers/usb/serial/ch341.c <https://github.com/torvalds/linux/blob/df7b16d1c00ecb3da3a30c999cdb39f273c99a2f/drivers/usb/serial/ch341.c#L12>`__
| *This driver only supports the asynchronous serial interface.*

CH341PAR_LINUX.ZIP -
`wch.cn <http://www.wch.cn/downloads/CH341PAR_LINUX_ZIP.html>`__
|vv| `CH341-Store <https://github.com/boseji/CH341-Store/blob/master/CH341-Linux-SPI-I2C-Driver+SDK-library/>`__
- identical

`usb-module association <https://unix.stackexchange.com/q/60078>`__ ::

   echo
   pushd /sys/bus/usb/devices/ 1>/dev/null && {
      shopt -s nullglob
      for i in !(*:*); do
         printf "%-7s %s:%s\n" "$i" "$(0< "$i"/idVendor)" "$(0< "$i"/idProduct)"
         for j in "$i:"*; do
            ALA="$(0< "$j"/modalias)"
            echo "$j $ALA $(modinfo $ALA | grep filename | cut -d' ' -f8- | uniq)"
         done
         echo
      done
      shopt -u nullglob
   } && popd 1>/dev/null


ROM
===

strings ::

   # https://stackoverflow.com/questions/5917576/sort-a-text-file-by-line-length-including-spaces
   strings 20210930-01:55:28.rom \
      | sort \
      | uniq \
      | perl -e 'print sort { length($b) <=> length($a) } <>' \
      | less -SRM +%

hex diff ::

   rm -v 2021????-??:??:??.hex
   ls -l *.rom
   sha512sum *.rom
   for i in *.rom; do
      echo "${i%.rom}.hex"
      hexdump "$i" 1>"${i%.rom}.hex"
   done

| `<https://softwarerecs.stackexchange.com/questions/30930/hexadecimal-diff-viewer-for-linux>`__
| `<https://superuser.com/questions/125376/how-do-i-compare-binary-files-in-linux>`__
| \
  ``colordiff --color=always -y <(xxd AAA.rom) <(xxd BBB.rom) | less -SRM +%``
| `GHex <https://wiki.gnome.org/Apps/Ghex>`__
| `okteta <https://apps.kde.org/okteta/>`__
| `wxHexEditor <https://github.com/EUA/wxHexEditor>`__
| `bless <https://github.com/afrantzis/bless>`__


Audio/Video/GPU
===============

:amz:`mini pcie to pcie adapter` + low-profile graphics card

LVDS to HDMI adapter

| `4-chipset-family-datasheet.pdf <https://www.intel.com/content/dam/www/public/us/en/documents/datasheets/4-chipset-family-datasheet.pdf>`__
  (`archive <https://web.archive.org/web/20210807102641/https://www.intel.com/content/dam/www/public/us/en/documents/datasheets/4-chipset-family-datasheet.pdf>`__)
| *Analog Display* - *Up to 2048x1536 @ 75 Hz refresh*
| :wp:`SDVO <Serial Digital Video Out>`


:wp:`PCIe`
==========


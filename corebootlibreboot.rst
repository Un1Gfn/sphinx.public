.. include:: include/substitution.txt

==========================
coreboot/Libreboot
==========================

Contacts
========

| `community <https://doc.coreboot.org/community/forums.html>`__
| |b| `mailing lists <https://mail.coreboot.org/>`__
| |b| `archive <https://mail.coreboot.org/hyperkitty/>`__

`coreboot for developers <https://www.coreboot.org/developers.html>`__
- `discord <https://discord.gg/JqT8NM5Zbg>`__

Misc
====

| `<https://thinkpads.com/forum/viewtopic.php?f=43&p=845241>`__
| `<https://www.thinkpads.com/forum/viewtopic.php?t=132686>`__

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
   hexdump "$F" | less -SRM +%
   '00f5fa0'


:wp:`BMP`
=========

:raw-html:`<details><summary><s>increase performance</s></summary>`

| |b| multithreading (divide into 4 parts)
| |b| :wp:`GPGPU <general-purpose computing on graphics processing units>` - :aw:`archwiki <GPGPU>`
| |b| `__builtin_expect <https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html#index-_005f_005fbuiltin_005fexpect>`__

:raw-html:`</details>`

:raw-html:`<details><summary>/dev/fb0</summary>`

::

   echo
   F=/tmp/test.$(uuidgen).sh
   cat <<EOF >$F
   cd ~/x200 && {
      clear; cat dump.bin >/dev/fb0
      read -r
      clear; cat reddit_r_SLASH_libreboot_SLASH_comments_SLASH_o2ygo1...Broccoli-Smooth_4MB.bin >/dev/fb0
      # clear; cat x200_4mb/seabios_grubfirst_x200_4mb_libgfxinit_txtmode_usqwerty.rom >/dev/fb0
   }
   EOF
   chmod +x $F
   echo "run '$F' in linux console"
   echo

:raw-html:`</details>`

decode ::

   wget $'\x68\x74\x74\x70\x73'://lmcnulty.gitlab.io/blog/bmp-output/1x1.bmp
   hexdump -v -e '1/1 "%02x "' 1x1.bmp; echo
   bash -c "$(head -1 bmp_r.c | cut -d' ' -f2-)"
   rm 1x1.bmp

:pkg:`extra/eog` = |dumpster_fire|

| feh
| :guilabel:`r` [reload_image] :guilabel:`w` [size_to_image] :guilabel:`x` [close]
| :guilabel:`Up` [zoom_in] :guilabel:`Down` [zoom_out]

::

   cd ~/x200 && bash -c "$(head -1 bmp_ombre.c | cut -d' ' -f2-)"

bmp_bin.c ::

    argv
   --------> h ----+       bpp
                   +--> w ----> pixarr --> filesz
   ------> binsz --+
    ftell

:aw:`list of applications#Image_viewers`

| okular
| |b| :menuselection:`Settings --> Configure Okular... --> Performance --> Enable graphics antialias = ☐`

| GIMP
| |b| `user manual <https://docs.gimp.org/en/>`__
| |b| factory reset
|        ``rm -rv ~/.cache/gimp ~/.config/GIMP``
| |b| focus
|        :menuselection:`Edit --> Preferences --> Image Windows --> Appearance -> Default Appearance in Fullscreen Mode`
|        background
         :raw-html:`<span style="background-color:#FFBF80;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>`
         ``#FFBF80``
| |b| reload
|        :menuselection:`File --> Revert --> Revert`
|        :menuselection:`File --> Open Recent --> garbage.bmp` :guilabel:`Ctrl+1`
| |b| combine
|        :menuselection:`File --> New --> 10000x1536`
|        :menuselection:`Image --> Guides --> New Guide...`
|        :menuselection:`File --> Open as Layers...` :guilabel:`Ctrl+Alt+O`
|        :menuselection:`Tools --> Transform Tools --> Move` :guilabel:`M`
| |b| script-fu
|        :menuselection:`Filters --> Script-Fu --> Console`
|        :menuselection:`Help --> Search and Run a Command` :guilabel:`/`

final product ::

   cd ~/x200 && (
      gcc -std=gnu11 -g -O0 -Wextra -Wall -Winline -Werror=shadow -fanalyzer -o bmp_bin.out bmp_bin.c || exit 1
      echo
      ./bmp_bin.out 0<un1gfn.rom  -h512  1>|un1gfn_512.bmp       &&
      ./bmp_bin.out 0<un1gfn.rom -uh512  1>|un1gfn_512_flip.bmp  &&
      ./bmp_bin.out 0<un1gfn.rom  -h1024 1>|un1gfn_1024.bmp      &&
      ./bmp_bin.out 0<un1gfn.rom -uh1024 1>|un1gfn_1024_flip.bmp &&
      printf "\e[32m%s\e[0m\n" done
      echo
   )


.. _ref_label_imagemagick_bin2bmp_diff:

imagemagick bin2bmp rotate flip compare

.. code::

     +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
     |                            un1gfn                             |
     +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
   >------------------------------#FFBF80------------------------------<
     +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
     |                            reddit                             |
     +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+

:file:`~/x200/magick_diff.sh`


Analyze
=======

strings

::

   # https://stackoverflow.com/questions/5917576/sort-a-text-file-by-line-length-including-spaces
   strings dump.bin \
      | sort \
      | uniq \
      | perl -e 'print sort { length($b) <=> length($a) } <>' \
      | less -SRM +%

::

   meld <(
      strings dump.bin \
         | grep -i -e TCPABIOS -e 7v -e 83
   ) <(
      strings reddit_r_SLASH_libreboot_SLASH_comments_SLASH_o2ygo1...Broccoli-Smooth_4MB.bin \
         | grep -i -e TCPABIOS -e 7x -e 72
   )

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

::

   grep --only-matching --byte-offset --binary -e $'\x88\x88\x88\x88\x87\x88' un1gfn.rom

   grep -F -e $'\x88\x88\x88\x88\x87\x88'    -o -b -U un1gfn.rom
   grep -F -e $'\x88\x88\x88\x88\x87\x88' -c    -b -U un1gfn.rom
   grep -F -e $'\x88\x88\x88\x88\x87\x88' -c       -U un1gfn.rom

   grep -F -e $'\x88\x88\x88\x88\x87\x88'       -b -U un1gfn.rom | hexdump -C
   grep -F -e $'\x88\x88\x88\x88\x87\x88'    -o -b -U un1gfn.rom | hexdump -C
   grep -F -e $'\x88\x88\x88\x88\x87\x88' -c    -b -U un1gfn.rom | hexdump -C
   grep -F -e $'\x88\x88\x88\x88\x87\x88' -c       -U un1gfn.rom | hexdump -C

   grep -F -e $'\x88\x88\x88\x88\x87\x88' -a -o un1gfn.rom | hexdump -C

binwalk ::

   binwalk un1gfn.rom

   for o in $(binwalk -R "\x88\x88\x88\x88\x87\x88" un1gfn.rom | tail -n +4 | head -n -1 | cut -d' ' -f1); do
      echo "$o"
      binwalk -W -o $((o-16)) -l $((48)) un1gfn.rom
   done

   {
      binwalk -R "\xc9\x3a" un1gfn.rom | tail -n +4 | head -n -1 | cut -d' ' -f1 | sed -e 's/$/ L/'
      binwalk -R "\x11\xfb" un1gfn.rom | tail -n +4 | head -n -1 | cut -d' ' -f1 | sed -e 's/$/ R/'
   } | sort -n


   # https://stackoverflow.com/a/47370223/
   tail -c+488488 un1gfn.rom | lzma -d 1>|blob

   dd if=un1gfn.rom skip=488488 bs=1 of=blob.lzma
   tail -c+488488 un1gfn.rom | lzma -d 1>|blob


`EOL`__
=======

.. __: https://download.lenovo.com/eol/index.html

.. table::
   :align: left
   :widths: auto

   ============= =============================================== ===============================================================================================================================
    version       item                                            url
   ============= =============================================== ===============================================================================================================================
    3.22-1.07     BIOS Update Bootable CD (including EC)          :eol:`6duj48us.iso`           461fe63039eb3849ff025d4bcb89b86a3607bf95 |br| :eol:`6duj48uc.txt`
    3.22-1.07     BIOS update utility (including EC)              :eol:`6duj48u6.exe`\ (64-bit) 4d65b53a566ca94dde09f0e5d0fed0fe940215d9 |br| :eol:`6duj48us.exe`\ (32-bit) :eol:`6duj48us.txt`
    4.2.60.1060   Intel AMT 4.2 Management Engine (ME) Firmware   :eol:`7ur6cdww.exe`           :eol:`7ur6cdww.txt`
    4.38          Monitor file (:aw:`ICC profiles`)               :eol:`79oi30ww.exe`           :eol:`79oi30ww.txt`
    4.0.1.1074    Intel Integrated TPM (Trusted Platform Module)  :eol:`7vza13ww.exe`           :eol:`7vza13ww.txt`
   ============= =============================================== ===============================================================================================================================

| get HSH FL1 FL2 with windows
|    1\. install :file:`6duj48u6.exe` to :file:`C:\DRIVERS\FLASH` on any windows machine or VM
|    2\. pack :file:`C:\DRIVERS\FLASH\6duj48u6\` into :file:`C:\DRIVERS\FLASH\6duj48u6.zip`
|    3\. compute sha1 with ``certutil -hashfile 6duj48u6.zip SHA1`` in cmd or powershell
|    4\. via :file:`~/cgi/form.html`, collect sha1
|    5\. via :file:`~/cgi/file.html`, collect :file:`C:\DRIVERS\FLASH\6duj48u6.zip`

| get HSH FL1 FL2 w/o windows
|    1\. :pkg:`AUR/geteltorito`
|    `BIOS_Upgrade#Using_UEFI use geteltorito.pl <https://www.thinkwiki.org/wiki/BIOS_Upgrade#Using_UEFI>`__

::

   geteltorito.pl -o 6duj48us.img 6duj48us.iso
   losetup -l -a
   losetup -l -a
   LP="$(sudo losetup -f --show -L -P -v 6duj48us.img)"
   [[ "$LP" =~ /dev/loop[0-9] ]] && {
      sudo mount -v "$LP"p1 /mnt
      tree -a -h -F --sort=size -C /mnt
   }

::

   ~/x200/magick_diff.sh \
      /mnt/Flash/6DET72WW/\$01B9000.FL1 \
      /mnt/Flash/6DET72WW/\$01B9000.FL2 \
      /mnt/Flash/7XET72WW/\$01B9100.FL1 \
      /mnt/Flash/7XET72WW/\$01B9100.FL2 \
   ;

detatch ::

   sudo losetup -l -a
   sudo losetup -D
   sudo losetup -l -a


ROM
===

un1gfn.rom
----------

.. warning::

   This is a T500/W500 x X200/X200s duct taped  |dumpster_fire|

.. table::
   :align: left
   :widths: auto

   ================================== ============================================== =============================================================
    \                                  BIOS                                           EC
   ================================== ============================================== =============================================================
    un1gfn.rom                         [|alpha|] 7VET83WW\ :sup:`ood`                 [|beta|]  7XHT24WW\ :sup:`ood`
    :eol:`6fuj46uc.txt` (T500/W500)    [|alpha|] 7VET83WW\ :sup:`ood`                 [|epsilon|] 7VHT16WW\ :sup:`latest`
    :eol:`6duj48uc.txt` (X200/X200s)   [|delta|] 6DET72WW/7XET72WW\ :sup:`latest`     [|gamma|] 7XHT25WW\ :sup:`latest` |br| [|beta|]  7XHT24WW\ :sup:`ood`
   ================================== ============================================== =============================================================


:raw-html:`<details><summary>identical dumps (removed)</summary>`

| 20210930-01:49:29.rom
| 20210930-01:51:02.rom
| 20210930-01:52:14.rom
| 20210930-01:54:13.rom
| 20210930-01:55:28.rom
| 20211002-23:40:51.rom
| 20211002-23:41:26.rom
| 20211002-23:42:20.rom
| 20211002-23:42:54.rom

:raw-html:`</details>`

.. table::

   ====================== ======================================================================================================================================
    :command:`md5sum`      ``526a880af8eea59d21b4ff3c0174a737``
    :command:`sha1sum`     ``c6a8af98223b22b6020cdf671af4fac2a834a309``
    :command:`sha224sum`   ``8bcf7a55dda7e670f548b2a0c5fe835f5472606421944980ee8f12ed``
    :command:`sha256sum`   ``a9489a49f0d4e1b5841b0c9c7b08253de2f64903ab3d795496dcfad27002b57d``
    :command:`sha384sum`   ``55c0fa6116711f71925af411a8625573baed789667f6c195a418adbc397d27ad22dca711d29f266b18b46500fac76549``
    :command:`sha512sum`   ``7776a2d4dfe51771e14b0b2475a89d616d850ba5e22cb95eb2d0fe1188e867a422b990645387a30c097b66d2d9ecc38bd3d7b154dbf32a631cc24ff93f8787e6``
    :command:`b2sum`       ``1cd2eaecd0aab60783f69d74b72c8e0d970066a42feb555e73d3017702dd4f14d7dd8c3f6928333c752164117aa3b40d08be45eec1c78ae6ca4828ca29245cfb``
   ====================== ======================================================================================================================================

:raw-html:`<details><summary>full contents of ~/x200/7VET83WW.dmidecode</summary>`

.. literalinclude:: ../x200/7VET83WW.dmidecode

:raw-html:`</details>`

BIOS UI

.. table::
   :align: left
   :widths: auto

   ============================== ======================================
    BIOS Version                   3.13 (7VET83WW)
    BIOS Date                      2010-03-12
    Embedded Controller Version    1.06
    System-unit serial number      745533ALV0039R
    System board serial number     1ZGMD28DFB6
    CPU Type                       Intel(R) Core(TM)2 Duo CPU P8600
    CPU Speed                      2.40GHz
    Installed Memory               8192MB
    UUID                           95e196a0-0b28-11dd-806e-c93a11fb16fb
    MAC Address (Internal LAN)     88 88 88 88 87 88
   ============================== ======================================

:raw-html:`<details><summary>[IMG_0146.JPG] photograph of BIOS UI</summary>`

.. image:: ../x200/IMG_0146.JPG
   :alt: [IMG_0146.JPG]

:raw-html:`</details>`

schemx.rom
----------

`schematic-x <https://schematic-x.blogspot.com/2018/04/bios-download.html>`__ - Lenovo Thinkpad X200.rar

reddit.rom
----------

reddit `comment <https://www.reddit.com/r/libreboot/comments/o2ygo1/comment/hf7r4z1/>`__
by `Broccoli-Smooth <https://www.reddit.com/u/Broccoli-Smooth/>`__

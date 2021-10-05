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

::

   cd ~/x200 && (
      [ 4194304 -eq "$(stat -c %s reddit.rom)" ] || exit

      [ 4194304 -eq "$((8192*512))" ] || exit
      D=/tmp/im
      rm -rf $D
      mkdir $D
      magick convert \( -depth 8 -size 512x8192+0 gray:un1gfn.rom \) -rotate 270       $D/un1gfn.bmp
      magick convert \( -depth 8 -size 512x8192+0 gray:reddit.rom \) -rotate 270 -flip $D/reddit_flip.bmp
      magick convert \(          -size   1x8192+0   xc:#FFBF80    \) -rotate 270       $D/split.bmp
      magick convert -append $D/{un1gfn,split,reddit_flip,diff}.bmp
      printf "\e[32m  %s\e[0m\n" "done"

      [ 4194304 -eq "$((4096*1024))" ] || exit
      # ...

      background gimp $D/diff.bmp

   )

.. include:: include/substitution.txt

================
|ico| `U-Boot`__
================

.. __: https://www.denx.de/wiki/U-Boot

Misc
====

`Title Capitalization Tool <https://capitalizemytitle.com/>`__

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

| misterious article
| `<http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.set.boards/index.html>`__

:el:`u-boot stages <panda how_to_mlo_&_u-boot#introduction>`

u-boot `PKGBUILDs <https://aur.archlinux.org/packages/?O=0&SeB=nd&K=u-boot&outdated=&SB=n&SO=a&PP=50&do_Search=Go>`__

buildroot - `build beaglebone+am335x-evm image <https://git.busybox.net/buildroot/tree/board/beaglebone/readme.txt>`__

| u-boot repo
| |b| `GitHub mirror <https://github.com/u-boot/u-boot>`__ |:zap:|\ |:zap:|\ |:zap:|
| |b| `GitLab repo <https://source.denx.de/u-boot/u-boot>`__ |:snail:|

| u-boot doc
| |b| `read the docs <https://u-boot.readthedocs.io/en/latest/index.html>`__
| |b| `Monitor Commands - Overview <https://github.com/u-boot/u-boot/blob/7a4ff7c41bab8b43767eacc0b30ca1573ab6acb1/README#L3127>`__
| |b| `List of environment variables (most likely not complete) <https://github.com/u-boot/u-boot/blob/7a4ff7c41bab8b43767eacc0b30ca1573ab6acb1/README#L3201>`__
| |b| `NAND <https://github.com/u-boot/u-boot/blob/fa840b09216c6ea728240294b66d2d9ae42c36e1/board/ti/am335x/README#L43>`__
      (copy from SD card to NAND)
| |b| `DULG Introduction <https://www.denx.de/wiki/view/DULG/Introduction>`__\
      /2.3. Availability/\
      `PDF manual <http://www.denx.de/wiki/publish/DULG/DULG-canyonlands.pdf>`__

| ti
| |b| `fork <https://git.ti.com/cgit/ti-u-boot/ti-u-boot>`__ of u-boot
| |b| `U-Boot on AM335x`_
| |b| `AM335x U-Boot User's Guide <https://web.archive.org/web/20210114145232/https://processors.wiki.ti.com/index.php/AM335x_U-Boot_User's_Guide>`__

.. table::
   :align: left
   :widths: auto

   =================================== ================= ================
    File                                `Use Case`__      `Header`__     
   =================================== ================= ================
    u-boot-spl.bin                      peripheral boot   520 bytes      
    :abbr:`MLO (Memory LOader)`\ [#]_                     `MMC loader`__ 
   =================================== ================= ================

.. __: https://e2e.ti.com/support/processors/f/processors-forum/367260/what-is-the-difference-between-mlo-and-spl
.. __: https://stackoverflow.com/a/60880147
.. __: https://stackoverflow.com/a/34805466

.. note::

   | \
     eMMC =
     NAND +
     :wp:`FTL <Flash_translation_layer_(FTL)_and_mapping>`

:yt:`Pentester Academy TV .. Embedded Linux Booting Process (Multi-Stage Bootloaders, Kernel, Filesystem) <DV5S_ZSdK0s>`

`local var space and globalenv var space are separated <https://www.denx.de/wiki/view/DULG/CommandLineParsing#Section_14.2.17.2.>`__

.. code:: text

   => setenv g mmc list
   => run g
   OMAP SD/MMC: 0
   OMAP SD/MMC: 1

.. code:: text

   => l="mmc"
   => $l
   mmc - MMC sub system

   Usage:
   mmc info - display info of the current MMC device
   mmc read addr blk# cnt
   mmc write addr blk# cnt
   mmc erase blk# cnt
   mmc rescan
   mmc part - lists available partition on current mmc device
   mmc dev [dev] [part] - show or set current mmc device [partition]
   mmc list - lists available devices
   mmc wp - power on write protect boot partitions
   mmc setdsr <value> - set DSR register value

   => l="$l list"
   => "$l"
   Unknown command 'mmc list' - try 'help'
   => $l
   OMAP SD/MMC: 0
   OMAP SD/MMC: 1


Get U-Boot
==========

.. https://docs.readthedocs.io/en/stable/guides/cross-referencing-with-sphinx.html
.. _reference_label_u-boot_build_manually:

|alpha|. build Manually [R]_
----------------------------

.. :prlink:`history <https://github.com/u-boot/u-boot/commits/master/configs/am335x_boneblack_vboot_defconfig>\ `\ :pr:`of configs/am335x_boneblack_vboot_defconfig`

.. table::
   :align: left
   :widths: auto

   =============================================== ============= ============= =========
    \                                                             successful?
   ------------------------------------------------------------- -----------------------
    :file:`configs/?`                               `release`__   stage 2       stage 3
   =============================================== ============= ============= =========
    :pr:`am335x_boneblack_vboot_defconfig` [#vb]_   `history`__
    :file:`am335x_evm_defconfig`                    v2021.04      |O|           |O|
    :file:`am335x_evm_defconfig`                    v2021.07      |O|           |O|
   =============================================== ============= ============= =========

.. __: https://github.com/u-boot/u-boot/releases
.. __: https://github.com/u-boot/u-boot/commits/master/configs/am335x_boneblack_vboot_defconfig

.. tip::

   | `contributing <https://archlinuxarm.org/wiki/Contributing>`__
   | send a PR to archlinuxarm/PKGBUILDs/\ `alarm/uboot-beaglebone <https://github.com/archlinuxarm/PKGBUILDs/tree/master/alarm/uboot-beaglebone>`__

| Docs » Build U-Boot » `Building with GCC <https://u-boot.readthedocs.io/en/latest/build/gcc.html>`__
| eLinux - :el:`building for BeagleBone`
| TI - `Create a Network Bootable U-Boot Image <https://web.archive.org/web/https://processors.wiki.ti.com/index.php/Sitara_Linux_Program_the_eMMC_on_Beaglebone_Black#Create_a_Network_Bootable_U-Boot_Image>`__

| :pkg:`AUR/distccd-alarm-armv7h`
| |b| `alarm wiki <https://archlinuxarm.org/wiki/Distcc_Cross-Compiling>`__
| |b| :aw:`ArchWiki <Distcc_Cross-Compiling>`

.. table:: u-boot tarball
   :align: left
   :widths: auto

   =================== ========== =========
    Source              Name       GPG sig
   =================== ========== =========
    `nginx`__            202?.??   |O|
    `GitLab`__          v202?.?? 
    `GitHub mirror`__   v202?.?? 
   =================== ========== =========

.. __: https://ftp.denx.de/pub/u-boot/
.. __: https://source.denx.de/u-boot/u-boot/-/tags
.. __: https://github.com/u-boot/u-boot/tags

get key [#gSR]_ ::

   gpg --search-key --keyserver-options "http-proxy=http://127.0.0.1:8080" 1A3C7F70E08FAB1707809BBF147C39FF9634B72C
   gpg --recv-keys  --keyserver-options "http-proxy=http://127.0.0.1:8080" 1A3C7F70E08FAB1707809BBF147C39FF9634B72C

verify tarball wigh signature [#gV]_ ::

   cd ~/beaglebone
   gpg --verify u-boot-2021.07.tar.bz2{.sig,}

.. _ref_label_already_built_BACKREF:

.. tip::

   If a previous build is available,
   :ref:`jump forth <ref_label_already_built>`\ |:dart:|
   to collect its output instead of building again.

.. warning::

   Previous build will be lost

tools/`genboardscfg.py <https://github.com/u-boot/u-boot/blob/master/tools/genboardscfg.py>`__

::

   cd ~/beaglebone
   rm -rf u-boot-2021.07/
   tar xf ~/beaglebone/u-boot-2021.07.tar.bz2
   cd u-boot-2021.07/

.. tip::

   ::

      tmux attach || tmux

.. warning::

   | Export vars before invoking ``make`` on **any target** in case of broken recipes
   | Vars survive **neither entering nor exiting** tmux

export vars ::

   # In tmux
   if [ -n "$PATH0" -o -n "$CROSS_COMPILE" -o -n "$KBUILD_OUTPUT" ]; then
      printf "\n\e[31m%s\e[0m\n\n" "error"
   else
      PATH0="$PATH"
      export PATH="$PATH:/opt/x-tools7h/arm-unknown-linux-gnueabihf/bin/"; hash -r
      export CROSS_COMPILE="armv7l-unknown-linux-gnueabihf-"
      export KBUILD_OUTPUT="O"
      printf "\n\e[32m%s\e[0m\n\n" "vars exported"
      echo PATH =
      tr ':' '\n' <<<"$PATH"; echo
      echo CROSS_COMPILE = "$CROSS_COMPILE"
      file "$(which "${CROSS_COMPILE}gcc")"
      echo
      echo KBUILD_OUTPUT = "$KBUILD_OUTPUT"; echo
   fi

| :pkg:`core/linux-headers`\ :file:`/usr/lib/modules/$(uname -r)/build/scripts/`
| |b| `diffconfig`__ - compare two .config files
| |b| `config`__ - manipulate options in a .config file

.. __: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/scripts/config
.. __: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/scripts/diffconfig

::

   # In tmux
   # make clean
   # make mrproper
   make distclean
   /usr/lib/modules/*/build/scripts/diffconfig configs/am335x_evm{,_spiboot}_defconfig | sed \
      -e "$(printf 's/^-\(.*\)$/%s- \\1%s/g' $'\e''[31m' $'\e''[0m')" \
      -e "$(printf 's/^+\(.*\)$/%s+ \\1%s/g' $'\e''[32m' $'\e''[0m')" \
      | sort -k 2
   make -j4 am335x_evm_defconfig
   make -s ubootrelease
   make -s ubootversion

:raw-html:`<details><summary>failed <code class="docutils literal notranslate">make pdfdocs</code> attempt</summary>`

| texbin/xelatex
| texlive-core/mktexfmt
| texbin/pdftex
| texlive-latexextra/fncychap.sty
| texlive-langchinese/ctexhook.sty

| `<https://01.org/linuxgraphics/gfx-docs/drm/doc-guide/sphinx.html#sphinx-build>`__
| `<https://www.sphinx-doc.org/en/master/man/sphinx-build.html#cmdoption-sphinx-build-D>`__
| `<https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language>`__

::

   make SPHINXOPTS="-D language=en" pdfdocs

.. code:: text

   Writing index file imx.idx
   No file imx.aux.
   (/usr/share/texmf-dist/tex/latex/base/ts1cmr.fd)
   *geometry* driver: auto-detecting
   *geometry* detected driver: xetex
   (/usr/share/texmf-dist/tex/latex/hyperref/nameref.sty
   (/usr/share/texmf-dist/tex/latex/refcount/refcount.sty)
   (/usr/share/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty))

   Package hyperref Warning: Rerun to get /PageLabels entry.


   Package xeCJK Warning: Unknown CJK family `\CJKsfdefault' is being ignored.
   (xeCJK)
   (xeCJK)                Try to use `\setCJKsansfont[...]{...}' to define it.

   (/usr/share/texmf-dist/tex/latex/amsfonts/umsa.fd)
   (/usr/share/texmf-dist/tex/latex/amsfonts/umsb.fd) [1] [2] [1] [2]
   Chapter 1.

   Underfull \hbox (badness 10000) in paragraph at lines 85--85
   |[][]\TU/DejaVuSans(0)/b/n/14.4 i.MX7D/i.MX8MM SRC_GPR10 PER-

   ! LaTeX Error: Too deeply nested.

   See the LaTeX manual or LaTeX Companion for explanation.
   Type  H <return>  for immediate help.
    ...

   l.181 \begin{itemize}

   ?

:raw-html:`</details>`

Configure
~~~~~~~~~

:raw-html:`<details><summary>ncurses menuconfig</summary>`

menuconfig\ :ltlink:`$MENUCONFIG_COLOR <https://www.kernel.org/doc/html/latest/kbuild/kconfig.html#menuconfig-color>`

::

   make MENUCONFIG_COLOR=mono menuconfig

:raw-html:`</details>`

:raw-html:`<details><summary>gtk2 gconfig</summary>`

:pkg:`AUR/glade-gtk2` or :pkg:`AUR/libglade` ?

::

   make -j4 gconfig

:raw-html:`</details>`

qt5 xconfig

::

   ldd scripts/kconfig/qconf | grep -i qt
      # libQt5Widgets.so.5 => /usr/lib/libQt5Widgets.so.5 (0x00007fb634061000)
      # libQt5Gui.so.5 => /usr/lib/libQt5Gui.so.5 (0x00007fb633987000)
      # libQt5Core.so.5 => /usr/lib/libQt5Core.so.5 (0x00007fb63342e000)
   make -j4 xconfig

**for 2021.07**, apply the following changes by hand

``Boot options -``

.. code:: text

   - Autoboot options - Autoboot - ☐

``Command line interface -``

.. code:: text

     - Memory commands        - sha1sum  - ✓
     - Memory commands        - sha1sum  - sha1sum -v - ✓
     - Device access commands - gpio     - ✓ # Command 'gpio' failed: Error -19
   # - Device access commands - poweroff - ✓ # lib/efi_loader/efi_runtime.c:217: undefined reference to `do_poweroff'

``Environment -``

.. code:: text

   - Environment is not stored          - ✓
   - Environment is in a FAT filesystem - ☐

``Device Drivers - USB support -``

.. code:: text

   # - EHCI HCD (USB 2.0) support - ✓ # asm/arch/ehci.h not found
   #
   # CONFIG_USB_GADGET_VBUS_DRAW undeclared
   # - MUSB host mode support - ☐
   # - MUSB gadget mode support - ☐
   # - Enable TI OTG USB controller - ☐
   # - USB Gadget Support - ☐
   #
   # ASIX
     - USB to Ethernet Controller Drivers - ✓
     - USB to Ethernet Controller Drivers - ASIX AX8817X (USB 2.0) support - ✓
     - USB to Ethernet Controller Drivers - ASIX AX88179 (USB 3.0) support - ✓

| :kbd:`<CTRL+S>` (File - Save)
| :kbd:`<CTRL+Q>` (File - Quit)

build ::

   # In tmux
   # /usr/bin/time --format="\n  wall clock time - %E\n" make -j4 all
     /usr/bin/time --format="\n  wall clock time - %E\n" make -j4 W=1 all

reset vars ::

   # https://stackoverflow.com/a/35322346
   if [ -n "$PATH0" ]; then
      export -n CROSS_COMPILE KBUILD_OUTPUT PATH0
      export PATH="$PATH0"; hash -r
      unset  -v CROSS_COMPILE KBUILD_OUTPUT PATH0
      printf "\n\e[32m%s\e[0m\n\n" "vars reset"
   else
      printf "\n\e[31m%s\e[0m\n\n" "error"
   fi

exit tmux ::

   logout

.. _ref_label_already_built:

| :ref:`jump back<ref_label_already_built_BACKREF>`\ |:dart:|
| check output

::

   cd ~/beaglebone/u-boot-2021.07
   # git check-ignore * | xargs file
   { \
      echo
      file O/* O/spl/* | grep -v -F -e ASCII -e directory
      echo
      find O/ -type f -a \( \
           -iname GARBAGE        \
        -o -iname "*bin"         \
        -o -iname "*dtb"         \
        -o -iname "*img"         \
        -o -iname "*spl"         \
        -o -iname "*spl*bin*"    \
        -o -iname "*spl*dtb*"    \
        -o -iname "*spl*img*"    \
        -o -iname "*u-boot"      \
        -o -iname "*u-boot*bin*" \
        -o -iname "*u-boot*dtb*" \
        -o -iname "*u-boot*img*" \
        -o -iname "mlo*"         \
      \)
      echo
   } | less +X -SRM +%

collect artifacts ::

   TS=(O/{spl/u-boot-spl.bin,MLO,u-boot.img}) &&
   echo && \
      ls -lh ${TS[@]} && echo && \
      rm -rfv /tmp/MINICOM_RES && \
      mkdir -pv /tmp/MINICOM_RES && echo && \
      cp -iv "${TS[@]}" /tmp/MINICOM_RES/ && echo
   unset -v TS

:pr:`β. from ALARM`
-------------------

.. error::

   | With :pkg:`alarm/uboot-beaglebone`\ ``2017.07-1``, sending :file:`emmc.img` (>2Mib), either
   |  |b| right after :file:`u-boot-spl.bin`, or
   |  |b| with\ ``loadx``/\ ``loady``\ when U-Boot is running,
   |  I get NAK at approx. 500K.
   | Anything other than
     :file:`u-boot-spl.bin` (80KiB) and
     :file:`u-boot.img` (400KiB)
     is not realy possible to send.


download :pkg:`alarm/uboot-beaglebone` ::

   pacman -Qqlp uboot-beaglebone-2017.07-1-armv7h.pkg.tar.xz

.. | :manpage:`tar(1)` emits ``tar: Ignoring unknown extended header keyword 'SCHILY.fflags'``
.. | use :manpage:`bsdtar(1)`\ [#]_

extract with :manpage:`bsdtar(1)`
instead of :manpage:`tar(1)`
in case of ``tar: Ignoring unknown extended header keyword 'SCHILY.fflags'``\
[#]_\ ::

   # sha1sum -c ArchLinuxARM-am33x-latest.tar.gz.sha1sum
   # tar -x -v --no-xattrs --strip-components 1 -f ArchLinuxARM-am33x-latest.tar.gz "./boot"
   rm -rfv /tmp/MINICOM_RES
   mkdir -pv /tmp/MINICOM_RES
   bsdtar -x \
      -C "/tmp/MINICOM_RES" \
      -f uboot-beaglebone-2017.07-1-armv7h.pkg.tar.xz \
      --no-xattrs \
      --strip-components 1 \
      -v
   # tar -x \
   #    -v \
   #    --no-xattrs \
   #    --strip-components 1 \
   #    -f uboot-beaglebone-2017.07-1-armv7h.pkg.tar.xz \
   #    -C "/tmp/MINICOM_RES"

``MLO``
|rarr| `strip 520-byte header <https://e2e.ti.com/support/processors/f/processors-forum/321500/serial-boot-on-am3359-mlo-does-not-give-prompt>`__ |rarr|
u-boot-spl.bin ::

   # dd if=MLO of=u-boot-spl.bin bs=1 skip=520
   { [ -f /tmp/MINICOM_RES/u-boot-spl.bin ] && echo error; } \
      || tail -c +521 /tmp/MINICOM_RES/MLO >/tmp/MINICOM_RES/u-boot-spl.bin
   diff -u10 \
      <(xxd -c 8 -u /tmp/MINICOM_RES/MLO            | cut -d':' -f2-) \
      <(xxd -c 8 -u /tmp/MINICOM_RES/u-boot-spl.bin | cut -d':' -f2-)

|gamma|. build w/ buildroot
---------------------------

| bump :pkg:`AUR/buildroot-meta` according to latest `requirements <https://buildroot.org/downloads/manual/manual.html>`__
| install :pkg:`AUR/buildroot-meta`

| `download <https://buildroot.org/download.html>`__ buildroot
| it builds u-boot version ``boot/uboot/Config.in:BR2_TARGET_UBOOT_VERSION``
  (`git <https://git.busybox.net/buildroot/tree/boot/uboot/Config.in>`__)

get key  [#gSR]_ ::

   gpg --search-key --keyserver-options "http-proxy=http://127.0.0.1:8080" AB07D806D2CE741FB886EE50B025BA8B59C36319
   gpg --recv-keys  --keyserver-options "http-proxy=http://127.0.0.1:8080" AB07D806D2CE741FB886EE50B025BA8B59C36319

verify clear signed message of checksum [#gV]_ ::

   gpg --verify buildroot-202?.??.?.tar.bz2.sign

verify tarball with checksum ::

   grep tar buildroot-202?.??.?.tar.bz2.sign
   md5sum buildroot-202?.??.?.tar.bz2
   sha1sum buildroot-202?.??.?.tar.bz2

| configure buildroot
| |b| `01 = little endian <https://serverfault.com/a/749469>`__
| |b| NEON\ |tm| `SIMD Coprocessor <https://www.ti.com/document-viewer/AM3358/datasheet/features-sprs7179524#sprs7179524>`__
| |b| NEON\ |:tm:| `SIMD Coprocessor <https://www.ti.com/document-viewer/AM3358/datasheet/features-sprs7179524#sprs7179524>`__

::

   $ hexdump -s 5 -n 1 -C ~/beaglebone/ArchLinuxARM_boot/initramfs-linux/bin/busybox
   00000005  01                                                |.|
   00000006

::

   Target options
      Target Architecture = ARM (little endian)
      Target Architecture Variant = cortex-A8
      Target ABI = EABIhf
      Floating point strategy = NEON
      ...

\... (incomplete)

Make eMMC image
===============

.. table:: :wp:`Design_of_the_FAT_file_system#Size_limits`
   :align: left
   :widths: auto

   ============================== =================  ==============
    Number of table element bits   Minimum size       Applicable?
   ============================== =================  ==============
    FAT12                          |asymp|\ 0.5B      |O|
    FAT16                          |asymp|\ 1MiB      |:question:|
    FAT32                          |asymp|\ 32MiB     |:x:|
   ============================== =================  ==============

|alpha|. with `genimage`__ [R]_
-------------------------------

.. __: https://github.com/pengutronix/genimage

`genimage <https://git.busybox.net/buildroot/tree/package/genimage>`__\
:superscript:`buildroot`

.. warning::

   | Use :pkg:`AUR/genimage-git` instead of genimage\ :superscript:`AUR`
     to avoid :pkg:`extra/mtools` :manpage:`mcopy(1)` bugs
   | |b| `issues/71 <https://github.com/pengutronix/genimage/issues/71>`__
   | |b| `pull/151 <https://github.com/pengutronix/genimage/pull/151>`__
   | |b| `pull/73 <https://github.com/pengutronix/genimage/pull/73>`__

.. warning::

   | Generated image is **not** ``2MiB``
   | It is **slightly more than** ``2MiB``

genimage.cfg `syntax <https://github.com/pengutronix/genimage/blob/master/README.rst>`__

::

   cd ~/beaglebone
   rm -rfv /tmp/genimage*
   # mkdir -pv /tmp/genimage_emptydir
   # Don't put u-boot-spl.bin here!
   f=(MLO u-boot.img)
   # For preserve of timestamps, in "image fat.partimg", use "mountpoint=" instead of "vfat{}"
   # for i in $f; do touch -c -d "1989-06-04T00:00:00" "/tmp/MINICOM_RES/$f"; done
   ./cfg.sh ${f[@]}
   python3 -m pygments -l cfg /tmp/genimage.cfg

.. https://stackoverflow.com/a/60394068
.. raw:: html

   <details><summary>What's in <code>cfg.sh</code>?</summary>

.. https://pygments.org/docs/lexers/#pygments.lexers.configs.IniLexer
.. https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-literalinclude
.. literalinclude:: ../beaglebone/cfg.sh
   :language: cfg
   :lines: 2-

:raw-html:`</details>`

`genimage is intended to be run in a fakeroot environment <https://github.com/pengutronix/genimage#genimage---the-image-creation-tool>`__

::

   # "+X" and it won't get stuck at the bottom of the screen
   fakeroot genimage --config /tmp/genimage.cfg |& less +X -S

| inspect
| |b|
  `mdir(1) <https://www.gnu.org/software/mtools/manual/mtools.html#mdir>`__
  :ltlink:`-i <https://www.gnu.org/software/mtools/manual/mtools.html#Drive-letters>`

::

   echo; sfdisk -Vl /tmp/genimage_outputpath/emmc.img
   echo; mdir -i /tmp/genimage_outputpath/fat.partimg

.. code:: text

   ... Boot   Start ... Size Id Type
   ... *    (not 1) ...   2M  1 FAT12
   No errors detected.


collect artifacts ::

   echo && \
      ls -Alh /tmp/MINICOM_RES && echo
      rm -fv /tmp/MINICOM_RES/emmc.img && \
         cp -iv /tmp/genimage_outputpath/emmc.img "$_" && echo && \
      ls -Alh /tmp/MINICOM_RES/ && echo

|alpha|. manually
-----------------

| :aw:`Partitioning#Tools`
| |b| :manpage:`sfdisk(8)` [#]_ [#]_
| |b| :manpage:`parted(8)` [#]_

| create empty image
| ``1MiB = 1024 * 1024B = 1048576B``

::

   # truncate -s 1048576 /tmp/emmc.img # Does not wipe existing content
   head -c 1048576 /dev/zero >/tmp/emmc.img
   if [ "$(sha1sum <emmc.img)" = '3b71f43ff30f4b15b5cd85dd9e95ebc7e84eb5a3  -' ]; then
      echo -e "\n\e[32mok   \e[0m\n"
   else
      echo -e "\n\e[31merror\e[0m\n"
   fi

partition (sfdisk)

::

   WRITE="/bin/sfdisk --color=always --lock -X dos -w always -W always"
   $WRITE           emmc.img <<<',,FAT12,*'
   $WRITE --disk-id emmc.img 0x19890604
   unset -v WRITE

   if [ "$(sha1sum <emmc.img)" = '868998a0e79a979da6f4a09ec44da7c44b0b1893  -' ]; then
      echo -e "\n\e[32mok   \e[0m\n"
   else
      echo -e "\n\e[31merror\e[0m\n"
   fi

   sfdisk --color=always    -d emmc.img; echo
   sfdisk --color=always    -g emmc.img; echo
   sfdisk --color=always    -J emmc.img; echo
   sfdisk --color=always -V -l emmc.img; echo
   sfdisk --color=always    -F emmc.img; echo

   # $WRITE        -N 1 emmc.img <<<'help'
   # $WRITE          -A emmc.img 1
   # $WRITE --part-type emmc.img 1 FAT12 # sfdisk -T | grep -i -e fat -e dos -e bios -e win -e w9

.. include:: include/escalate.txt

loop device
(`kpartx? <https://unix.stackexchange.com/questions/94103/how-can-i-partition-a-volume-in-a-regular-file-without-loop>`__)

::

   losetup -l -a
   losetup -f --show -L -P -v emmc.img
   losetup -l -a
   fdisk -l /dev/loop0

format ::

   lsblk -f
   mkfs.fat -F 12 -v /dev/loop0p1

write::

   mkdir  /tmp/mnt
   mount -v /dev/loop0p1 /tmp/mnt
   cp -v ~/MLO /tmp/mnt
   sync
   cp -v ~/u-boot.img /tmp/mnt
   sync
   umount -v /tmp/mnt
   rmdir -v /tmp/mnt

cleanup::

   losetup -l -a
   losetup -D
   losetup -l -a
   mv -v emmc.img ~/

.. _reference_label_section_connect_serial:

Connect Serial
==============

.. warning::

   | Don't supply any power to BBGW yet.
   | Don't connect PL2303 USB-A to PC yet.

:el:`BB Serial Debug Port <BeagleBone/Serial_Port>`

`The acme of foolishness <https://dave.cheney.net/2013/09/22/two-point-five-ways-to-access-the-serial-console-on-your-beaglebone-black>`__

.. code:: text

   the red wire, this carries +5v from the USB port and can blow the arse out of your BBB
   you must leave it unconnected
   Do not connect the red lead to anything!

:el:`eLinux <Beagleboard:BeagleBone_Black_Serial>`

.. code:: text

   an extra RED wire on this cable that supplies 5V @ 500mA
   which could power the board if connected to one of the VDD_5V pins (P9_05, P9_06)
   Just leave it unconnected.

.. https://docutils.sourceforge.io/docs/ref/rst/directives.html#table
.. table:: pinout
   :align: left
   :widths: auto

   ======== ================== ==== ==== ===== ================== ====
    \        1                  2    3    4     5                  6
   ======== ================== ==== ==== ===== ================== ====
    BBGW     GND                NC   NC   RX    TX                 NC
    PL2303   |:black_circle:|   NC   NC   |O|   |:white_circle:|   NC
   ======== ================== ==== ==== ===== ================== ====

1. Double check the pinout
2. Connect PL2303 USB-A to PC
3. .. code:: shell-session

      $ lsusb | grep -i pl
      Bus * Device *: ID 067b:2303 Prolific Technology, Inc. PL2303 Serial Port / Mobile Action MA-8910P

`067b:2303 <https://linux-hardware.org/?id=usb:067b-2303>`__


Send U-Boot
===========

.. warning::

   Don't supply any power to BBGW yet.

| :pkg:`community/python-pyserial` - `pypi`__ - `doc`__
| `xmodem`__ - `pypi`__ - `doc`__

.. __: https://pypi.org/project/pyserial
.. __: https://pythonhosted.org/pyserial

.. __: https://github.com/tehmaze/xmodem
.. __: https://pypi.org/project/xmodem
.. __: https://pythonhosted.org/xmodem

`SystemSetup <http://www.denx.de/wiki/view/DULG/SystemSetup>`__ < DULG < DENX

lists.denx.de - `minicom+kermit <https://lists.denx.de/pipermail/u-boot/2003-June/001527.html>`__

:aw:`Working_with_the_serial_console`

:el:`Beagleboard:BeagleBone_Black_Accessories#Serial_Debug_Cables`

.. https://docutils.sourceforge.io/docs/ref/rst/directives.html#table
.. table::
   :align: left
   :widths: auto

   =========== ========
    Baud        115200
    Bits        8
    Parity      N
    Stop Bits   1
    Handshake   None
   =========== ========

:yt:`Fastbit Embedded Brain Academy .. Beaglebone Black Serial booting procedure ( UART BOOT ) <3y1LMNPoaJI>`

.. warning::
   Make sure :pkg:`community/lrzsz` is installed.

.. include:: include/escalate.txt

convenience symlink for minicom ::

   sudo rm -rfv /root/MINICOM_RES
   sudo ln -sv "/tmp/MINICOM_RES" /root/MINICOM_RES

| run minicom
| |b| :ltlink:`busybox microcom <https://www.busybox.net/downloads/BusyBox.html#microcom>`?
| `stty cols/rows <https://unix.stackexchange.com/q/473599/>`__
| `tput cols/lines <https://stackoverflow.com/q/263890/>`__

::

   # --metakey
   minicom \
      -w \
      -c on \
      -b 115200 \
      -D /dev/ttyUSB0 \
      -8

.. code:: text

   <RESET>

   <POWER>

   USBUSB    AM3358     RAM

   USBUSB             *<USER>*
             SERIAL

1. Press down :kbd:`USER`
2. Keep holding :kbd:`USER`,
   supply 5v :stlink:`?A <https://electronics.stackexchange.com/questions/563406/which-wall-charger-for-beaglebone-green-wireless>`
   power through Micro USB
3. Keep holding :kbd:`USER`,
   wait for 5 seconds
4. Release :kbd:`USER`

Wait for at most 30 seconds until ``CCC...`` appears in minicom console

.. warning::

   | Use :file:`u-boot-spl.bin`
   | Don't use :file:`MLO`, which is for booting from eMMC

1. :kbd:`<CTRL+A>` |rarr| :kbd:`<S>` |rarr|    xmodem |rarr| ``[MINICOM_RES]/`` |rarr| ``u-boot-spl.bin``

.. code:: text

   U-Boot SPL 2017.07-1 (Sep 02 2017 - 21:04:29)
   Trying to boot from UART

.. tip::

   | Don't miss the chance to
   | ``Press SPACE to abort autoboot in 2 seconds``

2. :kbd:`<CTRL+A>` |rarr| :kbd:`<S>` |rarr| ymodem |rarr| ``[MINICOM_RES]/`` |rarr| ``u-boot.img``

.. code-block:: text
   :emphasize-lines: 13

   CRC mode, 8852(SOH)/0(STX)/0(CAN) packets, 4 retries
   Loaded 1132684 bytes


   U-Boot 2021.07 (Aug 07 2021 - 13:40:18 +0800)

   CPU  : AM335X-GP rev 2.1
   Model: TI AM335x BeagleBone Black
   DRAM:  512 MiB
   WDT:   Started with servicing (60s timeout)
   NAND:  0 MiB
   MMC:   OMAP SD/MMC: 0, OMAP SD/MMC: 1
   Loading Environment from nowhere... OK
   <ethaddr> not set. Validating first E-fuse MAC
   Net:   Could not get PHY for ethernet@4a100000: addr 0
   eth2: ethernet@4a100000, eth3: usb_ether

.. code:: text

   version
      # U-Boot 2021.07 (Aug 07 2021 - 13:40:18 +0800)

      # armv7l-unknown-linux-gnueabihf-gcc (crosstool-NG 1.23.0.418-d590) 10.2.0
      # GNU ld (crosstool-NG 1.23.0.418-d590) 2.35

.. code:: text

   printenv serial#
      # ...

.. code:: text

   coninfo
      List of available devices:
      serial@0 00000007 IO stdin stdout stderr
      serial   00000003 IO

:raw-html:`<details><summary>bdinfo</summary>`

.. literalinclude:: ../beaglebone/bdinfo.txt
   :language: text

:raw-html:`</details>`

:raw-html:`<details><summary>printenv</summary>`

.. https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-literalinclude
.. literalinclude cannot reach outside doc tree
.. literalinclude:: ../beaglebone/printenv.txt
   :language: text

:raw-html:`</details>`

Send & Write eMMC
=================

verify 512B-alignment of eMMC image in another terminal

::

   # Spawn a new terminal
   echo
   n_bytes_dec="$(wc -c </tmp/MINICOM_RES/emmc.img)"
   rem="$((n_bytes_dec%512))"
   n_blocks_dec="$((n_bytes_dec/512))"
   n_blocks_hex="$(printf "%x" "$n_blocks_dec")"
   sha1sum="$(sha1sum /tmp/MINICOM_RES/emmc.img|cut -d' ' -f1)"
   if [ "$rem" -eq 0 ]
   then printf "\n  \e[32m[%s]\e[0m %sB = %s(0x%s) * 512B + \e[32m%sB\e[0m\n\n" ok    "$n_bytes_dec" "$n_blocks_dec" "$n_blocks_hex" "$rem"
   else printf "\n  \e[31m[%s]\e[0m %sB = %s(0x%s) * 512B + \e[31m%sB\e[0m\n\n" error "$n_bytes_dec" "$n_blocks_dec" "$n_blocks_hex" "$rem"
   fi
   printf '  %s = %s\n\n'        '$sha1sum'        "$sha1sum"
   printf '  %s = %s\n\n' '0x$n_blocks_hex' "0x$n_blocks_hex"
   printf '  %s = %s\n\n'   '$n_blocks_dec'   "$n_blocks_dec"
   unset -v n_bytes_dec
   unset -v rem
   echo
   # Don't close this terminal

| make sure eMMC block size is ``512B``
| |b| `mmc <https://www.denx.de/wiki/view/DULG/UBootCmdGroupMMC>`__

.. code:: text

   mmc list
      # OMAP SD/MMC: 0
      # OMAP SD/MMC: 1

.. code:: text

   mmc dev 1
      # switch to partitions #0, OK
      # mmc1(part 0) is current device

.. https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-option-code-block-emphasize-lines
.. code-block:: text
   :emphasize-lines: 8

   mmc info
      # Device: OMAP SD/MMC
      # Manufacturer ID: 13
      # OEM: 14e
      # Name: Q2J54
      # Bus Speed: 48000000
      # Mode: MMC High Speed (52MHz)
      # Rd Block Len: 512
      # MMC version 5.0
      # High Capacity: Yes
      # Capacity: 3.6 GiB
      # Bus Width: 8-bit
      # Erase Group Size: 512 KiB
      # User Capacity: 3.6 GiB WRREL
      # Boot Capacity: 2 MiB ENH
      # RPMB Capacity: 512 KiB ENH
      # Boot area 0 is not write protected
      # Boot area 1 is not write protected

.. code:: text

   mmc part
      # ## Unknown partition table type 0

.. tip::
   | Make sure eMMC block size is ``512B``
   | ``0x5000blk * 512B/blk = 20480blk * 512B/blk`` (=10485760B=10*1024*1024B=\ **10MiB**\ )
   | Therefore the following are equivalent
   | |b| ``mmc erase 0 0x5000``
   | |b| ``dd if=/dev/zero of=/dev/mmcblk0 bs=512 count=20480``

erase the first 10MiB from eMMC

.. code:: text

   mmc erase 0 0x5000
      #
      # MMC erase: dev # 1, block # 0, count 20480 ... 20480 blocks erased: OK
   mmc rescan
   mmc part
      # ## Unknown partition table type 0

.. tip::

   | Why ``0x82000000``?
   | |b| ``bdinfo`` gives ``DRAM bank ... start = 0x80000000``
   | |b| ``printenv`` gives ``kernel_addr_r=0x82000000`` and ``loadaddr=0x82000000``
   |     |b| defined in include/configs/`ti_armv7_common.h`__
   |     |b| `propagated`__ in include/configs/`am335x_evm.h`__ ?
   |     |b| `u-boot relocation on ARM architecture`__

.. __: https://github.com/u-boot/u-boot/blob/master/include/configs/ti_armv7_common.h
.. __: https://stackoverflow.com/a/9113058
.. __: https://github.com/u-boot/u-boot/blob/master/include/configs/am335x_evm.h
.. __: https://stackoverflow.com/a/35348068

.. code:: text

   if test ${loadaddr} -eq 0x82000000; then echo ok; else echo err; fi

.. tip::
   | |b| RAM block size is ``1B``
   | |b| ``0xa00000blk * 1B/blk = 0xa00000B = 10485760B = 10240 * 1024B = 10MiB``
   | |b| :pr:`An all-zero chunk starts from 0x100000`
   | |b| :pr:`RAM address starts from 0x82000000`

| zerofill ``10MiB`` RAM
| |b| ``cmp.b addr1 addr2 count`` - `compare`__ byte
| |b| ``mw.b address value [count]`` - `memory write (fill)`__ byte

.. __: https://www.denx.de/wiki/view/DULG/UBootCmdGroupMemory#Section_5.9.2.3.
.. __: https://www.denx.de/wiki/view/DULG/UBootCmdGroupMemory#Section_5.9.2.8.

.. code:: text

   # Error prone, don't try accessing 0x100000 any more
   # cmp.b ${loadaddr}  0x100000 0xa00000
      mw.b ${loadaddr}         0 0xa00000

get ready for ``ymodem`` transfer

.. code:: text

   if test ${baudrate} -eq 115200; then
      echo ok
      loady ${loadaddr} ${baudrate}
   else
      echo err
   fi

minicom |rarr| :kbd:`<CTRL+A>` |rarr| :kbd:`<S>` |rarr| ymodem |rarr| ``[MINICOM_RES]/`` |rarr| ``emmc.img``

.. code-block:: text

   ## Ready for binary (ymodem) download to 0x82000000 at 115200 bps...
   CRC mode, ...(SOH)/0(STX)/0(CAN) packets, * retries
   ## Total Size      = 0x... = ... Bytes

| md.b - memory display byte
| |:eyes:| expect 512 bytes with some boot code and an MBR partition table near the end

.. code:: text

   md.b ${loadaddr} 0x200

| verify checksum [#]_
| |:eyes:| expect ``<SHA1SUM>`` to be the same value as ``$sha1sum``


.. code:: text

   sha1sum ${loadaddr} ${filesize}
      # sha1 for ... ... ... ==> <SHA1SUM>

| dump eMMC image from RAM to eMMC
  - `mmc <https://www.denx.de/wiki/view/DULG/UBootCmdGroupMMC>`__
| |:pencil2:| replace ``<N_BLOCKS_HEX>`` with ``0x$n_blocks_hex`` - |:warning:| add ``0x`` prefix
| |:eyes:|    expect ``<N_BLOCKS_DEC>`` to be the same value as ``$n_blocks_dec``

.. code-block:: text
   :emphasize-lines: 5,6

   mmc list
   mmc dev 1
   mmc info
   mmc part
   mmc write ${loadaddr} 0 <N_BLOCKS_HEX>
      MMC write: dev # 1, block # 0, count <N_BLOCKS_DEC> ... <N_BLOCKS_DEC> blocks written: OK

verify partition layout

.. code:: text

   mmc part
   mmc rescan
   mmc part

.. warning::

   There should be **no** ``u-boot-spl.bin`` here

inspect installed ``MLO`` and ``u-boot.img``

.. code:: text

   fatls mmc 1:1 /

Power Off
=========

.. warning::

   Exit & reset minicom before unplugging PL2303!

1. :kbd:`<CTRL-A><X>` eXit and reset minicom
2. Unplug PL2303 USB-A from PC
3. Press down :kbd:`POWER` button
4. Hold :kbd:`POWER` button for approx. 8s until LED ``PWR`` goes off, then
   `release POWER button immediately <https://github.com/beagleboard/beaglebone-black/wiki/System-Reference-Manual#power-button>`__

::

   lsusb | grep -i pl

if stray ``PL2303`` is still there ::

   eval "$(head -1 usbreset.c | cut -d'/' -f3-)"
   ./usbreset.out /dev/bus/usb/...
   lsusb | grep -i pl

Footnotes
=========

.. [R]    Recommended

.. [#] MLO = **M**\ MC **lo**\ ader
.. [#] http://lifeonubuntu.com/tar-errors-ignoring-unknown-extended-header-keyword/
.. [#vb] `no need for verified boot, use configs/am335x_evm_defconfig instead <https://lists.denx.de/pipermail/u-boot/2021-May/449518.html>`__
.. [#gSR] :aw:`GnuPG#Searching_and_receiving_keys`
.. [#gV]  :aw:`GnuPG#Verify_a_signature`

.. [#]  https://superuser.com/questions/332252/how-to-create-and-format-a-partition-using-a-bash-script
.. [#]  https://www.thegeekstuff.com/2017/05/sfdisk-examples/
.. [#]  https://unix.stackexchange.com/questions/53378/how-can-i-script-the-creation-of-a-single-partition-that-uses-the-entire-device

.. [#] `sh1sum.c <https://github.com/u-boot/u-boot/blob/master/cmd/sha1sum.c>`__:\
       ``do_sha1sum`` |larr|
       `hash.c <https://github.com/u-boot/u-boot/blob/master/common/hash.c>`__:\
       ``hash_command()``

.. include:: include/link.txt

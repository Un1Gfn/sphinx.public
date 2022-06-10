.. include:: include/substitution.txt

===
iOS
===

Downgrade
=========

| sysupgrade ``pacman -Fy; pacman -Syuu``
| force remove packages ``pacman -Rd``
| install git packages with paru
| depcheck ``pacman -Dk``

:r:`[Tutorial] downgrade from Ios 15 to 14.3 for A11 devices <jailbreak/comments/qri8w0/>`

`How to downgrade from iOS 15 to iOS 14 <https://gist.github.com/nyuszika7h/aac55c97f7925cddcf5ec3167f85dfe8>`__

`Restoring with blobs using FutureRestore <https://ios.cfw.guide/futurerestore/>`__

::

   function L_apple {
      P=('|  '
         ' \ '
         '  |'
         ' / ')
      N="${#P[@]}"
      for ((i=0;1;i++)); do
         sleep 0.3
         echo "${P[i%N]} $(lsusb | grep -i apple)"
      done
   }

| :tiw:`Enter DFU mode - A9 and older devices <DFU_Mode#A9_and_older_devices_.28iPad_other_than_the_ones_listed_below.2C_iPhone_6s_and_below.2C_iPhone_SE_and_iPod_touch_6_and_below.29>`
|    connect iPad
|    unlock iPad
|    run ``L``
|       *L() shows* ``05ac:12ab Apple, Inc. iPad 4/Mini1``
|          press & hold :guilabel:`Home`\ +\ :guilabel:`Lock`
|       *L() stops*
|          release :guilabel:`Lock` but keep holding :guilabel:`Home`
|       *L() shows* ``05ac:1227 Apple, Inc. Mobile Device (DFU Mode)``
|          release :guilabel:`Home`

.. tip::

   DFU times out in |asymp|\ 50 seconds then boots to SpringBoard

\... (set nounce, futurerestore) ...

| force remove git packages ``pacman -Rd``
| put non-git packages back ``pacman -S --needed --asdeps``
| depcheck again ``pacman -Dk``


Misc
====

todo: move everything from `Un1Gfn-obj/ios <https://github.com/Un1Gfn-obj/ios>`__

https://github.com/Cryptiiiic/ipwndfu/archive/A11-patch-rom.tar.gz

:aw:`archwiki <iOS>`

:yt:`[RESQ] MASTERWORK - iPHONE 6 RAM REPLACEMENT - HOW TO REPLACE THE A8 RAM - TUTORIAL <fOi1qMBMllE>`

AirPlay
|vv| :pkg:`AUR/uxplay`
|vv| :pkg:`AUR/rpiplay-git`

:pkg:`AUR/tsschecker-git`

:pkg:`AUR/futurerestore-git`


Backup
======

back up these things before erasing a device

`google authenticator <https://apps.apple.com/us/app/google-authenticator/id388497605>`__
:menuselection:`... --> Export accounts`



`checkra1n`__
=============

.. __: https://checkra.in/

.. tip::

   Perform an idevicepair if checkra1n cannot put j96ap to recovery mode

checksum ::

   cd ~/ios
   sha256sum -c - <<EOS
   63282886157dd08079c8e41522fdc6d58cfecda783ea8cca79ffc1116f13c355  ./checkra1n_0.12.1
   4bf2f7e1dd201eda7d6220350db666f507d6f70e07845b772926083a8a96cd2b  ./checkra1n_0.12.2
   845bd19fb857e5546ba312e768ab42e8aeab7a34470b07f60a9892e92fe8273e  ./checkra1n_0.12.3
   dac9968939ea6e6bfbdedeb41d7e2579c4711dc2c5083f91dced66ca397dc51d  ./checkra1n_0.12.4
   EOS

.. table::
   :align: left
   :widths: auto

   =========== ============================================================== ==========================================================================================
    checkra1n   :tiw:`J96AP`                                                   :tiw:`D20AP`                                                                             
   =========== ============================================================== ==========================================================================================
    0.12.1                                                                     |:green_circle:|                                                                         
    0.12.2                                                                     |:x:|\ |br|:file:`Error getting passcode state (parsing error)`                          
    0.12.3                                                                     |:x:|\ |br|:file:`Sorry, iPhone 8 (Global) is not supported on iOS 14.4.2 at this point` 
    0.12.4      |:green_circle:|\ |br|:file:`USBMUX Error (Error code: -92)`   |:x:|\ |br|:file:`Sorry, iPhone 8 (Global) is not supported on iOS 14.4.2 at this point` 
   =========== ============================================================== ==========================================================================================


ideviceinfo
===========

`gist <https://gist.github.com/adamawolf/3048717>`__ | theiphonewiki
- :tiw:`models`
- :tiw:`list of iPads`
- :tiw:`list of iPhones`

:raw-html:`<details><summary><code>D20AP</code></summary>`

.. literalinclude:: ../ios/ideviceinfo_D20AP
   :language: text

:raw-html:`</details>`

:raw-html:`<details><summary><code>J96AP</code></summary>`

.. literalinclude:: ../ios/ideviceinfo_J96AP
   :language: text

:raw-html:`</details>`


`ifuse`__
=========

.. __: https://github.com/libimobiledevice/ifuse

| unlock idevice screen
| com.apple.Preferences
  |rarr| Display & Brightness
  |rarr| ``Auto-Lock = Never``

.. include:: include/escalate.txt

attach/connect device to pc ::

   echo
   export SYSTEMD_LOG_COLOR=1 SYSTEMD_PAGER="" SYSTEMD_COLORS=1
   env  journalctl --no-pager -b -u usbmuxd.service
   echo
   systemctl status --no-pager usbmuxd.service
   echo
   lsusb | grep --color=never -i ap
   echo

pair ::

   idevicepair pair

::

   idevicepair pair
   idevicepair validate # Works as a handy command to get UDID!
   idevicepair list

| :aw:`file manager functionality#Mounting`
| :aw:`file manager functionality#Apple_access`

:pkg:`extra/thunar`
(:pkg:`extra/nautilus`)
:pkg:`extra/gvfs-afc`
:pkg:`extra/gvfs-gphoto2`

mount ::

   install -d -gdarren -m755 -odarren -v ~darren/mnt
   if [ -z "$(ls -A ~darren/mnt)" ]; then
      # ifuse -o allow_other,ro --root ~darren/mnt # JB required
        ifuse -o allow_other,ro ~darren/mnt
        findmnt ~darren/mnt
   else
      printf "\n\e[31m  %s\e[0m\n\n" "err"
   fi

.. warning::

   ``umount -v ~darren/mnt`` before detatching!

:file:`~/mnt/Downloads` is in fact :file:`/private/var/mobile/Media/Downloads`

:aw:`iOS#Importing_videos_and_pictures`

.. warning::

   If you remove media from :file:`/DCIM/100APPLE`,
   :aw:`trigger a rebuild of the "Camera Roll" database <iOS#Importing_pictures_and_deleting_them>` afterwards

drop privileges ::

   logout

locate media paths ::

   # exa -aT --sort=extension ~darren/mnt
   echo
   find ~darren/mnt -iname PLACEHOLDER_BEGIN \
      -o -iname 'img*' \
      -o -iname '*heic' \
      -o -iname '*jpg' \
      -o -iname '*m4a' \
      -o -iname '*mov' \
      -o -iname '*png' \
      -o -iname '*thm' \
      -o -iname '*tiff' \
      -o -iname '*webp' \
      -o -iname PLACEHOLDER_END \
      | pv -ptrl >/tmp/find.log
   echo

| paths related to media
|  :file:`~darren/mnt/Recordings`
|  :file:`~darren/mnt/DCIM/*`
|  :file:`~darren/mnt/PhotoData/Metadata/DCIM/*`
|  :file:`~darren/mnt/PhotoData/Mutations/DCIM/*`
|  :file:`~darren/mnt/PhotoData/Thumbnails/V2/DCIM/*`

harvest media ::

   background pcmanfm ~darren/mnt/DCIM/

unmount ::

   umount -v ~darren/mnt

detatch idevice


HEIC/:wp:`HEIF <High_Efficiency_Image_File_Format>`
===================================================

.. warning::

   | file manager :aw:`thumbmnail <file manager functionality#Thumbnail_previews>`
   | :pkg:`community/pcmanfm` can thumbnail heif/heic but it eats RAM |:warning:|
   | :pkg:`extra/nautilus` uses a resonable amount of :file:`buff/cache` |:green_circle:|
   | ``exa -alT ~/{,.cache/}thumbnails/ --sort=time --time-style=long-iso``

based on :wp:`HEVC <High_Efficiency_Video_Coding>` (H.265) (MPEG-H Part 2)

:aw:`archwiki <codecs and containers#Image_codecs>`

| decode
| |b| `nokiatech/heif <https://github.com/nokiatech/heif>`__
| |b| :prlink:`pushd/heif <https://github.com/pushd/heif>`
| |b| :pkg:`extra/imlib2` |rarr| :pkg:`AUR/imlib2-heic` |rarr| :pkg:`extra/feh`
| |b| :pkg:`extra/libde265` |rarr| :pkg:`extra/libheif` |rarr|
|                                                             |b| :pkg:`extra/gimp`
|                                                             |b| :pkg:`extra/imagemagick`
|                                                             |b| :pkg:`extra/gdk-pixbuf2` |rarr| :pkg:`extra/eog`

| view
| |b| :manpage:`display(1)`
| |b| :pkg:`extra/eog`
| |b| :pkg:`extra/gimp`

| convert
| |b| :manpage:`convert(1)`
| |b| :manpage:`ffmpeg(1)`
| |b| :manpage:`heif-info(1)` :manpage:`heif-convert(1)`
| |b| :pkg:`AUR/tifig-git` :pkg:`AUR/tifig-bin` :pr:`AUR/tifig`


YouTube
=======

`RebornAgain <https://altcatalog.meghrathod.tech/>`__

version
- :r:`1.5   <sideloaded/comments/p9ml5f/>`
- :r:`1.6.1 <sideloaded/comments/pfgxpd/>`
- :r:`1.7   <sideloaded/comments/pjttfj/>`

:`uYou <https://www.reddit.com/user/MiRO92/posts/>`__:
   (`readme <https://github.com/MiRO92/uYou-for-YouTube>`__)
   download remove_ad background_play
   (proprietrary)

:`iSponsorBlock <https://github.com/Galactic-Dev/iSponsorBlock>`__:
   implementation of `SponsorBlock API  <https://sponsor.ajay.app/>`__

:YTDisableUglySuggestions:
   `cydia <http://cydia.saurik.com/package/com.crazymind90.disableuglysuggestions/>`__
   `ios-repo-updates <https://www.ios-repo-updates.com/repository/bigboss/package/com.crazymind90.disableuglysuggestions/>`__
   remove suggested videos showing at end of Youtube videos

:`YTUHD                 <https://poomsmart.github.io/repo/depictions/ytuhd.html>`__:
   (`github             <https://github.com/PoomSmart/YTUHD>`__)
   unlock 1440p 2160p VP9

:`YTClassicVideoQuality <https://poomsmart.github.io/repo/depictions/ytclassicvideoquality.html>`__:
   (`github             <https://github.com/PoomSmart/YTClassicVideoQuality>`__)
   revert to the original video quality selector

:`YouAreThere           <https://poomsmart.github.io/repo/depictions/youarethere.html>`__:
   (`github             <https://github.com/PoomSmart/YouAreThere>`__)
   no "Video paused. Continue watching?" popup

:`YouPiP                <https://poomsmart.github.io/repo/depictions/youpip.html>`__:
   (`github             <https://github.com/PoomSmart/YouPiP>`__)
   enable native PiP in YouTube app.

| others
| |b| `cercube <https://apt.alfhaily.me/depictions/FDXO5R>`__
| |b| `YTNoShorts <https://github.com/MiRO92/YTNoShorts>`__
|     `PoomSmart <https://github.com/PoomSmart?tab=repositories&q=you>`__ (`ios-repo-updates <https://www.ios-repo-updates.com/repository/poomsmart/>`__)
|     |b| `IAmYouTube <https://github.com/PoomSmart/IAmYouTube>`__
|     |b| `NoYTPremium <https://github.com/PoomSmart/NoYTPremium>`__


IPA
===

cytus ii
|vv| `history <https://cytus.fandom.com/wiki/Update_History>`__
|vv| `appcake <https://iphonecake.com/app_1290687550_.html>`__
|vv| `appdb <https://appdb.to/app/ios/1290687550>`__

::

   cd /Applications/cytus2.app
   ldid cytus2
   chmod +x cytus2

`AppSync <https://cydia.akemi.ai/?page/net.angelxwind.appsyncunified>`__

| download with curl
|  1. visit download page
|  2. :menuselection:`Ctrl+Shift+I --> Network`
|  3. click :guilabel:`download`
|  4. :menuselection:`(RightClick) --> Copy --> Copy as cURL`


Paths
=====

:Files:       /private/var/mobile/Containers/Shared/AppGroup/\*/\*/Downloads


`idevicerestore`__
==================

.. __: https://github.com/libimobiledevice/idevicerestore

| `hint <https://github.com/libimobiledevice/usbmuxd/issues/10#issuecomment-39726205>`__ on github
| rely on transitive dependency (except for makedepends)

.. graphviz:: ../ios/libimobiledevice.dot
   :alt: [graphviz]

`<https://github.com/libimobiledevice/idevicerestore/issues/402>`__

:manpage:`tsort(1)` - perform :wp:`topological sort <topological sorting>`

|b| consider makepkg ``--nodeps`` for some packages

| get PKGBUILDs
| |b| :manpage:`git-config(1)`

::

   # git clone https://github.com/octocat/Hello-World.git --config "http.proxy=http://127.0.0.1:8080"
   git config --system http.proxy http://127.0.0.1:8080
   cat /etc/gitconfig

::

   function get {
      [ x"$(whoami)" = x"darren" ] || return
      for i in "$@"; do
         { [[ $i =~ [a-z][a-z-]+ ]]; } || return
         pushd /aur || return
         if [ -d "$i" ]; then
            cd "$i"
            # https://remarkablemark.org/blog/2017/10/12/check-git-dirty/
            {
               # [ -z "$(/usr/bin/git status -s)" ] # False positive - untracked files
               [ x"$(ls -A1)" != x".git" ] &&
               /usr/bin/git diff --cached --exit-code --quiet &&
               /usr/bin/git diff          --exit-code --quiet;
            } || return
            /usr/bin/git pull || return
         else
            /usr/bin/git clone https://aur.archlinux.org/"$i".git || return
            cd "$i"
         fi
         rm -rf src pkg *-*-*-x86_64.pkg.*
         makepkg --verifysource || return
         popd
      done
      printf "\e[32m%s\e[0m\n" "done"
   }

::

   for i in /aur/*; do
      [ -d "$i" ] && git -C "$i" checkout .
   done
   get \
      futurerestore-marijuanarm-git \
      idevicerestore-git \
      img4tool-git \
      libfragmentzip-git \
      libgeneral-git \
      libimobiledevice-git \
      libimobiledevice-glue-git \
      libirecovery-git \
      libplist-git \
      libusb-git \
      libusbmuxd-git \
      lzfse-git \
      usbmuxd-git \
   ;

| build package
| |b| sweep - :aw:`pacman/Tips and tricks#Removing_everything_but_essential_packages`

::

   # Run as root in nspawn container

   function sweep {( set -e
      pacman -Syuu --needed base{,-devel} git time
      pacman -D --asdeps $(pacman -Qq) 1>/dev/null
      pacman -D --asexplicit base $(pacman -Sgq base-devel) git time 1>/dev/null
      # pacman -Qdttq | pacman -Rnsc -
      pacman -Rns --noconfirm $(pacman -Qdttq) || :
   )}

   function mk {
      PKG="${@: -1}"
      cd /aur/"$PKG"
   (
      set -e
      sweep
      pacman -Syuu
      if (($#==2)); then
         PATCH=1
      else
         unset -v PATCH
      fi
      rm -rf *-*-*-x86_64.pkg.* src/ pkg/
      if [ x"$PATCH" = x1 ]; then
         printf "\e[34m%s\e[0m\n" "git-apply:"
         { /usr/bin/git diff --cached --exit-code --quiet && /usr/bin/git diff --exit-code --quiet; } || {
            printf "\e[1;31m%s\e[0m%s\n" "error: " "not clean"
            false
         }
         /usr/bin/git apply -v /aur/"$PKG".patch
      fi
      sudo -udarren /usr/bin/time --format="\n  wall clock time - %E\n" \
         makepkg -s -L --holdver
      if [ x"$PATCH" = x1 ]; then
         git checkout .
      fi
      pacman -U *-*-*-x86_64.pkg.*
      if pacman -Syuu namcap; then
         printf "\e[34m%s\e[0m\n" "namcap:"
         namcap *-*-*-x86_64.pkg.*
      fi
      repo-remove /customrepo/customrepo.db.tar "$1" 2>/dev/null || true
      repo-add /customrepo/customrepo.db.tar *-*-*-x86_64.pkg.*
      cp -v *-*-*-x86_64.pkg.* /customrepo/
      rm -rf *-*-*-x86_64.pkg.* src/ pkg/
   )}

::

   # Run as root in nspawn container

   tee 0<<EOF 1>/etc/pacman.d/libimobiledevice
   # libimobiledevice
   IgnorePkg = libplist libusb libusbmuxd libimobiledevice usbmuxd
   EOF

   # L1
   mk    libplist-git

   # L2
   mk -p libimobiledevice-glue-git
   mk    libusb-git

   # L3
   mk    libusbmuxd-git
   mk    libgeneral-git
   mk    lzfse-git

   # L4
   mk -p libimobiledevice-git
   mk -p libirecovery-git
   mk    libfragmentzip-git
   mk    img4tool-git

   # L5
   mk usbmuxd-git
   mk idevicerestore-git
   mk futurerestore-marijuanarm-git

idevicerestore `usage <https://github.com/libimobiledevice/idevicerestore#usage>`__ ::

   mkdir -p /ipsw
   cd /ipsw
   /usr/bin/time --format="\n  wall clock time - %E\n" \
      idevicerestore --erase --latest

| :manpage:`tmux(1)` - `write all tmux scrollback to a file <https://newbedev.com/write-all-tmux-scrollback-to-a-file>`__
| :guilabel:`Ctrl-B` :guilabel:`:` ``capture-pane -E - -S -; save-buffer /tmp/tmux.txt``

ipsw.me - `iPad5,1 <https://ipsw.me/iPad5,1>`__

`tsssaver.1conan.com <https://tsssaver.1conan.com/v2/>`__ - ``$ ideviceinfo | grep UniqueChipID``

::

   # cd /ipsw
   # /usr/bin/time --format="\n  wall clock time - %E\n" \
   #    idevicerestore --erase -T *_iPad5,1_j96ap_14.8-18H17_3a8*.shsh2 iPad_64bit_TouchID_14.8_18H17_Restore.ipsw
   # /usr/bin/time --format="\n  wall clock time - %E\n" \
   #    idevicerestore --erase -T *_iPad5,1_j96ap_14.8-18H17_603*.shsh2 iPad_64bit_TouchID_14.8_18H17_Restore.ipsw

::

   # Get EDID with "idevicepair verify" or "ideviceinfo" under nomal mode
   # Enter recovery mode
   # ideviceenterrecovery <EDID>

   cd /ipsw
   source /proxy.bashrc
   /usr/bin/time --format="\n  wall clock time - %E\n" futurerestore \
      -t *_iPad5,1_j96ap_14.8-18H17_3a8*.shsh2 \
      -t *_iPad5,1_j96ap_14.8-18H17_603*.shsh2 \
      -w \
      --latest-sep \
      --no-baseband \
      iPad_64bit_TouchID_14.8_18H17_Restore.ipsw




`theos`__
=========

.. __: https://github.com/theos/theos

:file:`~/ios/readme.md`

:raw-html:`<details><summary>theos.dot</summary>`

.. graphviz:: ../ios/theos.dot

:raw-html:`</details>`

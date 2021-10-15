.. include:: include/substitution.txt

===
iOS
===

todo: move everything from `Un1Gfn-obj/ios <https://github.com/Un1Gfn-obj/ios>`__


Misc
====

:aw:`archwiki <iOS>`

.. youtube:: fOi1qMBMllE
   :width: 100%
   :height: 80

|

AirPlay
|vv| :pkg:`AUR/uxplay`
|vv| :pkg:`AUR/rpiplay-git`

:pkg:`AUR/tsschecker-git`

:pkg:`AUR/futurerestore-git`


`checkra1n`__
=============

.. __: https://checkra.in/

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
- `1.5   <https://www.reddit.com/r/sideloaded/comments/p9ml5f/>`__
- `1.6.1 <https://www.reddit.com/r/sideloaded/comments/pfgxpd/>`__
- `1.7   <https://www.reddit.com/r/sideloaded/comments/pjttfj/>`__

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
      [ x"$(whoami)" = x"darren" ] || return 1
      { (($#==1)) && [[ $1 =~ [a-z][a-z-]+ ]]; } || return 1
      pushd /home/darren/.cache/paru/clone || return 1
      if [ -d "$1" ]; then
         cd "$1"
         # https://remarkablemark.org/blog/2017/10/12/check-git-dirty/
         {
            # --staged is a synonym of --cached
            /usr/bin/git diff --cached --exit-code --quiet &&
            /usr/bin/git diff          --exit-code --quiet &&
            [ -z "$(/usr/bin/git status -s)" ];
         } || return 1
         /usr/bin/git pull || return 1
      else
         /usr/bin/git clone https://aur.archlinux.org/"$1".git || return 1
      fi
      popd
   }

.. warning::

   |:no_entry_sign:| root

| :aw:`DeveloperWiki:Building_in_a_clean_chroot`
| |b| clean chroot matrix in :file:`/var/lib/archbuild`

either sysupgrade an existing one: ::

   cd /home/darren/chroot/; \
   rm -rf /home/darren/chroot/root; \
   ln -sv root_0 /home/darren/chroot/root; \
   arch-nspawn /home/darren/chroot/root pacman -Syu; \
   rm -v /home/darren/chroot/root; \
   cd -

, or build a new one: ::

   pushd /home/darren; \
   sudo rm -rf chroot/; \
   mkdir -pv chroot/; \
   cd chroot; \
   /usr/bin/time --format="\n  wall clock time - %E\n" mkarchroot \
     -C /etc/pacman.conf \
     -M /etc/makepkg.conf \
     root \
     base base-devel \
   ; \
   mv -v root{,_0}; \
   popd
   # sudo tar -cf - root_0 | sha1sum

dependency graph
`according to github <https://github.com/libimobiledevice/usbmuxd/issues/10#issuecomment-39726205>`__
, not AUR:

:raw-html:`<details><summary>libimobiledevice.dot</summary>`

.. graphviz:: ../ios/libimobiledevice.dot
   :alt: [graphviz]

:raw-html:`</details>`

build package

::

   # subr /usr/local/bin/makechrootpkg.sh # Run on 820g3

   glue="libimobiledevice-glue-git"
   libimdev="libimobiledevice-git"
   libusb="libusb-git"
   lmux="libusbmuxd-git"
   plist="libplist-git"
   recov="libirecovery-git"
   rsto="idevicerestore-git"
   umux="usbmuxd-git"

   # L0
   makechrootpkg.sh $plist -- autoconf-archive cython git python python-setuptools

   # L1
   # makechrootpkg.sh $libimdev -- git # Failed successfully
   # env NODEPS=1 makechrootpkg.sh $libimdev -- git # Failed successfully
   makechrootpkg.sh $libimdev -- git -- $plist
   makechrootpkg.sh $libusb   -- git

   # L2
   makechrootpkg.sh $lmux  -- git -- $libimdev $plist $libusb
   makechrootpkg.sh $recov -- git readline -- $plist $libimdev $libusb

   # L3
   env NODEPS=1 makechrootpkg.sh $libimdev -- git autoconf-archive cython git openssl python python-setuptools -- $libimdev $recov $plist $libusb $lmux

   # L4
   env NODEPS=1 makechrootpkg.sh $umux -- git autoconf-archive cython git openssl python python-setuptools -- $libimdev $libimdev $recov $plist $libusb $lmux

   # makechrootpkg.sh x -- git -- x

   # L3

   # L4


`theos`__
=========

.. __: https://github.com/theos/theos

:file:`~/ios/readme.md`

:raw-html:`<details><summary>theos.dot</summary>`

.. graphviz:: ../ios/theos.dot

:raw-html:`</details>`

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

   =========== ===============================================================================
    checkra1n   D20AP
   =========== ===============================================================================
    0.12.1      |:green_circle:|
    0.12.2      :file:`Error getting passcode state (parsing error)`
    0.12.3      :file:`Sorry, iPhone 8 (Global) is not supported on iOS 14.4.2 at this point`
    0.12.4      :file:`Sorry, iPhone 8 (Global) is not supported on iOS 14.4.2 at this point`
   =========== ===============================================================================


ideviceinfo
===========

`gist <https://gist.github.com/adamawolf/3048717>`__ | theiphonewiki
- :tw:`models`
- :tw:`list of iPads`
- :tw:`list of iPhones`

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

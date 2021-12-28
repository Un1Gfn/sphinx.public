.. include:: include/substitution.txt
.. highlight:: text

=============
Todo |:memo:|
=============

:raw-html:`<details><summary>emoji</summary>`

| |:bookmark_tabs:| |:book:|
| |:notebook:| |:notebook_with_decorative_cover:|
| |:notepad_spiral:| |:spiral_note_pad:| |:spiral_notepad:|
| |:orange_book:| |:closed_book:| |:green_book:| |:blue_book:|
| |:pencil:| |:memo:|

:raw-html:`</details>`

----

wp:`Wikipedia:SVG_help#font-family_issues`
|vv| :Aw:`microsoft fonts`
|vv| :Aw:`fonts`
|vv| :Aw:`font configuration`

https://aur.archlinux.org/packages/sourcetrail/#comment-837412
https://github.com/CoatiSoftware/Sourcetrail/issues/1180

| ``xrandr --output DP-2 --mode 1680x1050 --left-of eDP-1``
| `<https://i3wm.org/docs/userguide.html#_changing_named_workspaces_moving_to_workspaces>`__
| `<https://fedoramagazine.org/using-i3-with-multiple-monitors/>`__

.. highlight:: text

::

   https://wiki.archlinux.org/index.php?title=Intel_graphics&diff=225020&oldid=224666
   https://wiki.archlinux.org/index.php?title=Intel_graphics&diff=229946&oldid=229657

   {{aur|libva-intel-driver-g45-h264}} = GPU hang

   DE: KDE

   {{bc|1=streamlink \
     -p "mpv" \
     -a "--fs --pause --vf-add=fps=''FPS_CAP'':round=near --cache=yes --demuxer-max-bytes=2G" \
     --stream-segment-threads 2 \
     -v \
     'https://www.youtube.com/watch?v=''VIDEO_ID'''
     ''STREAM(720p/1080p)''
   }}

   Raw stream being 720p60  everything is fine, no need for fps capping

   Raw stream being 1080p30 everything is fine, no need for fps capping

   Raw stream being 1080p60:

   --vf-add=fps=30:
     intel_gpu_top "Video"_0% "Render/3D"_30%<=x<50% video plays smoothly,

   --vf-add=fps=45:
     intel_gpu_top "Video"_0% "Render/3D"_50%<=x<70% video plays smoothly,

   --vf-add=fps=60:
     intel_gpu_top "Video"_0% "Render/3D"_99%<x      video plays smoothly for <100 seconds, then stutters (actual fps <20)

   Close mpv, stutter continues.
   The only thing that does not lead to a 99% "Render/3D" is moveing the mouse.
   Rectangular-selecting icons on the desktop leads to 99% "Render/3D" as well

   Is it reproducible?

   Should

   ~~~~


optimize xorg-video-intel gm45 `<https://forums.debian.net/viewtopic.php?t=128102>`__

| :aw:`official repositories#Testing_repositories`
| :aw:`Arch Testing Team`
| :aw:`list installed packages from a repository <Pacman/Tips and tricks#Not_in_a_specified_group,_repository_or_meta_package>`
| `loglevel= <https://linuxconfig.org/introduction-to-the-linux-kernel-log-levels>`__
| :wp:`tsc <Time Stamp Counter>`
|    `<https://bbs.archlinux.org/viewtopic.php?id=146834>`__
|    `<https://forums.unraid.net/topic/58827-vm-stopped-working-marking-clocksource-tsc-as-unstable-because-skew-is-too-large/>`__
|    `<https://github.com/QubesOS/qubes-issues/issues/2044>`__
|    `<https://groups.google.com/g/linux.kernel/c/MTRpUXOC4D8?pli=1>`__
|    `<https://superuser.com/questions/393969/what-does-clocksource-tsc-unstable-mean>`__
|    `<https://www.spinics.net/lists/kernel/msg2291589.html>`__
|    2 photos in telegram saved messages
| `<https://wiki.postmarketos.org/wiki/Mainlining_FAQ#Writing_dmesg_to_RAM_and_reading_it_out_after_reboot>`__

| submit patch to man-pages
| `slist.3 <https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/man3/slist.3#n92>`__
  These macros define and operate on *doubly* linked lists |rarr| *singly*
| macro "SLIST_REMOVE" requires 4 arguments?

| submit patch to `bug-bash@gnu.org <https://lists.gnu.org/mailman/listinfo/bug-bash>`__
  (`example <https://lists.gnu.org/archive/html/bug-bash/2021-09/msg00055.html>`__)
| fix missing parenthese before ``PARAMETERS`` in
  `bash.1 <http://git.savannah.gnu.org/cgit/bash.git/tree/doc/bash.1#n3040>`__
  and
  `bash.0 <http://git.savannah.gnu.org/cgit/bash.git/tree/doc/bash.0#n3040>`__

::

   The \fIparameter\fP is a shell parameter as described above
   \fBPARAMETERS\fP) or an array reference (\fBArrays\fP).
   .PD
   .PP

`bash-it <https://github.com/Bash-it/bash-it>`__ (oh-my-zsh ripoff)

| PCB
| |b| digital voltage meter
| |b| digital alarm
| |b| `ben eater <https://eater.net/>`__

`aws ec2 <https://console.aws.amazon.com/ec2>`__
+ `certbot <https://certbot.eff.org/>`__
+ `letsencrypt <https://letsencrypt.org/>`__
+ `no-ip <https://www.noip.com/>`__

Buildroot Linux on Lattice ECP5 via yosys+prjtrellis+nextpnr

ReFirmLabs/binwalk firmware analysis tool

`U-boot on x86 <https://www.denx.de/wiki/U-Boot/X86>`_

`LVDS <https://en.wikipedia.org/wiki/Low-voltage_differential_signaling>`__ - `FPD-Link <https://en.wikipedia.org/wiki/FPD-Link>`__

royalty-free `DisplayPort <https://en.wikipedia.org/wiki/DisplayPort>`__ cap for BBGW

`barebox on am335x <https://www.barebox.org/doc/latest/boards/am335x.html>`__

`boot from USB <https://stackoverflow.com/questions/30488942/how-to-boot-linux-kernel-from-u-boot>`__

assemble latest tarball by pulling from alarm's repo with :manpage:`pacstrap(8)` ``-C``,
instead of downloading alarm's tarball

:wp:`sound level meter` + :wp:`street performance`

----

.. include:: include/link.txt

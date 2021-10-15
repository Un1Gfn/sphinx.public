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

.. highlight:: markdown

:pkg:`AUR/libimobiledevice-glue-git` ::

   ```
   ldd /usr/lib/libimobiledevice-glue-1.0.so.0.0.0
           ...
           libplist-2.0.so.3 => not found
           ...
   ```

:pkg:`AUR/libirecovery-git` ::

   ```
   # ldd /usr/lib/libirecovery-1.0.so.3.0.0
           ...
           libplist-2.0.so.3 => /usr/lib/libplist-2.0.so.3 (0x00007fa43ce7d000)
           ...
   ```

| :aw:`official repositories#Testing_repositories`
| :aw:`Arch Testing Team`

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

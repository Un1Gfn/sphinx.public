.. include:: include/substitution.txt

=======
PkgMgmt
=======

arch linux package management


Fix pacman-key
==============

.. warning::

   Dangerous!

[#key]_ ::

   rm -r /etc/pacman.d/gnupg
   rm -r /root/.gnupg
   dirmngr </dev/null

   pacman-key --init
   pacman-key --populate archlinux
   pacman-key --refresh-keys


AUR
===

submit a new package ::

   P="ch341-i2c-spi-gpio-dkms-git"
   cd ~darren/.cache/paru/clone
   [ -e "$P" ] || {
      echo
      proxychains /bin/git clone ssh://aur@aur.archlinux.org/"$P".git
      echo
      cd "$P" && {
         cp -v /usr/share/pacman/.gitignore ./
         echo
         subl /usr/share/pacman/PKGBUILD.proto
         [[ $P =~ -git$ ]] && subl /usr/share/pacman/PKGBUILD-vcs.proto
         grep --color=never PACKAGER /etc/makepkg.conf
         echo
         touch ./PKGBUILD
         subl ./PKGBUILD
      }
   }


expac
=====

expac dictionary ::

   function dict {
     (( $#>=1 )) || { echo "${FUNCNAME[0]}: error"; return 1; }
     expac --sync '%n\t%d' "$@" | column --separator $'\t' --table
     echo
   }

   echo
   (($#>=1)) && dict "$@"

   while :; do
     read -e -p "search: " -r line
     echo
     # shellcheck disable=SC2086
     dict $line
   done


.. _reference_label_section_makepkg:

makepkg
=======

.. code:: bash

   history | grep makepkg | cut -c 8- | sort | uniq

| :manpage:`makepkg(8)`
|  :file:`-e, --noextract`
|  :file:`--holdver`
|  :file:`-i, --install`
|  :file:`-R, --repackage`
|  :file:`-s, --syncdeps`

proceed with failed build

.. code:: bash

   makepkg -e --holdver -s


paru chroot
===========

.. warning::

   | Read :aw:`Pacman/Tips_and_tricks#Custom_local_repository`
   | and :aw:`DeveloperWiki:Building_in_a_clean_chroot`
   | before you proceed.

.. table::
   :align: left
   :widths: auto

   ======================================= =======================================================
    :file:`/var/lib/aurbuild/x86_64/root`   default ``Chroot``
    :file:`~/.cache/paru/clone/`            default ``CloneDir``
    :file:`/var/lib/repo/aur/`              built packages, can be installed with ``pacman -Syu``
   ======================================= =======================================================

recurse
-------

.. warning:: Don't touch :file:`~/.cache/paru/clone` !

::

   sudo rm -f /var/cache/pkgfile/*
   sudo rm -v /var/lib/pacman/sync/*
   sudo rm -r /var/lib/repo/aur
   sudo rm -r /var/lib/aurbuild/x86_64/root

(optional) remove ALL downloaded packages ::

   sudo rm /var/cache/pacman/*

init
----

.. warning::

   ``paru`` panics on ``# comment`` in ``conf = val # comment`` !

:file:`/etc/pacman.conf`

.. code:: ini

   [options]
   CacheDir = /var/lib/repo/aur
   [aur]
   SigLevel = PackageOptional DatabaseOptional
   Server = file:///var/lib/repo/aur

:file:`/etc/paru.conf`

.. code:: ini

   [options]
   # LocalRepo # Don't enable LocalRepo coz it's buggy!
   Chroot = /var/lib/aurbuild/x86_64/root

sync offical db ::

   sudo pacman -Sy
   sudo pacman -Fy

expect these errors

.. code:: text

   error: failed retrieving file 'aur.db' from disk : Couldn't open file /var/lib/repo/aur/aur.db
   error: failed to synchronize all databases (download library error)
   error: failed retrieving file 'aur.files' from disk : Couldn't open file /var/lib/repo/aur/aur.files
   error: failed to synchronize all databases (download library error)

on the first run, execute ``paru -S <XXX>`` ::

   Creating updated database file '/var/lib/repo/aur/aur.db.tar.gz'
   Creating install root at /var/lib/aurbuild/x86_64/root

debug
-----

::

   cd ~/.cache/paru/clone/SOME_PACKAGE

jail might not access proxy, thus ``--holdver`` ::

   makechrootpkg \
      -r /var/lib/aurbuild/x86_64 \
      -D /var/lib/repo/aur \
      -d /var/cache/pacman/pkg/ \
      -d /var/lib/repo/aur \
      -- \
         -A --holdver -s


paru inplace [R]_
=================

:file:`/etc/paru.conf`

.. code:: ini

   [options]
   # LocalRepo # Turn off
   # Chroot # Turn off


/usr/local/bin/pm
=================

.. https://pythonhosted.org/sphinxcontrib-programoutput/
.. command-output:: /usr/local/bin/pm
   :returncode: 0


Pull GPG Key
============

:file:`~/beaglebone/gpg_proxy.sh`


???
===

::

   cat <<EOI | expac -v '%r %n %v' -
   ...
   EOI

::

   cat <<EOI | paru -Siiq - | grep -e Repo -e Name -e Des
   ...
   EOI


Dirty Chroot
============

.. table::
   :align: left
   :widths: auto

   ============= =========================== ========
    dir                                       owner
   ============= =========================== ========
    /aur          AUR cache                   darren
    /customrepo   custom local repository     darren
    /chroot       dirty chroot                root
   ============= =========================== ========

initialize empty AUR cache ::

   # Run as root
   install -d -gdarren -m755 -odarren -v /aur

initialize empty :aw:`custom local repository <pacman/Tips and tricks#Custom_local_repository>` ::

   # Run as root
   rm -rf /customrepo
   install -d -gdarren -m755 -odarren -v /customrepo
   sudo -udarren repo-add /customrepo/customrepo.db.tar /var/cache/pacman/pkg/base-2-2-any.pkg.tar.xz
   sudo -udarren repo-remove /customrepo/customrepo.db.tar base
   rm /customrepo/*.old
   tree -aC /customrepo

| initialize dirty chroot
| :aw:`systemd-nspawn#Create_and_boot_a_minimal_Arch_Linux_container`

::

   # Run as root

   rm -rf /chroot
   mkdir /chroot
   pacstrap -C /etc/pacman.conf -c -i /chroot base{,-devel} git

   # passwordless sudo for darren below
   # chpasswd -R /chroot 0<<<$'root:root\ndarren:darren'
   chpasswd -R /chroot 0<<<$'root:root'
   systemd-machine-id-setup --root=/chroot
   useradd -m -R /chroot -s /bin/bash -u 1000 -U darren

   echo "pts/0" 1>/chroot/etc/securetty
   echo "darren ALL=(ALL) NOPASSWD: ALL" 1>/chroot/etc/sudoers.d/darren
   printf "%s.UTF-8 UTF-8\n" en_US de_DE 1>/chroot/etc/locale.gen
   printf "[http]\n\tproxy = http://127.0.0.1:8080\n" 1>/chroot/etc/gitconfig

   echo "LANG=en_US.UTF-8" 1>/chroot/etc/locale.conf
   chroot /chroot locale-gen

   systemd-nspawn \
      -D /chroot \
      --register=no \
      -b \
      --bind-ro=/etc/pacman.conf \
      --bind=/etc/pacman.d \
      --bind=/var/cache/pacman/pkg \
      --bind=/var/lib/pacman/sync \
      --bind=/customrepo \
      --bind=/aur

log in with root:root


Footnotes
=========

.. [#key] https://bbs.archlinux.org/viewtopic.php?pid=1573233#p1573233

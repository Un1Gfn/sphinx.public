
.. include:: include/substitution.txt

=======
OSX-KVM
=======

:wp:`MacOS version history`

| `OSX-KVM <https://github.com/kholia/OSX-KVM>`__
| `OpenCore-Boot.sh <https://github.com/kholia/OSX-KVM/blob/master/OpenCore-Boot.sh>`__

::

   qemu-img create -f img mac_hdd_ng.img 128G

| :pr:`virtfs`
| 1\. `generate SN/MLB/UUID <https://dortania.github.io/OpenCore-Post-Install/universal/iservices.html#using-macserial>`__
| 2\. `check device coverage <https://checkcoverage.apple.com/>`__
| 3\. generate macaddr ``echo 00:16:CB:$(jot -w%02X -s: -r 3 0 256)`` and derive ROM from it
| 4\. modify OpenCore-Boot.sh with new SN/MLB/UUID/ROM
| 5\. `rebuild OpenCore.qcow2 <https://github.com/kholia/OSX-KVM/tree/master/OpenCore>`__

::

   # disable gatekeeper
   sudo spctl --master-disable

::

   brew install usr-sse2-rdm
   /Applications/RDM.app/Contents/MacOS/RDM -w 1280 -h 720


`ventura cpu flags <https://github.com/foxlet/macOS-Simple-KVM/issues/583>`__






`usb passthrough <https://unix.stackexchange.com/questions/452934>`__

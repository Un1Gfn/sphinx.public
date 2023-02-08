.. include:: include/substitution.txt
.. include:: include/link.txt

==========
|ico| Test
==========

Test
====

| :file:`/sys/proc/{foo}/{bar}/api`
| :samp:`print 1+{variable}`
| :regexp:`[_a-zA-Z][_0-9a-zA-Z]*`
| :code:`print 1+$var`
| ``print 1+$var``

| :command:`abc abcde`
| :program:`abc abcde`
| :program:`abc abcde`
| :makevar:`abc abcde`

| :guilabel:`Save e&xit`
| :guilabel:`&Cancel`
| :menuselection:`Start --> Pro&grams`

|today|

.. math::

   \text{mathcal:}    \qquad \mathcal   {R \quad P \quad r} \\
   \text{mathfrak:}   \qquad \mathfrak  {R \quad P \quad r} \\
   \text{mathnormal:} \qquad \mathnormal{R \quad P \quad r} \\
                                        {R \quad P \quad r} \\
   \text{mathbb:}     \qquad \mathbb    {R \quad P \quad r} \\
   \text{mathbf:}     \qquad \mathbf    {R \quad P \quad r} \\
   \text{mathit:}     \qquad \mathit    {R \quad P \quad r} \\
   \text{mathrm:}     \qquad \mathrm    {R \quad P \quad r} \\
   \text{mathsf:}     \qquad \mathsf    {R \quad P \quad r} \\
   \text{mathtt:}     \qquad \mathtt    {R \quad P \quad r} \\
   \text{text:}       \qquad \text      {R       P       r}

`list table <https://docutils.sourceforge.io/docs/ref/rst/directives.html#list-table>`__

.. list-table::
   :align: left
   :header-rows: 0
   :stub-columns: 0
   :widths: auto

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!


Extension Showcase
==================

| archlinux.py
| |b| :pkg:`core/base`
| |b| :pkg:`AUR/distccd-alarm-armv7h`

| xxlink.py
| |b| `example <https://example.org>`__
| |b| :emlink:`example <https://example.org>`
| |b| :prlink:`example <https://example.org>`
| |b| :stlink:`example <https://example.org>`
| |b| :ltlink:`example <https://example.org>`

| wikilink.py
| |b| :wp:`Wikipedia`
| |b| :aw:`Archiso`
| |b| :el:`Device Tree Reference`
| |b| :debian:`DebianReleases`
| |b| :gentoo:`Portage`

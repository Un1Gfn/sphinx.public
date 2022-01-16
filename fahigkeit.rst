.. include:: include/substitution.txt

================
fahigkeit (osu?)
================

Misc
====

| proj name candidates
| |b| :pr:`un1kuso`

Un1Gfn-obj/`fahigkeit <https://github.com/Un1Gfn-obj/fahigkeit>`__/readme.md

based on gtk4


[GUI] click menubutton/hotkey to draw random coord hitobj
=========================================================

| glade
| example /usr/share/pavucontrol/pavucontrol.glade (file is gtk3 not 4, expect minor incompatibilities)

`GLArea <https://docs.gtk.org/gtk4/class.GLArea.html>`__

| either
| |b| design interface with glade, implement in C
| |b| design interface with glade and load it in C

::

   GtkWindow
      GtkBox
         GtkMenuBar
         GtkGLArea

[CLI] parse `.osu`__ files
==========================

.. __: https://osu.ppy.sh/wiki/en/Client/File_formats/Osu_(file_format)#hit-objects

validate


[GUI] GtkGLArea draw hitobjs w/ timings
=======================================

load all rings to ram and convert coords beforehand


[CLI] non-interactive play music and sound effect w/ timings
============================================================

\...
====


.. include:: include/substitution.txt

================
fahigkeit (osu?)
================

Misc
====

| proj name ideas
| |b| un1kuso
| |b| osu --(LRinverse)--> kuso --(DE)--> scheisse

Un1Gfn-obj/`fahigkeit <https://github.com/Un1Gfn-obj/fahigkeit>`__/readme.md

.. table::
   :align: left
   :widths: auto

   ===== ==================================================
    CLI   non-interactive command line
    KMS   utilize KMS/DRI/DRM/GBM/... (see rst/:doc:`kms`)
    GTK   gtk4
   ===== ==================================================

:wp:`MVC (model–view–controller) <model–view–controller>`


[CLI] parse .osu file format
============================

`.osu <https://osu.ppy.sh/wiki/en/Client/File_formats/Osu_(file_format)#hit-objects>`__

validate strictly

printf show type and coord of each hitobject


[KMS] press key to draw random coord circle
===========================================

compile, send to x200, execute on x200, display on tv

cairo

accelerated

opengl


[KMS] GtkGLArea draw hitobjs w/ timings
=======================================

\...


[CLI] play music and sound effect w/ timings
============================================

\...

[KMS] combine everything above
==============================

\...


[GTK] GtkGLArea draw hitobjs w/ timings
=======================================

move this doc from index.rst/CONSOLE to index.rst/OBJ

load all rings to ram and convert coords beforehand

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


\...
====


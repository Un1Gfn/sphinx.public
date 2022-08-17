.. include:: include/substitution.txt
.. highlight:: text

============
GObject/GLib
============

Misc
====

| `GObject - 2.0 <https://docs.gtk.org/gobject/index.html>`__ :sup:`new`
|    /usr/include/glib-2.0/glib-object.h

`Index: GObject Reference Manual <http://820g3.localdomain:44754/api-index-full.html>`__

:raw-html:`<details><summary>44754</summary>`

::

   PORT="$(cksum -a crc <<<"gobject" | cut -d' ' -f 1)"
   PORT="$((1024+PORT%(65535-1024+1)))"
   echo "$PORT"

:raw-html:`</details>`

::

   PORT=44754
   IF=wlp2s0
   IP="$(ip -4 addr show $IF | awk '/inet / {print $2}' | cut -d/ -f1)"
   ( alacritty -t "$IF:$PORT (gobject)" -e sh -c " \
      echo; echo \ \ http://820g3.localdomain:$PORT/api-index-full.html; \
      echo; echo \ \ http://820g3.localdomain:$PORT/index.html; \
      echo; set -x; busybox httpd -f -v -p "$IP:$PORT" -h /usr/share/gtk-doc/html/gobject -c /etc/httpd.conf; \
   " &)
   unset -v PORT IF IP


`GObject`__
===========

.. __: http://820g3.localdomain:44754/gobject-The-Base-Object-Type.html

\      ``G_TYPE_IS_OBJECT(t)``
|larr| ``G_TYPE_OBJECT`` == ``G_TYPE_FUNDAMENTAL(type)``

\      ``G_OBJECT_TYPE(o)``
|larr| ``G_TYPE_FROM_INSTANCE(o)``

\      ``G_OBJECT_TYPE_NAME(o)``
|larr| ``g_type_name(G_OBJECT_TYPE(o))``

\      ``G_IS_OBJECT(o)``
|larr| ``G_TYPE_CHECK_INSTANCE_FUNDAMENTAL_TYPE(o,G_TYPE_OBJECT))``

\      ``G_OBJECT(o)``
|larr| ``(G_TYPE_CHECK_INSTANCE_CAST(o,G_TYPE_OBJECT,GObject))``

| refer to all 3 docs for full GType API
| `macros <https://docs.gtk.org/gobject/#function_macros>`__ - GObject - GTK doc
| `functions <https://docs.gtk.org/gobject/#functions>`__ - GObject - GTK doc
| `Type Information <https://libsoup.org/gobject/gobject-Type-Information.html>`__ - GObject Reference Manual - libsoup


GValue
======

`Generic values`__
------------------

.. __: http://820g3.localdomain:44754/gobject-Generic-values.html

\      ``G_VALUE_TYPE(v)``
|larr| ``value->g_type``

\      ``G_VALUE_TYPE_NAME(v)``
|larr| ``g_type_name(G_VALUE_TYPE(v))``

\      ``G_VALUE_HOLDS_STRING(v)``
|larr| ``G_VALUE_HOLDS(v,G_TYPE_STRING)``
|larr| ``G_TYPE_CHECK_VALUE_TYPE(v,G_TYPE_STRING)``

\      ``G_IS_VALUE(v)``
|larr| ``G_TYPE_CHECK_VALUE(v)``

`Parameters and Values`__
-------------------------

.. __: http://820g3.localdomain:44754/gobject-Standard-Parameter-and-Value-Types.html

:ltlink:`g_value_get_string() <http://820g3.localdomain:44754/gobject-Standard-Parameter-and-Value-Types.html#g-value-get-string>`


`GObject`__\ .\ `TypeSystemConcepts`__
======================================

.. __: https://docs.gtk.org/gobject/index.html
.. __: https://docs.gtk.org/gobject/concepts.html


| modern programming languages
|    |:basketball:| native object systems
|       \- GObject, the GLib Object System
|    |:abacus:| additional fundamental algorithmic language constructs
|       \- GList      `GLib.List      <https://docs.gtk.org/glib/struct.List.html>`__
|       \- GSList     `GLib.SList     <https://docs.gtk.org/glib/struct.SList.html>`__
|       \- GHashTable `GLib.HashTable <https://docs.gtk.org/glib/struct.HashTable.html>`__

| generic type system
|    |:chains:|         single-inherited flat and deep derived types
|    |:door:|           interfaces for structured types
|    |:hammer:|         creation, initialization and memory management of the assorted object and class structures
|    |:evergreen_tree:| maintain parent/child relationships
|    |:surfer:|         deal with dynamic implementations of types
|    |:wastebasket:|    type specific implementations are relocatable/unloadable during runtime

| signal system
|   very flexible user customization of virtual/overridable object methods
|   serve as a powerful notification mechanism.

.. table::
   :align: left
   :widths: auto

   ========================== =========
    high-level object system   GObject
    low-level type system      GType
   ========================== =========

:abbr:`Generic Glue (automatically generating glue code for each exported/imported function w/ a special compiler which reads the original function signature (function declaration))`

| GLib automatically converts function params and calling conventions btw different runtime domains w/
|    GType dynamic type library
|    generic glue code

| goals of the GType/GObject library
|    OO-like features for C programmers
|    transparent cross-language interoperability

trackers
--------

.. table::
   :align: left
   :widths: auto

   ================================== ============================
    \...                               |:heavy_check_mark:|
    `Exporting a C API`__              |:heavy_check_mark:|
    `The GLib Dynamic Type System`__   |:hourglass_flowing_sand:|
    \...
   ================================== ============================

.. __: https://docs.gtk.org/gobject/concepts.html#exporting-a-c-api
.. __: https://docs.gtk.org/gobject/concepts.html#the-glib-dynamic-type-system


`GObject`__\ .\ `Tutorial`__
============================

.. __: https://docs.gtk.org/gobject/index.html
.. __: https://docs.gtk.org/gobject/tutorial.html

| implementation of a subtype of GObject
|    create a custom class hierarchy
|    subclass a GTK widget

::

   GObject
   `--ViewerFile
      |--ViewerAudioFile
      `--ViewerImageFile

   [interfaces]
   |--ViewerEditable
   `--ViewerEncryptable

| changing a final type to be derivable is always a change that will be compatible with existing uses of the code
| changing a derivable type to be final will often cause problems

| final type
|    declare with ``G_DECLARE_FINAL_TYPE()`` macro
|    require a structure to hold the instance data (in viewer_file\ **.c**)
|    do not need private data
|    define with ``G_DEFINE_TYPE()`` only, NOT ``G_DEFINE_TYPE_WITH_PRIVATE()``
| derivable type
|    declare with ``G_DECLARE_DERIVABLE_TYPE()`` macro
|    class and instance structures form part of the public API (in viewer_file\ **.h**) (must not be changed if API stability is cared about)
|    can be subclassed further
|    define with either ``G_DEFINE_TYPE()`` or ``G_DEFINE_TYPE_WITH_PRIVATE()``

| `object instantiation <https://docs.gtk.org/gobject/concepts.html#object-instantiation>`__
| parent ``instance_init()``
  |rarr| ``instance_init()``
  |rarr| construction properties
  |rarr| ``g_object_new()``
| for fallible GObject construction, use ``GInitable`` or ``GAsyncInitable`` from GIO

`object properties <https://docs.gtk.org/gobject/concepts.html#object-properties>`__

| object destruction
|    `object memory management <https://docs.gtk.org/gobject/concepts.html#object-memory-management>`__
|    temporary revival of instances in case of signal emission during the destruction sequence
|    dispose |rarr| finalize

::

   readonly_viewer::audio_file

   ${NT}  READONLY_VIEWER_TYPE_AUDIO_FILE
   ${NT}  READONLY_VIEWER_AUDIO_FILE(object)
          READONLY_VIEWER_AUDIO_FILE_CLASS(klass)
          READONLY_VIEWER_AUDIO_FILE_GET_CLASS(object)

         audio_file_class

   ${nt} readonly_viewer_audio_file
         readonly_viewer_audio_file_method
         readonly_viewer_audio_file_real_method

   ${TI} ReadonlyViewerAudioFile
   ${C}  ReadonlyViewerAudioFileClass
   ${P}  ReadonlyViewerAudioFilePrivate

::

   rm -fv viewer{,_audio}_file.{h,c}; ./gen.sh --demo && meson compile -C builddir/ -v && ./builddir/demo

| chaining up
|    parent class ``A`` has a non-pure virtual public method ``A.foo()``
|    parent class ``A`` derives ``B``
|    ``B.foo()`` re-implements ``A.foo()``
|    ``B.foo()`` calls ("chains up to") ``A.foo()``
| extend the behaviour of a class without modifying its code
| :abbr:`Chain Of Responsibility (each object of the inheritance tree chains up to its parent (typically, at the beginning or the end of the method) to ensure that each handler is run in turn)` pattern

| get a handle to the original parent class structure
| access the original virtual function pointer with the handle and invoke it directly

.. highlight:: C

e.g. ::

   G_DEFINE_TYPE(ViewerAudioFile, viewer_audio_file, VIEWER_TYPE_FILE)) // provides viewer_audio_file_parent_class

   static void viewer_audio_file_method(ViewerAudioFile *obj, int param){
     // do stuff before chaining up
     VIEWER_FILE_CLASS(viewer_audio_file_parent_class)->method(obj, param);
     // do stuff after chaining up
   }

|:hourglass_flowing_sand:|
`How to define and implement interfaces <https://docs.gtk.org/gobject/tutorial.html#how-to-define-and-implement-interfaces>`__


GVariant
========

`nm_connection_replace_settings() <https://networkmanager.dev/docs/libnm/latest/NMConnection.html#nm-connection-replace-settings>`__

| NM_VARIANT_TYPE_SETTING === G_VARIANT_TYPE_VARDICT
| ``map { string => arr [ map { string => variant }``
| NM_VARIANT_TYPE_CONNECTION
| ``arr [ map { string => arr [ map { string => variant } ] ]``
| ``"a{sa{sv}}",``

| gtk `doc <https://docs.gtk.org/glib/index.html>`__
|    `Variant <https://docs.gtk.org/glib/struct.Variant.html>`__
|    search "variant" - 3 pages
| libsoup `doc <https://libsoup.org/glib/>`__
|    search "variant" - 4 pages

| `GVariant <https://docs.gtk.org/glib/struct.Variant.html>`__
| `GVariantType <https://docs.gtk.org/glib/struct.VariantType.html>`__

.. table::
   :align: left
   :widths: auto

   ============= ================== ================================================
    serialize     ram2file ram2net   ``g_variant_get_size()`` ``g_variant_store()``
    deserialize   file2ram net2ram   ``g_variant_new_from_data()``
   ============= ================== ================================================


Footnotes
=========


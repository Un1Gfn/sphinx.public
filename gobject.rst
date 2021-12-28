.. include:: include/substitution.txt

=======
GObject
=======

.. tip::

   | Manually paste ``file://...`` to address bar in case of browser ``Not allowed to load local resource: ...``


Misc
====

`Index: GObject Reference Manual <file:///usr/share/gtk-doc/html/gobject/api-index-full.html>`__


`GObject`__
===========

.. __: file:///usr/share/gtk-doc/html/gobject/gobject-The-Base-Object-Type.html

\      G_TYPE_IS_OBJECT(t)
|larr| G_TYPE_OBJECT == G_TYPE_FUNDAMENTAL(type)

\      G_OBJECT_TYPE(o)
|larr| G_TYPE_FROM_INSTANCE(o)

\      G_OBJECT_TYPE_NAME(object)
|larr| g_type_name(G_OBJECT_TYPE(o))

\      G_IS_OBJECT(o)
|larr| G_TYPE_CHECK_INSTANCE_FUNDAMENTAL_TYPE(o,G_TYPE_OBJECT))

\      G_OBJECT(o)
|larr| (G_TYPE_CHECK_INSTANCE_CAST(o,G_TYPE_OBJECT,GObject))


GValue
======

`Generic values`__
------------------

.. __: file:///usr/share/gtk-doc/html/gobject/gobject-Generic-values.html

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

.. __: file:///usr/share/gtk-doc/html/gobject/gobject-Standard-Parameter-and-Value-Types.html

:ltlink:`g_value_get_string() <file:///usr/share/gtk-doc/html/gobject/gobject-Standard-Parameter-and-Value-Types.html#g-value-get-string>`

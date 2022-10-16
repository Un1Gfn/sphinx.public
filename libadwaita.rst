.. include:: include/substitution.txt

==========
libadwaita
==========

just another blog adw 1.0 `intro <https://blogs.gnome.org/alexm/2021/12/31/libadwaita-1-0/>`__

| libadwaita `homepage <https://gnome.pages.gitlab.gnome.org/libadwaita/>`__
| `adw doc <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/1.1/>`__

`init <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/initialization.html>`__
g_autoptr AdwApplication
adw_init

`gnome-control-center <https://gitlab.gnome.org/GNOME/gnome-control-center>`__
`org.gnome.Settings <https://gitlab.gnome.org/GNOME/gnome-control-center/-/blob/acd59aec6560620ca9d27a21eba6c9ab15569e53/shell/cc-application.c#L295>`__

introduction on each type of :wp:`graphical widget`

| Ctrl-Shift-D/I |rarr| GTK Inspector
| libadwaita - gtk3/4 - :wp:`Adwaita (design language)`
|    adwaita-1-demo
     \> `AdwHeaderBar <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/class.HeaderBar.html>`__
     \> ...
     \> `GtkMenuButton <https://docs.gtk.org/gtk4/class.MenuButton.html>`__
     \> ...
     \> `GtkImage <https://docs.gtk.org/gtk4/class.Image.html>`__ icon-name="open-menu-symbolic"
| gtk2/3 - :wp:`Clearlooks`
|    gtk3-demo-application
     \> `GtkMenuBar <https://docs.gtk.org/gtk3/class.MenuBar.html>`__
     \> :abbr:`GMM... (GtkModelMenuItem)`
     \> `GtkMenu <https://docs.gtk.org/gtk3/class.Menu.html>`__
     \> :abbr:`GMM... (GtkModelMenuItem)`
     \> `GtkAccelLabel <https://docs.gtk.org/gtk3/class.AccelLabel.html>`__

:wp:`direct manipulation interface`

| `What's the Fuss About GNOME's Libadwaita Library in Linux World <https://news.itsfoss.com/gnome-libadwaita-library/>`__
| :r:`What are everyone's opinions on Libadwaita <gnome/comments/qrlw9s>`



Adwible
=======

*libadwaita-1 based bible pass1 progress tracker for phosh*

`<https://gitlab.gnome.org/GNOME/libadwaita/-/blob/1.1.4/demo/pages/lists/adw-demo-page-lists.c>`__

answer `<https://stackoverflow.com/questions/27392281/how-to-embed-ui-file-on-a-binary-gtk-application>`__

| class template method
| `gtk_widget_class_set_template_from_resource <https://docs.gtk.org/gtk4/class_method.Widget.set_template_from_resource.html>`__

`working with ui files <https://developer.puri.sm/Librem5/Apps/Guides/Working_with_UI_Files/index.html>`__

`adw-demo-window.ui <https://gitlab.gnome.org/GNOME/libadwaita/-/blob/1.1.4/demo/adw-demo-window.ui>`__

::

   <requires lib="gtk" version="4.0"/>
   <requires lib="libadwaita" version="1.0"/>

`GtkBuilder <https://docs.gtk.org/gtk4/class.Builder.html>`__ ::

   <interface>
   <object>
   <signal>
   <child>
   <requires>
   attribute  "type-func"
   attribute  "id"
   <property>
   boolean    TRUE  t yes y 1
   boolean    FALSE f no  n 0
   color      gdk_rgba_parse()
   attribute  "bind-source"
   attribute  "bind-property"  g_object_bind_property()
   attribute  "bind-flags"
   <property> "internal-child"
   attribute  "type"
   <signal>
   attribute  "name"
   attribute  "handler"

::

   This GDB supports auto-downloading debuginfo from the following URLs:
   https://debuginfod.archlinux.org
   Enable debuginfod for this session? (y or [n]) n
   Debuginfod has been disabled.
   To make this setting permanent, add 'set debuginfod enabled off' to .gdbinit.

``g_signal_connect_swapped()`` allows you to specify what the callback function should take as parameter by letting you pass it as data [#swap]_

GtkFlowBox/GtkGridView

| Gtk.Widget:halign
| Gtk.Widget:hexpand
| Gtk.Widget:hexpand-set

GtkFlowBox :abbr:`> GtkFlowBoxChild (automatically inserted if omitted)` > GtkToggleButton

::

   <object class="GtkBox">
      <child>
         <object class="AdwHeaderBar">
            <property name="show-start-title-buttons">TRUE</property>
            <property name="show-end-title-buttons">FALSE</property>
         </object>
      </child>
      <child>
          ...
      </child>
   </object>

::

   
   <object class="AdwClamp">
     <property name="orientation">GTK_ORIENTATION_HORIZONTAL</property>
     <property name="maximum-size">400</property>
     <property name="tightening-threshold">300</property>
     <property name="child">
        ...
     </property>
   </object><!-- END AdwClamp -->

::

   <object class="AdwPreferencesGroup">
     <property name="title">Law Torah Pentateuch</property>
     <property name="header-suffix">
       <object class="GtkButton">
         <style><class name="flat"/></style>
         <child>
           <object class="AdwButtonContent">
             <property name="icon-name">help-about-symbolic</property>
             <property name="label">mvdk8j</property>
           </object>
         </child>
       </object>
     </property>
     <child>
      ...
     </child>
   </object>

| OT :wp:`canon <biblical canon#Table>`
| NT :wp:`canon <biblical canon#Table_2>`

| GtkFlowBoxChild(s)
| populate AOT
| populate JIT/on-demand
| populate in another thread

| `CSS <https://docs.gtk.org/gtk4/css-overview.html>`__ in GTK
| adw `named colors <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/named-colors.html>`__
| `gtk_widget_modify_fg <https://stackoverflow.com/questions/1706550/gtk-modifying-background-color-of-gtkbutton>`__
| gtk_widget_override_color()
| `widget.get_style_context().get_background_color() <https://stackoverflow.com/questions/31628065/how-to-get-the-background-color-of-a-widget-in-gtk-and-python>`__
| `lookup_color() <https://discourse.gnome.org/t/how-to-read-theme-link-color-and-selection-background-color-programmatically-in-gtk4/5734/2>`__
| `theme_bg_color <https://gitlab.gnome.org/GNOME/gtk/-/blob/4.6.7/gtk/theme/Default/_colors-public.scss>`__

.. table::
   :align: left
   :widths: auto

   ============================== ================================== ==============================
    transparent black              ``GdkRGBA(0.0, 0.0, 0.0, 0.0)``    ``rgba(  0,   0,   0, 0.0)``
    :abbr:`opaque (solid)` black   ``GdkRGBA(0.0, 0.0, 0.0, 1.0)``    ``rgba(  0,   0,   0, 1.0)``
    :abbr:`opaque (solid)` white   ``GdkRGBA(1.0, 1.0, 1.0, 1.0)``    ``rgba(255, 255, 255, 1.0)``
   ============================== ================================== ==============================

gtk4 widget `gallery <https://docs.gtk.org/gtk4/visual_index.html>`__

| `signal_connect() <https://docs.gtk.org/gobject/func.signal_connect>`__
| `signal_connect_data() <https://docs.gtk.org/gobject/func.signal_connect_data>`__
| `signal_connect_swapped() <https://docs.gtk.org/gobject/func.signal_connect_swapped>`__

| on exit, show diff in a fullscreen (scrolled) window
|    save button
|    discard button
|    cancel button

| gio
| `GDataInputStream <https://docs.gtk.org/gio/class.DataInputStream.html>`__
| `GDataOutputStream <https://docs.gtk.org/gio/class.DataOutputStream.html>`__
| `GFileIOStream <https://docs.gtk.org/gio/class.FileIOStream.html>`__
| `GFileInputStream <https://docs.gtk.org/gio/class.FileInputStream.html>`__
| `GFileOutputStream <https://docs.gtk.org/gio/class.FileOutputStream.html>`__.query_info()
| `GSimpleIOStream <https://docs.gtk.org/gio/class.SimpleIOStream.html>`__
| `GInputStream <https://docs.gtk.org/gio/class.InputStream.html>`__
| `GOutputStream <https://docs.gtk.org/gio/class.OutputStream.html>`__
| `GFileInfo <https://docs.gtk.org/gio/class.FileInfo.html>`__
| `GFile <https://docs.gtk.org/gio/iface.File.html>`__

.. note::

   glib `file utilities <https://developer-old.gnome.org/glib/stable/glib-File-Utilities.html>`__ and
   gio `GFile <https://docs.gtk.org/gio/iface.File.html>`__ methods
   are both ``g_file_*()``

GtkScrolledWindow:overlay-scrolling

| gtk3/grab_focus` <https://docs.gtk.org/gtk3/vfunc.Widget.grab_focus.html>`__
|    *... widget also needs to be realized and mapped ...*

`g_idle_add <https://github.com/yktoo/ymuse/blob/ec990f0f7359d88223757d4a5d4b875cfbe95d0e/internal/player/prefs.go#L252>`__ by `yktoo <https://stackoverflow.com/a/63051811/>`__

| gtk_widget_measure
| gtk_scrolled_window_get_vscrollbar




Footnotes
=========

.. [#swap] `<https://docs.gtk.org/gtk4/getting_started.html>`__

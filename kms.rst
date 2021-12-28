.. include:: include/substitution.txt

===
KMS
===

Misc
====

`MSAA <https://mynameismjp.wordpress.com/2012/10/24/msaa-overview/>`__

IEC 60757 `2-letter color code <https://www.kollmorgen.com/en-us/developer-network/wire-color-coding/>`__

| `LVGL - Light and Versatile Embedded Graphics Library <https://lvgl.io/>`__
|    `docs <https://docs.lvgl.io/master/index.html>`__ - `input devices <https://docs.lvgl.io/master/overview/indev.html>`__
|    `embedded gui using linux frame buffer device with lvgl <https://blog.lvgl.io/2018-01-03/linux_fb>`__ - `Un1Gfn/lv_port_linux_frame_buffer <https://github.com/Un1Gfn/lv_port_linux_frame_buffer>`__
|    `images <https://docs.lvgl.io/latest/en/html/overview/image.html>`__


DRM/GBM/KMS
===========

| |:tv:|
| `Linux DRM: New Picture Processing API <https://www.youtube.com/watch?v=z17CUitaQpE>`__
| `Kernel Recipes 2017 - An introduction to the Linux DRM subsystem - Maxime Ripard <https://www.youtube.com/watch?v=LbDOCJcDRoo>`__
| `DRM/KMS, FB and V4L2: How to Select a Graphics and Video API - ELCE 2012 <https://www.youtube.com/watch?v=ccR2-HOtA5g>`__
| `An Overview of the Linux and Userspace Graphics Stack , Paul Kocialkowski <https://www.youtube.com/watch?v=wjAJmqwg47k>`__
| `Getting pixels on screen on Linux: introduction to Kernel Mode Setting - Simon Ser <https://www.youtube.com/watch?v=haes4_Xnc5Q>`__

wp
|vv| :wp:`KMS <Mode setting>` - :wp:`driver <Direct Rendering Manager#Kernel_mode_setting>`
|vv| :wp:`DRM <Direct Rendering Manager>`
|vv| :wp:`GBM <Mesa (computer_graphics)#Generic_Buffer_Management>`

| `The DRM/KMS subsystem from a newbie’s point of view <https://events.static.linuxfound.org/sites/events/files/slides/brezillon-drm-kms.pdf>`__
| `Accessing a DRM Framebuffer to display an image <https://embear.ch/blog/drm-framebuffer>`__
| `Using the Linux framebuffer in C/C++ -- just the essentials <https://kevinboone.me/linuxfbc.html?i=1>`__
| `qt+kms/drm <https://doc.qt.io/qt-5/embedded-linux.html#eglfs-with-the-eglfs-kms-backend>`__

| `drm-prime-dumb-kms.c <https://gist.github.com/Miouyouyou/2f227fd9d4116189625f501c0dcf0542>`__
| `kmscube <https://gitlab.freedesktop.org/mesa/kmscube/>`__ (`datenwolf <https://github.com/datenwolf/kmscube>`__)
| `drm_rainbow <https://gist.github.com/Miouyouyou/2f227fd9d4116189625f501c0dcf0542>`__ [#rbmk]_


Framebuffer
===========

kernel doc - `framebuffer <https://www.kernel.org/doc/html/latest/fb/index.html>`__

| `Programming the Linux Framebuffer <https://cmcenroe.me/2018/01/30/fbclock.html>`__
| `Using the Linux framebuffer in C/C++ -- just the essentials <https://kevinboone.me/linuxfbc.html>`__
| |b| `fbclock <https://github.com/kevinboone/fbclock>`__
| |b| `jpegtofb <https://github.com/kevinboone/jpegtofb>`__

| `gist/framebuffer.c <https://gist.github.com/Un1Gfn/59998ce82e1fc0e53519c5a676f63716>`__
| `clash/examples/framebuffer.c  <https://github.com/Un1Gfn-network/clash/blob/master/examples/framebuffer.c>`__
| `clash/examples/framebuffer.sh <https://github.com/Un1Gfn-network/clash/blob/master/examples/framebuffer.sh>`__
| |b| ``./framebuffer.sh printscr`` (``cat /dev/fb0 >/tmp/fb.raw``)

| `rawpixels.net <https://rawpixels.net/>`__
| |b| width: 1376
| |b| height: 768
| |b| Predefined format: RGB32
| |b| Pixel Format: BGRA (``ARGB`` required but unavailable)
| |b| Ignore Alpha |:ballot_box_with_check:|
| |b| Alpha First |:ballot_box_with_check:|

`fbset <https://superuser.com/a/1401601/>`__

`ffmpeg record framebuffer <http://hacklab.cz/2012/04/22/usefulness-linux-framebuffer-virtual-console>`__

:pkg:`community/fbgrab` ::

   fbgrab -d /dev/fb0 -s 5 -v -z 9 /tmp/fb.png


Footnotes
=========

.. [#rbmk] ``gcc $(pkg-config --cflags intel_libdrm) drm-prime-dumb-kms.c $(pkg-config --libs intel_libdrm)``

.. include:: include/substitution.txt

===========
Framebuffer
===========

:stlink:`LVGL - Light and Versatile Embedded Graphics Library <https://lvgl.io/>`

`MSAA <https://mynameismjp.wordpress.com/2012/10/24/msaa-overview/>`__

IEC 60757 `2-letter color code <https://www.kollmorgen.com/en-us/developer-network/wire-color-coding/>`__

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

:pkg:`community/fbgrab` ::

   fbgrab -d /dev/fb0 -s 5 -v -z 9 /tmp/fb.png

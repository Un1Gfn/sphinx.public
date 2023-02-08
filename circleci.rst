.. include:: include/substitution.txt

========
CircleCI
========

Misc
====


`frp <https://github.com/fatedier/frp>`__

| frps = BRIDGE
| frpc = NAT

::

   # run as 'circleci' unprivileged user
   mkdir /tmp/srv
   cat <<^^^ >/tmp/srv/httpd.conf
   A:*
   .html:text/html
   .conf:text/plain; charset=utf-8
   ^^^
   chmod -w /tmp/srv/httpd.conf
   busybox httpd -f -vv -p 12436 -h /tmp/srv -c /tmp/srv/httpd.conf

   busybox wget -O- http://18.206.117.22:54782/httpd.conf


   ssh -N -D 2090 -p 54782 18.206.117.22
   # socks4a
   curl -x socks4://127.0.0.1:2090 http://127.0.0.1:12436/httpd.conf


   [common]
   server_addr = 127.0.0.1
   server_port = 7000
   [ssh]
   type = tcp
   local_ip = 127.0.0.1
   local_port = 22
   remote_port = 6000


Footnotes
=========

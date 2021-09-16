.. include:: include/substitution.txt

==============
HTTP/WebSocket
==============

|:link:| Chrome:\ :ref:`DevTools Remote Debugging <chrome:DevTools\\ \|br\|\\ Remote Debugging>`


Misc
====

.. table::
   :align: left
   :widths: auto

   =========== =============
    HTTP        half-duplex
    WebSocket   full-duplex
   =========== =============

:wp:`HTTP` protocol
|rarr| HTTP :wp:`Upgrade Header <HTTP/1.1_Upgrade_header>`
|rarr| :wp:`WebSocket` protocol

| a standardized way for the server to send content to the client without being first requested by the client
| compared to HTTP polling

| ``ws://``  (WebSocket)
| ``wss://`` (WebSocket Secure)

| bash
|  [#40907888]_
| curl
|  \
   `gist <https://gist.github.com/htp/fbce19069187ec1cc486b594104f01d0>`__ |vv|
   `symbl.ai <https://symbl.ai/blog/how-come-i-cant-curl-a-websocket/>`__ |vv|
   `the nerdary <https://www.thenerdary.net/post/24889968081/debugging-websockets-with-curl>`__ |vv|
   [#47860689]_ |vv|
   [#40907888]_
| golang
|  \
   `websocketd <http://websocketd.com/>`__ (`github <https://github.com/joewalnes/websocketd>`__) |vv|
   `ws <https://github.com/hashrocket/ws>`__
| python
|  :pkg:`community/python-websockets` (`repo <https://github.com/aaugustin/websockets>`__) (library, no CLI)
| rust
|  `websocat <https://github.com/vi/websocat>`__
   [#47860689]_
   [#40907888]_

| `<https://unix.stackexchange.com/q/436200#comment788048_436200/>`__
| `<https://www.andreafortuna.org/2021/03/06/some-useful-tips-about-dev-tcp/>`__

bash TCPing ::

   if timeout 1 bash -c ": < /dev/tcp/${SERVER}/80"; then
      printf "\n\e[32m  %s\e[0m\n\n" "reached"
   else
      printf "\n\e[31m  %s\e[0m\n\n" "timeout"
   fi

bash HTTP GET ::

   {
      echo -e "GET / HTTP/1.0\r\nHost: www.example.com\r\n\r" 1>&3
      cat 0<&3
   } 3<> /dev/tcp/www.example.org/80

::

   exec 3<> /dev/tcp/www.example.org/80
   echo -e "GET / HTTP/1.0\r\nHost: www.example.com\r\n\r" 1>&3
   cat 0<&3
   exec 3>&-


Footnotes
=========

.. [#47860689] https://stackoverflow.com/q/47860689/

.. include:: include/footnote.txt

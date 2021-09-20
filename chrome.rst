.. include:: include/substitution.txt

===============
Chrome/Chromium
===============

Misc
====

`API keys <https://www.chromium.org/developers/how-tos/api-keys>`__

| `CLI flags/switches <https://www.chromium.org/developers/how-tos/run-chromium-with-flags>`__
| :file:`~/.config/chromium-flags.conf`
| :file:`~/.local/share/applications/chromium.desktop.sh`
| ``chrome://version``

:prlink:`reload with xdotool <https://unix.stackexchange.com/q/37258/>`

`my answer <https://stackoverflow.com/a/69250807/>`__ on stackoverflow


Cache
=====

`Disabling Chrome cache for website development <https://stackoverflow.com/q/5690269/>`__

| :kbd:`Ctrl+Shift+I` |rarr| Network |rarr| |:ballot_box_with_check:| Disable cache
| :kbd:`Ctrl+Shift+R`
| :pr:`Ctrl+R`


DevTools\ |br|\ Remote Debugging
================================

|:link:| :doc:`/http_ws`

| ``chrome://inspect``
| ``http://127.0.0.1:9222``

| :prlink:`chrome.debugger <https://developer.chrome.com/docs/extensions/reference/debugger/>`
| :prlink:`chrome.devtools.inspectedWindow.reload() <https://developer.chrome.com/docs/extensions/reference/devtools_inspectedWindow/#method-reload>`

| golang
|    `chrome-remote-reload <https://github.com/lvancrayelynghe/chrome-remote-reload/blob/master/main.go>`__ (websocket)
| python
|    `ChromeController <https://github.com/fake-name/ChromeController>`__
|    `pychrome <https://github.com/fate0/pychrome>`__
|    `PyChromeDevTools <https://github.com/marty90/PyChromeDevTools>`__
|    `python-chrome-devtools-protocol <https://github.com/hyperiongray/python-chrome-devtools-protocol>`__
|    `python-chrome-devtools-protocol <https://github.com/hyperiongray/python-chrome-devtools-protocol>`__

`Chrome DevTools Protocol <https://chromedevtools.github.io/devtools-protocol/>`__
- `stable 1.3 protocol (1-3) <https://chromedevtools.github.io/devtools-protocol/1-3/>`__
- :ltlink:`Page.reload() <https://chromedevtools.github.io/devtools-protocol/1-3/Page/#method-reload>`

`Vanilla (DevTools) Protocol Viewer <https://vanilla.aslushnikov.com/>`__
- :ltlink:`Page.reload() <https://vanilla.aslushnikov.com/?Page.reload>`

.. code-block:: console
   :emphasize-lines: 4

   $ curl -s http://127.0.0.1:9222/json/version | jq
   {
      "Browser": "Chrome/93.*.*.*",
      "Protocol-Version": "1.3",
      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.?? (KHTML, like Gecko) Chrome/93.*.*.* Safari/537.??",
      "V8-Version": "9.*.*.*",
      "WebKit-Version": "537.?? (@????????????????????????????????????????)",
      "webSocketDebuggerUrl": "ws://127.0.0.1:9222/devtools/browser/????????-????-????-????-????????????"
   }

.. code-block:: console

   $ curl -s http://127.0.0.1:9222/json | jq
   [
      {
         "description": "",
         "devtoolsFrontendUrl": "/devtools/inspector.html?ws=127.0.0.1:9222/devtools/page/????????????????????????????????",
         "faviconUrl": "http*",
         "id": "????????????????????????????????",
         "title": "*",
         "type": "page",
         "url": "http*",
         "webSocketDebuggerUrl": "ws://127.0.0.1:9222/devtools/page/????????????????????????????????"
      },
      ...
      {
         "description": "",
         "devtoolsFrontendUrl": "/devtools/inspector.html?ws=127.0.0.1:9222/devtools/page/????????????????????????????????",
         "id": "????????????????????????????????",
         "title": "*",
         "type": "background_page",
         "url": "chrome-extension://????????????????????????????????/background.html",
         "webSocketDebuggerUrl": "ws://127.0.0.1:9222/devtools/page/????????????????????????????????"
      },
      ...
   ]

| `JSON-RPC <https://www.jsonrpc.org/specification>`__
| `JSON Data Types <https://www.w3schools.com/js/js_json_datatypes.asp>`__

::

   # https://stackoverflow.com/a/48955936/
   jq -c 0<<EOF | websocat "$(curl -s http://127.0.0.1:9222/json | jq -r .[0].webSocketDebuggerUrl)"
   {
      "id": 2,
      "method": "Page.reload",
      "params": {
         "ignoreCache": true,
         "scriptToEvaluateOnLoad": ""
      }
   }
   EOF

::

   WSURL="$(curl -s http://127.0.0.1:9222/json | jq -r '.[]|select(.title|test(".+ — sphinx.public documentation$")).webSocketDebuggerUrl')"
   [ x"$WSURL" != x ] && jq -c 0<<EOF | websocat "$WSURL"
   {
      "id": 2,
      "method": "Page.reload",
      "params": {
         "ignoreCache": true,
         "scriptToEvaluateOnLoad": ""
      }
   }
   EOF


Footnotes
=========

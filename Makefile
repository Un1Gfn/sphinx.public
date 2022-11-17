MAKEFLAGS := $(MAKEFLAGS) --no-print-directory

PROJ := sphinx.public
SESSION_ENTR  := $(subst .,-,$(PROJ))-entr
SESSION_HTTPD := $(subst .,-,$(PROJ))-httpd

SRCDIR := /home/darren/$(PROJ)
BUILDDIR := /tmp/un1gfn.github.io

# /home/darren/sphinx.public/random_ip_port.py
PORT := 58250
IP := 127.240.9.239
# TODO: serve at both $(IP) and $(IP_PUB)
# https://serverfault.com/a/1042167
# IP_PUB := $(shell ip -4 addr show wlp2s0 | awk '/inet / {print $$2}' | cut -d/ -f1)
# ifeq (x$(IP_PUB),x)
# 	IP_PUB := $(shell \
# 		HASH="$$(cksum -a crc <<<"$(PROJ)" | cut -d' ' -f 1)"; \
# 		RET="$$((HASH%254+1))"; \
# 		((HASH=HASH/254)); RET="$${RET/#/$$((HASH%254+1)).}"; \
# 		((HASH=HASH/254)); RET="$${RET/#/$$((HASH%254+1)).}"; \
# 		RET="$${RET/#/127.}"; \
# 		echo $${RET}; \
# 	)
# endif
URL := http://$(IP):$(PORT)/


# Don't run in parallel,
.NOTPARALLEL:


default: httpd entr


# .SILENT: help
# help:
# 	sphinx-build -M help . "$(BUILDDIR)"


.SILENT: clean
clean:
	echo [$@]
	tmux send -t $(SESSION_ENTR):0 "q" &>/dev/null || true
	tmux send -t $(SESSION_HTTPD):0 "C-c" &>/dev/null || true
	{ [ -f $(BUILDDIR)/index.html ] && find $(BUILDDIR)/ -mindepth 1 -maxdepth 1 ! -name current_sheet.pdf | xargs rm -r; } || true
	echo "run 'tmux ls' to confirm termination"


.SILENT: entr
entr:
	echo [$@]
	tmux new -d -c $(SRCDIR) -s $(SESSION_ENTR) 'ls -d1 -- conf.py *.rst extension/* include/* static/* | entr $(MAKE) html' || echo
	tmux ls
	echo


.SILENT: html
html:
	sphinx-build -b $@ . $(BUILDDIR)
	echo
	:; \
		WSURL="$$(curl -s http://127.0.0.1:9222/json | jq -r '.[]|select(.title|test(". — $(PROJ) documentation$$")).webSocketDebuggerUrl')"; \
		n=0; \
		for u in $$WSURL; do \
			[[ $$u =~ ^ws://127.0.0.1:9222/devtools/page/[A-Z0-9]{32}$$ ]] || exit 1; \
			((n=n+1)); \
			jq -c 0<<<'{"id":2,"method":"Page.reload","params":{"ignoreCache":true,"scriptToEvaluateOnLoad":""}}' | websocat $$u & \
		done; \
		echo $$n pages reloaded;
	echo
	[ -e "$(BUILDDIR)/.nojekyll" ]
	ln -s /usr/share/mathjax/ $(BUILDDIR)/_static/mathjax 2>/dev/null || true
	echo "  file://$(BUILDDIR)/index.html"
	echo "  $(URL)"
	echo


.SILENT: httpd
httpd:
	echo [$@]
	mkdir -pv $(BUILDDIR)
	ln -s $(SRCDIR)/404.txt $(BUILDDIR)/ 2>/dev/null || true
	tmux ls || true
	sh -c "builtin echo >/dev/tcp/$(IP)/$(PORT)" 2>/dev/null || \
		tmux new -d -c /tmp -s $(SESSION_HTTPD) " \
			echo; \
			echo \ \ $(URL); \
			echo; \
			qrencode -tUTF8 $(URL); \
			echo; \
			set -x; \
			busybox httpd -f -v -p $(IP):$(PORT) -h $(BUILDDIR) -c /etc/httpd.conf; \
		"
	tmux ls
	echo

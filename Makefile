MAKEFLAGS := $(MAKEFLAGS) --no-print-directory

# https://serverfault.com/a/1042167
BUILDDIR      := /tmp/un1gfn.github.io
IP            := $(shell ip -4 addr show wlp2s0 | awk '/inet / {print $$2}' | cut -d/ -f1)
# [1024,65535] are unprivileged
PORT          :=  $(shell \
	HASH="$$(cksum <<<"$(shell basename $(BUILDDIR))" | cut -d' ' -f 1)"; \
	echo $$((1024+HASH%(65535-1024+1))); \
)
URL           := http://$(IP):$(PORT)/
PROJ          := $(shell basename $(shell pwd))

# port:
# 	@echo '$(PORT)'

# Don't run in parallel,
# otherwise clean can remove newly-built pages because of race
.NOTPARALLEL:
default: clean httpd entr

# .SILENT: help
# help:
# 	sphinx-build -M help . "$(BUILDDIR)"

clean:
	shopt -s dotglob; rm -rf $(BUILDDIR)/*

.SILENT: entr
entr:
	@printf "\e]0;%s\a" $(PROJ)
	echo
	ls -d1 -- conf.py *.rst extension/* include/* static/* | entr $(MAKE) html

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
.SILENT: html
html:
%:
	# sphinx-build -M $@ . "$(BUILDDIR)"
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
	echo "  file://$(BUILDDIR)/index.html"
	echo "  $(URL)"
	echo

.SILENT: httpd
httpd:
	mkdir -pv $(BUILDDIR)
	if ! sh -c "builtin echo >/dev/tcp/$(IP)/$(PORT)" 2>/dev/null; then \
		( alacritty -t "httpd $(IP):$(PORT) ($(shell basename $(BUILDDIR)))" -e sh -c "\
			echo; \
			echo \ \ $(URL); \
			echo; \
			qrencode -tUTF8 $(URL); \
			echo; \
			sudo busybox httpd -f -vv -p $(IP):$(PORT) -u $(USER):$(USER) -h $(BUILDDIR) -c /etc/httpd.conf; \
		" & ); \
	fi

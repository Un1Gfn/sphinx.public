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
	@printf "\e]0;%s\a" $(shell basename $(shell pwd))
	echo
	ls -d1 -- conf.py *.rst extension/* include/* static/* | entr $(MAKE) html

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
.SILENT: html
html:
%:
	# sphinx-build -M $@ . "$(BUILDDIR)"
	sphinx-build -b $@ . $(BUILDDIR)
	[ -e "$(BUILDDIR)/.nojekyll" ]
	echo
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

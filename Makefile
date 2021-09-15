MAKEFLAGS := $(MAKEFLAGS) --no-print-directory

# https://serverfault.com/a/1042167
BUILDDIR      := /tmp/un1gfn.github.io
LINK          := $(HOME)/cgi/cgi-tmp/$(shell basename $(BUILDDIR))
LINK_REL      :=             cgi-tmp/$(shell basename $(BUILDDIR))
IP            := $(shell ip -4 addr show wlp2s0 | awk '/inet / {print $$2}' | cut -d/ -f1)

# Don't run in parallel,
# otherwise clean can remove newly-built pages because of race
.NOTPARALLEL:
default: clean lnk_and_httpd entr

# .SILENT: help
# help:
# 	sphinx-build -M help . "$(BUILDDIR)"

clean:
	@rm -fv $(LINK)
	rm -rf $(BUILDDIR)

.SILENT: entr
entr:
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
	printf "  file://%s\n" "$(BUILDDIR)/index.html"
	printf "  http://%s/%s/index.html\n" "$(IP)" "$(LINK_REL)"
	echo

.SILENT: lnk_and_httpd
lnk_and_httpd:
	mkdir -pv $(BUILDDIR)
	if [ ! -e "$(LINK)" ] && [ ! -L "$(LINK)" ]; then ln -sv '$(BUILDDIR)' '$(LINK)'; fi
	sh -c "builtin echo >/dev/tcp/$(IP)/80" 2>/dev/null || \
		( alacritty -t "httpd $(IP):80 ($(shell basename $(BUILDDIR)))" -e bash ~/cgi/httpd.sh & )

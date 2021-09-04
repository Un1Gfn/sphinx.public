# https://serverfault.com/a/1042167
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     := $(realpath .)
BUILDDIR      := /tmp/un1gfn.github.io
LINK          := $(HOME)/cgi/cgi-tmp/$(shell basename $(BUILDDIR))
IP            := $(shell ip -4 addr show wlp2s0 | awk '/inet / {print $$2}' | cut -d/ -f1)

# .PHONY: default help clean html entr # make[1]: Nothing to be done for 'html'.
.PHONY:   default help clean      entr

# Don't run in parallel,
# otherwise clean can remove newly-built pages because of race
.NOTPARALLEL:
default: clean lnk_and_httpd entr

.SILENT: help
help:
	$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean:
	@rm -fv '$(LINK)'
	shopt -s dotglob; rm -rf "$(BUILDDIR)"/*

.SILENT: entr
entr:
	echo
	ls -d1 -- conf.py *.rst extension/* include/* rtd_linux/* | entr $(MAKE) html

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
.SILENT: html
html:
%:
	# $(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) # $(BUILDDIR)/html
	$(SPHINXBUILD) -b $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) # $(BUILDDIR)
	[ -e "$(BUILDDIR)/.nojekyll" ]
	echo
	printf "  file://%s\n" "$(BUILDDIR)/index.html"
	printf "  http://%s/cgi-tmp/sphinx/index.html\n" "$(IP)"
	echo

# .SILENT: lnk_and_httpd
lnk_and_httpd:
	mkdir -pv $(BUILDDIR)
	if [ ! -e "$(LINK)" ] && [ ! -L "$(LINK)" ]; then ln -sv '$(BUILDDIR)' '$(LINK)'; fi
	sh -c "builtin echo >/dev/tcp/$(IP)/80" 2>/dev/null || \
		( alacritty -t "httpd $(IP):80 ($(shell basename $(BUILDDIR)))" -e bash ~/cgi/httpd.sh & )

# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     := $(realpath .)
BUILDDIR      := $(HOME)/cgi/cgi-tmp/sphinx
# BUILDDIR      := _build

# .PHONY: default help clean html entr # make[1]: Nothing to be done for 'html'.
.PHONY: default help clean entr

default: html

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean:
# 	-rm -r "$(BUILDDIR)"
	rm -rf "$(BUILDDIR)"

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
html:
%:
# 	$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) # $(BUILDDIR)/html
	$(SPHINXBUILD) -b $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) # $(BUILDDIR)
# 	sphinx.ext.githubpages
# 	touch "$(BUILDDIR)/.nojekyll"
	@echo
	@printf "  file://%s\n"                         \
		"$(BUILDDIR)/index.html"
# 	https://serverfault.com/a/1042167
	@printf "  http://%s/cgi-tmp/sphinx/index.html\n" \
		"$(shell ip -4 addr show wlp2s0 | awk '/inet / {print $$2}' | cut -d/ -f1)"
	@echo

entr:
	@echo
	ls -d1 -- conf.py *rst *txt extension/* | entr $(MAKE) html

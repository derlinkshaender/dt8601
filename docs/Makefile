# MakeFile for building all the docs at once.
# Inspired by the Makefile used by bazaar. 
# http://bazaar.launchpad.net/~bzr-pqm/bzr/2.3/
 
PYTHON = python
 
.PHONY: all clean html latexpdf epub htmlhelp
 
# Dependencies to perform before running other builds.
SPHINX_DEPENDENCIES = \
	de/Makefile
 
# Copy-paste the de Makefile everwhere its needed.
%/Makefile: de/Makefile
	$(PYTHON) -c "import shutil; shutil.copyfile('$<', '$@')"
 
# Make the HTML version of the documentation with correctly nested language folders.
html: $(SPHINX_DEPENDENCIES)
	cd de && make html LANG=de
	cd en && make html LANG=en
 
htmlhelp: $(SPHINX_DEPENDENCIES)
	cd de && make htmlhelp LANG=de
	cd en && make htmlhelp LANG=en
 
epub: $(SPHINX_DEPENDENCIES)
	cd de && make epub LANG=de
	cd en && make epub LANG=en
 
latexpdf: $(SPHINX_DEPENDENCIES)
	cd de && make latexpdf LANG=de
	cd en && make latexpdf LANG=en
 
clean:
	rm -rf build/*
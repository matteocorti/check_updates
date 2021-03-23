#!/bin/sh

PERL_FILES="check_updates t/*.t"
FILES="${PERL_FILES} AUTHORS COPYING COPYRIGHT Changes INSTALL Makefile.PL NEWS README.md TODO check_distribution.sh"

FAILED=

if ! perlcritic -1 ${PERL_FILES} ; then
    FAILED=1
fi

if grep -q '\t' ${FILES} ; then
    echo "Tabs"
    grep -n '\t' ${FILES}
    FAILED=1
fi

if grep -q '[[:blank:]]$' ${FILES} ; then
    echo "Blanks at the end of a line"
    grep -n '[[:blank:]]$' ${FILES}
    FAILED=1
fi

YEAR=$( date +"%Y" )
if ! grep  -q "(c) Matteo Corti, 2007-${YEAR}" README.md ; then
    echo "Wrong (c) in README.md"
    FAILED=1
fi
if ! grep -q "Copyright (c) 2007-${YEAR} Matteo Corti" COPYRIGHT ; then
    echo "Wrong (c) in COPYRIGHT"
    FAILED=1
fi
if ! grep -q "Copyright (c) 2007-${YEAR} Matteo Corti <matteo@corti.li>" check_updates ; then
    echo "Wrong (c) in check_updates"
    FAILED=1
fi

if [ -n "${FAILED}" ] ; then
    exit 1
else
    exit 0
fi

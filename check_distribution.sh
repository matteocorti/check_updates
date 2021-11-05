#!/bin/sh

PERL_FILES="check_updates t/*.t"
FILES="${PERL_FILES} AUTHORS COPYING COPYRIGHT Changes INSTALL Makefile.PL NEWS check_distribution.sh"
MARKDOWN_FILES="README.md"

FAILED=

# shellcheck disable=SC2250
for file in $FILES $PERL_FILES $MARKDOWN_FILES; do
    if ! [ -r "${file}" ]; then
        echo "${file} is missing"
        FAILED=1
    fi
done

if [ -n "${FAILED}" ]; then
    # skip the next tests as at leadt file is missing
    echo "Skipping the next tests as not all the files are present"
    exit 1
fi

# shellcheck disable=SC2086
if ! perlcritic -1 ${PERL_FILES}; then
    echo "Perl Critic failed"
    FAILED=1
fi

if uname -a | grep -q '^Linux'; then
    # shellcheck disable=SC2086
    if grep -P -q '\t' ${FILES} ${MARKDOWN_FILES}; then
        echo "Tabs"
        # shellcheck disable=SC2086
        grep -P -n '\t' ${FILES} ${MARKDOWN_FILES}
        FAILED=1
    fi
elif uname -a | grep -q '^Darwin'; then
    # shellcheck disable=SC2086
    if grep -E -q '\t' ${FILES} ${MARKDOWN_FILES}; then
        echo "Tabs"
        # shellcheck disable=SC2086
        grep -E -n '\t' ${FILES} ${MARKDOWN_FILES}
        FAILED=1
    fi
else
    echo "Unable to check for tabs"
    FAILED=1
fi

# shellcheck disable=SC2086
if grep -q '[[:blank:]]$' ${FILES}; then
    echo "Blanks at the end of a line"
    # shellcheck disable=SC2086
    grep -n '[[:blank:]]$' ${FILES}
    FAILED=1
fi

YEAR=$(date +"%Y")
if ! grep -q "&copy; Matteo Corti, 2007-${YEAR}" README.md; then
    echo "Wrong (c) in README.md"
    FAILED=1
fi
if ! grep -q "Copyright (c) 2007-${YEAR} Matteo Corti" COPYRIGHT; then
    echo "Wrong (c) in COPYRIGHT"
    FAILED=1
fi
if ! grep -q "Copyright (c) 2007-${YEAR} Matteo Corti <matteo@corti.li>" check_updates; then
    echo "Wrong (c) in check_updates"
    FAILED=1
fi

if [ -n "${FAILED}" ]; then
    exit 1
else
    exit 0
fi

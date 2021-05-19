#!/bin/sh

VERSION=$( grep "our\ \$VERSION\ =\ " check_updates | sed "s/^[^']*'\([0-9.]*\)';/\1/" )

echo "Publishing release ${VERSION}"

echo 'RELEASE_NOTES.md:'
echo '------------------------------------------------------------------------------'

cat RELEASE_NOTES.md

echo '------------------------------------------------------------------------------'

echo 'Did you update the RELEASE_NOTES.md? '
read -r ANSWER
if [ "x${ANSWER}" = "xy" ] ; then

    perl Makefile.PL
    make dist
    gh release create "v${VERSION}" --title "check_updates-${VERSION}" --notes-file RELEASE_NOTES.md "check_updates-${VERSION}.tar.gz"

fi

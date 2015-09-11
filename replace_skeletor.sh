#!/bin/bash

if [ $# -lt 1 ] ; then
    echo "Usage: $0 name"
    exit 1
fi

NAME=$1

find . -type f | xargs sed -i -e "s/skeletor/$NAME/g"

mv skeletor $NAME
for FILE in `find . -name "skeletor*"`; do
    mv $FILE ${FILE//skeletor/$NAME}
done

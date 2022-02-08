#!/bin/bash

set +ex

DECODER_ZIP="decoder.zip"
OUTPUTS_ZIP="outputs.zip"

TMP_SERVER_DIR=unpacker

if [[ -d $TMP_SERVER_DIR ]]; then
   rm -rf $TMP_SERVER_DIR
fi

# The server puts yor zip files into
# a temp folder...
mkdir -p $TMP_SERVER_DIR
cp $DECODER_ZIP $TMP_SERVER_DIR
cp $OUTPUTS_ZIP $TMP_SERVER_DIR

pushd $TMP_SERVER_DIR
unzip $DECODER_ZIP
# ...then calls decode
./decode

popd
rm -rf $TMP_SERVER_DIR
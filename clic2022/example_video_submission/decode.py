#!/usr/bin/env python3

from typing import Sequence

import decode_helper

import os
import glob
from zipfile import ZipFile


FILES_ZIP = 'outputs.zip'


def unpack_encoded() -> Sequence[str]:
    assert os.path.isfile(FILES_ZIP), 'Expected {}. {}'.format(
        FILES_ZIP, os.listdir("."))

    print('Unzipping', FILES_ZIP, '...')
    with ZipFile(FILES_ZIP) as zipfile:
        zipfile.extractall()

    encoded_files = sorted(glob.glob("output/*.mp4"))
    if len(encoded_files) != 30:
        files = os.listdir(".")
        files_output = os.listdir("output")
        raise ValueError(
            f'Expected 30 .mp4 files, found {len(encoded_files)}. '
            f'Files in cwd: {files} // '
            f'Files in output: {files_output}')

    return encoded_files


def main():
    encoded = unpack_encoded()
    print(f'Got {len(encoded)} files, mapping to pngs...')
    for i, p in enumerate(encoded, 1):
        decode_helper.convert_video_to_pngs(p)
        print(f"Converted {i}/{len(encoded)}")


if __name__ == '__main__':
    main()

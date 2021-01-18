# clic2021-devkit  

Challenge homepage: [compression.cc](http://www.compression.cc).

The following helps working with the **Video challenge**.

## Downloading data

To download all files, run:

```bash
bash download.sh path/to/data
```

It will create a folder `path/to/data` and extract all frames there, into a structure like:

```
video1/
    video1_frame1_y.png
    video1_frame1_u.png
    video1_frame1_v.png
    video1_frame2_y.png
    video1_frame2_u.png
    video1_frame2_v.png
    ...
video2/
    video2_frame1_y.png
    video2_frame1_u.png
    video2_frame1_v.png
    ...
```

For this, one of `gsutil`, `wget`, or `curl` must be available. `gsutil` is probably the most efficient way.

To download only some videos, use `--max_vides`: `bash download.sh path/to/data --max_videos 10`

**NOTE**: The script first downloads all vidoes as .zip files, resulting in 250GB+ of data.
Then all zips are decompressed one by one and subsequently deleted. If you interrupt the script
while unpacking, and later re-run it, it will re-download those that were already unpacked.
To prevent this at the expense of more hard-drive space used, you can keep the zip files by passing `--no_delete_zip`.

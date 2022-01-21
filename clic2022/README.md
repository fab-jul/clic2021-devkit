
# Video Challenge: Format 

We expect the decoder to output Y, U, V as separate (single-channel) PNGs.
The U, V PNGs are expected to have half the size of the Y PNGs.

The files must be outputed in the following structure:

```
out_root_dir/
  video_name_1/
    {frame_idx:05d}_y.png  # Note that `frame_idx` must start at 1
    {frame_idx:05d}_u.png
    {frame_idx:05d}_v.png
```

For example:

```
out_root_dir/
    60c4bc5c67871f7ce8cf00b6c6b939a96434e2bc9919ad2f2002c65dac9f2b00/
      00001_y.png
      00001_u.png
      00001_v.png
      00002_y.png
      00002_u.png
      00002_v.png
      00003_y.png
      00003_u.png
      00003_v.png
      ...
    76869d54aa334fb9860e13dae8701bdeb4e51dfcd18a106d9951f861a412e301/
      00001_y.png
      00001_u.png
      00001_v.png
      ...
```
        
We provide a script to convert the .mp4s of the validation set
into PNGs *of the required format*:

```bash
python convert_to_pngs.py path/to/where/you/extracted/videos.zip \
  --png_out_root path/to/output --num_processes 8
```

**NOTE:** This expands the validation set to ~100GB.

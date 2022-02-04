
# Video Challenge: Format 

We expect the decoder to output Y, U, V as separate (single-channel) PNGs.
The U, V PNGs are expected to have half the size of the Y PNGs.

The files must be outputed in the following structure:

```
out_root_dir/
  {video_name_1}_{frame_idx:05d}_y.png  # Note: `frame_idx` must start at 1
  {video_name_1}_{frame_idx:05d}_u.png  
  {video_name_1}_{frame_idx:05d}_v.png  
  {video_name_2}_{frame_idx:05d}_y.png  
  ...
```

For example:

```
out_root_dir/
    60c4bc5c67871f7ce8cf00b6c6b939a96434e2bc9919ad2f2002c65dac9f2b00_00001_y.png
    60c4bc5c67871f7ce8cf00b6c6b939a96434e2bc9919ad2f2002c65dac9f2b00_00001_u.png
    60c4bc5c67871f7ce8cf00b6c6b939a96434e2bc9919ad2f2002c65dac9f2b00_00001_v.png
    60c4bc5c67871f7ce8cf00b6c6b939a96434e2bc9919ad2f2002c65dac9f2b00_00002_y.png
    60c4bc5c67871f7ce8cf00b6c6b939a96434e2bc9919ad2f2002c65dac9f2b00_00002_u.png
    60c4bc5c67871f7ce8cf00b6c6b939a96434e2bc9919ad2f2002c65dac9f2b00_00002_v.png
    ...
    76869d54aa334fb9860e13dae8701bdeb4e51dfcd18a106d9951f861a412e301_00001_y.png
    76869d54aa334fb9860e13dae8701bdeb4e51dfcd18a106d9951f861a412e301_00001_u.png
    ...
```
        
We provide a script to convert the .mp4s of the validation set
into PNGs *of the required format*:

```bash
python convert_to_pngs.py path/to/where/you/extracted/videos.zip \
  --png_out_root path/to/output --num_processes 8
```

**NOTE:** This expands the entire validation set to ~100GB.

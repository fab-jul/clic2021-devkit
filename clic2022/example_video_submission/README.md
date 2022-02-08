# Example Video Submission

This directory contains an example video submission.

You would use it as follows:

## Get validation videos

Download the 30 validation videos from the [website](http://compression.cc/tasks).

## Encode validation videos with the encoder.

```sh
python3 encode.py path/to/validation/videos --output_dir=output
zip outputs.zip -r output 
```

This will create a `output.zip` file that stores the encoded videos.
Note that the example encoder uses H264 for this.

## Package the decoder

The submission server expects a decoder.zip file. 
For the example submission, it can be creates as follows

```sh
chmod +x decode
zip decoder.zip decode decode.py decode_helper.py
```

Note that we package three files. The server will then unpack the zip
and execute `decode`. For us, `decode` just calls the python version:

```
# Our decode
#!/bin/bash
python3 decode.py
```

But you could do more complicated things. See also `simuilate_server_decode.sh`.

## Test locally

```sh
bash simulate_server_decode.sh
```

## Upload to the server

Go to [the submission page (TODO)](TODO), and upload the
two zip files.

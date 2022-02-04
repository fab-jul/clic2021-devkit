"""Example encoder.

Note that it produces a output folder
that must then be zipped for the server.

It uses H264 as an encoder, with a 1mbps target bitrate.
"""
import argparse
from concurrent import futures
import glob
import subprocess
import os

from typing import Sequence


def _encode(video_path, output_dir):
    out_path = os.path.join(output_dir, os.path.basename(video_path))
    subprocess.run([
        "ffmpeg", "-i", video_path,  
        "-c:v", "libx264",
        "-b:v", "1M",  # Target 1mbps
        "-maxrate", "1M", "-bufsize", "1M",
        out_path,
    ], check=True, capture_output=True)
    return out_path


def encode(video_paths: Sequence[str],
           output_dir: str,
           num_processes: int = 8):
    print(f"Starting conversion with {num_processes} processes...")
    if os.path.isdir(output_dir):
        raise ValueError("Output dir already exists!")
    os.makedirs(output_dir)
    pool = futures.ProcessPoolExecutor(num_processes)
    futs = []
    for video_path in video_paths:
        futs.append(
            pool.submit(_encode, video_path, output_dir=output_dir))
    for i, fut in enumerate(futures.as_completed(futs), 1):
        out_p = fut.result()
        print(f"{i}/{len(futs)}: {out_p}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("path_of_videos",
                   help="Folder with 30 mp4.s")
    p.add_argument("--output_dir", help="Where to store the output.",
                   required=True)
    p.add_argument("--num_processes", type=int, default=4,
                   help="How many processes (cores) to use for conversion.")
    flags = p.parse_args()

    videos = glob.glob(os.path.join(flags.path_of_videos, "*.mp4"))
    if len(videos) != 30:
        raise ValueError("Expected exactly 30 videos!")
    encode(videos, flags.output_dir, flags.num_processes)


if __name__ == "__main__":
    main()
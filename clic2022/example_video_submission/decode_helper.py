"""Showcase how to use multiple files in the decoder."""

import os
import subprocess


def convert_video_to_pngs(video_path: str):
    """Converts `video_path` to pngs in the current working directory."""
    video_name = os.path.basename(os.path.splitext(video_path)[0])
    out_path_base = video_name + "_%05d"
    subprocess.run([
        "ffmpeg", "-i", video_path, "-filter_complex", "extractplanes=y+u+v[y][u][v]",
        "-map", "[y]", out_path_base + "_y.png",
        "-map", "[u]", out_path_base + "_u.png",
        "-map", "[v]", out_path_base + "_v.png",
    ], check=True, capture_output=True)

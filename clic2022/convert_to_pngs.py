import argparse
import glob
import os
import subprocess
from concurrent import futures

from typing import Sequence


EXPECTED_FOLDERS = ["general", "webcam", "near_lossless"]


def _convert_video_to_pngs(video_path: str, png_out_root: str):
    video_name = os.path.basename(os.path.splitext(video_path)[0])
    out_path_base = os.path.join(
        png_out_root, video_name, "%05d")
    os.makedirs(os.path.dirname(out_path_base), exist_ok=True)

    subprocess.run([
        "ffmpeg", "-i", video_path, "-filter_complex", "extractplanes=y+u+v[y][u][v]",
        "-map", "[y]", out_path_base + "_y.png",
        "-map", "[u]", out_path_base + "_u.png",
        "-map", "[v]", out_path_base + "_v.png",
    ], check=True, capture_output=True)

    return os.path.dirname(out_path_base)


def convert_videos_to_pngs(video_paths: Sequence[str],
                           png_out_root: str,
                           num_processes: int = 8):
    pool = futures.ProcessPoolExecutor(num_processes)
    futs = []
    for video_path in video_paths:
        futs.append(
            pool.submit(_convert_video_to_pngs, 
                        video_path, png_out_root=png_out_root))
    for i, fut in enumerate(futures.as_completed(futs), 1):
        out_p = fut.result()
        print(f"{i}/{len(futs)}: {out_p}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("dataset_download_location",
                   help="Where you extracted the videos.zip file.")
    p.add_argument("--png_out_root", help="Root dir of where to store PNGs.",
                   required=True)
    flags = p.parse_args()

    dataset_download_location = flags.dataset_download_location
    png_out_root = flags.png_out_root
    
    video_paths = []
    for folder in EXPECTED_FOLDERS:
        full_folder_path = os.path.join(dataset_download_location, folder)
        if not os.path.isdir(full_folder_path):
            raise ValueError(f"Expected {full_folder_path}!")
        video_paths_of_folder = sorted(
            glob.glob(os.path.join(full_folder_path, "*.mp4")))
        if not video_paths_of_folder:
            raise ValueError(f"No mp4 found in {video_paths_of_folder}")
        video_paths += video_paths_of_folder

    convert_videos_to_pngs(video_paths, png_out_root)


if __name__ == "__main__":
    main()
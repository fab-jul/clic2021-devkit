import glob
import sys
import argparse
import os
import re


_SUFFIXES = ('_y.png', '_u.png', '_v.png')

_COMPONENTS_RE = re.compile(r'(.*?)_(\d{5})_([yuv]\.png)')

_COMPONENTS_RE_SUB = r'\1_{:05d}_\3'


def get_yuv_globs(data_root):
    """
    Expected structure:
    `data_root`/
        video1/
            video1_frame1_y.png
            video1_frame1_u.png
            video1_frame1_v.png
            video1_frame2_y.png
            ...
        video2/
            video2_frame1_y.png
            video2_frame1_u.png
            video2_frame1_v.png
            video2_frame2_y.png
            ...
        ...
    :returns globs (as strings) for Y, U, V frames
    """
    y_glob, u_glob, v_glob = (os.path.join(data_root, '*', '*' + suffix)
                              for suffix in _SUFFIXES)
    return y_glob, u_glob, v_glob


def get_paths_for_frame_sequences(data_root, num_frames_per_sequence):
    """
    Returns a list of tuples, where each tuple is a tuple of strings, and the strings are paths, representing:
    :return [((f11_y, f11_u, f11_v), (f12_y, f12_u, f12_v)),  # tuple for video 1, frame 1, 2
             ((f12_y, f12_u, f12_v), (f13_y, f13_u, f13_v)),  # tuple for video 1, frame 2, 3
             ...                                              # rest of video 1
             ((f21_y, f21_u, f21_v), (f22_y, f22_u, f22_v)),  # tuple for video 2, frame 1, 2
             ((f22_y, f22_u, f22_v), (f23_y, f23_u, f23_v)),  # tuple for video 2, frame 2, 3
             ...
    """
    globs = get_yuv_globs(data_root)
    y_ps, u_ps, v_ps = (sorted(p for p in glob.glob(g)) for g in globs)
    assert len(y_ps) == len(u_ps) == len(v_ps)
    assert len(y_ps) > 0, 'No frames in {}'.format(data_root)
    out = []
    for y_p, u_p, v_p in zip(y_ps, u_ps, v_ps):
        # first frame of the sequence
        seq = [(y_p, u_p, v_p)]
        # get subsequent frames
        for offset in range(1, num_frames_per_sequence):
            yi_p, ui_p, vi_p = (get_frame_path(p, offset=offset) for p in (y_p, u_p, v_p))
            if not os.path.isfile(yi_p):
                # This happens on the final frame of the video, when no subsequent frames are available!
                seq = None
                break
            seq.append((yi_p, ui_p, vi_p))
        if seq:
            assert len(seq) == num_frames_per_sequence
            out.append(tuple(seq))
    return out


def get_previous_frame_path(p):
    """Vlog_720P-7b30_00338_u.png"""
    return get_frame_path(p, offset=-1)


def get_frame_path(p, offset):
    """
    INPUT a frame path `p` of the format NAME_INDEX_SUFFIX, where
        - NAME is the video name
        - INDEX is a five-digit number indexing the video
        - SUFFIX is one of (_y.png, _u.png, _v.png)
    :returns NAME_NEWINDEX_SUFFIX, where NEWINDEX = INDEX + `offset`.
    """
    dirname, basename = os.path.split(p)
    m = _COMPONENTS_RE.search(basename)
    if not m:
        raise ValueError('Invalid format: {}'.format(p))
    try:
        number = int(m.group(2))
    except ValueError:
        raise ValueError('Invalid format: {}'.format(p))
    new_number = number + offset
    new_basename = _COMPONENTS_RE.sub(_COMPONENTS_RE_SUB.format(new_number), basename)
    return os.path.join(dirname, new_basename)


def validate_data(data_root):
    """ Check if for every frame we have Y, U, V files. """
    # check all files are available
    globs = get_yuv_globs(data_root)
    all_ps = tuple(sorted(glob.glob(g)) for g in globs)
    assert len(all_ps[0]) > 0, 'No files found in {}'.format(data_root)
    # get a set of prefixes for each Y, U, V by replacing the suffix of each path
    ys_pre, us_pre, vs_pre = (set(re.sub(suffix + '$', '', p) for p in ps)
                              for suffix, ps in zip(_SUFFIXES, all_ps))
    if not (len(ys_pre) == len(us_pre) == len(vs_pre)):
        _print_validation_error(ys_pre, us_pre, vs_pre)
        return 1

    print('Found {} frames, and Y, U, V for each.'.format(len(ys_pre)))
    # just checking that this runs:
    ps = get_paths_for_frame_sequences(data_root, num_frames_per_sequence=2)
    print('Found {} frame-sequences.'.format(len(ps)))
    return 0


def _print_validation_error(ys_pre, us_pre, vs_pre):
    all_frames = ys_pre | us_pre | vs_pre
    ys_missing, us_missing, vs_missing = (all_frames - pre for pre in (ys_pre, us_pre, vs_pre))
    print('ERROR:\nMissing Y for: {}\nMissing U for: {}\nMissing V for: {}'.format(
            ys_missing or '-', us_missing or '-', vs_missing or '-'))


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--validate', metavar='DATA_ROOT_FOLDER')
    flags = p.parse_args()
    if flags.validate:
        sys.exit(validate_data(flags.validate))


if __name__ == '__main__':
    main()



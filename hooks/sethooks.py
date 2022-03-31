#!/usr/bin/env python3

from pathlib import Path

p = Path('.')
source = p / Path('../.git/hooks')

commit_file = Path('commit-msg')
merge_file = Path('post-merge')

dest_commit = source / commit_file
dest_merge = source / merge_file

if dest_commit.is_file():
    print(f"REMOVING EXISTING FILE {dest_commit}")
    dest_commit.unlink()

if dest_merge.is_file():
    print(f"REMOVING EXISTING FILE {dest_merge}")
    dest_merge.unlink()

dest_commit.symlink_to((p / commit_file).resolve())
dest_merge.symlink_to((p / merge_file).resolve())

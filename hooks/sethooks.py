#!/usr/bin/env python3

from pathlib import Path

p = Path('.')
source = p / Path('../.git/hooks')

commit_file = Path('commit-msg')
merge_file = Path('post-merge')

(source / commit_file).symlink_to((p / commit_file).resolve())
(source / merge_file).symlink_to((p / merge_file).resolve())

from __future__ import print_function
from __future__ import division

import os
import sys
from pdb import set_trace
from glob2 import glob

root = os.path.join(os.getcwd().split("src")[0], "src")
if root not in sys.path:
    sys.path.append(root)


def get_jar_paths():
    project_dir = os.path.join(root, "data/java/raw/")
    projects = glob(os.path.join(project_dir,"*"))
    path_dict = dict()
    for project in projects:
        files = glob(os.path.join(project, "**/*.jar"))
        for f in files:
            name = f.split("raw")[0]
            set_trace()
    pass


if __name__ == "__main__":
    get_jar_paths()

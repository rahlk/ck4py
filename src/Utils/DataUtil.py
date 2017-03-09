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
    for project in projects:
        files = glob(os.path.join(project, "**/*.jar"))
        set_trace()
    pass


if __namane__ == "__main__":
    get_jar_paths()

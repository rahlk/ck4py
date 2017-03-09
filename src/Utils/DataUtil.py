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
    projects = glob(os.path.join(project_dir, "*"))
    path_dict = dict()
    for project in projects:
        files = glob(os.path.join(project, "**/*.jar"))
        for f in files:
            chunks = f.split("raw")[1].split("/")[1:]
            print(chunks[:2])
            try:
                path_dict[chunks[0]][chunks[1]].append(f)
            except Exception as e:
                if chunks[0] in e:
                    set_trace()
                    path_dict.update({
                        chunks[0]: {
                            chunks[1]: [f]
                        }})
                elif chunks[1] in e:
                    set_trace()
                    path_dict[chunks[0]].update({chunks[1]: [f]})


        set_trace()
    pass


if __name__ == "__main__":
    get_jar_paths()

from __future__ import print_function
from __future__ import division

import os
import sys
from pdb import set_trace
from glob2 import glob
from pprint import pprint
import json

root = os.path.join(os.getcwd().split("src")[0], "src")
if root not in sys.path:
    sys.path.append(root)


def get_jar_paths():
    project_dir = os.path.join(root, "data/java/")
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
                    path_dict.update({
                        chunks[0]: {
                            chunks[1]: [f]
                        }})
                elif chunks[1] in e:
                    path_dict[chunks[0]].update({chunks[1]: [f]})

    with open(os.path.join(project_dir, 'paths.json'), 'w') as fp:
        json.dump(path_dict, fp, sort_keys=True, indent=2)

    pass


def create_find_bugs_project(jar_path):

    all_jars = json.load(open(jar_path))
    project_dir = os.path.join(root, "data/java/fbp/")

    def warp_fbp(version, jarfiles):
        wrapped_paths = "\n\t".join(["<Jar>{}</Jar>".format(path) for path in jarfiles])
        return '<Project projectName="{}">\n\t{}\n</Project>'.format(version,wrapped_paths)


    for project, jar in all_jars.iteritems():

        fbp_dir = os.path.abspath(os.path.join(project_dir,project))

        if not os.path.isdir(fbp_dir):
            os.mkdir(fbp_dir)

        for version, jarfiles in jar.iteritems():
            fbp_file = os.path.join(fbp_dir, version+".fbp")
            fbp_text = warp_fbp(version, jarfiles)
            print(fbp_text, file=open(fbp_file, "w+"))


if __name__ == "__main__":
    create_find_bugs_project(
        jar_path=os.path.join(root, "data/java/", 'paths.json'))

    # get_jar_paths()

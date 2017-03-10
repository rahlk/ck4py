from __future__ import division
from __future__ import print_function

import os
import subprocess
from pdb import set_trace
import json

from FileUtils import XMLUtil

root = os.getcwd()


class JavaUtil:
    def __init__(self, jar_path_json, save_path="metrics", file_name="metrics"):

        self.jar_path = jar_path_json
        self.file_name = file_name if ".xml" in file_name else file_name + ".xml"

        self.save_path = os.path.abspath(save_path)

    def _run_ckjm(self):
        cmd = ["java", "-jar", os.path.join(root, "tools/ckjm_ext.jar"),
               "-x",
               "-s",
               self.jar_file]

        return subprocess.Popen(cmd, stdout=subprocess.PIPE
                                , stderr=open(os.devnull, "w"))

    def _run_findbugs(self):
        cmd = [os.path.join(root, "tools/findbugs-3.0.1/bin/findbugs"),
               "-textui",
               "-project", self.fbp_file,
               "-xml", "-outputFile",
               os.path.join(self.save_path, "bugs-" + self.file_name)]
        return subprocess.Popen(cmd, stdout=subprocess.PIPE
                                , stderr=open(os.devnull, "w"))

    def save_metrics(self):


        metrics = self._run_ckjm().communicate()[0]
        foundbugs = self._run_findbugs().communicate()[0]

        print("<metrics>", metrics, "</metrics>", sep="\n",
              file=open(os.path.join(self.save_path, self.file_name), "w+"))


class JSUtil:
    def __init__(self, js_path, save_path="metrics", file_name="metrics"):
        self.file_name = file_name if ".json" in file_name else file_name + ".json"
        self.js_path = os.path.abspath(js_path)
        self.save_path = os.path.abspath(os.path.join(root, save_path))

    def run_escomplex(self):
        cmd = ["cr", "--ignoreerrors", "--output"
            , os.path.join(self.save_path, self.file_name),
               "--format", "json",
               self.js_path]
        return subprocess.Popen(cmd, stdout=subprocess.PIPE
                                , stderr=open(os.devnull, "w"))

    def save_metrics(self):
        metrics = self.run_escomplex().communicate()[0]
        return


def __test_util():
    """
    Run a test case
    :return:
    """
    m = JavaUtil(jar_file="data/ant-1.8.2/build/lib/ant.jar",
                 file_name="ant.xml")
    m.save_metrics()
    xml = XMLUtil(metrics_name="ant.xml")
    xml.save_as_csv()


if __name__ == "__main__":
    __test_util()
    set_trace()

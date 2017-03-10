from __future__ import division
from __future__ import print_function

import os
import subprocess
from pdb import set_trace

from FileUtils import XMLUtil

root = os.getcwd()


class JavaUtil:
    def __init__(self, jar_path_json, fbp_path, save_path="metrics", file_name="metrics"):

        self.jar_path = jar_path_json
        self.fbp_path = fbp_path
        self.file_name = file_name if ".xml" in file_name else file_name + ".xml"

        self.save_path = os.path.abspath(save_path)

    @staticmethod
    def _run_ckjm(jar):
        cmd = ["java", "-jar", os.path.join(root, "tools/ckjm_ext.jar"),
               "-x",
               "-s",
               jar]

        return subprocess.Popen(cmd, stdout=subprocess.PIPE
                                , stderr=open(os.devnull, "w"))

    @staticmethod
    def _run_findbugs(fbp_file):
        cmd = [os.path.join(root, "tools/findbugs-3.0.1/bin/findbugs"),
               "-textui", "-project", fbp_file, "-xml"]

        return subprocess.Popen(cmd, stdout=subprocess.PIPE
                                , stderr=open(os.devnull, "w"))

    def save_metrics(self):

        for version, jarfiles in self.jar_path.iteritems():
            metrics = []
            fbp_file = os.path.join(self.fbp_path, version+".fbp")
            print("\t+ Version: {}".format(version))
            print("\t+ -- Computing CK Metrics")
            for jar in jarfiles:
                metrics.append(self._run_ckjm(jar).communicate()[0])

            print("\t+ -- Running FindBugs")
            foundbugs = self._run_findbugs(fbp_file).communicate()[0]

            print(foundbugs,
                file=open(os.path.join(self.save_path, "bug-"+version+".xml"), "w+"))
            print("<metrics>", "\n".join(metrics), "</metrics>", sep="\n",
                file=open(os.path.join(self.save_path, version+".xml"), "w+"))


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

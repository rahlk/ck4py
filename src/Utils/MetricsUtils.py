from __future__ import print_function
from __future__ import division
import os
import subprocess
import numpy as np
import pandas as pd
from pdb import set_trace
import xml.etree.ElementTree as ET
import json


root = os.getcwd()


class JavaMetricsUtil:

    def __init__(self, jar_file, class_path=None, save_path="metrics",
                 file_name="metrics"):
        self.file_name = file_name if ".xml" in file_name else file_name + ".xml"
        self.jar_file = os.path.abspath(jar_file)
        self.save_path = os.path.abspath(save_path)
        self.class_path = os.path.abspath(class_path) if class_path else None

    def run_ckjm(self):
        cmd = ["java", "-jar", os.path.join(root, "jar/ckjm_ext.jar"),
               "-x",
               "-s",
               self.jar_file]

        return subprocess.Popen(cmd, stdout=subprocess.PIPE
                                , stderr=open(os.devnull, "w"))

    @staticmethod
    def qmood():
        return

    def save_metrics(self, as_xml=False):
        metrics = self.run_ckjm().communicate()[0]
        print("<metrics>", metrics, "</metrics>", sep="\n",
              file=open(os.path.join(self.save_path, self.file_name), "w+"))


class JSMetricsUtil:

    def __init__(self, js_path, save_path="metrics", file_name="metrics"):
        self.arg = arg
        self.file_name = file_name if ".json" in file_name else file_name + ".json"
        self.js_path = os.path.abspath(js_path)
        self.save_path = os.path.abspath(os.path.join(root, save_path))
        self.class_path = os.path.abspath(class_path) if class_path else None

    def run_escomplex(self):
        cmd = ["cr", "--ignoreerrors", "--output"
                , os.path.join(self.save_path, self.file_name),
                "--format json",
                self.js_path]
        return subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                   , stderr=open(os.devnull, "w"))

    def save_metrics(self):
        metrics = run_escomplex()
        

def __test_util():
    """
    Run a test case
    :return:
    """
    m = MetricUtil(jar_file="data/ant-1.8.2/build/lib/ant.jar",
                   file_name="ant.xml")
    m.save_metrics()
    xml = XMLUtil(xml_name="ant.xml")
    xml.as_csv()


if __name__ == "__main__":
    __test_util()
    set_trace()

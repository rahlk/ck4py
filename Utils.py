from __future__ import print_function
from __future__ import division
import os
import sys
import csv
import subprocess
from pdb import set_trace
import xml.etree.ElementTree as ET

root = os.getcwd()

class XMLUtil:
    def __init__(self, xml_path="metrics", xml_name="metrics.xml"):
        self.xml_path = xml_path
        self.xml_name = xml_name

    def as_list(self):
        tree = ET.parse(os.path.join(self.xml_path, self.xml_name))
        root = tree.getroot()
        

    def as_DataFrame(self):



class MetricUtil:
    def __init__(self, jar_file, class_path=None, save_path="Metrics", file_name="metrics"):
        self.file_name = file_name
        self.jar_file = jar_file
        self.save_path = save_path
        self.class_path = class_path

    def run_ckjm(self):
        cmd = ["java", "-jar", os.path.join(root, "jar/ckjm_ext.jar"), "-x", "-s",
               os.path.abspath(self.jar_path), ">",
               os.path.join(self.save_path, self.file_name+".xml")]
        return subprocess.Popen(cmd)

    @staticmethod
    def qmood():
        return

    def save_metrics(self, as_csv=True):
        return

    def get_metrics(self):

        return


if __name__ == "__main__":

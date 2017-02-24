from __future__ import print_function
from __future__ import division
import os
import sys
import csv
import subprocess
import numpy as np
import pandas as pd
from pdb import set_trace
import xml.etree.ElementTree as ET

root = os.getcwd()


class XMLUtil:
    def __init__(self, xml_path="metrics", xml_name="metrics.xml"):
        self.xml_path = os.path.abspath(xml_path)
        self.xml_name = xml_name if ".xml" in xml_name else xml_name + ".xml"

    def as_list(self):
        tree = ET.parse(os.path.join(self.xml_path, self.xml_name))
        root = tree.getroot()
        names = []
        metrics = []
        for member in root.iter("class"):
            values = []
            for child in member.iter():
                if child.tag != 'class':
                    if child.tag == 'cc':
                        if not "avg_cc" in names:
                            names.append("avg_cc")
                        if not "max_cc" in names:
                            names.append("max_cc")
                        cc = [float(child0.text) for child0 in child.iter() if
                              not child0.tag == 'cc']
                        try:
                            values.extend([np.mean(cc), np.max(cc)])
                        except ValueError:
                            values.extend([0, 0])
                    elif child.tag != "method":
                        if not child.tag in names:
                            names.append(child.tag)
                        try:
                            values.append(float(child.text))
                        except ValueError:
                            values.append(child.text)
            metrics.append(values)
        metrics.insert(0, names)
        return metrics

    def as_DataFrame(self):
        metrics = self.as_list()
        return pd.DataFrame(metrics[1:], columns=metrics[0])


class MetricUtil:
    def __init__(self, jar_file, class_path=None, save_path="Metrics",
                 file_name="metrics"):
        self.file_name = file_name
        self.jar_file = jar_file
        self.save_path = save_path
        self.class_path = class_path

    def run_ckjm(self):
        cmd = ["java", "-jar", os.path.join(root, "jar/ckjm_ext.jar"), "-x",
               "-s",
               os.path.abspath(self.jar_path), ">",
               os.path.join(self.save_path, self.file_name + ".xml")]
        return subprocess.Popen(cmd)

    @staticmethod
    def qmood():
        return

    def save_metrics(self, as_csv=True):
        return

    def get_metrics(self):
        return


if __name__ == "__main__":
    xml = XMLUtil(xml_name="ant.xml")
    set_trace()

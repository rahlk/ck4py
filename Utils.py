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
        self.xml_name = xml_name.split(".xml")[
            0] if ".xml" in xml_name else xml_name

    def as_list(self):
        tree = ET.parse(os.path.join(self.xml_path, self.xml_name + ".xml"))
        root = tree.getroot()
        names = []
        metrics = []
        for member in root.iter("class"):
            values = []
            for child in member.iter():
                if child.tag != 'class':
                    if child.tag == 'cc':
                        if "avg_cc" not in names:
                            names.append("avg_cc")
                        if "max_cc" not in names:
                            names.append("max_cc")
                        cc = [float(child0.text) for child0 in child.iter() if
                              not child0.tag == 'cc']
                        try:
                            values.extend([np.mean(cc), np.max(cc)])
                        except ValueError:
                            values.extend([0, 0])
                    elif child.tag != "method":
                        if child.tag not in names:
                            names.append(child.tag)
                        try:
                            values.append(float(child.text))
                        except ValueError:
                            values.append(child.text)
            metrics.append(values)
        metrics.insert(0, names)
        return metrics

    def as_dataframe(self):
        metrics = self.as_list()
        return pd.DataFrame(metrics[1:], columns=metrics[0])

    def as_csv(self):
        metrics_df = self.as_dataframe()
        metrics_df.to_csv(os.path.join(self.xml_path, self.xml_name + ".csv"))


class MetricUtil:
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


if __name__ == "__main__":
    m = MetricUtil(jar_file="data/ant-1.8.2/build/lib/ant.jar",
                   file_name="ant.xml")
    m.save_metrics()
    xml = XMLUtil(xml_name="ant.xml")
    xml.as
    set_trace()

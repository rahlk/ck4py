from __future__ import print_function
from __future__ import division
import os
import subprocess
import numpy as np
import pandas as pd
from pdb import set_trace
import xml.etree.ElementTree as ET
import json
from pprint import pprint

root = os.getcwd()


class JSONUtil:
    def __init__(self, json_path="metrics", json_name="metrics.json"):
        self.json_path = os.path.abspath(json_path)
        self.json_name = json_name.split(".json")[
            0] if ".json" in json_name else json_name

    @staticmethod
    def unpack_aggregate(aggregate_dict):
        for key, value in aggregate_dict.iteritems():
            

    def module_metrics(self):
        with open(os.path.join(self.json_path,
                               self.json_name + ".json")) as data_file:
            data = json.load(data_file)

        names = ["path", "dependencies", ""]

        return metrics

    def as_dataframe(self):
        metrics = self.as_list()
        return pd.DataFrame(metrics[1:], columns=metrics[0])

    def save_as_csv(self):
        metrics_df = self.as_dataframe()
        metrics_df.to_csv(os.path.join(self.json_path, self.json_name + ".csv"),
                          index=False)


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

    def save_as_csv(self):
        metrics_df = self.as_dataframe()
        metrics_df.to_csv(os.path.join(self.xml_path, self.xml_name + ".csv"),
                          index=False)

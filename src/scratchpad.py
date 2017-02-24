"""
Test code snippets for integration
"""
from __future__ import print_function
from __future__ import division
import os
import sys
import csv
import subprocess
from pdb import set_trace
import numpy as np
import pandas as pd

import xml.etree.ElementTree as ET


def xml2list():
    tree = ET.parse("metrics/ant.xml")
    root = tree.getroot()
    names = []
    metrics = []
    for member in root.iter("class"):
        values = []
        for child in member.iter():
            if child.tag!='class':
                if child.tag == 'cc':
                    if not "avg_cc" in names:
                        names.append("avg_cc")
                    if not "max_cc" in names:
                        names.append("max_cc")
                    cc = [float(child0.text) for child0 in child.iter() if not child0.tag == 'cc']
                    try:
                        values.extend([np.mean(cc), np.max(cc)])
                    except ValueError:
                        values.extend([0, 0])
                elif child.tag != "method":
                    if not child.tag in names:
                        names.append(child.tag)
                    values.append(child.text)
        metrics.append(values)
    set_trace()



if __name__ == "__main__":
    xml2list()

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
import xml.etree.ElementTree as ET


def xml2list():
    tree = ET.parse("metrics/ant.xml")
    root = tree.getroot()
    set_trace()
    pass


if __name__ == "__main__":
    xml2list()

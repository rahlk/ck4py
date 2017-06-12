from __future__ import division
from __future__ import print_function

import os
import json
from glob2 import glob
from pdb import set_trace
from utils.FileUtils import JSONUtil
from utils.MetricsUtil import JSUtil


def js_sample_case():

    m = JSUtil(js_path="data/javascript/react/",
               save_path="metrics",
               file_name="react")
    m.save_metrics()
    json = JSONUtil(json_name="react.json", json_path="metrics")
    json.save_as_csv()

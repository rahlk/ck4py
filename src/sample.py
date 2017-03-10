from __future__ import division
from __future__ import print_function

import os
from Utils.FileUtils import JSONUtil, XMLUtil
from Utils.MetricsUtil import JavaUtil, JSUtil
import json


def jar_sample_case():

    files = json.load(os.path.abspath(os.path.join(os.getcwd(), "data/java/paths.json")))
    fbp_path = os.path.abspath(os.path.join(os.getcwd(), "data/java/fbp/ant"))
    m = JavaUtil(jar_path_json=files["ant"],
                 fbp_path=fbp_path,
                 save_path="metrics")
    m.save_metrics()
    # xml = XMLUtil(metrics_name="ant.xml")
    # xml.save_as_csv()


def js_sample_case():
    m = JSUtil(js_path="data/javascript/react/",
               save_path="metrics",
               file_name="react")

    m.save_metrics()

    json = JSONUtil(json_name="react.json", json_path="metrics")
    json.save_as_csv()


if __name__ == "__main__":
    jar_sample_case()

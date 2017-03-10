from __future__ import division
from __future__ import print_function

import os
from Utils.FileUtils import JSONUtil, XMLUtil
from Utils.MetricsUtil import JavaUtil, JSUtil
import json
from glob2 import glob
import multiprocessing as mp


def jar_sample_case():

    files = json.load(open(os.path.abspath(os.path.join(os.getcwd(), "data/java/paths.json"))))

    for project, versions in files.iteritems():
        print("Project: {}".format(project))
        fbp_path = os.path.abspath(os.path.join(os.getcwd(), "data/java/fbp/{}".format(project)))
        save_path = "metrics/{}".format(project)

        m = JavaUtil(jar_path_json=version,
                     fbp_path=fbp_path,
                     save_path=save_path)

        if not os.path.isdir(save_path):
            os.mkdir(save_path)

        m.save_metrics()

        for metric_file in glob("mertics/{0}/*{0}-*.xml".format(project)):
            xml = XMLUtil(metrics_name=metric_file)
            xml.save_as_csv()

        set_trace()


def js_sample_case():
    m = JSUtil(js_path="data/javascript/react/",
               save_path="metrics",
               file_name="react")

    m.save_metrics()

    json = JSONUtil(json_name="react.json", json_path="metrics")
    json.save_as_csv()


if __name__ == "__main__":
    jar_sample_case()

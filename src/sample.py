from __future__ import division
from __future__ import print_function

import os
import json
from glob2 import glob
from pdb import set_trace
import multiprocessing as mp
from Utils.FileUtils import JSONUtil, XMLUtil
from Utils.MetricsUtil import JavaUtil, JSUtil


def par_deploy(dict_elem):
    project, versions = dict_elem
    print("Project: {}".format(project))
    fbp_path = os.path.abspath(os.path.join(os.getcwd(), "data/java/fbp/{}".format(project)))
    save_path = "metrics/{}".format(project)

    m = JavaUtil(jar_path_json=versions,
    fbp_path=fbp_path,
    save_path=save_path)

    if not os.path.isdir(save_path):
        os.mkdir(save_path)
        m.save_metrics()


def jar_sample_case():

    files = json.load(open(os.path.abspath(os.path.join(os.getcwd(), "data/java/paths.json"))))

    par_args = [(p,v) for p,v in files.iteritems()]

    # "Set up Parallel Environment"
    # N = len(par_args)  # Number of parallel processes to run
    # pool = mp.Pool(processes=N)  # Pool of processes
    # deployed = pool.map(par_deploy, par_args)
    # set_trace()

    for metric_file in glob("mertics/**/*.xml"):
        set_trace()
        xml = XMLUtil(metrics_name=metric_file)
        xml.save_as_csv()


def js_sample_case():
    m = JSUtil(js_path="data/javascript/react/",
               save_path="metrics",
               file_name="react")

    m.save_metrics()

    json = JSONUtil(json_name="react.json", json_path="metrics")
    json.save_as_csv()


if __name__ == "__main__":
    jar_sample_case()

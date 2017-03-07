from __future__ import division
from __future__ import print_function

from Utils.FileUtils import JSONUtil, XMLUtil
from Utils.MetricsUtil import JavaUtil, JSUtil


def jar_sample_case():
    m = JavaUtil(jar_file="data/java/raw/ant/ant-1.1/bin/jakarta-ant/lib/ant.jar",
                 fbp_file="data/java/fbp/ant/ant-1.1.fbp",
                 file_name="ant.xml")
    m.save_metrics()
    xml = XMLUtil(metrics_name="ant.xml")
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
    # js_sample_case()

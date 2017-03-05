from __future__ import division
from __future__ import print_function

from Utils.FileUtils import JSONUtil, XMLUtil
from Utils.MetricsUtils import JavaUtil, JSUtil


def jar_sample_case():
    m = JavaUtil(jar_file="data/java/ant-1.8.2/build/lib/ant.jar",
                 file_name="ant.xml")
    m.save_metrics()
    xml = XMLUtil(xml_name="ant.xml")
    xml.save_as_csv()


def js_sample_case():
    m = JSUtil(js_path="data/javascript/react/",
               save_path="metrics",
               file_name="react")

    m.save_metrics()

    json = JSONUtil(json_name="react.json", json_path="metrics")
    json.save_as_csv()


if __name__ == "__main__":
    js_sample_case()

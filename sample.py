from __future__ import print_function
from __future__ import division

from Utils import MetricUtil, XMLUtil


def sample_case():
    m = MetricUtil(jar_file="data/ant-1.8.2/build/lib/ant.jar",
                   file_name="ant.xml")
    m.save_metrics()
    xml = XMLUtil(xml_name="ant.xml")
    xml.as_csv()

if __name__ == "__main__":
    sample_case()

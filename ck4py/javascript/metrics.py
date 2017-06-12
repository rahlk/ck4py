from __future__ import division
from __future__ import print_function

import os
import sys
import json
from glob2 import glob
from pdb import set_trace
from utils.FileUtils import JSONUtil
from utils.MetricsUtil import JSUtil
from utils.git_core import Git


def compute_metrics(hash):
    m = JSUtil(git_url="https://github.com/facebook/react.git")
    m.fetch_project(hash)
    metrics = m.get_metrics()
    set_trace()


if __name__ == "__main__":
    compute_metrics(hash="30e6c6c9c9f8e52776981a0e91ccfbabb95f7974")

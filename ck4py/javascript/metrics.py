from __future__ import division
from __future__ import print_function

from pdb import set_trace
from ck4py.utils.MetricsUtil import JSUtil
import sys


def compute_metrics(git_site, git_hash):
    m = JSUtil(git_url=git_site)
    m.fetch_project(git_hash)
    metrics = m.get_metrics()
    # set_trace()
    return metrics


if __name__ == "__main__":
    git_site = sys.argv[1]
    git_hash = sys.argv[2]
    if len(sys.argv) != 3 or ".git" not in git_site:
        # Temporary Usage statement
        print("Usage: python metrics.py gitWebsite.git Hash")
    else:
        metrics = compute_metrics(git_site, git_hash)
        print(metrics)
    # compute_metrics(hash="30e6c6c9c9f8e52776981a0e91ccfbabb95f7974")

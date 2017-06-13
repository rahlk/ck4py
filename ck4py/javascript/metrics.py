from __future__ import division
from __future__ import print_function
import sys
from ck4py.utils.MetricsUtil import JSUtil



def compute_metrics(git_site, git_hash):
    m = JSUtil(git_url=git_site)
    m.fetch_project(git_hash)
    metrics = m.get_metrics()
    # set_trace()
    m.clean_up()
    return metrics


if __name__ == "__main__":
    arg_len = len(sys.argv)
    if arg_len != 3 or ".git" not in sys.argv[1]:
        # Temporary Usage statement
        print("Usage: python metrics.py gitWebsite.git Hash")
    else:
        metrics = compute_metrics(sys.argv[1], sys.argv[2])
        print(metrics)
    # git_site = sys.argv[1]
    # git_hash = sys.argv[2]
    # compute_metrics(hash="30e6c6c9c9f8e52776981a0e91ccfbabb95f7974")

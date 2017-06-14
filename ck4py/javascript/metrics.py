from __future__ import division
from __future__ import print_function
from ck4py.utils.MetricsUtil import JSUtil



def compute_metrics(git_site, git_hash):
    m = JSUtil(git_url=git_site)
    m.fetch_project(git_hash)
    metrics = m.get_metrics()
    m.isolate_changes(git_hash)
    m.clean_up()
    return metrics


if __name__ == "__main__":
    compute_metrics("https://github.com/facebook/react.git",
                    "30e6c6c9c9f8e52776981a0e91ccfbabb95f7974")

from __future__ import print_function, division
import os
import sys
import pandas as pd
from pdb import set_trace
from glob import glob
from tabulate import tabulate

def details(dir="./class/"):
    files = glob(os.path.join(os.path.abspath(dir), "*.csv"))
    head = ["Name", "Samples", "% Smelly"]
    rows = []
    for file in files:
        name = file.split("/")[-1].split(".csv")[0]
        dframe = pd.read_csv(file)
        N = len(dframe)
        p_smells = round(100 * sum([1 if s > 0 else 0 for s in dframe["SMELLS"].values]) / N, 0)
        if N>= 8:
            rows.append([name, N, p_smells])
        else:
            os.remove(file)

    stats = pd.DataFrame(rows, columns=head)
    stats.set_index("Name", inplace=False)
    stats.sort_values("Samples", ascending=False, inplace=True)
    print(tabulate(stats, headers=head, showindex="never", tablefmt="fancy_grid"))
    set_trace()


if __name__ == "__main__":
    details()

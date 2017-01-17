from __future__ import print_function, division
import os
import sys
import pandas as pd
from pdb import set_trace
from glob import glob
from tabulate import tabulate


def details():
    for dir in ["DataClass", "GodClass", "LongMethod", "FeatureEnvy"]:
        print(dir)
        head = ["Dataset", "Samples", " Smelly (%)", "# metrics", "Nature"]
        rows = []
        files = glob(os.path.join(os.path.abspath(dir), "*.csv"))
        nature = "Class" if dir == "DataClass" or dir == "GodClass" else "Method"
        for file in files:
            name = file.split("/")[-1].split(".csv")[0]
            name = name.split("-")[0][:10]
            dframe = pd.read_csv(file)
            N = len(dframe)
            n_metrics = len(dframe.columns)
            smells = sum([1 if s > 0 else 0 for s in dframe["SMELLS"].values])
            p_smells = round(100 * smells / N, 0)
            if N >= 8:
                rows.append([name, N, "{} ({})".format(smells, p_smells), n_metrics, nature])
            else:
                os.remove(file)

        stats = pd.DataFrame(rows, columns=head)
        stats.set_index("Dataset", inplace=False)
        stats.sort_values("Samples", ascending=False, inplace=True)
        stats.to_csv(os.path.abspath(os.path.join(".", dir+".csv")))
        print(tabulate(stats, headers=head, showindex="never"), end="\n\n")
    set_trace()


if __name__ == "__main__":
    details()

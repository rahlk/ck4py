from __future__ import print_function, division
import os
from scipy.io.arff import loadarff
import pandas as pd
from glob import glob
from pdb import set_trace



def bool_sum(a,b):
    if a and b:
        return 2
    if a or b:
        return 1
    else:
        return 0

def konvert():
    files = glob(os.path.join(os.path.abspath("./"), "*.csv"))

    file0 = pd.read_csv(files[0])
    head0 = file0.columns[:-1]
    depn0 = file0.columns[-1]

    file1 = pd.read_csv(files[1])
    head1 = file1.columns[:-1]
    depn1 = file1.columns[-1]

    heads = list(set(head0).intersection(head1))
    final = pd.concat([file0[heads], file1[heads]])
    smelly = [bool_sum(el1, el2) for el1, el2 in zip(file0[depn0].values, file1[depn1])]
    final["SMELLS"] = pd.Series(smelly)
    final.reset_index(inplace=True)
    N = len(final)
    for prj in list(set(final["project"].values.tolist())):
        filename = prj.split("/")[-1]+".csv"
        rows = [final.iloc[k].values.tolist()[1:] for k in xrange(N) if final.iloc[k]["project"] is prj]
        rows = pd.DataFrame(rows, columns=final.columns[1:])
        rows.drop("project", axis=1, inplace=True)
        rows.to_csv(filename, index=False)

    set_trace()


if __name__ == "__main__":
    konvert()

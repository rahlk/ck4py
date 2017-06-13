from __future__ import print_function
import os
import re
from shutil import rmtree
import subprocess
import pandas as pd
from pdb import set_trace


class Git:
    def __init__(self, project, url, clone_path):
        self.url = url
        self.project = project
        self.current = os.getcwd()
        self.clone_path = os.path.abspath(clone_path)

    def _local_clone(self):
        cmd = ["git", "clone", "--depth=1", self.url, self.clone_path]
        return subprocess.Popen(cmd, stdout=subprocess.PIPE
                                , stderr=open(os.devnull, "w")).communicate()[0]

    def _fetch(self, hash):
        if not os.path.isdir(self.clone_path) or hash is None:
            return self._local_clone()
        else:
            os.chdir(self.clone_path)
            cmd = ["git", "reset", "--hard", hash]
            os.chdir(self.current)
            return subprocess.Popen(cmd, stdout=subprocess.PIPE
                                    , stderr=open(os.devnull, "w")).communicate()[0]

    def get_commit_log(self):
        print("Clonning into: {}".format(self.url))
        self._local_clone()
        os.chdir(os.path.abspath(self.clone_path))
        cmd = ["git", "log", "--pretty=format:\"%H :: %s\""]
        print("\t+-- Getting commit logs.")
        log = subprocess.Popen(cmd, stdout=subprocess.PIPE
                               , stderr=open(os.devnull, "w")).communicate()[0]
        log = re.sub("\"", "", log)
        log = [l.split(" :: ") for l in log.split("\n")]
        os.chdir(self.current)
        commits = pd.DataFrame(log)
        return commits

    def fetch_commit_hash(self, hash):
        state = self._fetch(hash)
        print(state)


if __name__ == "__main__":
    git = Git(project="react", url="https://github.com/facebook/react.git", clone_path='./tmp/')
    git.fetch_commit_hash()
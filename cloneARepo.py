#!/usr/bin/python3
from git import Repo
import sys
import os.path as osp



HTTPS_REMOTE_URL = sys.argv[1]
DEST_NAME = sys.argv[2]

print ("cloning : " +  HTTPS_REMOTE_URL + "\nto :" + DEST_NAME )


cloned_repo = Repo.clone_from(HTTPS_REMOTE_URL, DEST_NAME)



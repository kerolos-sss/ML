#!/usr/bin/python3
from git import Repo
import sys
import os.path as osp



#TODO we may need to use a git credential manager or somting like .... https://stackoverflow.com/questions/44784828/gitpython-git-authentication-using-user-and-password


#we can manage for now by putting the password into the git url
# url for testing git auth
#url = "https://kerolos_innuva:passofkero123@bitbucket.org/kerolos_innuva/testgitauth.git"

#project url
url = "https://kerolos-sss@github.com/kerolos-sss/ML.git"


#TODO explore other git URI types

#destination directory
dest = "./testgitauth"

# HTTPS_REMOTE_URL = sys.argv[1]
# DEST_NAME = sys.argv[2]
def clone(url, dest):
    print ("cloning : " +  url + "\nto :" + dest )


    cloned_repo = Repo.clone_from(url, dest)

    print("Done")

if __name__ == "__main__":
    clone(url, dest)

    print("")

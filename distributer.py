#in repo have one 'uploaded' directory
#all files not in there go to appropriate locations
#then those dirs are moved to 'uploaded' and program 
#pushes to git 

import time
import git
from git import Repo
from privateData import pwd
from github_pusher import toGitHub
import csv
import subprocess
import shutil
import os
import stat
from os import path
from getpass import getpass


#/mcdanibj/Desktop -> /mcdanbj2
local_path = "/home/mcdanbj2/dispenser"
username = "Ben-McDaniel"
password = pwd.token
target_repo = f"https://{username}:{password}@github.com/Ben-McDaniel/dispenser"

#/mcdanibj/Desktop -> /mcdanbj2
localrepo = git.Repo("/home/mcdanbj2/dispenser")
repoRemote = git.remote.Remote(localrepo, "origin")

def main():
    #Repo.clone_from(target_repo, local_path)
    polling_count = 0
    time_since_last_commit = 0

    while True:
        time.sleep(1)
        polling_count += 1
        time_since_last_commit +=1
        
        print('[',time_since_last_commit, '||' ,polling_count,']Now Checking for new Commits...')
        commits = list(localrepo.iter_commits())
        recent_Commit=commits[0].committed_datetime


        #True when new files written to github
        #if compare(recent_Commit):
        if True:
            time_since_last_commit = 0
            #Repo.git.pull_request(target_repo, local_path)
            #repoRemote.pull()
            #deleteRepo(local_path)

            #os.environ['GIT_ASKPASS'] = os.path.join(target_repo, 'askpass.py')
            #os.environ['GIT_USERNAME'] = username
            #os.environ['GIT_PASSWORD'] = password
            g = git.cmd.Git(target_repo)
            g.pull()
            print("Pulled")
            x = input()





#if this is true, you must pull
#compares passed datetime with most recent in .csv
#if matches returns false, otherwise returns true
#always appends most recent poll to .csv
def compare(recent_datetime):
    with open('commitLog.csv') as csv_file:
        csv_reader = list(csv.reader(csv_file, delimiter=','))
        cleanedStr = str(csv_reader[-1])
        cleanedStr = cleanedStr[2:len(cleanedStr)-2]
        print('-----------')
        print(cleanedStr)
        print(recent_datetime)
        print("Last Recorded Change:",cleanedStr)
        if cleanedStr == str(recent_datetime):
            with open('commitLog.csv', mode='a') as commit_log:
                csv_writer = csv.writer(commit_log, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow([recent_datetime])
            return False

    with open('commitLog.csv', mode='a') as commit_log:
        csv_writer = csv.writer(commit_log, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([recent_datetime])
    return True



#deletes repo, must do this way to allow deleting
#read-only .git files
def deleteRepo(local_path):
    for root, dirs, files in os.walk(local_path):  
        for dir in dirs:
            os.chmod(path.join(root, dir), stat.S_IRWXU)
        for file in files:
            os.chmod(path.join(root, file), stat.S_IRWXU)
    shutil.rmtree(local_path)


if __name__ == "__main__":
    main()
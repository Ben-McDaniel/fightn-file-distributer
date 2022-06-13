import time
import git
from git import Repo
from privateData import pwd
from github_pusher import toGitHub

local_path = "/home/mcdanbj2/fightn-file-distributer-tmp"
username = "Ben-McDaniel"
password = pwd.token
target_repo = f"https://{username}:{password}@github.com/Ben-McDaniel/fightn-file-distributer"


def main():
    #Repo.clone_from(target_repo, local_path)
    polling_count = 0
    time_since_last_commit = 0
    while True:
        polling_count += 1
        time_since_last_commit +=1
        print('[',time_since_last_commit, '||' ,polling_count,']Now Checking for new Commits...')
        x=input()
        if x == 'y':
            time_since_last_commit = 0
        global target_repo
        print(target_repo.git.log())

if __name__ == "__main__":
    main()
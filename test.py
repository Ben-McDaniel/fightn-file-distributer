import time
import git
from git import Repo
from privateData import pwd

local_path = "/home/mcdanbj2/fightn-file-distributer-tmp"
username = "Ben-McDaniel"
password = pwd.token
target_repo = f"https://{username}:{password}@github.com/Ben-McDaniel/fightn-file-distributer"


def main():
    #Repo.clone_from(target_repo, local_path)
    polling_count = 0
    while True:
        polling_count += 1
        print('[',polling_count,']Now Checking for new Commits...')
        time.sleep(1)

if __name__ == "__main__":
    main()
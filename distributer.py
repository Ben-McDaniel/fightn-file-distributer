import time
import git
from git import Repo
from privateData import pwd
from github_pusher import toGitHub
import csv

local_path = "/home/mcdanbj2/fightn-file-distributer-tmp"
username = "Ben-McDaniel"
password = pwd.token
target_repo = f"https://{username}:{password}@github.com/Ben-McDaniel/fightn-file-distributer"
repo = git.Repo("/home/mcdanbj2/fightn-file-distributer")

def main():
    #Repo.clone_from(target_repo, local_path)
    polling_count = 0
    time_since_last_commit = 0

    while True:
        polling_count += 1
        time_since_last_commit +=1
        
        print('[',time_since_last_commit, '||' ,polling_count,']Now Checking for new Commits...')
        commits = list(repo.iter_commits())
        a=commits[0].committed_datetime
        print(a)
        print(compare(a))
        x=input()
        if x == 'y':
            time_since_last_commit = 0
        #print(target_repo.git.log())


#if this is true, you must pull
def compare(recent_datetime):
    with open('commitLog.csv') as csv_file:
        csv_reader = list(csv.reader(csv_file, delimiter=','))
        cleanedStr = str(csv_reader[-1])
        cleanedStr = cleanedStr[2:len(cleanedStr)-2]
        print('-----------')
        print(cleanedStr)
        print(recent_datetime)
        print("Last Recorded Change:",cleanedStr)
        if cleanedStr == recent_datetime:
            with open('commitLog.csv', mode='a') as commit_log:
                csv_writer = csv.writer(commit_log, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow([recent_datetime])
            return False

        
    with open('commitLog.csv', mode='a') as commit_log:
        csv_writer = csv.writer(commit_log, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
       #csv_writer.writerow([recent_datetime])
    return True

if __name__ == "__main__":
    main()
#new plan
#pull whole repo
#grab stuff thats new
#move those files to the right spots
#delete whole pull


import time
import git
from git import Repo
from privateData import pwd
from github_pusher import toGitHub
import csv
#/mcdanibj/Desktop -> /mcdanbj2
local_path = "/home/mcdanibj/Desktop/fightn-file-distributer-tmp"
username = "Ben-McDaniel"
password = pwd.token
target_repo = f"https://{username}:{password}@github.com/Ben-McDaniel/fightn-file-distributer"

#/mcdanibj/Desktop -> /mcdanbj2
repo = git.Repo("/home/mcdanibj/Desktop/fightn-file-distributer")

def main():
    #Repo.clone_from(target_repo, local_path)
    polling_count = 0
    time_since_last_commit = 0

    while True:
        time.sleep(10)
        polling_count += 1
        time_since_last_commit +=1
        
        print('[',time_since_last_commit, '||' ,polling_count,']Now Checking for new Commits...')
        commits = list(repo.iter_commits())
        recent_Commit=commits[0].committed_datetime


        #True when new files written to github
        if compare(recent_Commit):
            time_since_last_commit = 0
            commit_to_pull = target_repo + '/tree/' + str(commits[0])
            print(commit_to_pull)
            Repo.clone_from(commit_to_pull, local_path)
            
        #print(target_repo.git.log())


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

if __name__ == "__main__":
    main()
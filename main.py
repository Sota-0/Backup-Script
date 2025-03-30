 
import os
import git
import shutil
import datetime

current_date = datetime.date.today()



# file locations

backup1 = '' #directory
backup2 = '' #directory
backup3 = '' #directory


FILES_TO_UPLOAD = [backup1, backup2, backup3]



# Repo information
# fill in information bellow

GITHUB_USERNAME = ''
GITHUB_REPO = ''
GITHUB_TOKEN = ''
REPO_URL = f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/Backup.git"
Local_Repo_Path = './Repo_Path'





# Clone the repo if it doesn't exist locally
if os.path.exists(Local_Repo_Path):
    shutil.rmtree(Local_Repo_Path)  # Delete existing clone to ensure a fresh start

repo = git.Repo.clone_from(REPO_URL, Local_Repo_Path)

# Copy files/folders to the repo directory
for item in FILES_TO_UPLOAD:
    src_path = os.path.abspath(item)  # Get absolute path of source file
    dest_path = os.path.join(Local_Repo_Path, os.path.basename(item))  # Copy into repo folder


    if os.path.isdir(src_path):
        shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
    elif os.path.isfile(src_path):
        shutil.copy2(src_path, dest_path)

# Add, commit, and push changes
repo.git.add(A=True)
repo.index.commit(f"New Backup: {current_date}")
origin = repo.remote(name="origin")
origin.push()


print("Backup completed successfully!")

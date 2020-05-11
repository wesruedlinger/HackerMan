#Add one or more files to staging (index):
git add <filename>
-or-
git add *

#Commit changes to head (but not yet to the remote repository):
git commit -m "Commit message"

#Commit any files you've added with git add, and also commit any files you've changed since then
git commit -a

#Send changes to the master branch of your remote repository:
git push origin master

#Fetch and merge changes on the remote server to your working directory:
git pull

#Configure the author name and email address to be used with your commits.
git config --global user.name "Wes"

git config --global user.email wes.ruedlinger91@gmail.com

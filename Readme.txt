#Add one or more files to staging (index):
git add <filename>
-or-
git add *

#Commit any files you've added with git add, and also commit any files you've changed since then
git commit -a

#Send changes to the master branch of your remote repository:
git push origin master

#Configure the author name and email address to be used with your commits.
git config --global user.name "Wes"

git config --global user.email wes.ruedlinger91@gmail.com

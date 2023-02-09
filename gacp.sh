#!/bin/bash
message=$1
echo "adding changes to staging enviroment....."
git add .
sleep 1
echo "committing staged changes.... "
git commit -m "$message"
sleep 1
echo "pushing code to remote repo..."
git push

#!/bin/bash
git add pushScript.sh
git add RESULTS.txt
git add trumpData.db
git add hourFile.db

git commit -m "Daily update"
git push origin master

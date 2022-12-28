export WORK_PATH_MAIN="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $WORK_PATH_MAIN

# venv
source venv/bin/activate

# python
python main.py > log/`date +\%Y-\%m-\%d_\%H_\%M_\%S`_fetch_and_tweet.log

# Keep only first 288 (24 hrs) log
set -- log/*
while [ $# -gt 288 ]
do
  echo "Removing old log: $1"
  rm "$1"
  shift
done

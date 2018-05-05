#!/bin/sh

#usage update mode             : sh start.sh startmin startsec longtime [timefilename]
#usage only latest time update : sh start.sh u [timefilename]

sec=`expr $(date +%s) % 3600 % 60`
min=`expr $(date +%s) % 3600 / 60`

# start schedule
START_MIN=59
START_SEC=57
LONGTIME=20
FILENAME=timecheck

COUNT=0
TEST="test"
if [ $# -eq 1 ]; then
  if [ $1 = "u" ]; then
    echo $1
    echo "only time update"
    python3 ./urlopen.py $1
    exit;
  fi
fi
if [ $# -eq 2 ]; then
  if [ $1 = "u" ]; then
    echo $1
    python3 ./urlopen.py $1 $2
    echo "array has begun"
    array=("00" "05" "10" "15" "20" "25" "30" "35" "40" "45" "50" "55")
    for test1 in ${array[@]}; do
      if [ $test1 != $2 ]; then
        echo "copy that! "$2" to "$test1
        cp $2 $test1
      fi
    done
    exit;
  fi
fi

if [ $# -gt 3 ]; then
  echo $1.$2.$3
  START_MIN=$1
  START_SEC=$2
  LONGTIME=$3
  if [ $# -eq 4 ]; then
    echo "filename:".$4
    FILENAME=$4
  fi
else
  echo "usage sh ./start.sh mode[u or else] startmin startsec longtime [filename]"
  exit;
fi

sec2=`expr $sec + 1`
sec3=`expr $sec - 1`

while :
do
  while [ $min.$sec != $START_MIN.$START_SEC ] && [ $min.$sec2 != $START_MIN.$START_SEC ] && [ $min.$sec3 != $START_MIN.$START_SEC ] ; do
    echo $min.$sec
    sleep 1 
    sec=`expr $(date +%s) % 3600 % 60`
    min=`expr $(date +%s) % 3600 / 60`
  done

  lltime=0
  sec2=$sec
  while [ $lltime -lt $LONGTIME ]; do 
    echo $sec2.$sec
    if [ $sec2 -ne $sec ]; then
      lltime=`expr $lltime + 1`
      sec2=$sec
    fi
    echo "app start".$lltime
    python3 ./urlopen.py a $FILENAME
    #echo ${?}
    if [ $? -eq 2 ]; then
      array=("00" "05" "10" "15" "20" "25" "30" "35" "40" "45" "50" "55")
      for test1 in ${array[@]}; do
        if [ $test1 != $FILENAME ]; then
          cp $FILENAME $test1
        fi
      done
      break 1 
    fi

    COUNT=`expr $COUNT + 1` 
    sec=`expr $(date +%s) % 3600 % 60`
    min=`expr $(date +%s) % 3600 / 60`
  done
done

exit


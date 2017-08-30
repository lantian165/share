#!/bin/sh

SRCDIR=/root/yichen/space_clean

date_str=`date +%m-%d`

LOGFILE=$SRCDIR/${date_str}_find_large_files_v1.log

OUTPUTFILE1=$SRCDIR/${date_str}_find_large_files_v1-1.log

TMPLOGFILE=$SRCDIR/filename.log

if [ ! -f $LOGFILE ];
then 
   echo "Not "$LOGFILE"found"
   exit
fi

if [ ! -f $OUTPUTFILE1 ];
then 
   touch $OUTPUTFILE1
fi

cat /dev/null > $OUTPUTFILE1

while read line
do
   ls --full-time `echo $line |cut -d " " -f 2` | awk '{print $5" "$6" "$7" "$9}' >> $OUTPUTFILE1
done < $LOGFILE

exit 0
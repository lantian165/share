#!/bin/sh

LOGFILE=/root/yichen/180_space_clean.log

if [ ! -f $LOGFILE ];
then
  touch $LOGFILE
fi

GetSize()
{
   echo -e "============================Now The Size Is(In Byte)============================" >> $LOGFILE
   ls -l /home/apache-tomcat-5.5.33/logs/catalina.out   >> $LOGFILE
   ls -l /home/apache-tomcat-5.5.33-1/logs/catalina.out >> $LOGFILE
   ls -l /home/apache-tomcat-5.5.33-2/logs/catalina.out >> $LOGFILE
   ls -l /home/apache-tomcat-5.5.33-3/logs/catalina.out >> $LOGFILE
}

DATESTR=`date +"%Y-%m-%d %H:%M:%S"`

echo "["$DATESTR"]:" >> $LOGFILE
echo "Space Clean Process Begin..." >> $LOGFILE

echo -e "\nBefore clean:" >> $LOGFILE
GetSize

cat /dev/null > /home/apache-tomcat-5.5.33/logs/catalina.out
cat /dev/null > /home/apache-tomcat-5.5.33-1/logs/catalina.out
cat /dev/null > /home/apache-tomcat-5.5.33-2/logs/catalina.out
cat /dev/null > /home/apache-tomcat-5.5.33-3/logs/catalina.out

echo -e "\nAfter Clean:" >> $LOGFILE
GetSize

echo -e "\nSpace Clean Process Finished...\n\n" >> $LOGFILE

exit 0
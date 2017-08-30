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

#Part 1: Apache Tomcat:
cat /dev/null > /home/apache-tomcat-5.5.33/logs/catalina.out
cat /dev/null > /home/apache-tomcat-5.5.33-1/logs/catalina.out 
cat /dev/null > /home/apache-tomcat-5.5.33-2/logs/catalina.out
cat /dev/null > /home/apache-tomcat-5.5.33-3/logs/catalina.out

# Create Log Bak Dir:
LOG_BAK_DATE_DIR=/data1/180_log_clean_bak/`date +"%m-%d"`

#Part 2: Weblogic log files:
#1./home/weblogic/bea/user_projects/domains/webcluster/zjgpwebnode5/
# Generate 3 Gb log files per month
WEBLOGIC_NODE5=${LOG_BAK_DATE_DIR}/weblogic/node5
WEBLOGIC_COREAPP=${LOG_BAK_DATE_DIR}/weblogic/coreapp

mkdir -p ${WEBLOGIC_NODE5}
mkdir -p ${WEBLOGIC_COREAPP}

find /home/weblogic/bea/user_projects/domains/webcluster/zjgpwebnode5/ -maxdepth 1 -type f -mtime +25 -name access.log* -exec mv {} ${WEBLOGIC_NODE5} \;
find /home/weblogic/bea/user_projects/domains/webcluster/ -maxdepth 1 -type f -mtime +25 -name coreapp.log* -exec mv {} ${WEBLOGIC_COREAPP} \;

#Part 3: Move log files to: /data1/180_log_clean_bak
LOG_BAK_DIR=${LOG_BAK_DATE_DIR}/tomcat-logs
LOG_BAK_DIR1=${LOG_BAK_DATE_DIR}/tomcat-logs-1
LOG_BAK_DIR2=${LOG_BAK_DATE_DIR}/tomcat-logs-2
LOG_BAK_DIR3=${LOG_BAK_DATE_DIR}/tomcat-logs-3

mkdir -p ${LOG_BAK_DIR}
mkdir -p ${LOG_BAK_DIR1}
mkdir -p ${LOG_BAK_DIR2}
mkdir -p ${LOG_BAK_DIR3}

find /home/apache-tomcat-5.5.33/logs/ -maxdepth 1 -type f -mtime +15 -name jeecms*.zip -exec mv {} ${LOG_BAK_DIR} \;
find /home/apache-tomcat-5.5.33-1/logs/ -maxdepth 1 -type f -mtime +15 -name jeecms*.zip -exec mv {} ${LOG_BAK_DIR1} \;
find /home/apache-tomcat-5.5.33-2/logs/ -maxdepth 1 -type f -mtime +15 -name jeecms*.zip -exec mv {} ${LOG_BAK_DIR2} \;
find /home/apache-tomcat-5.5.33-3/logs/ -maxdepth 1 -type f -mtime +15 -name jeecms*.zip -exec mv {} ${LOG_BAK_DIR3} \;

echo -e "\nAfter Clean:" >> $LOGFILE
GetSize

echo -e "\nSpace Clean Process Finished...\n\n" >> $LOGFILE

exit 0

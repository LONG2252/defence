#!/bin/bash


cat /var/log/secure | grep Failed | awk -F "from" '{print $2}'| awk '{print $1}' >/home/alex/defence/iplog.log

cat /etc/hosts.allow | grep sshd | awk -F ":" '{print $2}' >/home/alex/defence/allowedip.log

cat /etc/hosts.deny | grep sshd | awk -F ":" '{print $2}' >/home/alex/defence/denyip.log

python3 /home/alex/defence/defence.py

for row in $(cat /home/alex/defence/denyip.log)
do
echo sshd:$row:deny >>/etc/hosts.deny

#echo sshd:$row:deny
done








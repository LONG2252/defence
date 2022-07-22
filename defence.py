
import re

new_iplist_path=r'/home/alex/defence/iplog.log'
new_denyip_path=r'/home/alex/defence/denyip.log'
new_alowed_path=r'/home/alex/defence/allowedip.log'

ipfile=open(new_iplist_path,mode='r')
iplist_whole=ipfile.read()
iplist=re.split('\n+',iplist_whole)
ipfile.close()

denyipfile=open(new_denyip_path,mode='r+')
denyip_whole=denyipfile.read()
denyiplist=re.split('\n+',denyip_whole)
denyipfile.close()
denyipfile_2=open(new_denyip_path,mode='w+')


alowedipfile=open(new_alowed_path,mode='r')
alowedip_whole=alowedipfile.read()
alowediplist=re.split('\n+',alowedip_whole)
alowedipfile.close()

st= alowediplist+denyiplist
new_repet_ip_list=[]

for row in iplist:
	if iplist.count(row)>5:
		new_repet_ip_list.append(row)

for row in new_repet_ip_list:
	if row not in st and denyiplist.count(row)==0:
		denyipfile_2.write(row+"\n")
		denyiplist.append(row)
		print("add new ip "+str(row))
denyipfile_2.close()

	# if iplist.count(row)>10 and row not in alowediplist and row not in denyiplist:
	# 	denyiplist.append(row)
	# 	denyipfile.write(row+"\n")


import findBusinesses
from threading import Thread

threads=[]

default_keyword='software'
keyword=raw_input("Business search keyword [{}]:".format(default_keyword))
if keyword=='':
	keyword=default_keyword

default_location_file='eastcoast'
loc_file_name=raw_input("File with locations to search [locations/{}]: locations/".format(default_location_file))
if loc_file_name=='':
	loc_file_name=default_location_file
loc_file_name="locations/"+loc_file_name

default_jobkey='software'
jobkey=raw_input("Job search keyword [{}]:".format(default_keyword))
if jobkey=='':
	jobkey=default_jobkey

loc_file=open(loc_file_name,"r")
loc_name=loc_file.readline()

while loc_name:
	loc_name=loc_name[:-1]
	filename="jobs/"
	filename+=loc_name
	filename+="-"
	filename+=keyword
	outfile=open(filename, "w")
	outfile.close()
	findBusinesses.businessSearch(loc_name,keyword,jobkey,threads)
	loc_name=loc_file.readline()


loc_file.close()

for t in threads:
	t.join()

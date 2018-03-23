import googlemaps
import time

apifile = open("api key")
MY_API_KEY = apifile.readline()
MY_API_KEY=MY_API_KEY[:-1]
gmaps = googlemaps.Client(key=MY_API_KEY)

ifh=open("locations","r")
loc_name=ifh.readline()
key="software"
print "Searching keyword:", key

while loc_name:
	loc_name=loc_name[:-1]
	fp="websites/"
	fp+=loc_name
	fh = open(fp,"w")
	fh.close()
	print "Searching", loc_name, "..."
	latlong = gmaps.geocode(loc_name)

	latitude = latlong[0]['geometry']['location']['lat']
	longitude = latlong[0]['geometry']['location']['lng']

	print "(", latitude, " ", longitude, ")"

	places_list = gmaps.places_radar([latitude,longitude],1000,type=['establishment'],keyword=key)

	num_places = len(places_list['results'])
	print num_places, "locations found."
	count=1
	for x in range(0,num_places):
		if count%10==0:
			print count, "/", num_places
		current_id = places_list['results'][x]['place_id']
		deets = gmaps.place(current_id)
		if 'establishment' in deets['result']['types']:
			if 'website' in deets['result']:
				fp="websites/"
				fp+=loc_name
				fh = open(fp,"a")
				fh.write(deets['result']['website'])
				fh.write("\n")
				fh.close()
		time.sleep(0.11)
		count+=1
	loc_name=ifh.readline()

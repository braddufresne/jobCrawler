import googlemaps, time, findJobs

def businessSearch(loc_name, search_term, job_key, threads):
	apifile = open("api key")
	MY_API_KEY = apifile.readline()
	MY_API_KEY=MY_API_KEY[:-1]
	gmaps = googlemaps.Client(key=MY_API_KEY)

	print "Searching keyword:", search_term

	print "Searching", loc_name, "..."
	latlong = gmaps.geocode(loc_name)

	latitude = latlong[0]['geometry']['location']['lat']
	longitude = latlong[0]['geometry']['location']['lng']

	print "(", latitude, " ", longitude, ")"

	places_list = gmaps.places_radar([latitude,longitude],1000,type=['establishment'],keyword=search_term)

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
				findJobs.webCrawl(deets['result']['website'],job_key,loc_name, threads)
		time.sleep(0.11)
		count+=1

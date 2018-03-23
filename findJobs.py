import sys, thread, Queue, re, urllib, urlparse, time, os, sys

dupcheck = set()

def saveCareers(link,key,loc):
	filename="jobs/"
	filename+=loc
	filename+="-"
	filename+=key
	outfile=open(filename, "a")
	outfile.write(link)
	outfile.write("\n")
	outfile.close()

def checkListing(link, keyword):
	try:
		html = urllib.urlopen(link).read() 
		matches = re.findall(keyword,html,re.I)
		if len(matches) != 0:
			saveCareers(link,keyword, loc)
	except (KeyboardInterrupt, SystemExit): 
		raise
	except Exception:
		pass

def getCareers(html, origLink, keyword, loc): 
    for url in re.findall('''<a[^>]+href=["'](.[^"']+)["']>careers</a>''', html, re.I): 
	link = url.split("#", 1)[0] if url.startswith("http") else '{uri.scheme}://{uri.netloc}'.format(uri=urlparse.urlparse(origLink)) + url.split("#", 1)[0] 
	if link in dupcheck:
	    continue
	dupcheck.add(link)
	if len(dupcheck) > 99999: 
	    dupcheck.clear()
	checkListing(link,keyword, loc)

def findCareers(link,keyword, loc): 
    try:
	print "crawling", link
	html = urllib.urlopen(link).read() 
	getCareers(html, link, keyword, loc) 
    except (KeyboardInterrupt, SystemExit): 
	raise
    except Exception:
	pass

def webCrawl(start_page, job_keyword, loc):
	print "spawning thread"
	thread.start_new_thread( findCareers, start_page, job_keyword, loc)
	print "webcrawl return"

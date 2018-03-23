import sys, Queue, re, urllib, urlparse, time, os, sys
from threading import Thread

dupcheck = set()

def saveCareers(link,key,loc):
	print "job match found at ", link
	filename="jobs/"
	filename+=loc
	filename+="-"
	filename+=key
	if os.path.exists(filename):
		append_write='a'
	else:
		append_write='w'
	outfile=open(filename, append_write)
	outfile.write(link)
	outfile.write("\n")
	outfile.close()

def checkListing(link, keyword):
	try:
		print "career page found at", link
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
	print "page = ", html
	getCareers(html, link, keyword, loc) 
    except (KeyboardInterrupt, SystemExit): 
	raise
    except Exception:
	pass

def webCrawl(start_page, job_keyword, loc, threads):
	print "spawning thread"
	threads.append(Thread( target=findCareers, args=(start_page, job_keyword, loc)))
	threads[-1].start()
	print "webcrawl return"

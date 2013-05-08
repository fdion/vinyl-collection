#!/usr/bin/python

# TODO: Year and format!

# Caveats:
# Use unicode() not str() because of ZZ Top's "Deg[umlaut]ello" etc...

import discogs_client as discogs # Use helper class
discogs.user_agent = 'TestDiscogsPythonApp/0.1 +james@james-bennet.com' # This must be set according to API docs

# Counters
found = 0;
failed = 0;

print "Processing..."

# Read in and iterate over file of barcodes I scanned in on my phone.
for line in open('in.txt','r').readlines():
  try:
		# Flags
		is_found = False

		# Process input
		line = line.strip() # Get rid of whitespace and newlines etc...

		# Quick sanity check
		if not line.isdigit():
			# A strange barcode we cant handle, for example "A-tnh37v" or some nonsense..
			failed = failed + 1
			continue

		# Query the discogs API. My code has about 50% success with my CDs.
		s = discogs.Search(line)

		# If a single result was returned, nice and simple.
		if len(s.results()) == 0:
			failed = failed + 1  # 0 results at all.
			continue
		elif len(s.results()) == 1:
			if type(s.results()[0]) == discogs.Release: # Which it should be, if only one result.
				# Format like "008811281625 - Argus (Expanded Edition - Remastered & Revisited) (Wishbone Ash)"
				print unicode(line) + " - " + unicode(s.results()[0].title) + " (" + unicode(s.results()[0].artists[0].name) + ")"
				found = found + 1 # Success - done here.
				continue
			else:
				failed = failed + 1 # Failure - Was an unexpected type. Not sure if this can ever occur, but we cater for it.
				continue
		else: # If > 1 results
			for result in s.results(): # If many, iterate through them to try and find MasterRelease
				if type(result) == discogs.MasterRelease:
					print unicode(line) + " - " + unicode(result.title) + " (" + unicode(result.artists[0].name) + ")"
					found = found + 1 # Success - done here.
					is_found = True
					break

			# If we didnt find a MasterRelease and broke, just take the first release we find. TODO: This is crap. 
			if not is_found:	
				for result in s.results():
					if type(result) == discogs.Release:
						print unicode(line) + " - " + unicode(result.title) + " (" + unicode(result.artists[0].name) + ")"
						is_found = True
						found = found + 1 # Success - done here.
						break

			# If we still cant find a release, then no results were of the right type. Not sure if this can ever occur, but we cater for it.
			if not found:
				failed = failed + 1
				continue
	except discogs.DiscogsAPIError as e: # We sometimes get some 404 error?
		failed = failed + 1
	except Exception as e: # We sometimes get socket error?
		failed = failed + 1

# Summary
print unicode(found) + "/" + unicode(found + failed)  + " Barcodes Processed OK."

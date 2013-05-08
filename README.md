vinyl-collection
================

vinyl-collection takes barcodes and spits out the title and artist, if it can, using the Discogs API.

We use discogs_client - hosted on GitHub, to do this. Looks a bit dead, though... 

TODO:
*Year and format.
*Make it less crappy.
*Make it work with an androud app to scan batches of music.
*Import/Export the data nicely.
*Be able to type/scan in codes too.
*Getting album art could be cool
*Store in DB

Note:
I use unicode() not str() because of ZZ Top's "Deg[umlaut]ello" etc...

Example output:

[jamesb@bsg75 ~]$ ./code.py
Processing...
8714092643220 - Smash (Offspring, The)
016861804824 - Shot To Hell (Black Label Society)
5011781189629 - Southern Accents (Tom Petty And The Heartbreakers)
731454003025 - Greatest Hits (Police, The)
093624573524 - From The Cradle (Eric Clapton)
093624950073 - Living Things (Linkin Park)
075992583824 - Greatest Hits (Fleetwood Mac)
008811281625 - Argus (Expanded Edition - Remastered & Revisited) (Wishbone Ash)
093624963332 - A Thousand Suns (Linkin Park)
5099750212820 - Stained Class (Judas Priest)
602517737266 - Death Magnetic (Metallica)
5060072303626 - Hold Your Colour (Pendulum)
5099748102621 - Evil Empire (Rage Against The Machine)
724384938826 - Tubular Bells (Mike Oldfield)
075597963311 - El Camino (Black Keys, The)
5099750213124 - British Steel (Judas Priest)
724381008829 - Discovery (Daft Punk)
602527168463 - Sabbath Bloody Sabbath (Black Sabbath)
075992740029 - Degüello (ZZ Top)
075992534222 - Afterburner (ZZ Top)
5099751013020 - Audioslave (Audioslave)
081227896621 - Tres Hombres (ZZ Top)
724349692008 - Powerslave (Iron Maiden)
042283814127 - Master Of Puppets (Metallica)
602527815978 - Lulu (Lou Reed)
5099749199323 - The Battle Of Los Angeles / Renegades (Rage Against The Machine)
5099747222429 - Rage Against The Machine (Rage Against The Machine)
042283056824 - Strong Persuader (Robert Cray)
042283606227 - ...And Justice For All (Metallica)
731452188120 - The Cream Of Clapton (Eric Clapton)
5017615830422 - Vol 4 (Black Sabbath)
724353611125 - Echoes - The Best Of Pink Floyd (Pink Floyd)
5099750213322 - Screaming For Vengeance (Judas Priest)
602517806993 - Best Of Stereophonics: Decade In The Sun (Stereophonics)
634904052027 - 21 (Adele)
602517130418 - Back To Black (Amy Winehouse)
602527225388 - Sigh No More (Mumford & Sons)
082839390217 - Every Breath You Take (The Singles) (Police, The)
042283492318 - Don't Be Afraid Of The Dark (Robert Cray Band, The)
075992377416 - Eliminator (ZZ Top)
042283814110 - Master Of Puppets (Metallica)
075992607414 - Journeyman (Eric Clapton)
8712725737711 - Nothin But Love (Robert Cray Band, The)
042283056817 - Strong Persuader (Robert Cray)
042286801070 - Sit Down (James)
45/56 Barcodes Processed OK.
[jamesb@bsg75 ~]$ 

Cool, Huh!

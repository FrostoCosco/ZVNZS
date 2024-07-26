This Github page was supposed to be the actual website for this mod, however I changed my mind, or not idk, but this for now is used to host certain files for it to use.

How does auto updating work,

the compiled client application for the mod has an embedded script which reads this Python file hosted on this Github page: 
https://frostocosco.github.io/ZVNZS/UpdateChecker.py

that Python file has all the code needed to update the client, the embedded script runs this Python script, that script will then install the new version which packages all the files the game needs, these are updated new files, and are bundled within a zip, it extracts all the files needed to patch the game and update it and then removes it, simple,

well I had a headache making the application, but still simple..

and the Start script checks if it's on the newest version as well

(yes it auto installs python and pip, all latest versions)

This is a multiclipboard app that stores content from clipboard which you can save and access later on.

To run this file from the command line simply:
1. Search for the file directory on your computer and obtain the file path.

2. Open up the command line and change directory into the file path:
   Example:
   cd C:\Users\dvdva\Desktop\Python\Portfolio

3. From this path you can run the file by typing: 
   Windows: python multi-clipboard.py
   MAC or Linux: python3 multi-clipboard.py

4. Using command line arguments:
There are three arguments:
   - save: you will be prompted to insert a key. Any text you currently have attached to your clipboard will be saved in a json file and will be associated to the inserted key.
   - load: you will be prompted to insert an existing key. This allows you reference copy the associated content to your clipboard.
   - list: prints the json object (key - value pairs) onto the CLI



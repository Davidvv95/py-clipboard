#Import modules
import sys #Access CLI arguments
import clipboard #Copy and paste with clipboard
import json #Store content in JSON file

SAVED_DATA = "clipboard.json"

#Create and/or write into JSON file
def saveData(filepath, data):
    with open(filepath, "w") as f: #Write will override items in the file if file already exists, or create a new file
        json.dump(data, f) #Write the py dictionary as json object into json file

#Read json file 
def loadData(filepath):
    try:
        with open(filepath, "r") as f: 
            data = json.load(f) #It will give us the py dictionary representation of the JSON file
            return data
    except:
        return {}

#sys.argv creates a list out of the arguments typed into the CLI
if len(sys.argv) == 2: #(First arg = multi-clipboard.py, Second arg = command)
    command = sys.argv[1]
    data = loadData(SAVED_DATA) #Contains py dictionary from json content

    #Available commands for the app: save, load, list.
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste() 
        saveData(SAVED_DATA, data) 
        print("Data saved!")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key]) 
            print("Data copied to clipboard!")
        else:
            print("Key doesn't exist!")
    elif command == "list": 
        print(data)
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command")
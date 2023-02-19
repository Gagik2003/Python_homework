import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--val')
args = parser.parse_args()
key, val = args.key, args.val

if val:
    try:
        with open('storage.data') as json_file:
    	    data = json.load(json_file)
    	    if str(key) in data.keys():
    	        data[str(key)].append(val)
    	    else:
                data[str(key)] = [val]
        data = json.dumps(data)
        with open("storage.data", "w") as outfile:
    	    outfile.write(data)
    except:
        data = json.dumps({key: [val]})
        with open("storage.data", "w") as outfile:
    	    outfile.write(data)
else:
    with open('storage.data') as json_file:
        data = json.load(json_file)
        if str(key) in data.keys():
            for i in data[str(key)][:-1]:
                print(i, end=', ')
            print(data[str(key)][-1])
        else:
            print(None)


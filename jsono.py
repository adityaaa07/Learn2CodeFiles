import ijson
with open('new.jsonl') as thefile:
	stuff = [ijson.parse(line) for line in thefile]
print(stuff)

for i in stuff:
    for (prefix, the_type, value) in i:
        print('prefix: ', prefix, 'type: ', the_type,'value: ', value, '*'*9)


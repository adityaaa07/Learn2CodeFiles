import ijson
with open('new.jsonl') as thefile:
    for line in thefile:
        record = ijson.parse(line)
        for (prefix, the_type, value) in record:
            print('prefix: ', prefix, 'type: ', the_type,'value: ', value, '*'*9)


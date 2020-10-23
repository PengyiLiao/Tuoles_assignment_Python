name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
time=list()
counts=dict()
handle = open(name)
for line in handle:
    if line.startswith('From '): #find the special sentence
        #line.split()
        pos = line.find(':') #find position
        #print(line)
        #print(line[pos-2: pos])
        time.append(line[pos-2: pos])#use append is good,find hour
        #print(time)
#
for word in time:
    counts[word]=counts.get(word,0)+1
#print(counts)
for k,v in sorted(counts.items()):
    print(k,v)

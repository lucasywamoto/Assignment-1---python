import re


#open file and read all words into a list
f = open("sample.txt", 'r')
words = []
pattern = re.compile(r'\b\w+(?:\'\w+)?\b')

for line in f:
    words += pattern.findall(line.lower())

f.close()

#sort words alphabetically
words.sort(key=str.lower)

#count words
wordCount = {i:words.count(i) for i in words}

#write to file
report = open("report.txt", 'w')

report.write("%15s%2s%10s\n" % ("Word"," | ", "Frequency"))
report.write("%15s%2s%10s\n" % (""," | ", ""))

for word in wordCount:
    report.write("%15s%2s%-3s\n" % (word," | ", wordCount[word]))

report.close()
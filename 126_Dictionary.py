#wap to find the frequency of each word in a given string using dictionary
string="This is a string is this a string"
string=string.split()
frequency={}
for word in string:
    if word in frequency:
        frequency[word]+=1
    else:
        frequency[word]=1
print(frequency)

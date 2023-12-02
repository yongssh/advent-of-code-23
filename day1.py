## replace path with actual file path
file = open('path', 'r')
input = file.readlines()

## pt 1 ##

filelength = len(input)
numpair = [''] * filelength
numpairindex = 0

# array of strings without \n
cleanedarray = [None] * filelength
for i in range(filelength):
    cleanedarray[i] = input[i].splitlines()

for i in range(filelength):
    string = str(cleanedarray[i])
    strlen = len(string)
    #print(string)
    for j in range(strlen):
        #print(string[j])
        if string[j].isdigit():
            numpair[numpairindex] += str(string[j])
        ## for part 2 ##
        for index, val in enumerate(['one', 'two', 'three', 'four', 'five','six', 'seven', 'eight', 'nine']):
            if string[j:].startswith(val):
                numpair[numpairindex] += str(index + 1)
        ## end part 2 ##
    numpairindex += 1
    
print(numpair)

finalnums = [0] * filelength
index = 0
for num in numpair: 
    first = str(num[0])
    last = str(num[-1]) 
    finalnum = first + last   
    finalnums[index] = int(finalnum)
    index += 1
#print(finalnums)    

total = sum(finalnums)

print(total)




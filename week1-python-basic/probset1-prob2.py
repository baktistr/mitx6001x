num_bob = 0
index = 0
for char in s:
    
    if char == 'b' and index <= (len(s)-3):
        if s[index+1] == 'o' and s[index+2] == 'b':
            num_bob += 1
    index += 1
print('Number of times bob occurs is: ' + str(num_bob))

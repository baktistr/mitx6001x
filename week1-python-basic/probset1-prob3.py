the_string = ''
the_prev_string = ''
the_longest_string = ''

index = 0
for char in s:
    if index < len(s)-1:
        
        if char <= s[index+1] and index != len(s)-2:
            the_string = the_string+s[index]
            
        elif index != len(s)-2:
            the_string = the_string+s[index]
            
            if len(the_string) > len(the_longest_string):
                the_longest_string = the_string
           
            the_string = ''
        else:
            the_string = the_string+s[index]
            if char <= s[index+1]:
                the_string = the_string+s[index+1]
            if len(the_string) > len(the_longest_string):
                the_longest_string = the_string
            
                   
        index +=1
        

print ('Longest substring in alphabetical order is: ' + (the_longest_string))

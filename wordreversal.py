#create boolean variable to store palandrome status
#start as True

#create variable to store negative index 
#start at -1

#for each letter in Andrew, loop
    #compare current index with negative index
    #if different
        #not a palandrome, assign Fasle to boolean
        #break
    #set negative index to current negative index -1

def palendromedoitbe(user_input):
    negindex = -1

    user_input = user_input.lower()

    for index in range(int(len(user_input)/2)):
        if user_input[index] != user_input[negindex]:
            return False
        negindex = negindex - 1 


    #for letter in user_input:
     #   if letter != user_input[negindex]:
      #      return False
       # negindex = negindex - 1 
    return True



def hill(code):
    
    code = code.lower()
    output = [[0],
              [0],
              [0]]
    counter = 0
    for character in code:
        number = ord(character) - 97
        output[counter][0] = number
        counter += 1

##    key = [[1,7,2],
##           [6,4,5],
##           [3,8,9]]

##    key = [[5,4,9],
##           [8,7,3],
##           [2,6,1]]

##    key = [[6,8,3],
##           [2,1,9],
##           [7,4,5]]
##
##    key = [[4,9,6],
##           [8,1,3],
##           [2,5,7]]
####
##    key = [[3,2,7],
##           [4,5,6],
##           [1,9,8]]
##
##    key = [[8,5,1],
##           [9,7,2],
##           [4,3,6]]
##
##    key = [[9,6,4],
##           [7,3,1],
##           [5,2,8]]
##
##    key = [[7,1,5],
##           [6,8,2],
##           [9,3,4]]
##
    key = [[3,2,8],
           [5,9,4],
           [1,6,7]]
    
    result = [[0],
             [0],
             [0]]

    # iterate through rows of X
    for i in range(len(key)):
       # iterate through columns of Y
       for j in range(len(output[0])):
           # iterate through rows of Y
           for k in range(len(output)):
               result[i][0] += key[i][k] * output[k][j]

    for r in result:
       a = r[0] % 26
       val = chr(a + 97)
       print(val)


while(True):
    code = raw_input("Enter Code: ")
    hill(code)

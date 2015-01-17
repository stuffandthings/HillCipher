def hill(code): 
    key = [[3,2,8],
           [5,9,4],
           [1,6,7]]

    code = code.lower()
    output = [[0],[0],[0]]
    counter = 0
    for character in code:
        number = ord(character) - 97
        output[counter][0] = number
        counter += 1
    
    result = [[0],
             [0],
             [0]]

    for i in range(len(key)):
       for j in range(len(output[0])):
           for k in range(len(output)):
               result[i][0] += key[i][k] * output[k][j]

    for r in result:
       numeric_letter = r[0] % 26
       val = chr(numeric_letter + 97)
       print(val)


while(True):
    code = raw_input("Enter Code: ")
    hill(code)

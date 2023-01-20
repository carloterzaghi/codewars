#Description:

# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]

# Link for Kata: https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

# My code:

def snail(snail_map):
    retornar = []
    while len(snail_map) > 0:
        # Read Right
        retornar.extend(snail_map[0])
        del(snail_map[0])
        # Read Down
        for i in snail_map:
            if i == []:
                break
            retornar.append(i[-1])
            del(i[-1])
        # Read Left
        try:
            retornar.extend(snail_map[-1][::-1])
            del(snail_map[-1])
        except: break
        # Read Top
        for i in snail_map[::-1]:
            if i == []:
                break
            retornar.append(i[0])
            del(i[0])
    return retornar
#### MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 *or* if one of the integers is 20. If not, return False
# def makes_twenty(n1,n2):
#     if n1+n2==20 or n1==20 or n2==20:
#         return True
#     else:
#         return False
    

# print(makes_twenty(12,8))
# print(makes_twenty(20,10))
# print(makes_twenty(2,3))

#### OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# def old_macdonald(name):   
#     newname = list(name)
#     newname[0] = newname[0].upper()
#     newname[3] = newname[3].upper()
#     return ''.join(newname)
    

# print(old_macdonald('macdonald'))



# def master_yoda(text):
#     newtext = text.split()
#     newtext.reverse()
#     return ' '.join(newtext)

# print(master_yoda('I am home'))

#### ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# def almost_there(n):
#     if n < 90 or n > 110 and n < 190 or n > 210:
#         return False
#     else:
#         return True


# print(almost_there(95))
# print(almost_there(104))
# print(almost_there(209))


# def has_33(nums):
#     for i in range(0,len(nums)-1):
#         if nums[i] == 3 and nums[i+1] == 3:
#             return True
#     return False

# print(has_33([1, 3, 3]))
# print(has_33([1, 3, 1, 3,1,1,2,1,1,2,1,2,1,2,3,2,3,2,1,2,3,3]))
# print(has_33([3, 1, 3]))

# def paper_doll(text):
#     newtext = ''
#     for char in text:
#         newtext += char * 3
#     return newtext


# print(paper_doll('Hello'))
# print(paper_doll('Mississippi'))


# def blackjack(a,b,c):
#     suma = a+b+c
#     if suma <=21:
#         return suma
#     elif suma>21 and 11 in [a,b,c]:
#         return suma - 10
#     else:
#         return 'BUST'
    
# print(blackjack(5,6,7))
# print(blackjack(9,9,9))
# print(blackjack(9,9,11))

def summer_69(arr):
    for i in arr:
        if i == range(6,9):
            return None
    # return sum(arr)

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
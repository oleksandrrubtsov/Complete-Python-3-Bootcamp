# **Use for, .split(), and if to create a Statement that will print out words that start with 's':**
# st = 'Print only the words that start with s in this sentence'

# for word in st.split():
#     if word[0] == 's':
#         print(word)
        

# lst = [x for x in range(0,51) if x % 3 == 0]
# print(lst)



# for i in range(0,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)


st = 'Create a list of the first letters of every word in this string'
lst = [x[0] for x in st.split()]
print(lst)




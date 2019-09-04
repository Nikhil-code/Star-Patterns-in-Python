# Method 1
# print('How many row you want to print:')
# row = int(input())
# print('Enter the type:\n1 for Right-angle Triangle\n0 for its reverse')
# bool_val = int(input())
# if bool_val == 1:
#     for i in range(0,row+1):
#         print('*' * i)
# if bool_val == 0:
#     for i in range(row,0,-1):
#         print('*' * i)

# Method 2
# try:
#     print('How many row you want to print:')
#     row = int(input())
#     print('Enter the type:\n1 for Right-angle Triangle\n0 for its reverse')
#     bool_val = int(input())
#     if bool_val == 1:
#         count = 0
#         while(count<=row):
#             print('*' * count)
#             count +=1
#     elif bool_val == 0:
#         count = row
#         while(count!=0):
#             print('*' * count)
#             count -=1
#     else:
#         print('Invalid pattern!')
# except Exception as e:
#     print(e)

# Method 3: using function
def pattern():
    a = int(input('Enter the row'))
    b = bool(int(input('Enter the type:\n1 for Right-angle Triangle\n0 for its reverse')))
    if b == True:
        i = 1
        while(i <= a):
            print(i * "*")
            i += 1
    elif b == False:
        while(a > 0):
            print(a * '*')
            a -= 1
    else:
        print('Invalid Input!')

try:
    pattern()
except Exception as e:
    print(e)
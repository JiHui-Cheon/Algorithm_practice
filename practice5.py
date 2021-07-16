print('*', end = '')
print('*', end = '')
print('*', end = '')
print('*', end = '')
print('*')

for i in range(4):
    print('*'*5)

print()

for j in range(4):
    for i in range(5):
        print('*', end = '')
    print("")

print()

for i in range(1, 6):
    print('*'*i)

print()

for j in range(5):
    for i in range(5-j):
        print('*', end = '')
    print("")

print()

for i in range(5):
    print("*" * (5-i))

print()

for j in range(5):
    for i in range(4-j):
        print(' ', end = '')
    for i in range(j+1):
        print('*', end = '')
    print("")

print()

for i in range(1, 6):
    print(' ' * (5-i) + ("*" * i))

# apart = [[101, 102, 103, 104], [201, 202, 203, 204], [301, 302, 303, 304], [401, 402, 403, 404]]
# arrears = [101, 203, 301, 404]

# for floor in apart:
#     for room in floor:
#         print("Newspaper diliver: %s" % room - floor)


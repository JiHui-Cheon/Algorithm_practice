
apart = [[101, 102, 103, 104], [201, 202, 203, 204], [301, 302, 303, 304], [401, 402, 403, 404]]
arrears = [101, 203, 301, 404]


# for floor in apart:
#     for room in floor:
#         if room in arrears:
#             continue
#         print("newspaper deliver: ", room)


coffee = {'아메리카노': 4100, '카페라떼': 4600, '카라멜마끼아또': 5100}
# print(coffee['아메리카노'])

# n = int(input())
# sum = 0
# for i in range(n):
#     coffee_name = input()
#     sum += coffee[coffee_name]
# print(sum)

total = 0
for i in range(int(input())):
    item = input()
    if item in coffee:
        total += coffee[item]
print(total)

# a = [100, 90, 80]
# i = 0
# sum = 0
# while i < len(a):
#     sum += a[i]
#     i += 1
# print(sum)
# print(len(a))
# print(sum/len(a))

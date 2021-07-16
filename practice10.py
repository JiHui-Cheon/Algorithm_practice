# def myaverage(a, b):
#     print((a + b)/ 2)

# myaverage(2, 3)

# def get_max_min(data_list):
#     return (max(data_list), min(data_list))

# def get_max_min(data_list):
#     max_val = max(data_list)
#     min_val = min(data_list)
#     return (max_val, min_val)

# max_val, min_val = get_max_min([5, 3, 2, 6])

# print(max_val)

# print(get_max_min([5, 3, 2, 6]))

# def get_text_list(path):
#     return list(path)


# kg = int(input())
# m = int(input()) * 0.01

# BMI = (kg /(m**2))
# print(BMI)

# if BMI< 18.5:
#     print("마른체형")
# elif 18.5 <= BMI < 25.0 :
#     print("표준")
# elif 25.0 <= BMI < 30.0 :
#     print("비만")
# else:
#     print("고도비만")

# def cal_bmi2(height, weight):
#     height = height * 0.01
#     bmi = weight / (height * height)
#     print("BMI: ", bmi)
#     if bmi< 18.5:
#         print("마른체형")
#     elif 18.5 <= bmi < 25.0 :
#         print("표준")
#     elif 25.0 <= bmi < 30.0 :
#         print("비만")
#     else:
#         print("고도비만")

# while 1:
#     height = input("Height(cm): ")
#     weight = input("Weight(kg): ")
#     cal_bmi2(float(height), float(weight))

def add_start_to_end(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum

print(add_start_to_end(1, 10))
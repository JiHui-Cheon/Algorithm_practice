# def print_ntimes(n):
#     for i in range(n):
#         print("대신증권")

# print_ntimes(2)

def cal_upper(price):
    increment = price * 0.3
    upper_price = price + increment
    return upper_price

print(cal_upper(10000))




def cal_lower(price):
    decrement = price * 0.3
    lower_price = price - decrement
    print(lower_price)


cal_lower(10000)

author = "pystock"

print(__name__)

if __name__ == "__main__":
    print(cal_upper(10000))
    print(cal_lower(10000))
    print(__name__)
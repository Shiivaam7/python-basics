# cities = ["delhi", "patna" ,"mumbai", "noida", "pune", "chennai"]
# heros = ["thor",  "ironman",  "captain america",  "shaktiman"]

# def print_len(list):
#     print(len(list))

# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(heros)
# print_list(cities)
# print(len(cities))

#usd to inr
# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(f"{usd_val} USD = {inr_val} INR")  # Using f-string for better formatting

# converter(599)


#recursion

# def fact(n):
#     if(n == 0 or n == 1):
#         return 1
#     return fact(n-1) * n

# print(fact(6))

# def calc_sum(n):
#     if (n == 0):
#         return 0
#     return calc_sum(n-1) + n

# sum = calc_sum(50)
# print(sum)

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
    
fruits= ["mango", "litchi", "apple", "banana"]

print_list(fruits)
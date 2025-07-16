def is_even(num):
    return num % 2 == 0
def is_odd(num):
    return num % 2 != 0
    
def square(num):
    return num ** 2
# Test Fuctions
num = int(input("Enter a nuber: "))
if is_even(num):
    print(f"{num} is even")

else:
    print(f"{num} is odd")
print(f" The sqaure of {num} is sqare{(num)}" )
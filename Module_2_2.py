first = input()
second = input()
third = input()
if (first == second and first == third):
    print(3)
elif (first == second or first == third or second == third):
    print(2)
else:
    print(1)
import numpy as np

arr_1 = np.array([float(input("Enter Your 1st Number: "))])
arr_2 = np.array([float(input("Enter Your 2nd Number: "))])

print("\n1.Add\n2.Sub\n3.Divide\n4.Multiply\n")

choose = input("Enter Your Operation:") or int(input("Enter Your Operation: "))

if choose == "Add".lower and "Add" or 1:
    print(f"Your Sum is: {arr_1 + arr_2}")

elif choose == "Sub".lower and "Sub" or 2:
    print(f"Your Sub is: {arr_1 - arr_2}")

elif choose == "Divide".lower and "Divide" or 3:
    print(f"Your Divide is: {arr_1 / arr_2}")

elif choose == "Multiply".lower and "Multiply" or 1:
    print(f"Your Multiply is: {arr_1 * arr_2}")

else:
    print("Invalid Operation")
def double_input_values():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    num3 = int(input("Enter number 3: "))

    

    num_list = [num1, num2, num3]


    doubled_list = [num * 2 for num in num_list]
    print(doubled_list)

double_input_values()

# Test Case 1
result_1 = double_input_values () == [2, 4, 6]

# Test Case 2
result_2 = double_input_values () == [-2, -4, -6]

# Test Case 3
result_3 = double_input_values () == [0, 0, 0]

# Test Case 4
result_4 = double_input_values () == [20, 40, 60]


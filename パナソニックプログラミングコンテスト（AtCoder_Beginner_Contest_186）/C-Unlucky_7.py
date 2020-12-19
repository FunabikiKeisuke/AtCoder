n_input = int(input())
array = list(range(1, n_input+1, 1))
str_array = [str(s) for s in array]
not_in_7 = [i for i in str_array if "7" not in i]
int_array = [int(s) for s in not_in_7]
str_oct_array = [oct(s) for s in int_array]
not_in_7 = [i for i in str_oct_array if "7" not in i]
print(len(not_in_7))

how_many_number = int(input("How many numbers do you want to compare?"))
print(how_many_number)
data_list = [ int(x) for x in input("enter your numbers: ").split() ]

print(data_list)
print(max(data_list))
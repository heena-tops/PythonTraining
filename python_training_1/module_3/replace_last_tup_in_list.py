# Write a Python program to replace last value of tuples in a list.

sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

for i in range(len(sample_list)):

   upd_list=list(sample_list[i])

   upd_list[-1] = 100

   sample_list[i]=tuple(upd_list)

print(sample_list)


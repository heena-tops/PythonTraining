#convert tuple to a string

t = ('I',' ','a','m',' ','G','r','o','o','t','!')

string = ' '

for i in t:
    string += i


print(string)

#using join() Function
print(''.join(t))

#using map() Function
print(''.join(map(str,t)))
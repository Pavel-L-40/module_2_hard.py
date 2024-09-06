num = int(input('введите число от 3 до 20: '))
#num = 12
multipy = []
end_list = []
for i in range(3,num+1):
    if num % i == 0:
        multipy.append(i)
        print(i)
#print(multipy)
for i in multipy:
    for j in range((i+1)//2):
        if i - j != 0 and j != 0:
            end_list.append([j,i-j])
    #print(i)
end_list = sorted(end_list)
code = str()
for i in end_list:
    for j in i:
        code += (f'{j}')
print(f'{num} - {code}')
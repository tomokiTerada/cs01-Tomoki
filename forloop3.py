count=0
num=int(input('ใส่เลขของท่าน:'))

for number in range(1,num):
    if(number%2!=0):
        count+=1
        print(number)
lst = []
while True:
    a = int(input('nhập giá trị :'))
    hoi = input('(tiếp tục nhập giá trị?(1/0):')
    lst.insert(0,a)
    if hoi == '0':
        lst.reverse()
        print('list:',lst)
        break
#loại bỏ các phần tử âm
for i in a: #i=4->0
    if a[i]<0:
        a.pop(a[i])
print(lst)
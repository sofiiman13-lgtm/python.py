'''s=int(input('enter a number:66'))
if s%2==0:
    print('even')
else:
    print('odd')'''


'''print(ord('a'))'''


'''print(ord('z'))'''


'''print(ord('Z'))'''

'''ch=input('Enter ch:')
if 'A'<=ch<='Z':
    print('true')
else:
    print('false')'''


'''ch=input('Enter ch:')
if 'a'<=ch<='z':
    print('true')
else:
    print('false')'''


'''num=int(input('enter number:'))
if 10<= num <=99:
 print('true')
else:
 print('false')'''


'''num=int(input('enter number:'))
if 100<= num <=9999:
 print('true')
else:
 print('false')'''

'''a=int(input('Enter'))
if a>b:
    print(f'{a} is greater')
elif b>a:
    print(f'{b}is greater')
else:
    print(f'{a,b}both are equal')'''

'''ch=input('enter:')
if 'A'<=ch<='Z':
    print('upper case')
elif 'a'<=ch<='z':
    print('lower case')
elif '0'<=ch<='9':
 print('it is num')
else:
   print('spl charatcer')'''


'''ch=input('enter:')
if 'A'<=ch<='Z':
    print('upper case')
elif 'a'<=ch<='z':
    print('lower case')
elif '0'<=int(ch)<='9':
 print('it is num')
else:
   print('spl character')'''


'check given character is vowel'
'''ch=input('enter:')
if ch.isalpha():
    if ch in 'aeiouAEIOU':
        print('it is vowel')
    else:
        print('it is consonant')
else:
    print('not an alphabet')'''


'whether given list length is even or not and print it'
'''l=eval(input('Enter:'))
if len(l)%2==0:
        print('l')
    else:
        print('Odd length')
else:
print('not a list')'''



'''i=1
while i<=10:
    print(1)'''

'''i=1
while i<=5:
    i+=1
    print('hello')'''


'input elements in a list'
'''l=[3,6,7,4]
i=0
while i<len(l):
    print(l[i])
    i+=1'''

'reverse a number'
'''n=int(input('enter:'))
rev=0
while n>0:
    ld=n%10
    n=n//10
    rev=rev*10+ld
    print(rev)'''


'for loop'
'''for i in range(1,10):
    print(i)'''

'''for i in range(1,5):
    print('hello')'''

'convert upper case to lower case'
'''s=input('enter:')
out=''
for i in s:
    if 'A'<=i<='Z':
        out=out+chr(ord(i)+32)
    else:
        out+=i
print(out)'''


'''print(ord('h'))'''

'convert lower case to upper case'
'''s=input('enter:')
out=''
for i in s:
    if 'a'<=i<='z':
        out=out+chr(ord(i)-32)
    elif 'A'<=i<='Z':
        out=out=out+chr(ord(i)+32)
    else:
        out+=i
print(out)'''

'''s=[12,10,'hello','good',5j,'bye']
out={}
for i in s:
    if type(i)==str:
        out[i]=i[0]=i[-1]
        pass
print(out)'''

'''s=input('enter:')
out=''
for i in s:
    if 'A'<=i<='Z':
        out=out+chr(ord(i)+32)
    elif 'a'<=i<='z':
        out=out+chr(ord(i)-32)
    else:
        out+=i
print(out)'''    


for i in range(1,6):
    for j in range(1,6):
        print('*',end=' ')
    print()


'''def convert(s):
    s=input('enter:')
    out=''
    for i in s:
          if 'A'<=i<='Z':
            out=out+chr(ord(i)+32)
        else:
            out+=i
    print(out)convert())'''

'with arguments with return type'
'''def add(a,b):
    return a+b
print(add(20,30))'''


'''def add(a,b):
    print(a+b)
add(20,30)'''
    

def add():
   a=10
   b=10
   print(a+b)
add()
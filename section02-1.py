#Section02-1
#Print 구문의 이해

#기본출력
print('Hello Python!')
print("Hello Pythin!")

print()

#Separator option
print('T', 'E', 'S', 'T', sep='')
print('2021', '09', '01', sep='-')

#end Option
print('Welcome To', end='')
print('the black parade')

#format 사용
print('{} and {}'.format('You', 'Me'))
print("{0} and {1}".format('You','Me'))
print('{a} and {b}'.format(a='You', b='Me'))

print("") #%s %d %f
print("%s's favorite number is %d" % ('hoseok',7))

print('Test1: %5d, price: %4.2f' % (776, 6543.123))
print('Test1: {0: 5d}, Price: {1:4.2f}'.format(776, 6543.123))

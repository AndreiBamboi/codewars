
'''
spam, ham = 'yum', 'YUM'
[sspam, hham] = ['yyum', 'YYUM']
a,b, c, d = 'spam'
T, *t = 'spam'
print(spam, sspam, ham, hham)
print(a)
print(t)
'''
import sys
olista= [1,2,3]
temp = sys.stdout
sys.stdout = open('fisier.txt', 'w')
print(olista)
sys.stdout = temp
print(open('fisier.txt').read())
print('%s %s %s' % ('ta', 'ra', 'rap'))
print('{0} {1} {2}'.format('bla', 'cla' , 'ta'))


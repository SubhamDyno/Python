'''
11111
2222
333
44
5
'''

class Pattern(object):
    def user(num):
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i<=j:
                    print(i,end='')
            print('\r')

obj = Pattern.user(5)

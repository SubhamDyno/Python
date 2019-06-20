'''
1
12
123
1234
12345
'''

class Pattern(object):
    def user(num):
        for i in range(1,num+1):
            for j in range(1,num+1):
                if j>=i:
                    print(j,end='')
            print('\r')

obj = Pattern.user(5)

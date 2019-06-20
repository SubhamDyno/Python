'''
12345
1234
123
12
1
'''

class Pattern(object):
    def user(num):
        for i in range(1,num+1):
            for j in range(1,num+1):
                if i>=j:
                    print(j,end='')
            print('\r')

obj = Pattern.user(5)

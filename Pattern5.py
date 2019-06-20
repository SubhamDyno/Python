'''
54321
5432
543
54
5

'''

class Pattern(object):
    def user(num):
        for i in range(1,num+1):
            for j in range(num,0,-1):
                if i<=j:
                    print(j,end='')
            print('\r')

obj = Pattern.user(5)

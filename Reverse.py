class Reverse:
    def revNum(num):
        rev = 0
        digit = num
        while(num != 0):
            digit = num%10
            rev = rev*10 + digit
            num = num//10
        print("Reversed number is : " + str(rev))

obj = Reverse
obj.revNum(12345)

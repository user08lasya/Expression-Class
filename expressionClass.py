class Addition:
    def __init__(self,a,b,c):
        self.num1=a
        self.num2=b
        self.num3=c
    def result(self):
        self.num=self.num1+self.num2+self.num3
        print('Output:' ,self.num)

a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
c = int(input("Enter 3rd Number: "))
Sum = Addition(a,b,c)

Sum.result()
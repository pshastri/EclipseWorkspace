'''
Created on Sep 29, 2016

@author: PShastri
'''
class calc():
    def __init__(self,num1,num2):
        self.number1=int(num1)
        self.number2=int(num2)
    def addme(self):
        return (self.number1+self.number2)
    def subme(self):
        return (self.number1-self.number2)
if __name__=='__main__':
    print "Welcome"
    num1=raw_input("Enter 1st number: ")
    num2=raw_input("Enter 2nd number: ")
    mycalc=calc(num1,num2)
    print mycalc.addme()
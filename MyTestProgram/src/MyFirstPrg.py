'''
Created on Sep 26, 2016

@author: PShastri
'''


    
def AddNum(a,b):
    total = a+b
    return total

if __name__=='__main__':
    a = int(raw_input("Enter 1st Number: "))
    b = int(raw_input("Enter 2nd Number: "))
    print "Total is: ", AddNum(a, b)
    
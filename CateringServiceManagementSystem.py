print("Welcome to the Rocky Catering ServiceManagement System")




class Rockey:
    def __init__(self):
        print("\n")
        condition=True
        while condition==True:
            # try:
            #     self.name=input("Please enter booking name : ")
            
            #     self.num=int(input("Enter the number of guests : "))
            #     condition=False
            # except:
            #     print("Error please enter the required data.")
            #     condition=True
            self.name=input("Please enter booking name : ")
            if not self.name:
                print("Error please enter booking name.")
                condition=True
            else:
                self.num=int(input("Enter number of guests : "))
                if self.num < 0 or self.num is not None:
                    print("Error please enter number of guests : ")
                    condition=False
                else:
                    condition=False


    def returnName(self):
        return self.name

    def returnNum(self):
        return self.num

    def calculate(self):
        if(self.num<10):
            print("ERROR number of guest must be greater or equal to ten.")
            return
        else:
            if(self.num>=10 and self.num<=20):
                return 29.50*self.num
            elif(self.num>=21 and self.num<=40):
                return 590+24.50*(self.num-20)
            elif(self.num>=41):
                return 1080+19.50*(self.num-40)
            else:
                return 0

    def displayData(self):
        print("The tour charge of "+self.name+" for "+str(self.num)+" is $"+str(self.calculate()))

    def getMin(self):
        print("Booking: "+self.name+" has the minimum number of "+str(self.num)+" guests.")

    def getMax(self):
        print("Booking: "+self.name+" has the maximum number of "+str(self.num)+" guests.")


# obj1=Rockey()
# obj1.displayData()

# obj2=Rockey()
# obj2.displayData()

# obj3=Rockey()
# obj3.displayData()

# n=Rockey()
var=[]

num=int(input("Enter no of obj : "))
for i in range(num):
    i = Rockey()
    i.displayData()

print("\n")

# print("*-*-*-*Statistical information for Rockey Caterying Service*-*-*-*")
# print("\n")
# if max(obj1.returnNum(),obj2.returnNum(),obj3.returnNum())==obj1.returnNum():
#     obj1.getMax()
# elif max(obj1.returnNum(),obj2.returnNum(),obj3.returnNum())==obj2.returnNum():
#     obj2.getMax()
# else:
#     obj3.getMax()

# if min(obj1.returnNum(),obj2.returnNum(),obj3.returnNum())==obj1.returnNum():
#     obj1.getMin()
# elif min(obj1.returnNum(),obj2.returnNum(),obj3.returnNum())==obj2.returnNum():
#     obj2.getMin()
# else:
#     obj3.getMin()
# print("\n")


# print(" The average number of guests per booking is "+str(((obj1.returnNum()+obj2.returnNum()+obj3.returnNum())/3)))
# print(" Total charge collected is $"+str(obj1.calculate()+obj2.calculate()+obj3.calculate()))

print("\n")
print("Thank you for using the Rocky Catering Service Management System")
print("Program written by : Sushil Dhakal")
print("\n")
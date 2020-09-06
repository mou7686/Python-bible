class Product:
    def getData(self,name,code,amount):
        self.name=name
        self.code=code
        self.amount=amount
    def displayProduct(self):
        print("Name of the product:",self.name)
        print("Product code:",self.code)
        print("Total sale amount:",self.amount)
class Sales(Product):
    def getpayamount(self,day,tax,totamt):
        self.day=day
        self.tax=tax
        self.totamt=totamt
    def displaypayamount(self):
        print("Number of days taken to pay the sale amount:",self.day)
        print("The service tax:",self.tax)
        m=self.day
        if m>30:
            self.rate="Actual sale amount + service tax + fine"
            self.totamt=self.amount+(self.amount*self.tax)+(self.day*0.025)
        else:
            self.rate="Actual sale amount + service tax"
        print("Amount paid by the retailer to the wholesaler:",self.rate,"=",self.totamt)
name=input("Enter name of the product:")
code=int(input("Enter the code:"))
amount=float(input("Enter the amount of the product:"))
day=int(input("Enter number of days:"))
tax=float(input("Enter service tax:"))
totamt=float(input("Retailer paid amount:"))
print("Update Bill")
product1=Sales()
product1.getData(name,code,amount)
product1.getpayamount(day,tax,totamt)
product1.displayProduct()
product1.displaypayamount()
        

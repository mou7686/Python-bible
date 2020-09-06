class stock:
    def getData(self,item,qty,rate,amt):
        self.item=item
        self.qty=qty
        self.rate=rate
        self.amt=amt
    def displaystock(self):
        print(" name item:",self.item)
        print("quantity:",self.qty)
        print("unit price:",self.rate)
        print("net value:",self.amt)
class Purchase(stock):
    def getquantity(self,pqty,prate):
        self.pqty=pqty
        self.prate=prate
    def displayquantity(self):
        print("purchase:",self.pqty)
        print("unit price:",self.prate)
        print("update stock:",self.qty+self.pqty)
        print("update amount:",(self.qty+self.pqty)*self.prate)
        
item=input("Enter item name:")
qty=int(input("Quantity of item:"))
rate=int(input("Unit price of item:"))
amt=int(input("Amount of item:"))
pqty=int(input("New quantity of item:"))
prate=int(input("New unit price:"))
print("Updated Stock")
item1=Purchase()
item1.getData(item,qty,rate,amt)
item1.getquantity(pqty,prate)
item1.displaystock()
item1.displayquantity()
      

class Share:
    
    def __init__(self,curprice,moneyhave=0,numshares=0,finprice=0):
        self.moneyhave = float(moneyhave)
        self.curprice = float(curprice)
        self.var = .0001/2
        self.numshares = -1 * float(numshares)
        self.finprice = float(finprice)
    def quant(self):
        denom = self.var*2
        outfr = self.var - self.curprice
        undersq = (self.curprice - self.var)**2 + 4 * self.var * self.moneyhave
        quantity = (outfr + undersq**(1/2))/denom
        return quantity
    def moneyback(self):
        costfin = self.curprice*self.numshares + ((self.numshares - 1)*self.numshares)*self.var
        sellprice = -1*costfin
        return sellprice
    def quant2(self):
        costlist = []
        ourshares = (self.finprice - self.curprice)/(10**-4)
        thecost = self.var*ourshares*(ourshares-1) + ourshares*self.curprice
        costlist.append(thecost)
        costlist.append(ourshares)
        return costlist

tester = int(input("Would you like to know how much stock you can buy (Enter 0), know how much selling would make (Enter 1), know how much stock to sell to get a certain amount (Enter 2), or know how much stock to buy to get a stock to a certain price (Enter 3)? "))
if tester == 0:
    print(str(int(Share(input("Enter share price: "),input("Enter how much money you have: "),0).quant()//1)) + " shares can be purchased.")
if tester == 1:
    print(str(int(Share(input("Enter share price: "),0,input("Enter how many shares you would like to sell: ")).moneyback()//1)) + " dollars can be made off of that many shares.")
if tester == 2:
    print("You would have to sell " + str(int((-1*Share(input("Enter share price: "),"-"+str(input("Enter how much money you'd like: ")),).quant())//1)) + " shares")
if tester == 3:
    qbert = Share(input("Enter current share price: "),0,0,input("Enter final share price: ")).quant2()
    print("To get to that price, you would have to spend "+str(int(qbert[0]))+" dollars and would have to buy "+str(int(qbert[1]))+" shares.")
        

# Python Object Oriented Programming by Joe Marini course example
# Programming challenge: implement a dataclass

# Challenge: convert your classes to dataclasses
# The subclasses are required to override the magic method
# that makes them sortable
from dataclasses import dataclass

@dataclass
class Asset():
    price: float
    
@dataclass
class Stock(Asset):
    ticker : str
    company: str

    def __str__(self):
        return f"Ticker :{self.company} --${self.price}"
    
    def __lt__(self,anotherStock):
        return self.price < anotherStock.price

@dataclass
class Bond(Asset):
    description: str
    duration:int
    yieldamt:float

    def __str__(self):
        return f"{self.description}: {self.duration}'yr' : ${self.price} : {self.yieldamt}%"
    
    def __lt__(self,anotherBond):
        return self.yieldamt < anotherBond.yieldamt

# ~~~~~~~~~ TEST CODE ~~~~~~~~~
stocks = [
    Stock("MSFT", 342.0, "Microsoft Corp"),
    Stock("GOOG", 135.0, "Google Inc"),
    Stock("META", 275.0, "Meta Platforms Inc"),
    Stock("AMZN", 120.0, "Amazon Inc")
]

bonds = [
    Bond(95.31, "30 Year US Treasury", 30, 4.38),
    Bond(96.70, "10 Year US Treasury", 10, 4.28),
    Bond(98.65, "5 Year US Treasury", 5, 4.43),
    Bond(99.57, "2 Year US Treasury", 2, 4.98)
]

try:
   ast = Asset(100.0)
except:
   print("Can't instantiate Asset!")

stocks.sort()
bonds.sort()

for stock in stocks:
   print(stock)
print("-----------")
for bond in bonds:
   print(bond)
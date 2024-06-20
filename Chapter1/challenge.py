class Stock:
    def __init__(self,ticker,price,company_name):
        self.ticker=ticker
        self.price=price
        self.company_name=company_name

    def get_description(self):
        return f"{self.ticker} : {self.company_name} -- {self.price}"



msft=Stock("MSFT",342.0,"MicroSoft Corp")
goog=Stock("GOOG",342.0,"Google Inc")
meta=Stock("META",342.0,"Meta Platforms Inc")
amzn=Stock("AMZN",342.0,"Amazon Inc")

print(msft.get_description())
print(goog.get_description())
print(meta.get_description())
print(amzn.get_description())


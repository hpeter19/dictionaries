#Setting default values for discount and tax
def net_price(list_price,discount=0,tax=0.05):
    return list_price *(1-discount)*(1+tax)

print(net_price(1000,0,0.05))
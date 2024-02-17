
def profit(info):
    [a,b,c]= info.values()
    lista = list(info.values())
    print(round((lista[1]-lista[0])*lista[2]))
    print([a,b,c])
    return  round((b-a)*c)




print(profit({'cost_price': 0.1, 'sell_price': 0.18, 'inventory': 259800}))

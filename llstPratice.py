product=['rice','wheat','oil','soap']
productprice = [20,30,40,50]
productsold=['wheat','rice']
soldprice=[40,20]
def priceComparision(product,price,sold,soldprice):
    print(product)
    print(price)
    print(sold)
    print(soldprice)
    errorcount = 0

    for number,i in enumerate(productsold):
        if i in product:
            indexofproduct = product.index(i)
['rice', 'wheat', 'oil', 'soap']
[20, 30, 40, 50]
['wheat', 'rice']
[40, 20]
wheat 30 40
rice 20 20
            originalprice = productprice[indexofproduct]
            itemsoldprice = soldprice[number]
            print(i,originalprice,itemsoldprice)
            if originalprice != itemsoldprice:
                errorcount = errorcount + 1
    print ('number of items difference in price: ' + str(errorcount))
if __name__ == '__main__':
    priceComparision(product,productprice,productsold,soldprice)


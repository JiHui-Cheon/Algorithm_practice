naver_closing_price = [488550, 500500, 501000, 461500, 474500]

print(naver_closing_price)
print(max(naver_closing_price))
print(min(naver_closing_price))
print("가격차:" , (max(naver_closing_price) - min(naver_closing_price)))

print("수요일 종가:" , naver_closing_price[2])

naver_closing_price2 = {'09/11': 488500, '09/10': 500500, '09/09': 501000, '09/08': 461500, '09/07': 474500}

print(naver_closing_price2['09/09'])
print(naver_closing_price2.values())

mystock = "Naver"
print(mystock == "Naver")

wikibooks_cur_price = 9000
if wikibooks_cur_price >= 10000:
    print("Buy 10")
elif wikibooks_cur_price <= 9000:
    print("Sell 10")

wikibooks_cur_price = 11000
if wikibooks_cur_price >= 10000:
    print("Buy 5")
    print("Buy 5")
    print("Buy 5")

price = 7000
if price < 1000:
    bid = 1
elif price >= 1000 and price < 5000:
    bid = 5
elif price >= 5000 and price < 10000:
    bid = 10
elif price >= 10000 and price < 50000:
    bid = 50
elif price >= 50000 and price < 100000:
    bid = 100
elif price >= 100000 and price < 500000:
    bid = 500
elif price >= 500000:
    bid = 1000

print(bid)
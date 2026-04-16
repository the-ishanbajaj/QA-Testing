raw_cart_prices = ["  $15.99", "$45.50  ", "FREE", " $12.00", "  $100.25 "]
sum = 0.0
for i in raw_cart_prices :
    i=i.strip()
    i=i.replace("$","")
    if i == "FREE" :
        i="0"
    sum += float(i)

print(sum)
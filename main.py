member_type = "Gold"
coupon = 0.50


comic_price = 0
total = 0

if member_type == "Silver":
    comic_price = 3.50
elif member_type == "Gold":
    comic_price = 2.99
else:
    comic_price = 4.99

print("Comic Price:")
print(comic_price)

total = comic_price * 0.025

if coupon > 0:
    total = comic_price - coupon



print("Total:")
print(total)

#constants
usb_price=6 #price of one USB stick
total_money= 50 # total money available
#calculation how many USB stick she can buy 
usb_count=total_money // usb_price

#calculate how many pounds shw will left
money_left=total_money % usb_price
#print the result 
print("she can buy",usb_count,"USB_sticks.")
print("she will have £",money_left,"left.")
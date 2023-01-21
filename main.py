# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
leek_price = 2
leek_price = str(leek_price)

print ("Leek is " + leek_price + " euro per kilo.")


#We've got an order of 4 leeks
leek_4 = ('We got an order for 4 leeks')

#Use find and slicing to extract the number from this string.
find_leek_four = leek_4.find('four')


#Cast it into an integer.
int(find_leek_four)

#Use this and leek_price to compute the sum total and store it in sum_total. Print out the value #for this variable.
sum_total = (int(leek_price) * 4)
print (sum_total)

#Broccoli costs 2.34 euros per kg. We got an order: 'broccoli 1.6'.

price_broccoli = (2.34)
order_broccoli = (1.6)

total_price = (price_broccoli *order_broccoli)

print ('1.6kg broccoli costs ' + str(round(total_price,2))+'e')







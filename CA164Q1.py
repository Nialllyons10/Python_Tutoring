def main(): 
	
	numOfShares = 2000
	amountPaidForStock = numOfShares * 40 
	stockBrokerAmount = amountPaidForStock * 0.03
	
	
	amountStockSoldFor = numOfShares * 42.75
	stockBrokerAfterSale = amountStockSoldFor * 0.03
	
	amountStockBrokerGot = stockBrokerAmount + stockBrokerAfterSale
	
	moneyLeft = amountStockSoldFor - amountStockBrokerGot
	
	print("mark paid: ", amountPaidForStock, " for stock")
	print("mark paid: ", stockBrokerAmount, "to the stockbroker")
	print()
	print("mark sold the stock for: ", amountStockSoldFor) 
	print("Amount stockbroker got after sale ", stockBrokerAfterSale)
	print()
	
	if moneyLeft > 0:
		print("Made a profit")
	else: 
		print("Did not make a profit")
	
main()
	
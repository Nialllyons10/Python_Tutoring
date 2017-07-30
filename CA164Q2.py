def main(): 
	packetOfSaus = 10 
	packetOfBuns = 8 
	
	attending = int(input("How many people will be attending? "))
	amountOfSaus = int(input("How many sausages will each person get? "))
	
	sausagesNeeded = attending * amountOfSaus
	bunsNeeded = attending * packetOfBuns 
	
	amountOfPacketsNeeded = sausagesNeeded // packetOfSaus
	packetReaminder = sausagesNeeded % packetOfSaus
	
	if packetReaminder >= 1: 
		amountOfPacketsNeeded += 1
	
	totalSaus = amountOfPacketsNeeded * packetOfSaus 
	leftoverSaus = totalSaus - sausagesNeeded
		
	totalAmountOfSausPackets = amountOfPacketsNeeded
	
	bunPackets = sausagesNeeded // packetOfBuns
	remianderbun = sausagesNeeded % packetOfBuns
	
	if remianderbun >= 1:
		bunPackets += 1
	
	print("Sausage Packets: ", totalAmountOfSausPackets)
	print("Bun PAckets: " , bunPackets)
	print("Leftover sausages: ", leftoverSaus)
	
	
main()
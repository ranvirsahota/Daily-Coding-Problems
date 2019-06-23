listOfNumbers = [10, 15, 3, 7]
k = 17

def addition():
	for index in range (len(listOfNumbers)):
		searchForNumber = k - listOfNumbers[index]
		if index == len(listOfNumbers):
			return False
		for number in listOfNumbers[index+1:]:
			if number == searchForNumber:
				print ("{0} + {1} = {2}".format(listOfNumbers[index], number, k)) 
				return True
		
print(addition())
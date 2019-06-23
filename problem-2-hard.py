multiplyers = [1, 2, 3, 4, 5]
product = [1] * len(multiplyers)
for index in range(len(multiplyers)):
                       modifyMultiplyers = list(multiplyers)
                       del modifyMultiplyers[index]
                       for num in modifyMultiplyers:
                           product[index] *= num
                           
                        
                        
print(product)

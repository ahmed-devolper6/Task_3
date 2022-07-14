from num2words import num2words
def words(Given_Number): #give i number and output word of this number
    if Given_Number == int(Given_Number):
        return num2words(Given_Number)
    else:
        return "Plese Type i number..."

sixty = words(60)
print(sixty)
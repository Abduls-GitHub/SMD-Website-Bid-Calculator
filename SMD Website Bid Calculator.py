print("This is the bid calculator")
print("")

bidAmount = int(input("Enter bid amount:" + "R"))


buyersCommision = int((bidAmount * 0.05))

DocumentationFee = 2500


totalExcVat = int(bidAmount + buyersCommision + DocumentationFee)

print("Amount excl vat")


print("R" + str(totalExcVat))

VAT = int((totalExcVat * 0.15))

print("")

totalIncVat = int(totalExcVat + VAT)

print("Amount incl vat")

print("R" + str(totalIncVat))


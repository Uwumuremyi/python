totalGallons = 0
totalMiles = 0

while 1:
    gallons = input("Enter the gallons used, (-1 to end) : ")
    gallons = float( gallons )

    if gallons == -1:
        break

    miles = input("Enter the miles driven: ")
    miles = float(miles)

    totalGallons = totalGallons + gallons
    totalMiles = totalMiles + miles

    milesPerGallons = miles / gallons

    print("The miles / gallons for this tank was %f" % milesPerGallons)


overallMilesPerGallon = totalMiles / totalGallons
print("The overall average miles / gallons was %f" % overallMilesPerGallon)
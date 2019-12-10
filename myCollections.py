from array import array

cityList = ["Stockholm", "Uppsala", "Malmo"]
cityList.append("Copenhagen")
#cityList.append(54) # A list can store different type of objects (an array cannot)
print(cityList)
print(cityList[0])
print(cityList[-1])
print()
print(cityList[1:-1]) # From (including) : To (not including)
print()
stationArray = array("d") #array of digits (d)
stationArray.append(1)
stationArray.append(2)
stationArray.insert(0, 3)
print(stationArray)
print(stationArray[-1])
print("Array: " + str(stationArray))
print("Length of the array: " + str(len(stationArray)))
print("Sorted list: " + str(cityList.sort()))
print("List: " + str(cityList))

print()
stationDictionary = {"Stockholm":1, "Goteborg":2, "Malmo":3} #Control D control D
print(stationDictionary)
print(stationDictionary["Stockholm"])
print(stationDictionary["Uppsala"])
#Made by Albin Westerlund with help
#This python code creates a list of estimated production and a list with timestamps.
#First estimated production has the first timestamp in the other list, second estimation the second timestamp and so on.

from urllib.request import urlopen
import xml.etree.ElementTree as ET

url = urlopen('http://opendata.fmi.fi/wfs?service=WFS&version=2.0.0&request=getFeature&storedquery_id=fmi::forecast::hirlam::surface::point::multipointcoverage&place=palosaari,vaasa&parameters=TotalCloudCover')
xmldocument = ET.parse(url)
root = xmldocument.getroot()

#for loop finds cloud data from xml document
#cloudXML is some kind of string
list = []
for cloudXML in root.findall(".//{http://www.opengis.net/gml/3.2}doubleOrNilReasonTupleList"):
    list = cloudXML.text.split()

#turns the list containing strings to float numbers
listFloat = []
for x in list:
    number = float(x)
    listFloat.append(number)

#calculates estimated production
listProducePower = []
for y in listFloat:
    #100 minus the cloud percent value e.g. 100% is 0%, 75% is 25% -> 100% cloud coverage = zero production, 50% = 50% production
    produce = (100 - y)
    #turns percent value into decimal e.g. 100% = 1, 75% = 0,75 etc.
    produce = produce / 100
    #multiplies with 5, The solar plants max output is 5 kw (kilowatt)
    produce = produce * 5
    #rounds the estimated production to 3 decimals
    produce = round(produce, 3)
    #puts estimated production into a new list
    listProducePower.append(produce)

#------------End of cloud data--------------------------------------------------------

#------------Start of time data-------------------------------------------------------

#for loop finds position and date data from xml document
#positionDate is some kind of string
for positionDate in root.findall(".//{http://www.opengis.net/gmlcov/1.0}positions"):
	#print (positionDate.text)
    list2 = positionDate.text.split()

#turns the list2 containing strings of position and date to float numbers
listFloat2 = []
for a in list2:
    number2 = float(a)
    listFloat2.append(number2)

#adds only timestamp (unix) to new timtestamp list
listTimeStamp = []
for b in listFloat2:
    if not b == 21.59122:
        if not  b == 63.10703:
            #changes b from float to integer to remove decimals
            b = int(b)
            listTimeStamp.append(b)

#prinst list of estimated production and timestamp for testing purposes
print(listProducePower)
print(listTimeStamp)

#creates testing lists so it is easier to see on the graph in IoT Tickets dashboard
#listProducePower = [5.0, 10.0, 7.0, 5.0, 10.0, 0.0, 4.0, 7.0, 7.0, 7.0, 6.0, 4.0, 3.0, 1.0, 1.0, 1.0, 4.0, 2.0, 3.0, 7.0, 6.0, 5.0, 4.0, 2.0, 8.0, 8.087, 2.0, 1.0, 4.0, 4.0, 4.0, 3.0, 4.0, 10.0, 4.0, 9.0]

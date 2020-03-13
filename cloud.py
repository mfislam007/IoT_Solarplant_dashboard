import xml.etree.ElementTree as ET
tree = ET.parse('totalcloudcover.xml')
root = tree.getroot()
print(root)
#https://docs.python.org/3/library/xml.etree.elementtree.html
#print("test")
for cloud in root.findall(".//{http://www.opengis.net/gml/3.2}doubleOrNilReason$"): #no error if ...OrNilReason$"):
	print(cloud.text)

#print("test2")
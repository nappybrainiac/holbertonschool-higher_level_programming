from xml.dom.minidom import Document
import json
from car import Car

''' Open the json file and put it's contents in cars_json'''
jsonfile = "5-main.json"
file_open = open(jsonfile)
diffCars = json.load(file_open)
file_open.close()

'''initialize lists and variables'''
cars = []
brands = []
totalDoors = 0
doc = Document()

'''special XML stuff to create an element'''
element_cars = doc.createElement('cars')

'''special XML stuff to create a child element'''
doc.appendChild(element_cars)

'''Iterating through the json file to place
   items in the list and update the number of
   total doors'''
for item in diffCars:
    obj = Car(item)
    cars.append(obj)
    if not obj.get_brand() in brands:
        brands.append(obj.get_brand())
    totalDoors = totalDoors + obj.get_nb_doors()
    objXml = obj.to_xml_node(doc)
    element_cars.appendChild(objXml)

print len(brands)
print totalDoors
print cars[3]
print doc.toxml(encoding = 'utf-8')

import json

class Car:

    '''Initializing the class'''
    def __init__(self, *args, **kwargs):

        if len(args) > 0:
            if isinstance(args[0], dict):
                name = args[0].get('name')
                brand = args[0].get('brand')
                nb_doors = args[0].get('nb_doors')
            elif isinstance(args[0], basestring):
                split_args = args[0].split(",")
                name = split_args[0]
                brand = split_args[1]
                nb_doors = int(split_args[2])
        else:
            name = kwargs.get('name')
            brand = kwargs.get('brand')
            nb_doors = kwargs.get('nb_doors')

        if name == "" or not isinstance(name, basestring):
            raise Exception("name is not a string")
        if brand == "" or not isinstance(brand, basestring):
            raise Excpetion("brand is not a string")
        if type(nb_doors) != int or nb_doors <= 0:
            raise Exception("nb_doors is not > 0")
        self.__name = name
        self.__brand = brand
        self.__nb_doors = nb_doors

    '''Getters'''

    def get_name(self):
        return self.__name

    def get_brand(self):
        return self.__brand

    def get_nb_doors(self):
        return self.__nb_doors

    '''to return a dictionary data structure which describes the car'''
    def to_hash(self):
        return {'name': self.__name, 'brand': self.__brand, "nb_doors": self.__nb_doors}

    '''to return a string with all information: ":name :brand (:nb_doors)"'''
    def __str__(self):
        return "%s %s (%s)" % (self.__name, self.__brand, self.__nb_doors)

    '''to update the private attribute nb_doors'''
    def set_nb_doors(self, number):
        self.__nb_doors = number

    '''to return a string in JSON format'''
    def to_json_string(self):
        return json.dumps(self.to_hash())

    '''To return an XML document'''
    def to_xml_node(self, doc):
        car = doc.createElement("car")

        car.setAttribute("nb_doors", str(self.__nb_doors))
        name = doc.createElement("name")
        name.appendChild(doc.createCDATASection(self.__name))
        car.appendChild(name)

        brand = doc.createElement('brand')
        brand.appendChild(doc.createTextNode(self.__brand))
        car.appendChild(brand)

        return car

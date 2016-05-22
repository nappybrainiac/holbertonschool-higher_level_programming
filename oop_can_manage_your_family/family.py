'''
Project:            OOP can manage your family
Dependent files:    0-main.py, 1-main.py, 2-main.py, 3-main.py,
                    4-main.py, 5-main.py

Task 0:             A script that describes the 'Person' class.
Task 1:
Task 2:
Task 3:
Task 4:
Task 5:

Gloria Bwandungi, 2016.
'''

class Person(object):

    '''Class Attributes'''
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male", "Non-Binary"]

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):

        ''' Private Attributes'''
        if type(id) is not int or id < 0:
            raise Exception("id is not an integer")
        self.__id = id
        if type(first_name) is not str or (first_name == ""):
            raise Exception("first_name is not a string")
        self.__first_name = first_name


        if len(date_of_birth) !=3 :
            raise Exception("date_of_birth is not a valid date")
        if(date_of_birth[0] > 12 or date_of_birth[0] < 1 ):
            raise Exception("date_of_birth is not a valid date")
        if(date_of_birth[1] > 31 or date_of_birth[1] < 1):
            if date_of_birth[0] == 2 and date_of_birth[1] > 28:
                raise Exception("date_of_birth is not a valid date")
            raise Exception("date_of_birth is not a valid date")
        self.__date_of_birth = date_of_birth

        if genre not in Person.GENRES:
            raise Exception("genre is not valid")
        self.__genre = genre
        if eyes_color not in Person.EYES_COLORS:
            raise Exception("eyes_color is not valid")
        self.__eyes_color = eyes_color

    ''' Getters '''
    def get_id(id):
        return self.__id

    def get_first_name(self):
        return self.__first_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_eyes_color(self):
        return self.__eyes_color

    def get_genre(self):
        return self.__genre

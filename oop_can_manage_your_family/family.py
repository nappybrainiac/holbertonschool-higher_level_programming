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

import json
import os.path

class Person(object):

    '''Class Attributes'''
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male", "Non-Binary"]

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):

        ''' Private Attributes'''
        if type(id) is not int or id < 0:
            raise Exception("id is not an integer")
        self.__id = id
        if type(first_name) is not str or first_name == "":
            raise Exception("first_name is not a string")
        self.__first_name = first_name


        if len(date_of_birth) !=3 :
            raise Exception("date_of_birth is not a valid date")
        if date_of_birth[0] > 12 or date_of_birth[0] < 1:
            raise Exception("date_of_birth is not a valid date")
        if date_of_birth[1] > 31 or date_of_birth[1] < 1 :
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

    '''  Public Attributes '''
    def is_married_to(int):
        self.is_married_to = is_married_to

    ''' Public Methods'''
    def can_run(self):
        return False

    def need_help(self):
        return True

    def is_young(self):
        return True

    def can_vote(self):
        return False

    def can_be_married(self):
        return False

    def is_married(self):
        if self.is_married_to == 0:
            return False
        else:
            return True

    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0


    def just_married_with(self, p):
        if self.can_be_married() or p.can_be_married() == False:
            raise Exception("Can't be married")
        if self.is_married_to != 0 or p.is_married_to != 0:
            raise Exception("Already married")
        self.is_married_to = p.__id
        p.is_married_to = self.__id
        if self.__genre == "Male":
            p.last_name = self.last_name
        if p.__genre == "Male":
            self.last_name = p.last_name

    ''' Getters '''
    def get_id(self):
        return self.__id

    def get_first_name(self):
        return self.__first_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_eyes_color(self):
        return self.__eyes_color

    def get_genre(self):
        return self.__genre

    def __str__(self):
        ''' Returns full name '''
        return str(self.__first_name  + " " + self.last_name)

    def is_male(self):
        if Person.GENRES == "male":
            return True

    def age(self):
        date = [05, 20, 2016]

        if self.__date_of_birth[0] >= date[0]:
            if self.__date_of_birth[1] > date[1]:
                age = (date[2] - 1) - self.__date_of_birth[2]
        else:
            age = date[2] - self.__date_of_birth[2]
        return age

    ''' Overloading Methods '''

    def __lt__(self,other):
        return self.age() < other.age()

    def __le__(self,other):
        return self.age() <= other.age()

    def __gt__(self,other):
        return self.age() > other.age()

    def __ge__(self,other):
        return self.age() >= other.age()

    def __eq__(self,other):
        return self.age() == other.age()

    def __ne__(self,other):
        return self.age() != other.age()

    '''The JSON Method'''
    def json(self):
        json = {
            'id': self.__id,
            'eyes_color': self.__eyes_color,
            'genre': self.__genre,
            'date_of_birth': self.__date_of_birth,
            'first_name': self.__first_name,
            'last_name': self.last_name,
            'is_married_to': self.is_married_to
        }

    '''Sets Person attributes by value from the dictionary(Hash)'''
    def load_from_json(self, json):
        if type(json) != dict:
            raise Exception("json is not valid")

        self.__id = json['id']
        self.__eyes_color = json['eyes_color']
        self.__genre = json['genre']
        self.__date_of_birth = json['date_of_birth']
        self.__first_name = json['first_name']
        self.last_name = json['last_name']
        self.is_married_to = json['is_married_to']




''' Subclasses Defined '''
class Baby(Person):
    '''Public Methods'''
    def can_run(self):
        return False

    def need_help(self):
        return True

    def is_young(self):
        return True

    def can_vote(self):
        return False

    def can_be_married(self):
        return False


class Teenager(Person):
    '''Public Methods'''
    def can_run(self):
        return True

    def need_help(self):
        return False

    def is_young(self):
        return True

    def can_vote(self):
        return False

    def can_be_married(self):
        return False

class Adult(Person):
    '''Public Methods'''
    def can_run(self):
        return True

    def need_help(self):
        return False

    def is_young(self):
        return False

    def can_vote(self):
        return True

    def can_be_married(self):
        return True


class Senior(Person):
    '''Public Methods'''
    def can_run(self):
        return False

    def need_help(self):
        return True

    def is_young(self):
        return False

    def can_vote(self):
        return True

    def can_be_married(self):
        return True


''' Takes a list and saves it to a JSON file'''
def save_to_file(list, filename):
    if os.path.exists(filename) == False or type(filename) is not str:
        raise Exception('Filename does not exist')
    else:
        with open(filename, 'w') as outfile:
            json.dump(list, outfile)

''' Takes a JSON file and parses the information into a list'''
def load_from_file(filename):
    if os.path.exists(filename) == False or type(filename) is not str:
        raise Exception('Filename does not exist')
    else:
        with open(filename, 'r') as json_data:
            data = json.load(json_data)
        return data

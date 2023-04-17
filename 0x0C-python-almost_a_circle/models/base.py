#!/usr/bin/python3
""" The Base Class Module"""


import json

class Base:
    """A base class that is the
    base of all other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """A constructor method"""

        if id is not None:
            self.id = id
        else:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A method that returns a json
        representative of a string
        """

        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """A class method to write on a file
        """

        dic = []
        if list_objs is None:
            pass
        else:
            for i in range(len(list_objs)):
                dic.append(list_objs[i].to_dictionary())

        a = cls.to_json_string(dic)
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, 'w') as f:
            f.write(a)

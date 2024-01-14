#!/usr/bin/python3
"""Module for class Base."""
import json
import csv
import turtle

class Base:
    """
    The base class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the base class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string.
        Args:
            list_dictionaries: List of dictionaries
        Returns:
            The JSON string representation of list_dictionaries
        """
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file.
        Args:
            list_objs: List of objects to be saved
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Deserializes a JSON string to a Python object.

        Args:
            json_string: A JSON-formatted string to be deserialized.

        Returns:
            A Python list or dictionary representing deserialized JSON data.
        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Method that creates an instance with attributes already set.
        Args:
            dictionary: A dictionary with keys corresponding to class attributes.
        Returns:
            An instance of the class with all attributes set.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy_instance = cls(1, 1)
            else:
                dummy_instance = cls(1)
            dummy_instance.update(**dictionary)
            return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Loads a list of objects from a JSON file."""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves a list of objects to a CSV file.
        Args:
            list_objs: A list of objects to be saved to a CSV file.
        Returns:
            None
        """
        filename = cls.__name__ + ".csv"

        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)

            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "size", "x", "y"]

            csv_writer.writerow(fieldnames)

            for obj in list_objs:
                csv_writer.writerow([getattr(obj, attr) for attr in fieldnames])

    @classmethod
    def load_from_file_csv(cls):
        """Loads a list of instances from a CSV file."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                next(list_dicts)
            
                list_dicts = [dict([k, int(v)] for k, v in d.items()) for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]

        except IOError:
            return []

    @classmethod
    def draw(cls, list_rectangles, list_squares):
        """
        Draws rectangles and squares.
        Args:
            list_rectangles: List of rectangle objects to draw.
            list_squares: List of square objects to draw.
        """
        turt = turtle.Turtle()

        turt.screen.bgcolor('#23110c')
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()

            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()

            for i in range(4):
                turt.forward(sq.size)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

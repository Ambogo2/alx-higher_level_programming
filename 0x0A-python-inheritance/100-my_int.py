 #!/usr/bin/python3
""" Define a Class MyInt """


class MyInt(int):
    """ A class that defines MyInt"""

    def __new__(cls, *args, **kwargs):
        """A method that initializes rectangle with height and width"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """Invert the behavior of the equality operator"""
        return int(self) != other

    def __ne__(self, other):
        """Invert the behavior of the inequality operator"""
        return int(self) == other

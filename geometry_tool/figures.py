# Pascal Mehnert
# 25.04.2016
# Multiple classes representing figures in the coordinate system.
# V 1.0


class Point(object):
    def __init__(self, coordinates, position, tkinter_objects):
        self.__coordinates = coordinates
        self.__position = position
        self.__tkinter_objects = [tkinter_objects]

    def get_coordinates(self):
        return self.__coordinates

    def get_position(self):
        return self.__position

    def get_tkinter_objects(self):
        return self.__tkinter_objects


class Distance(object):
    def __init__(self, coord_a, coord_b, pos_a, pos_b, tkinter_objects):
        self.__coordinates_a = coord_a
        self.__coordinates_b = coord_b
        self.__position_a = pos_a
        self.__position_b = pos_b
        self.__tkinter_objects = tkinter_objects

    def get_coordinates_a(self):
        return self.__coordinates_a

    def get_coordinates_b(self):
        return self.__coordinates_b

    def get_position_a(self):
        return self.__position_a

    def get_position_b(self):
        return self.__position_b

    def get_tkinter_objects(self):
        return self.__tkinter_objects


class Line(object):
    def __init__(self, coord_sup, coord_dir, pos_sup, pos_dir, tkinter_objects):
        self.__coordinates_support_vector = coord_sup
        self.__coordinates_direction_vector = coord_dir
        self.__position_support_vector = pos_sup
        self.__position_direction_vector = pos_dir
        self.__tkinter_objects = [tkinter_objects]

    def get_coordinates_support_vector(self):
        return self.__coordinates_support_vector

    def get_coordinates_direction_vector(self):
        return self.__coordinates_direction_vector

    def get__position_support_vector(self):
        return self.__position_support_vector

    def get_position_direction_vector(self):
        return self.__position_direction_vector

    def get_tkinter_objects(self):
        return self.__tkinter_objects


class Function(object):
    def __init__(self, function_term, tkinter_objects):
        self.__function_term = function_term
        self.__tkinter_objects = tkinter_objects

    def get_function_term(self):
        return self.__function_term

    def get_tkinter_objects(self):
        return self.__tkinter_objects

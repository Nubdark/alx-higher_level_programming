#!/usr/bin/python3
def list_division(list_1, list_2, list_length):
    """Divides two lists element by element.
    Args:
        list_1 (list): The first list.
        list_2 (list): The second list.
        list_length (int): The number of elements to divide.
    Outputs:
        A new list of length containing all the divisions.
    """
    new_list = []
    for i in range(0, list_length):
        try:
            division = list_1[i] / list_2[i]
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            new_list.append(division)
    return (new_list)

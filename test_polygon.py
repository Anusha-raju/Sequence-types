#-----------Tests to check polygon and polygon_sequence module---------------
import pytest
import os
import inspect
import re
import polygon,polygon_sequence
import test_polygon




#-------------Tests for polygon------------------


def test_polygon_constructor():
    """
    This function tests the initializer function of polygon
    """
    with pytest.raises(ValueError, match=r".*Number of edges/vertices should be equal to or greater than 3(Three)*"):
        p1 = polygon.Polygon(2,10)

p2 = polygon.Polygon(6, 10)
def test_polygon_interior_angle():
    """This function tests the interior angle calculated by polygon class
    """

    assert p2.interior_angle == 120.0 , "Interior angle not right....."

def test_polygon_edge_length():
    """This function tests the edge length calculated by polygon class
    """

    assert p2.edge_length == 9.999999999999998, "Egde length not right....."


def test_polygon_apothem():
    """This function tests the apothem calculated by polygon class
    """

    assert p2.apothem == 8.660254037844387, "Apothem not right....."


def test_polygon_area():
    """This function tests the area calculated by polygon class
    """

    assert p2.area == 259.80762113533154, "Area not right....."


def test_polygon_perimeter():
    """This function tests the perimeter calculated by polygon class
    """

    assert p2.perimeter == 59.999999999999986, "perimeter not right....."

p3 = polygon.Polygon(6, 10)
p4 = polygon.Polygon(7,10)

def test_equal_to():
    """This test checks the equal to operator"""

    assert p2 == p3 , "Equal to not working"

def test_greater_than():
    """
    This function tests the greater than operator
    """

    assert p4>p2 ,"Greater than should be greater than"

#---------Tests for polygon sequence---------


def test_polygon_sequence_constructor():
    """
    This function tests the initializer function of polygon sequence
    """
    with pytest.raises(ValueError, match=r".*Number of edges/vertices should be equal to or greater than 3(Three)*"):
        p5 = polygon_sequence.Polygon_sequence(2,10)

p6 = polygon_sequence.Polygon_sequence(6,10)
def test_len_operator():
    """This function tests the len method
    """
    assert len(p6) == 4 , "length not working....."






#-----------------General tests----------------------------------

def test_session10_readme_exists():
    """ Checks if README file exists"""
    assert os.path.isfile("README.md"), "README.md file missing!"



def test_session10_readme_file_for_more_than_10_hashes():
    """Checks if README file has proper formatting (minimum of 10 hashes)"""
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10



def test_session10_function_name_had_cap_letter():
    """ test fails if Capital letter(s) used for function names """
    functions = inspect.getmembers(polygon, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_function_count():
    """ tests number of test function > 20 in test_poker file"""
    functions =inspect.getmembers(test_polygon, inspect.isfunction)
    assert len(functions) >= 10, 'Test cases seems to be low. Work harder man...'


def test_function_repeatations():
    """ tests if any repeated tests in test_poker file"""
    functions = inspect.getmembers(test_polygon, inspect.isfunction)
    names = []
    for function in functions:
        names.append(function)
    assert len(names) == len(set(names)), 'Test cases seems to be repeating...'



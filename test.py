import pytest

from job import calculate_average

def test_calculate_average():
    # Test avec une liste non vide
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    
    # Test avec une liste vide
    assert calculate_average([]) == None
    
    # Test avec une liste contenant un seul élément
    assert calculate_average([7]) == 7.0

    # Test avec une liste contenant des nombres négatifs
    assert calculate_average([-1, -2, -3, -4, -5]) == -3.0

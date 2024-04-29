from exercices.src.fonctions_simples import add,divide ,add_integer,alea_uniform
from exercices.src.fonctions_difficiles import input_function_fois_deux,create_file, randomize
from unittest.mock import patch
import random
import pytest

def test_add():
    assert add(4,3) == 7
    assert add("a","a") == "aa"
    assert add([1,2,3],[4,5,6]) == [1,2,3,4,5,6]
    assert add ([],[]) == []

def test_divide():
    assert divide (10,2) == 5
    with pytest.raises(ZeroDivisionError):
        divide(88,0)

def test_add_integer():
    assert add(4,3) == 7
    with pytest.raises(TypeError) :
         add_integer(9,"a") 

def test_alea_uniform():
    # assert alea_uniform(10,20) > 10 
    assert  10 < alea_uniform(10,20) < 20

def test_input_function_fois_deux():
    with patch('builtins.input', return_value ='3'):
         assert input_function_fois_deux() == 6

def test_create_file(tmpdir):
        file_path = tmpdir.join("liste_apprenants.txt")
        create_file(file_path, "\nAlfred")
        with open(file_path, "r") as fichier:
                  assert "\nAlfred" in fichier.read()

random.seed(0)

def test_randomize():
     assert randomize() == 0.7579544029403025
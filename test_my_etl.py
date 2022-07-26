import pytest
import requests
from bs4 import BeautifulSoup
import csv
from prints import print_input
from My_ETL import get_pokemon_name
from My_ETL import get_response
from My_ETL import get_data_api

def test_get_pokemon():
    all_gem = get_pokemon_name()
    assert isinstance(all_gem, list)
    assert len(all_gem) == 721
    assert isinstance(all_gem[0], str)

def test_response():
    pokemon_response = get_response()
    assert pokemon_response == 200
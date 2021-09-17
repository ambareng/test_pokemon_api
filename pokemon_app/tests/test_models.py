import pytest
from pokemon_app.tests.factories import *


@pytest.mark.django_db
def test_type(test_type_factory):
    assert test_type_factory.name


@pytest.mark.django_db
def test_species(test_species_factory):
    assert True


# @pytest.mark.django_db
# def test_pokemon(create_test_pokemon):
#     print(create_test_pokemon)
#     assert True

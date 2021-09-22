# import pytest
# from pokemon_app.models import *
# from pytest_factoryboy import register
# from pokemon_app.tests.factories import *
#
#
# register(TypeFactory)
# register(SpeciesFactory)
# register(TrainerFactory)
# register(PokemonFactory)
#
#
# @pytest.fixture
# def type_data():
#     test_type = Type.objects.create(name='Grass')
#     return test_type
#
#
# # @pytest.fixture
# # def pokemon_data():
# #     return {
# #         'species': 1,
# #         'current_level': 16,
# #         'trainer': 1,
# #     }
# #
# #
# # @pytest.fixture
# # def create_test_pokemon(pokemon_data):
# #     test_pokemon = Pokemon.objects.create(**pokemon_data)
# #     return test_pokemon
#
#
# @pytest.fixture
# def test_type_factory(db, type_factory):
#     test_type = type_factory.build()
#     return test_type
#
#
# @pytest.fixture
# def test_species_factory(db, species_factory):
#     test_species = species_factory.build()
#     return test_species

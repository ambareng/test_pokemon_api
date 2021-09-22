# import pytest
# from pokemon_app.tests.factories import *
#
#
# @pytest.mark.django_db
# def test_type(test_type_factory):
#     assert test_type_factory.name
#
#
# @pytest.mark.django_db
# def test_species(test_species_factory):
#     assert True
#
#
# # @pytest.mark.django_db
# # def test_pokemon(create_test_pokemon):
# #     print(create_test_pokemon)
# #     assert True

import pytest
from mixer.backend.django import mixer
from pokemon_app.models import Type, Species, Trainer, Pokemon


class Test:
    @staticmethod
    def test():
        print('======================')
        print('SAMPLE TEST')
        print('======================')
        assert True


@pytest.mark.django_db
class TestTypeModel:
    def test_type_str(self):
        test_type = mixer.blend(Type, name='Grass')
        assert str(test_type) == 'Grass'


@pytest.mark.django_db
class TestSpeciesModel:
    def test_species_str(self):
        test_species = mixer.blend(Species, name='Charmander')
        assert str(test_species) == 'Charmander'


@pytest.mark.django_db
class TestTrainerModel:
    def test_trainer_str(self):
        test_trainer = mixer.blend(Trainer, name='Arvin')
        assert str(test_trainer) == 'Arvin'


@pytest.mark.django_db
class TestPokemonModel:
    def test_pokemon_str(self):
        test_pokemon = mixer.blend(Pokemon, name='Saur')
        assert str(test_pokemon) == 'Saur'

    def test_pokemon_evolution(self):
        test_pokemon_02 = mixer.blend(Pokemon)
        test_species = mixer.blend(Species, level_to_evolve=16, next_evolution=test_pokemon_02.species)
        test_pokemon_01 = mixer.blend(Pokemon, species=test_species, current_level=15)
        assert test_pokemon_01.species == test_species
        test_pokemon_01.current_level += 1
        test_pokemon_01.save()
        assert test_pokemon_01.species == test_pokemon_02.species

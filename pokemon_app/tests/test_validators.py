import pytest
from mixer.backend.django import mixer
from django.test import TestCase
from pokemon_app.models import Pokemon
from pokemon_app.validators import level_validator
from django.core.exceptions import ValidationError


@pytest.mark.django_db
class TestLevelValidator(TestCase):
    def test_level_validator(self):
        test_pokemon = mixer.blend(Pokemon)
        test_pokemon.full_clean()
        test_pokemon.current_level = 6969
        with pytest.raises(Exception) as excinfo:
            test_pokemon.full_clean()
        err_msg, = excinfo.value.args
        assert err_msg == '100 is the max limit for a pokemon\'s level.'
        test_pokemon.current_level = -6969
        with pytest.raises(Exception) as excinfo:
            test_pokemon.full_clean()
        err_msg, = excinfo.value.args
        assert err_msg == '1 is the minimum limit for a pokemon\'s level.'

import factory
from faker import Faker
from django.contrib.auth.models import User
import faker.providers
from pokemon_app.models import *
from django.contrib.auth.hashers import make_password

TYPES = [
    'Grass',
    'Water',
    'Fire',
]

SPECIES = [
    'Rattatta',
    'Fearow',
    'Pikachu',
]

NEXT_EVOLUTION = [
    'Raticate',
    'Spearow',
    'Raichu'
]

# Providers


class TypesProvider(faker.providers.BaseProvider):
    def type_names(self):
        return self.random_element(TYPES)


class SpeciesProvider(faker.providers.BaseProvider):
    def species_names(self):
        return self.random_element(SPECIES)


class NextEvolutionsProvider(faker.providers.BaseProvider):
    def evolution_names(self):
        return self.random_element(NEXT_EVOLUTION)


fake = Faker()
fake.add_provider(TypesProvider)
fake.add_provider(SpeciesProvider)
fake.add_provider(NextEvolutionsProvider)


# Factories


class TypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Type

    name = fake.unique.type_names()


class SpeciesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Species

    name = fake.unique.species_names()
    type = factory.SubFactory(TypeFactory)
    next_evolution = factory.RelatedFactory(
        SpeciesFactory
    )
    level_to_evolve = fake.pyint(min_value=10, max_value=70)


m = SpeciesFactory(parent__parent__parent__parent=None)


class TrainerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Trainer

    name = fake.name()
    email = fake.unique.email()
    password = make_password('Password1!')


class PokemonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pokemon

    name = fake.name()
    level_to_evolve = fake.pyint(min_value=5, max_value=100)
    trainer = factory.SubFactory(TrainerFactory)

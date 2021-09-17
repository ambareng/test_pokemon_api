from rest_framework.serializers import ModelSerializer,ValidationError
from pokemon_app.models import Type, Species, Pokemon, Trainer


class TypeSerializer(ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name', 'created_at', 'updated_at']


class SpeciesSerializer(ModelSerializer):
    class Meta:
        model = Species
        fields = ['id', 'name', 'type', 'next_evolution', 'level_to_evolve', 'created_at', 'updated_at']
        depth = 0

    # def validate_type(self, value):
    #     if len(value) >= 3:
    #         raise ValidationError("Each Pokemon can only have at MOST 2 TYPES!!!")
    #     return value

    def validate(self, data):
        if len(data.get('type')) >= 3:
            raise ValidationError('Each Pokemon can only have at most 2 types only.')
        if len(data.get('name')) <= 4:
            raise ValidationError('Pokemon must have at least 4 characters in it\'s name.')
        return data


class PokemonSerializer(ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'current_level', 'species', 'trainer', 'created_at', 'updated_at']
        depth = 0


class TrainerSerializer(ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['id', 'name', 'email', 'password', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        depth = 0

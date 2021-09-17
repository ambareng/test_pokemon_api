from django.shortcuts import render
from pokemon_app.serializers import TypeSerializer, SpeciesSerializer, PokemonSerializer, TrainerSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from pokemon_app.models import Type, Species, Pokemon, Trainer
from django.shortcuts import get_object_or_404
import jwt
import datetime
from rest_framework.exceptions import AuthenticationFailed


class TypeViewSet(viewsets.ViewSet):
    def list(self, request):
        types = Type.objects.all()
        serializer = TypeSerializer(types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        token = request.COOKIES.get('jwt')
        trainer_id = is_authenticated(token).data['id']

        if not is_admin(trainer_id):
            raise AuthenticationFailed('Only admins are allowed to do this')

        serializer = TypeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TypeDetailViewSet(viewsets.ViewSet):
    def perform_authentication(self, request):
        token = request.COOKIES.get('jwt')
        trainer_id = is_authenticated(token).data['id']

        if not is_admin(trainer_id):
            raise AuthenticationFailed('Only admins are allowed to do this')

    def retrieve(self, request, pk):
        type_detail = get_object_or_404(Type, pk=pk)
        serializer = TypeSerializer(type_detail)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializer = TypeSerializer(get_object_or_404(Type, pk=pk), data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        get_object_or_404(Type, pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpeciesViewSet(viewsets.ViewSet):
    def list(self, request):
        species = Species.objects.all()
        serializer = SpeciesSerializer(species, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        token = request.COOKIES.get('jwt')
        trainer_id = is_authenticated(token).data['id']

        if not is_admin(trainer_id):
            raise AuthenticationFailed('Only admins are allowed to do this')

        serializer = SpeciesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpeciesDetailViewSet(viewsets.ViewSet):
    def perform_authentication(self, request):
        token = request.COOKIES.get('jwt')
        trainer_id = is_authenticated(token).data['id']

        if not is_admin(trainer_id):
            raise AuthenticationFailed('Only admins are allowed to do this')

    def retrieve(self, request, pk):
        species_detail = get_object_or_404(Species, pk=pk)
        serializer = SpeciesSerializer(species_detail)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializer = SpeciesSerializer(get_object_or_404(Species, pk=pk), data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        get_object_or_404(Species, pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PokemonViewSet(viewsets.ViewSet):
    def perform_authentication(self, request):
        token = request.COOKIES.get('jwt')
        is_authenticated(token)

    def list(self, request):
        token = request.COOKIES.get('jwt')
        trainer_id = is_authenticated(token).data['id']

        if is_admin(trainer_id):
            pokemon = Pokemon.objects.all()
        else:
            pokemon = Pokemon.objects.filter(trainer=trainer_id)

        serializer = PokemonSerializer(pokemon, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = PokemonSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PokemonDetailViewSet(viewsets.ViewSet):
    def perform_authentication(self, request):
        token = request.COOKIES.get('jwt')
        is_authenticated(token)

    def retrieve(self, request, pk):
        token = request.COOKIES.get('jwt')
        trainer_id = is_authenticated(token).data['id']

        is_trainer_of_pokemon(trainer_id, pk)

        pokemon_detail = get_object_or_404(Pokemon, pk=pk)
        serializer = PokemonSerializer(pokemon_detail)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        pokemon_detail = get_object_or_404(Pokemon, pk=pk)
        serializer = PokemonSerializer(pokemon_detail, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        get_object_or_404(Pokemon, pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TrainerViewSet(viewsets.ViewSet):
    def list(self, request):
        trainer = Trainer.objects.all()
        serializer = TrainerSerializer(trainer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        token = request.COOKIES.get('jwt')
        trainer_id = is_authenticated(token).data['id']

        if not is_admin(trainer_id):
            raise AuthenticationFailed('Only admins are allowed to do this')

        serializer = TrainerSerializer(data=request.data)

        if serializer.is_valid():
            trainer = serializer.save()
            trainer.set_password(trainer.password)
            trainer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TrainerDetailViewSet(viewsets.ViewSet):
    def perform_authentication(self, request):
        token = request.COOKIES.get('jwt')
        trainer_id = is_authenticated(token).data['id']

        if not is_admin(trainer_id):
            raise AuthenticationFailed('Only admins are allowed to do this')

    def retrieve(self, request, pk):
        trainer_detail = get_object_or_404(Trainer, pk=pk)
        serializer = TrainerSerializer(trainer_detail)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        trainer_detail = get_object_or_404(Trainer, pk=pk)
        serializer = TrainerSerializer(trainer_detail, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        get_object_or_404(Trainer, pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Register(viewsets.ViewSet):
    def create(self, request):
        password = request.data['password']
        serializer = TrainerSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            trainer = serializer.save()
            trainer.set_password(trainer.password)
            trainer.save()
        return Response(serializer.data)


class RegisterAdmin(viewsets.ViewSet):
    def perform_authentication(self, request):
        token = request.COOKIES.get('jwt')
        trainer_id = is_authenticated(token).data['id']

        if not is_admin(trainer_id):
            raise AuthenticationFailed('Only admins are allowed to do this')

    def create(self, request):
        password = request.data['password']
        serializer = TrainerSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            trainer = serializer.save()
            trainer.set_password(trainer.password)
            trainer.is_admin = True
            trainer.save()
        return Response(serializer.data)


class Login(viewsets.ViewSet):
    def create(self, request):
        email = request.data['email']
        password = request.data['password']

        trainer = Trainer.objects.filter(email=email).first()

        if trainer is None or not trainer.check_password(password):
            raise AuthenticationFailed('Invalid Email/Password')

        payload = {
            'id': trainer.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {"jwt": token}

        return response


def is_authenticated(token):
    if not token:
        raise AuthenticationFailed('Must be authenticated')
    try:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Token is expired')

    trainer = Trainer.objects.filter(id=payload['id']).first()
    serializer = TrainerSerializer(trainer)

    return Response(serializer.data)


def is_admin(trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)

    if not trainer.is_admin:
        return False

    return True


def current_trainer(trainer_id):
    try:
        trainer = Trainer.objects.get(id=trainer_id)
    except trainer.DoesNotExist():
        raise AuthenticationFailed('User does not exist')

    return trainer


def is_trainer_of_pokemon(trainer_id, pokemon_id):
    if not is_admin(trainer_id):
        pokemon_detail = Pokemon.objects.filter(pk=pokemon_id, trainer=trainer_id).first()
        if pokemon_detail is None:
            raise AuthenticationFailed('You are not the trainer of this pokemon')


class GetCurrentUser(viewsets.ViewSet):
    def list(self, request):
        token = request.COOKIES.get('jwt')

        return is_authenticated(token)


class Logout(viewsets.ViewSet):
    def perform_authentication(self, request):
        token = request.COOKIES.get('jwt')
        is_authenticated(token)

    def create(self, request):
        token = request.COOKIES.get('jwt')

        is_authenticated(token)

        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Logged Out Successfully'
        }
        return response

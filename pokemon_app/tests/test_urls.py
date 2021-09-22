import datetime
import jwt
import pytest

from django.test import TestCase
from django.contrib.auth.hashers import make_password

from mixer.backend.django import mixer

from pokemon_app.models import Type, Trainer

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


class TestPokemonAppUrls(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.token = Token.objects.create(
            user=mixer.blend(Trainer, email="test_trainer@test.com", password=make_password('Yeahyeahyeah1!'))
        )
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_types_list(self):
        test_type = mixer.blend(Type, name='Grass')
        url = reverse('types-list')
        response = self.client.get(url)
        assert len(response.json()) == 1
        assert response.json()[0]['name'] == test_type.name
        assert response.status_code == 200

    # def test_types_create(self):
    #     test_type_data = {
    #        "name": "Grass"
    #     }
    #     test_trainer = mixer.blend(Trainer, email="test_trainer@test.com", password=make_password('Yeahyeahyeah1!'))
    #     payload = {
    #         'id': test_trainer.id,
    #         'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
    #         'iat': datetime.datetime.utcnow()
    #     }
    #     # token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
    #     # response = Response()
    #     # response.set_cookie(key='jwt', value=token, httponly=True)
    #     # response.data = {"jwt": token}
    #     url = reverse('types-list')
    #     response = self.client.post(url, test_type_data)
    #     print(response)
    #     # # assert len(response.json()) == 1
    #     # print(response.json())
    #     # assert response.json()['name'] == 'Grass'
    #     # assert response.status_code == 201
    #     # assert Type.objects.count() == 1

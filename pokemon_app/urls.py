from django.urls import path, include
from pokemon_app.views import TypeViewSet, TypeDetailViewSet, SpeciesViewSet, SpeciesDetailViewSet, PokemonViewSet, \
    PokemonDetailViewSet, TrainerViewSet, TrainerDetailViewSet, Register, Login, GetCurrentUser, Logout, RegisterAdmin
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('types', TypeViewSet, basename='types')
router.register('type', TypeDetailViewSet, basename='type')
router.register('species', SpeciesViewSet, basename='species')
router.register('species', SpeciesDetailViewSet, basename='species')
router.register('pokemon', PokemonViewSet, basename='pokemon')
router.register('pokemon', PokemonDetailViewSet, basename='pokemon')
router.register('trainers', TrainerViewSet, basename='trainers')
router.register('trainers', TrainerDetailViewSet, basename='trainers')
# Authentication
router.register('register', Register, basename='register')
router.register('register_admin', RegisterAdmin, basename='register_admin')
router.register('login', Login, basename='login')
router.register('user', GetCurrentUser, basename='user')
router.register('logout', Logout, basename='logout')

urlpatterns = [
    path('viewsets/', include(router.urls)),
    path('viewsets/<int:pk>/', include(router.urls)),
]

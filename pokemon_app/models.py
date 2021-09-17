from django.db import models
from pokemon_app.validators import level_validator
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=64, unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Type(BaseModel):
    def __str__(self):
        return self.name


class Species(BaseModel):
    type = models.ManyToManyField(Type)
    next_evolution = models.OneToOneField('self', on_delete=models.CASCADE, null=True, blank=True)
    level_to_evolve = models.IntegerField(null=True, blank=True, validators=[level_validator])

    def __str__(self):
        return self.name


class Trainer(AbstractUser, BaseModel):
    email = models.EmailField(max_length=64, unique=True, null=True)
    password = models.CharField(max_length=64, null=True)
    username = None
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name


class Pokemon(BaseModel):
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    current_level = models.IntegerField(default=1, validators=[level_validator])
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.species.next_evolution:
            if self.current_level >= self.species.level_to_evolve:
                self.species = self.species.next_evolution
        super(Pokemon, self).save(*args, **kwargs)

    def __str__(self):
        return self.nickname

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

class MeningIsmim(models.Model):
    ism = models.CharField(max_length=100)


class MeningFamilyam(models.Model):
    familya = models.CharField(max_length=100)


class University(models.Model):
    university = models.CharField(max_length=200)


class Yoshim(models.Model):
    yosh = models.IntegerField()

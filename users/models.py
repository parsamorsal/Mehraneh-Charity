import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from .choices import *


class CustomUser(AbstractUser):
    state = models.NullBooleanField(default=None)
    isBen = models.BooleanField(default=False)
    isOrg = models.BooleanField(default=False)
    image = models.ImageField(upload_to='../media/profile_pics/', default='../media/profile_pics/no-picture.png')

    def __str__(self):
        return self.username


class WeeklySchedule(models.Model):
    id = models.AutoField(primary_key=True)
    c0 = models.CharField(max_length=5, default='off', blank=True)
    c1 = models.CharField(max_length=5, default='off', blank=True)
    c2 = models.CharField(max_length=5, default='off', blank=True)
    c3 = models.CharField(max_length=5, default='off', blank=True)
    c4 = models.CharField(max_length=5, default='off', blank=True)
    c5 = models.CharField(max_length=5, default='off', blank=True)
    c6 = models.CharField(max_length=5, default='off', blank=True)
    c7 = models.CharField(max_length=5, default='off', blank=True)
    c8 = models.CharField(max_length=5, default='off', blank=True)
    c9 = models.CharField(max_length=5, default='off', blank=True)
    c10 = models.CharField(max_length=5, default='off', blank=True)
    c11 = models.CharField(max_length=5, default='off', blank=True)
    c12 = models.CharField(max_length=5, default='off', blank=True)
    c13 = models.CharField(max_length=5, default='off', blank=True)
    c14 = models.CharField(max_length=5, default='off', blank=True)
    c15 = models.CharField(max_length=5, default='off', blank=True)
    c16 = models.CharField(max_length=5, default='off', blank=True)
    c17 = models.CharField(max_length=5, default='off', blank=True)
    c18 = models.CharField(max_length=5, default='off', blank=True)
    c19 = models.CharField(max_length=5, default='off', blank=True)
    c20 = models.CharField(max_length=5, default='off', blank=True)
    c21 = models.CharField(max_length=5, default='off', blank=True)
    c22 = models.CharField(max_length=5, default='off', blank=True)
    c23 = models.CharField(max_length=5, default='off', blank=True)
    c24 = models.CharField(max_length=5, default='off', blank=True)
    c25 = models.CharField(max_length=5, default='off', blank=True)
    c26 = models.CharField(max_length=5, default='off', blank=True)
    c27 = models.CharField(max_length=5, default='off', blank=True)


class TotalRate(models.Model):
    id = models.AutoField(primary_key=True)
    totalRate = models.FloatField(default=0)
    f1 = models.FloatField(default=0)
    f2 = models.FloatField(default=0)
    f3 = models.FloatField(default=0)
    f4 = models.FloatField(default=0)
    f5 = models.FloatField(default=0)


class Benefactor(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='benefactor')
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=10, choices=SEX_CHOICES, default='Male')
    day = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    education = models.CharField(max_length=10, choices=EDUCATION_CHOICES, default='nothing')
    major = models.CharField(max_length=20, blank=True)
    nationalId = models.CharField(max_length=10)
    city = models.CharField(max_length=10, default='blank')
    address = models.CharField(max_length=100, default='st')
    phone = models.CharField(max_length=12)
    typeOfCooperation = models.CharField(max_length=15, choices=COOP_CHOICES, default='inOffice10')
    wId = models.ForeignKey(WeeklySchedule, on_delete=models.CASCADE, related_name='userWeek', null=True)
    rate = models.ForeignKey(TotalRate, on_delete=models.CASCADE, related_name='rate')


class Organization(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='organizer')
    name = models.CharField(max_length=20)
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=10, default='blank')
    phone = models.CharField(max_length=15)
    website = models.URLField()
    license = models.CharField(max_length=20)
    rate = models.ForeignKey(TotalRate, on_delete=models.CASCADE, related_name='orgRate')


class Project(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='creator')
    name = models.CharField(max_length=50)
    budget = models.IntegerField(default=0)
    city = models.CharField(max_length=15, default='blank')
    description = models.TextField(max_length=300)
    paymethod = models.CharField(max_length=10, choices=BANK_CHOICES)
    cardno = models.CharField(max_length=20, blank=True)
    accno = models.CharField(max_length=25, blank=True)
    alreadyPaid = models.IntegerField(default=0)


class Rate(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rater')
    ratedUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rated')
    f1 = models.IntegerField()
    f2 = models.IntegerField()
    f3 = models.IntegerField()
    f4 = models.IntegerField()
    f5 = models.IntegerField()
    description = models.TextField(max_length=300, blank=True)


class Ability(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)


class UserAbilities(models.Model):
    class Meta:
        unique_together = ('abilityId', 'username')

    abilityId = models.ForeignKey(Ability, on_delete=models.DO_NOTHING, related_name='ability')
    username = models.ForeignKey(CustomUser, to_field='username', on_delete=models.DO_NOTHING, related_name='benefactorusername')


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)


class CategoryProject(models.Model):
    class Meta:
        unique_together = ('categoryId', 'projectId')

    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    projectId = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project')


class Requirement(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owner')
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    wId = models.ForeignKey(WeeklySchedule, on_delete=models.CASCADE, related_name='week')
    description = models.TextField(max_length=200)
    typeOfCooperation = models.CharField(max_length=15, choices=COOP_CHOICES, default='inOffice10')
    NOPs = models.IntegerField(default=0)


class RequirementAbilities(models.Model):
    class Meta:
        unique_together = ('abilityId', 'reqId')

    reqId = models.ForeignKey(Requirement, on_delete=models.CASCADE, related_name='req')
    abilityId = models.ForeignKey(Ability, on_delete=models.CASCADE, related_name='ab')


class Request(models.Model):
    id = models.AutoField(primary_key=True)
    benefactorId = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reqben')
    organizationId = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reqorg')
    wId = models.ForeignKey(WeeklySchedule, on_delete=models.CASCADE, related_name='reqweek', default=None, null=True)
    reqId = models.ForeignKey(Requirement, on_delete=models.CASCADE, related_name='reqreq', default=None, null=True)
    state = models.BooleanField(default=False)
    isAccepted = models.BooleanField(default=False)
    isAtHome = models.BooleanField(default=False)
    whoSubmit = models.CharField(max_length=1, default='1')
    city = models.CharField(max_length=20)
    description = models.TextField(blank=True)


class Report(models.Model):
    id = models.AutoField(primary_key=True)
    benefactor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ben', default=None, null=True)
    organization = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='org', default=None, null=True)
    type = models.CharField(max_length=1)
    description = models.TextField(max_length=100, default=None, null=True)
    operator = models.CharField(max_length=1)
    date = models.DateField()
    time = models.TimeField()
    rateId = models.ForeignKey(Rate, on_delete=models.CASCADE, related_name='rate', default=None, null=True)
    wId = models.ForeignKey(WeeklySchedule, on_delete=models.CASCADE, related_name='weekly', default=None, null=True)
    reqId = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='repreq', default=None, null=True)
    payment = models.IntegerField(default=None, null=True)
    isAtHome = models.BooleanField(default=False)


class RequestAbilities(models.Model):
    class Meta:
        unique_together = ('reqId', 'abilityId')

    reqId = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='request')
    abilityId = models.ForeignKey(Ability, on_delete=models.CASCADE, related_name='requestAbility')

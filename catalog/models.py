from django.db import models
import uuid
from datetime import time

# Create your models here.
mark_ = (
        ('0', 'Не сдано'),
        ('1', '2'),
        ('2', '3'),
        ('3', '4'),
        ('4', '5')
    )


class students(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=15, help_text='Имя студента')
    last_name = models.CharField(max_length=20, help_text='Фамилия студента')
    math = models.CharField(choices=mark_, default='0', max_length=1)
    astronomy = models.CharField(choices=mark_, default='0', max_length=1)
    football = models.CharField(choices=mark_, default='0', max_length=1)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name

    def info(self):
        return 'Математика: %s, Астрономия: %s, Футбол: %s' % (mark_[int(self.math)][1], mark_[int(self.astronomy)][1], mark_[int(self.football)][1])


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    cabinet = models.ManyToManyField('Cabinet')

    def __str__(self):
        return self.name
    def cabinets(self):
        return "\n".join([str(p) for p in self.cabinet.all()])


class Cabinet(models.Model):
    number = models.IntegerField()

    def __str__(self):
        s = str(self.number)
        return s



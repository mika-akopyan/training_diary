# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse


class Asanas(models.Model):
    sequence_number = models.SmallIntegerField(verbose_name='Порядковый номер')
    asana = models.CharField(primary_key=True, max_length=70, verbose_name='Асана')
    technique_execution = models.TextField(blank=True, null=True, verbose_name='Техника выполнения')
    works_time = models.CharField(max_length=30, blank=True, null=True, verbose_name='Время работы')
    sides_quantity = models.IntegerField(verbose_name='Количество сторон')

    def get_absolute_url(self):
        return reverse("yoga:asana_detail", kwargs={"asana_pk": self.pk})
    
    def __str__(self) -> str:
        return self.asana

    class Meta:
        ordering = ['asana']
        db_table = 'asanas'


class AsanasSpecializations(models.Model):
    asana = models.ForeignKey(Asanas, models.DO_NOTHING, db_column='asana')
    specialization = models.ForeignKey('Specializations', models.DO_NOTHING, db_column='specialization')

    class Meta:
        db_table = 'asanas_specializations'


class Complexes(models.Model):
    complex = models.CharField(primary_key=True, max_length=40)

    class Meta:
        db_table = 'complexes'


class DataYoga(models.Model):
    week_field = models.IntegerField(db_column='week_тДЦ')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    day_field = models.IntegerField(db_column='day_тДЦ')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    complex = models.ForeignKey(Complexes, models.DO_NOTHING, db_column='complex')
    specialization = models.ForeignKey('Specializations', models.DO_NOTHING, db_column='specialization')
    field_pose = models.SmallIntegerField(db_column='тДЦ_pose')  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    asana = models.ForeignKey(Asanas, models.DO_NOTHING, db_column='asana')
    side = models.CharField(max_length=2)
    time_work = models.IntegerField()
    time_rest = models.IntegerField()
    note = models.CharField(max_length=5000, blank=True, null=True)
    date_yoga = models.DateField()

    class Meta:
        db_table = 'data_yoga'


class Specializations(models.Model):
    complex = models.ForeignKey(Complexes, models.DO_NOTHING, db_column='complex')
    specialization = models.CharField(primary_key=True, max_length=20)

    class Meta:
        db_table = 'specializations'

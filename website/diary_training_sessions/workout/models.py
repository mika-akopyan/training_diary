# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse


class DataWorkout(models.Model):
    week_field = models.IntegerField(db_column='week_тДЦ')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    day_field = models.IntegerField(db_column='day_тДЦ')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    mesocycle = models.ForeignKey('Mesocycles', models.DO_NOTHING, db_column='mesocycle')
    microcycle = models.ForeignKey('Microcycles', models.DO_NOTHING, db_column='microcycle')
    muscle_group = models.ForeignKey('MuscleGroups', models.DO_NOTHING, db_column='muscle_group')
    muscle = models.ForeignKey('Muscles', models.DO_NOTHING, db_column='muscle')
    exercise = models.ForeignKey('Exercises', models.DO_NOTHING, db_column='exercise')
    side = models.CharField(max_length=2)
    warm_up_1_time_rest_minutes = models.DecimalField(max_digits=4, decimal_places=2)
    warm_up_1_weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    warm_up_1_rq_times = models.IntegerField()
    warm_up_2_time_rest_minutes = models.DecimalField(max_digits=4, decimal_places=2)
    warm_up_2_weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    warm_up_2_rq_times = models.IntegerField()
    pre_worker_time_rest_minutes = models.DecimalField(max_digits=4, decimal_places=2)
    pre_worker_weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    pre_worker_rq_times = models.IntegerField()
    worker_1_time_rest_minutes = models.DecimalField(max_digits=4, decimal_places=2)
    worker_1_weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    worker_1_rq_times = models.IntegerField()
    worker_2_time_rest_minutes = models.DecimalField(max_digits=4, decimal_places=2)
    worker_2_weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    worker_2_rq_times = models.IntegerField()
    qrl = models.SmallIntegerField()
    training_volume = models.DecimalField(max_digits=6, decimal_places=2)
    note = models.CharField(max_length=5000, blank=True, null=True)
    date_workout = models.DateField()

    class Meta:
        db_table = 'data_workout'


class Exercises(models.Model):
    muscle = models.ForeignKey('Muscles', models.DO_NOTHING, db_column='muscle', verbose_name='Мышца')
    exercise = models.CharField(verbose_name='Упражнение', primary_key=True, max_length=100)
    technique_execution = models.TextField(verbose_name='Техника выполнения', blank=True, null=True)
    sides_quantity = models.IntegerField(verbose_name='Количество сторон')

    def get_absolute_url(self):
        return reverse("workout:exercise_detail", kwargs={"exercise_pk": self.pk})

    class Meta:
        ordering = ['exercise']
        db_table = 'exercises'


class Mesocycles(models.Model):
    mesocycle = models.CharField(primary_key=True, max_length=30)

    class Meta:
        db_table = 'mesocycles'


class Microcycles(models.Model):
    mesocycle = models.ForeignKey(Mesocycles, models.DO_NOTHING, db_column='mesocycle')
    microcycle = models.CharField(primary_key=True, max_length=60)

    class Meta:
        db_table = 'microcycles'


class MuscleGroups(models.Model):
    muscle_group = models.CharField(primary_key=True, max_length=15)

    class Meta:
        db_table = 'muscle_groups'


class Muscles(models.Model):
    muscle_group = models.ForeignKey(MuscleGroups, models.DO_NOTHING, db_column='muscle_group')
    muscle = models.CharField(primary_key=True, max_length=40)

    def __str__(self) -> str:
        return self.muscle

    class Meta:
        db_table = 'muscles'


class RepsQuantity(models.Model):
    exercise = models.ForeignKey(Exercises, models.DO_NOTHING, db_column='exercise')
    side = models.CharField(max_length=1)
    reps_quantity = models.IntegerField(blank=True, null=True)
    column_4 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'reps_quantity'


class TimeRests(models.Model):
    mesocycle = models.ForeignKey(Mesocycles, models.DO_NOTHING, db_column='mesocycle')
    microcycle = models.ForeignKey(Microcycles, models.DO_NOTHING, db_column='microcycle')
    muscle_group = models.ForeignKey(MuscleGroups, models.DO_NOTHING, db_column='muscle_group')
    approach = models.CharField(max_length=20)
    time_rest = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        db_table = 'time_rests'

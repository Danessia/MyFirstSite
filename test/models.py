from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200, default = '', blank=True, null=True)
    question = models.TextField()
    right_variant = models.ForeignKey('Variant', blank=True, null=True, related_name='right_variant_questions')
    complexity = models.ForeignKey('Complexity')

    def get_formatted_question(self):
        return self.question.replace('___', '<span id="answer"></span>')

    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class Complexity(models.Model):
    name = models.CharField(max_length=64)
    level = models.PositiveIntegerField(default=1)
    series = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    def get_next_level(self):
        return Complexity.objects.filter(level__gt=self.level).order_by('level').first()

    def get_previous_level(self):
        return Complexity.objects.filter(level__lt=self.level).order_by('-level').first()


class Variant(models.Model):
    question = models.ForeignKey('Question', related_name='variants')
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class ResultQuestion(models.Model):
    question = models.ForeignKey('Question')
    user = models.ForeignKey(User)
    answer = models.ForeignKey('Variant')
    attempt = models.PositiveIntegerField(default=0)

    def is_right_answer(self):
        return self.question.right_variant_id == self.answer_id


class UserProgress(models.Model):
    user = models.OneToOneField(User)
    current_level = models.ForeignKey('Complexity', null=True, blank=True)
    current_question = models.ForeignKey('Question', null=True, blank=True)
    attempt = models.PositiveIntegerField(default=0)
    is_done = models.BooleanField(default=False)
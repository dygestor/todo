from django.db import models

class Person(models.Model):
        name = models.CharField(max_length=50)
        email = models.EmailField(max_length=100)

        def __str__(self):
                return self.name + " " + self.email

class Task(models.Model):
        task_text = models.CharField(max_length=200)
        finished = models.BooleanField(default=False)
        person = models.ForeignKey(Person)

        def __str__(self):
                return self.task_text + " " + str(self.finished) + " " + str(self.person)

class Tag(models.Model):
        tag_text = models.CharField(max_length=50)
        task = models.ForeignKey(Task)

        def __str__(self):
                return self.tag_text + " " + task

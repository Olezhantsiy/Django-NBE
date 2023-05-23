from django.db import models

class vocabulary(models.Model):
    enword = models.CharField('Английское слова', max_length=40)
    ruword = models.CharField('Английское слова', max_length=40)

    def __str__(self):
        return self.enword



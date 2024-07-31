from django.db import models
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import User

class Candidate(models.Model):

    class Status(models.TextChoices):
        VALIDE = 'V', gettext_lazy('Validé')
        ENATTENTE = 'A', gettext_lazy('En attente')



    name = models.CharField(max_length=255)
    status = models.CharField(
        max_length=2,
        choices = Status.choices,
        default=Status.ENATTENTE,
    )
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    cv = models.FileField(default='fallback.txt', blank=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)

    def __str__(self):
        return self.name
    
    def get_status(self) -> Status:
        return self.Status(self.status)

from django.db import models
from django.utils.translation import gettext_lazy

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

    def __str__(self):
        return self.name
    
    def get_status(self) -> Status:
        return self.Status(self.status)

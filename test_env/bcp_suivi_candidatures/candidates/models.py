from django.db import models
from django.utils.translation import gettext_lazy
from users.models import Employee
from django.template.defaultfilters import slugify

class Candidate(models.Model):

    class Status(models.TextChoices):
        VALIDE = 'V', gettext_lazy('Validé')
        ENATTENTE = 'EA', gettext_lazy('En attente')
        NONRETENUE = 'NR', gettext_lazy('Non retenu')
        ABSENT = 'AB', gettext_lazy('Absent')
        NEGOTIATION = 'NG', gettext_lazy('Négotiation')



    name = models.CharField(max_length=255)
    status = models.CharField(
        max_length=2,
        choices = Status.choices,
        default=Status.ENATTENTE,
    )
    date = models.DateTimeField(auto_now_add=True)
    cv = models.FileField(default='fallback.txt', blank=True)
    author = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, default=None)
    position = models.CharField(max_length=300)
    entity = models.CharField(max_length=256, null=True, blank=True)
    sub_entity = models.CharField(max_length=256, blank=True, null=True)
    teams_interview = models.DateField(blank=True, null=True)
    technical_interview = models.DateField(blank=True, null=True)
    oto_interview = models.DateField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name
    
    def get_status(self) -> Status:
        return self.Status(self.status)
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)


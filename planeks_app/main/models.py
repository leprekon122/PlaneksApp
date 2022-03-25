from django.db import models


# Create your models here.
class SchemasList(models.Model):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    email = models.EmailField()
    domain_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    company_name = models.CharField(max_length=255)
    text = models.TextField()
    address = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.job} {self.email}" \
               f" {self.domain_name} {self.phone_number} {self.company_name}" \
               f" {self.text} {self.address} {self.date}"

    class Meta:
        verbose_name = 'SchemasList'
        verbose_name_plural = 'SchemasList'


class CeleryStatus(models.Model):
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.status}"


class Meta:
    verbose_name = 'celery_status'
    verbose_name_plural = 'celery_status'

from django.db import models

class TugasAkhir(models.Model):
    no_ta = models.CharField(max_length=10)
    nim = models.CharField(max_length=15)
    nama = models.CharField(max_length=100)
    judul = models.TextField()

    def __str__(self):
        return f"{self.no_ta} - {self.nama}"

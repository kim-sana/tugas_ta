import json
from django.core.management.base import BaseCommand
from pencarian.models import TugasAkhir

class Command(BaseCommand):
    help = "Memuat data dari file JSON"

    def handle(self, *args, **kwargs):
        try:
            with open('pencarian/data/ta_data.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                for item in data:
                    TugasAkhir.objects.create(
                        no_ta=item['No TA'],
                        nim=item['Nim'],
                        nama=item['Nama'],
                        judul=item['Judul']
                    )
            self.stdout.write(self.style.SUCCESS("Data berhasil dimuat!"))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR("File JSON tidak ditemukan."))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR("Terjadi kesalahan saat mengurai file JSON."))

from django.db import models

picture_url = 'https://place-hold.it/100x60'


class Specialty(models.Model):
    code = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    picture = models.CharField(max_length=30, default=picture_url)

    def __str__(self):
        return self.code


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.CharField(max_length=30, default=picture_url)
    description = models.TextField(default='')
    employee_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(max_length=100, default='')
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies", null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies", null=True)
    skills = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    salary_min = models.IntegerField(default=0)
    salary_max = models.IntegerField(default=0)
    published_at = models.DateField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_at']

from django.core.management import BaseCommand

from data import specialties, companies, jobs
from vacancies.models import Specialty, Company, Vacancy


class Command(BaseCommand):

    def handle(self, *args, **options):

        for specialty in specialties:

            Specialty.objects.create(code=specialty['code'], title=specialty['title'])

        for company in companies:
            Company.objects.create(name=company['title'], location=company['location'],
                                   employee_count=company['employee_count'], description=company['description'])

        for job in jobs:
            specialty = Specialty.objects.get(code=job['specialty'])
            company = Company.objects.get(id=job['company'])

            Vacancy.objects.create(title=job['title'], specialty=specialty, company=company,
                                   description=job['description'], salary_min=job['salary_from'],
                                   salary_max=job['salary_to'], published_at=job['posted'],
                                   skills=job['skills'])

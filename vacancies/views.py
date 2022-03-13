from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views import View

from conf.services import vacancies_in_specialty, vacancies_by_specialties
from vacancies.models import Specialty, Company, Vacancy


class MainView(View):
    def get(self, request):
        return render(request, 'index.html',  context={
            'specialties': Specialty.objects.all(),
            'companies': Company.objects.all()
        })


class VacanciesView(View):
    def get(self, request):
        return render(request, 'vacancies.html', context={
            'vacancies_specialties': vacancies_by_specialties()
        })


class VacanciesCategoryView(View):
    def get(self, request, category):
        if not Specialty.objects.filter(code=category).exists():
            raise Http404

        return render(request, 'vacancies.html', context={
            'vacancies_specialties': vacancies_in_specialty(category)
        })


class VacanciesDetailsView(View):
    def get(self, request, vacancy_id):
        vacancy = get_object_or_404(Vacancy, pk=vacancy_id)

        return render(request, 'vacancy.html', context={
            'vacancy': vacancy,
        })


class CompaniesView(View):
    def get(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)
        return render(request, 'company.html', context={
            'company': company
        })

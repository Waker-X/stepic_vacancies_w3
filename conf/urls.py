from django.contrib import admin
from django.urls import path

from vacancies.views import MainView, VacanciesView, VacanciesCategoryView, VacanciesDetailsView, CompaniesView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', MainView.as_view(), name='main'),
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('vacancies/cat/<str:category>/', VacanciesCategoryView.as_view(), name='vacancies_category'),
    path('vacancies/<int:vacancy_id>/', VacanciesDetailsView.as_view(), name='vacancies_details'),
    path('companies/<int:company_id>/', CompaniesView.as_view(), name='companies_details'),
]

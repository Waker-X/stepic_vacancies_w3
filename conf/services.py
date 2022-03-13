from vacancies.models import Specialty, Vacancy


def vacancies_by_specialties():
    vacancies = dict()
    for specialty in Specialty.objects.all():
        if specialty is not None:
            vacancies[specialty] = []
    for vacancy in Vacancy.objects.select_related():
        if vacancy.specialty is not None:
            vacancies[vacancy.specialty].append(vacancy)
    return vacancies


def vacancies_in_specialty(code):
    vacancies = dict()
    specialty = Specialty.objects.filter(code=code).first()
    vacancies[specialty] = specialty.vacancies.all()
    return vacancies

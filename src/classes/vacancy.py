from hh import HH


class Vacancy:
    All_vacancies = []
    hh = HH()
    data = hh.get_vacancies('Python')

    def __init__(self, name, url, pay, requirement):
        self.name = name
        self.url = url
        self.pay = pay
        self.requirement = requirement

        Vacancy.All_vacancies.append(self)


def __str__(self):
    return f'{Vacancy.All_vacancies}'
    # return f'{self.name}, {self.url}, {self.pay}, {self.requirement}'







for x in range(len(Vacancy.data)):
    name = Vacancy.data[x]['name']
    url = Vacancy.data[x]['alternate_url']
    requirement = Vacancy.data[x]['snippet']['requirement']
    if Vacancy.data[x]['salary'] == None:
        pay = None
    else:
        salary_from = Vacancy.data[x]['salary']['from']
        salary_to = Vacancy.data[x]['salary']['to']
        pay = f'{salary_from} - {salary_to}'

    vacancy = Vacancy(name, url, pay, requirement)
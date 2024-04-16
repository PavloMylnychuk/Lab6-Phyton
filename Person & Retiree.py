import datetime

class Person:
    def __init__(self, last_name, first_name, middle_name, birth_date):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.birth_date = birth_date

    def calculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

class Retiree(Person):
    def __init__(self, last_name, first_name, middle_name, birth_date, retirement_age, gender, pension_size, experience):
        super().__init__(last_name, first_name, middle_name, birth_date)
        self.retirement_age = retirement_age
        self.gender = gender
        self.pension_size = pension_size
        self.experience = experience

    def pension_earnings(self):
        years_retired = self.calculate_age() - self.retirement_age
        total_earnings = years_retired * self.pension_size
        return total_earnings

    @staticmethod
    def average_retirement_age_women(retirees):
        women_retirees = [retiree for retiree in retirees if retiree.gender.lower() == 'female']
        if not women_retirees:
            return 0
        total_age = sum(retiree.calculate_age() for retiree in women_retirees)
        average_age = total_age / len(women_retirees)
        return average_age

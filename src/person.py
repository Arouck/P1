import json


class Person:
    def __init__(self,
                 email = '',
                 name = '',
                 lname = '',
                 residence = '',
                 education = '',
                 skills = [],
                 experience = [],
                 serie = '',
                 from_json = False):
        if from_json:
            self.__dict__ = json.loads(serie)
        else:
            self.email = email
            self.name = name
            self.lname = lname
            self.residence = residence
            self.education = education
            self.skills = skills
            self.experience = experience

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_lname(self):
        return self.name

    def set_lname(self, lname):
        self.lname = lname

    def get_residence(self):
        return self.residence

    def set_residence(self, residence):
        self.residence = residence

    def get_education(self):
        return self.education

    def set_education(self, education):
        self.education = education

    def get_skills(self):
        return self.skills

    def add_skills(self, skill):
        self.skills.append(skill)

    def get_experience(self):
        return self.experience

    def add_experience(self, experience):
        self.experience.append(experience)

    def to_json(self):
        return json.dumps(self, default=lambda x: x.__dict__, indent=2)

    def __str__(self):
        return f"Email: {self.email}, First Name: {self.name}, Last Name: {self.lname}, Residence: {self.residence}, " + f"Education: {self.education}, \nSkills: {self.skills}, Experience: {self.experience}.\n"

import json


class Person:
    def __init__(
        self,
        email: str = "",
        name: str = "",
        lname: str = "",
        residence: str = "",
        education: str = "",
        skills: list[str] = [],
        experience: list[str] = [],
        serie: str = "",
        from_json: bool = False,
    ):
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

    def get_email(self) -> str:
        return self.email

    def set_email(self, email: str):
        self.email = email

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_lname(self) -> str:
        return self.name

    def set_lname(self, lname: str):
        self.lname = lname

    def get_residence(self) -> str:
        return self.residence

    def set_residence(self, residence: str):
        self.residence = residence

    def get_education(self) -> str:
        return self.education

    def set_education(self, education: str):
        self.education = education

    def get_skills(self) -> list[str]:
        return self.skills

    def add_skills(self, skill: str):
        self.skills.append(skill)

    def get_experience(self) -> list[str]:
        return self.experience

    def add_experience(self, experience: str):
        self.experience.append(experience)

    def to_json(self):
        return json.dumps(self, default=lambda x: x.__dict__, indent=2)

    def __str__(self):
        return (
            f"Email: {self.email}, First Name: {self.name}, Last Name: {self.lname}, Residence: {self.residence}, "
            + f"Education: {self.education}, \nSkills: {self.skills}, Experience: {self.experience}.\n"
        )

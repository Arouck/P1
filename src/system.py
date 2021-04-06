from person import Person
import Pyro4
import json


@Pyro4.expose
@Pyro4.behavior(instance_mode='single')
class System:
    def __init__(self, users: list[Person] = []):
        self._users = users

    @property
    def users(self) -> list[Person]:
        return [user.to_json() for user in self._users]

    @users.setter
    def users(self, users: list[Person]):
        self._users = users

    @users.deleter
    def users(self):
        del self._users

    def add_user(self, user: str):
        user = Person(serie=user, from_json=True)
        self._users.append(user)

    def add_xp_to_user(self, email: str, experience: str):
        for user in self._users:
            if user.get_email() == email:
                user.add_experience(experience)

    def get_user_by_email(self, email: str) -> list[Person]:
        return next(user.to_json() for user in self._users
                    if user.email == email)

    def get_user_by_education(self, education: str) -> list[Person]:
        return next(user.to_json() for user in self._users
                    if user.get_education() == education)

    def get_xp_by_email(self, email: str) -> list[str]:
        return next(user.get_experience() for user in self._users
                    if user.get_email() == email)

    def get_xp_by_residence(self, residence: str) -> list[str]:
        return next(user.get_experience() for user in self._users
                    if user.get_residence() == residence)

    def show_users(self):
        print(*self._users, sep='\n')

    def clean_cache(self):
        self._users = []


def server():
    Pyro4.Daemon.serveSimple({System: "system.core"}, ns=True)


if __name__ == '__main__':
    server()

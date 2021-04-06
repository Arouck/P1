import json

import click
import Pyro4

from person import Person


@Pyro4.expose
@Pyro4.behavior(instance_mode='single')
class System:
    def __init__(self, users: list[Person] = []):
        self._ids = set()
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

    @property
    def ids(self) -> set:
        return self._ids

    @ids.setter
    def ids(self, ids: set):
        self._ids = ids

    @ids.deleter
    def ids(self):
        del self._ids

    def add_user(self, user: str):
        user = Person(serie=user, from_json=True)
        email = user.get_email()
        if email in self.ids:
            print('Email already registered.')
        else:
            self._users.append(user)
            self._ids.add(email)

    def add_xp_to_user(self, email: str, experience: str):
        for user in self._users:
            if user.get_email() == email:
                user.add_experience(experience)

    def get_user_by_email(self, email: str) -> list[Person]:
        return next(user.to_json() for user in self._users
                    if user.email == email)

    def get_users_by_education(self, education: str) -> list[Person]:
        return [
            user.to_json() for user in self._users
            if user.get_education() == education
        ]

    def get_xp_by_email(self, email: str) -> list[str]:
        return next(user.get_experience() for user in self._users
                    if user.get_email() == email)

    def get_xps_by_residence(self, residence: str) -> list[str]:
        return [
            user.get_experience() for user in self._users
            if user.get_residence() == residence
        ]

    def show_users(self):
        print(*self._users, sep='\n')

    def clean_cache(self):
        self._ids = set()
        self._users = []


@click.command()
@click.option('--remote', is_flag=True)
@click.option('-host', type=str)
@click.option('-port', type=int)
def server(remote, host, port):
    if remote:
        Pyro4.Daemon.serveSimple({System: 'system.core'},
                                 host=host,
                                 port=port,
                                 ns=False)
    else:
        Pyro4.Daemon.serveSimple({System: 'system.core'}, ns=True)


if __name__ == '__main__':
    server()

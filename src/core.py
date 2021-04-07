import sys

import time
import click
import Pyro4
import Pyro4.util

from person import Person
from system import System


LOOP_SIZE = 20


def calculate_task_time_in_ms(function, args):
    start = time.time()
    for i in range(LOOP_SIZE):
        function(*args)
    end = time.time()
    return str((end - start) * 1000)


@click.command()
@click.option("--verbose", is_flag=True)
@click.option("--remote", is_flag=True)
@click.option("-host", type=str)
@click.option("-port", type=int)
def core(verbose, remote, host, port):
    aian = Person(
        "aianshay@gmail.com",
        "Aian",
        "Shay",
        "Belem",
        "UFPA",
        ["Python", "Data Science", "Machine Learning"],
        ["Student at Ideal", "Temp at Labes", "Fellow at Vibe"],
    )
    joao = Person(
        "jvcanavarro@gmail.com",
        "Joao",
        "Canavarro",
        "Belem",
        "UFPA",
        ["Python", "NLP", "Speech Recognition"],
        ["Student at Equipe", "Temp at Labvis", "Fellow at Nubank"],
    )
    pedro = Person(
        "ppvitor@gmail.com",
        "Pedro",
        "Melo",
        "Belem",
        "UFPA",
        ["Java", "Design", "SQL"],
        ["Student at Madre", "Temp at Labsc", "Fellow at Figma"],
    )
    isabela = Person(
        "isa.maues@gmail.com",
        "Isabela",
        "Maues",
        "Belem",
        "UFPA",
        ["C++", "Design", "Figma"],
        ["Student at Logos", "Temp at LAAI", "Fellow at Vale"],
    )

    results = open("../results/times.txt", "w")

    sys.excepthook = Pyro4.util.excepthook
    system = (
        Pyro4.Proxy(f"PYRO:system.core@{host}:{port}")
        if remote
        else Pyro4.Proxy("PYRONAME:system.core")
    )
    system.add_user(user=aian.to_json())
    system.add_user(user=isabela.to_json())
    system.add_user(user=joao.to_json())
    system.add_user(user=pedro.to_json())

    tasks = {
        system.add_xp_to_user: ["ppvitor@gmail.com", "Developer at w"],
        system.get_user_by_email: ["jvcanavarro@gmail.com"],
        system.get_xp_by_email: ["aianshay@gmail.com"],
        system.get_users_by_education: ["UFPA"],
        system.get_xps_by_residence: ["Belem"],
        system.get_users_information: [],
    }

    ellapses = []
    for i, task in enumerate(tasks):
        ellapses.append(calculate_task_time_in_ms(task, tasks[task]))
        print(f"Task {i+1}: {ellapses[i]} milliseconds.")

    if verbose:
        print(system.get_user_by_email(email="jvcanavarro@gmail.com"))
        print(system.get_xp_by_email(email="aianshay@gmail.com"))

        print(*system.get_users_by_education(education="UFPA"), sep="\n")
        print(*system.get_xps_by_residence(residence="Belem"), sep="\n")

        print(*system.get_users_information(), sep="\n")

    results.write('\n'.join(ellapses))
    results.close()

    # Server Side
    system.show_users()
    system.clear_cache()


if __name__ == "__main__":
    core()

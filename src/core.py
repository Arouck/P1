import sys

import time
import click
import Pyro4
import Pyro4.util

from person import Person
from system import System


@click.command()
@click.option("--remote", is_flag=True)
@click.option("-host", type=str)
@click.option("-port", type=int)
def core(remote, host, port):
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

    file = open("times.txt", "w")

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
    #system.add_user(user=pedro.to_json())

    loop_size = 20
    start = time.time()
    for i in range(loop_size):
            system.add_xp_to_user(email="ppvitor@gmail.com", experience="Developer at w")
    end = time.time()
    ellapse_1 = end - start

    file.write(repr(ellapse_1*1000) + "\n")
    print(f"Task 1: {ellapse_1*1000} milliseconds.")


    start = time.time()
    for i in range(loop_size):
            system.get_user_by_email(email="jvcanavarro@gmail.com")
    end = time.time()
    ellapse_2 = end - start

    file.write(repr(ellapse_2*1000) + "\n")
    print(f"Task 2: {ellapse_2*1000} milliseconds.")
    #print(system.get_user_by_email(email="jvcanavarro@gmail.com"))
    start = time.time()
    for i in range(loop_size):
            system.get_xp_by_email(email="aianshay@gmail.com")
    end = time.time()
    ellapse_3 = end - start

    file.write(repr(ellapse_3*1000) + "\n")
    print(f"Task 3: {ellapse_3*1000} milliseconds.")
    #print(system.get_xp_by_email(email="aianshay@gmail.com"))
    
    start = time.time()
    for i in range(loop_size):
            system.get_users_by_education(education="UFPA")
    end = time.time()
    ellapse_4 = end - start

    file.write(repr(ellapse_4*1000) + "\n")
    print(f"Task 4: {ellapse_4*1000} milliseconds.")
    #print(*system.get_users_by_education(education="UFPA"), sep="\n")
    start = time.time()
    for i in range(loop_size):
            system.get_xps_by_residence(residence="Belem")
    end = time.time()
    ellapse_5 = end - start
    
    file.write(repr(ellapse_5*1000) + "\n")
    print(f"Task 5: {ellapse_5*1000} milliseconds.")
    #print(*system.get_xps_by_residence(residence="Belem"), sep="\n")

    start = time.time()
    for i in range(loop_size):
            system.users
    end = time.time()
    ellapse_6 = end - start
    
    file.write(repr(ellapse_6*1000))
    print(f"Task 6: {ellapse_6*1000} milliseconds.")
    file.close()
    #print(*system.users, sep="\n")

    # Server Side
    system.show_users()
    system.clean_cache()


if __name__ == "__main__":
    core()

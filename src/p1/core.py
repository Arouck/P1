import sys
import Pyro4
import Pyro4.util
from person import Person
from system import System

sys.excepthook = Pyro4.util.excepthook
system = Pyro4.Proxy("PYRONAME:example.system")

aian = Person("aianshay@gmail.com", "Aian", "Shay", "Belém", "UFPA",
              ["Python", "Data Science", "Machine Learning"],
              ['Student at xxxx', 'Temp at yyyy', 'Fellow at zzzz'])
joao = Person("jvcanavarro@gmail.com", "Joao", "Canavarro", "Belém", "UFPA",
              ["Python", "NLP", "Speech Recognition"],
              ['Student at xxxx', 'Temp at yyyy', 'Fellow at zzzz'])
pedro = Person("ppvitor@gmail.com", "Pedro", "Melo", "Belém", "UFPA",
               ["Java", "Design", "SQL"],
               ['Student at xxxx', 'Temp at yyyy', 'Fellow at zzzz'])
isabela = Person("isa.maues@gmail.com", "Isabela", "Maues", "Belém", "UFPA",
                 ["C++", "Design", "Figma"],
                 ['Student at xxxx', 'Temp at yyyy', 'Fellow at zzzz'])

# system = System(users=[aian, joao, pedro])

system.add_user(user=isabela)
system.add_xp_to_user(email="ppvitor@gmail.com", experience="Developer at w")

system.get_user_by_email(email="jvcanavarro@gmail.com")
system.get_user_by_education(education="UFPA")

system.get_xp_by_email(email="aianshay@gmail.com")
system.get_xp_by_residence(residence="Belém")

system.show_users()

import sys
import Pyro4
import Pyro4.util
from person import Person
from system import System

aian = Person("aianshay@gmail.com", "Aian", "Shay", "Belem", "UFPA",
              ["Python", "Data Science", "Machine Learning"],
              ['Student at Ideal', 'Temp at Labes', 'Fellow at Vibe'])
joao = Person("jvcanavarro@gmail.com", "Joao", "Canavarro", "Belem", "UFPA",
              ["Python", "NLP", "Speech Recognition"],
              ['Student at Equipe', 'Temp at Labvis', 'Fellow at Nubank'])
pedro = Person("ppvitor@gmail.com", "Pedro", "Melo", "Belem", "UFPA",
               ["Java", "Design", "SQL"],
               ['Student at Madre', 'Temp at Labsc', 'Fellow at Figma'])
isabela = Person("isa.maues@gmail.com", "Isabela", "Maues", "Belem", "UFPA",
                 ["C++", "Design", "Figma"],
                 ['Student at Logos', 'Temp at LAAI', 'Fellow at Vale'])

sys.excepthook = Pyro4.util.excepthook
system = Pyro4.Proxy("PYRONAME:system.core")

system.add_user(user=aian.to_json())
system.add_user(user=isabela.to_json())
system.add_user(user=joao.to_json())
system.add_user(user=pedro.to_json())
system.add_user(user=pedro.to_json())

system.add_xp_to_user(email="ppvitor@gmail.com", experience="Developer at w")

print(system.get_user_by_email(email="jvcanavarro@gmail.com"))
print(*system.get_users_by_education(education="UFPA"), sep='\n')

print(system.get_xp_by_email(email="aianshay@gmail.com"))
print(*system.get_xps_by_residence(residence="Belem"), sep='\n')

print(*system.users, sep='\n')

# Server Side
system.show_users()
system.clean_cache()

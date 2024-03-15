import os
from typing import Dict


class PeopleRegisterView:
    def register_people_view(self) -> Dict:
        os.system("cls||clear")

        print("Cadastrar Pessoa\n")
        name = input("Digite o nome da pessoa: ")
        age = input("Digite a idade da pessoa: ")
        height = input("Digite a altura da pessoa: ")

        people_register_informations = {
            "name": name,
            "age": age,
            "height": height
        }

        return people_register_informations

import os
from typing import Dict


class PeopleFinderView:
    def find_people_view(self) -> Dict:
        os.system("cls||clear")

        print("Buscar Pessoa\n")
        name = input("Digite o nome da pessoa para busca: ")

        people_finder_informations = {
            "name": name
        }

        return people_finder_informations

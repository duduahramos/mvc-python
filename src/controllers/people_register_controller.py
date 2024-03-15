from typing import Dict
from datetime import datetime


class PeopleRegisterController:
    def register(self, new_people_informations: Dict) -> Dict:
        try:
            self.__validate_field(new_people_informations)
            # enviar para model para cadastro de dados

            response = self.__format_response(new_people_informations)
            return response
        except Exception as exception:
            print(exception)
            return {"error": str(exception)}

    def __validate_field(self, new_people_informations: Dict) -> None:
        if not isinstance(new_people_informations.get("name"), str):
            raise Exception("Nome inválido!")

        try:
            int(new_people_informations.get("age"))
        except Exception as e:
            print(e)
            raise Exception("Idade inválida!")

        try:
            int(new_people_informations.get("height"))
        except Exception as e:
            print(e)
            raise Exception("Altura incorreta!")

        try:
            date_of_birth = new_people_informations.get("date_of_birth")
            datetime.strptime(date_of_birth, "%d/%m/%Y")
        except Exception as e:
            print(e)
            raise Exception("Altura incorreta!")

    def __format_response(self, new_people_informations: Dict) -> Dict:
        return {
            "count": 1,
            "type": "People",
            "attributes": new_people_informations
        }

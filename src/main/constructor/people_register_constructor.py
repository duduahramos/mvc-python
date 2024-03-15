from src.views.people_register_view import PeopleRegisterView


def people_register_constructor():
    people_register_view = PeopleRegisterView()

    new_people_informations = people_register_view.register_people_view()

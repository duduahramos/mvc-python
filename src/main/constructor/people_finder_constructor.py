from src.views.people_finder_view import PeopleFinderView


def people_finder_constructor():
    people_finder_view = PeopleFinderView()
    # controller

    people_finder_informations = people_finder_view.find_people_view()
    # enviar para controller

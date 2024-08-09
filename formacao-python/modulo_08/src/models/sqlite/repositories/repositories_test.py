import pytest
from src.models.sqlite.settings.connection import db_connection_handler

from .people_repository import PeopleRepository
from .pets_repository import PetsRepository

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="Interação com o banco de dados")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print()
    print(response)


@pytest.mark.skip(reason="Interação com o banco de dados")
def test_delete_pets():
    name = "belinha"

    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(name)


@pytest.mark.skip(reason="Interação com o banco de dados")
def test_insert_person():
    repo = PeopleRepository(db_connection_handler)
    repo.insert_person(first_name="Patrick", last_name="Nascimento", age=29, pet_id=1)


@pytest.mark.skip(reason="Interação com o banco de dados")
def test_get_person():
    person_id = 2

    repo = PeopleRepository(db_connection_handler)
    response = repo.get_person(person_id)
    print(response)

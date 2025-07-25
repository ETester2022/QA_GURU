"""Написать API-тесты:
1. на каждый из методов GET/POST/PUT/DELETE ручек reqres.in!!!!!!!!!!!!!!!!!!!!
2. Позитивные/Негативные тесты на одну из ручек.!!!!!!!!!!!!!!!!!!!!
3. На разные статус-коды 200/201/204/404/400!!!!!!!!!!!!!!!!!!!!
4. На разные схемы (4-5 схем)
5. С ответом и без ответа!!!!!!!!!!!!!!!!!!!!!!!1

Дополнительно со * :
6. На бизнес-логику (заметить какую-то фичу и автоматизировать, как делали на уроке)

Автотесты должны иметь говорящее название, которое будет понятно человеку не глядя в код."""
from jsonschema import validate
from test_hw17 import schemas
import requests
import pytest


# pytest -m hw17 -vv
# pytest -m tests_positive -vv
@pytest.mark.hw17
@pytest.mark.tests_positive
class TestsPositive:

    # pytest -m test_get_count_of_users -vv
    @pytest.mark.test_get_count_of_users
    def test_get_count_of_users(self):

        response = requests.get(url="https://reqres.in/api/users",
                                params={"page": "2"},
                                headers={
                                    "x-api-key": "reqres-free-v1"
                                })
        count_of_users = len(response.json()["data"])

        assert response.status_code == 200
        assert count_of_users == 6
        validate(response.json(), schema=schemas.get_count_of_users)


    # pytest -m test_create_user -vv
    @pytest.mark.test_create_user
    def test_create_user(self):

        name = "morpheus"
        job = "leader"

        response = requests.post(url="https://reqres.in/api/users",
                                 headers={
                                     "x-api-key": "reqres-free-v1"
                                 },
                                 json={
                                    "name": f"{name}",
                                    "job": f"{job}"
                                 })
        body = response.json()
        user_name = body["name"]
        user_job = body["job"]

        assert response.status_code == 201
        assert name == user_name
        assert job == user_job
        validate(body, schema=schemas.create_user)


    # pytest -m test_update_user -vv
    @pytest.mark.test_update_user
    def test_update_user(self):

        name = "morpheus"
        job = "zion resident"

        response = requests.put(url="https://reqres.in/api/users/2",
                                headers={
                                     "x-api-key": "reqres-free-v1"
                                 },
                                json={
                                    "name": f"{name}",
                                    "job": f"{job}"
                                })
        body = response.json()
        user_name = body["name"]
        user_job = body["job"]

        assert response.status_code == 200
        assert name == user_name
        assert job == user_job
        validate(body, schema=schemas.update_user)


    # pytest -m test_delete_user -vv
    @pytest.mark.test_delete_user
    def test_delete_user(self):

        response = requests.delete(url="https://reqres.in/api/users/2",
                                   headers={
                                       "x-api-key": "reqres-free-v1"
                                   })

        assert response.status_code == 204


    # pytest -m test_register_user_success -vv
    @pytest.mark.test_register_user_success
    def test_register_user_success(self):

        response = requests.post(url="https://reqres.in/api/register",
                                 json={
                                    "email": "eve.holt@reqres.in",
                                    "password": "pistol"
                                 },
                                 headers={
                                     "x-api-key": "reqres-free-v1"
                                 })

        assert response.status_code == 200
        validate(response.json(), schema=schemas.register_user_success)


# pytest -m tests_negative -vv
@pytest.mark.hw17
@pytest.mark.tests_negative
class TestsNegative:

    # pytest -m test_get_single_user_not_found -vv
    @pytest.mark.test_get_single_user_not_found
    def test_get_single_user_not_found(self):

        response = requests.get(url="https://reqres.in/api/users/23",
                                headers={
                                   "x-api-key": "reqres-free-v1"
                                })

        assert response.status_code == 404


    # pytest -m test_register_user_unsuccessful -vv
    @pytest.mark.test_register_user_unsuccessful
    def test_register_user_unsuccessful(self):

        response = requests.post(url="https://reqres.in/api/register",
                                 json={
                                    "email": "sydney@fife"
                                 },
                                 headers={
                                    'x-api-key': 'reqres-free-v1'
                                 })

        assert response.status_code == 400
        validate(response.json(), schema=schemas.register_user_unsuccessful)

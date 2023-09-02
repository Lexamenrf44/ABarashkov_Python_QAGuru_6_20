import requests
from jsonschema.validators import validate
from conftest import load_json_schema


def test_get_users_list_by_page():
    page = 2
    response = requests.get(url='https://reqres.in/api/users',
                         params={'page': page})

    assert response.status_code == 200
    assert response.json()['page'] == page


def test_get_users_list_data_by_per_page():
    per_page = 6
    response = requests.get(url='https://reqres.in/api/users',
                         params={'per_page': per_page})

    assert response.status_code == 200
    assert response.json()['per_page'] == per_page
    assert len(response.json()['data']) == per_page


def test_positive_get_single_user_data_by_id():
    id = 1
    response = requests.get(url='https://reqres.in/api/users',
                         params={'id': id})

    assert response.status_code == 200
    assert response.json()['data']['id'] == id


def test_negative_get_single_user_data_by_id():
    id = 23
    response = requests.get(url='https://reqres.in/api/users',
                         params={'id': id})

    assert response.status_code == 404


def test_get_users_list_response_format():
    schema = load_json_schema('get_users_list_response_schema.json')

    response = requests.get(url='https://reqres.in/api/users')

    validate(instance=response.json(),
               schema=schema)


def test_patch_user_format_json():
    schema = load_json_schema('update_user_response_schema.json')

    payload = {
        "name": "Alexander",
        "job": "QAGuru"
    }

    response = requests.patch(url='https://reqres.in/api/users/2',
                            json=payload)

    assert response.status_code == 200
    validate(response.json(), schema=schema)
    assert response.json()['name'] == payload['name']
    assert response.json()['job'] == payload['job']


def test_put_user_format_json():
    schema = load_json_schema('update_user_response_schema.json')

    payload = {
        "name": "Alexander",
        "job": "QAGuru"
    }

    response = requests.put(url='https://reqres.in/api/users/2',
                            json=payload)

    assert response.status_code == 200
    validate(response.json(), schema=schema)
    assert response.json()['name'] == payload['name']
    assert response.json()['job'] == payload['job']


def test_delete_user_by_id():
    id = 2
    response = requests.delete(url='https://reqres.in/api/users/2',
                            params={'id': id})

    assert response.status_code == 204


def test_create_user_format_json():
    schema = load_json_schema('create_user_response_schema.json')

    payload = {
        "name": "Alexander",
        "job": "QAGuru"
    }

    response = requests.post(url='https://reqres.in/api/users',
                            json=payload)

    assert response.status_code == 201
    validate(response.json(), schema=schema)
    assert response.json()['name'] == payload['name']
    assert response.json()['job'] == payload['job']


def test_register_user_format_json():
    schema = load_json_schema('register_user_response_schema.json')

    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    response = requests.post(url='https://reqres.in/api/register',
                            json=payload)

    assert response.status_code == 200
    validate(response.json(), schema=schema)

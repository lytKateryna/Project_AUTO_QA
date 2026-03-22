import requests


class EmployeeApi:
    """Класс для взаимодействия с API компаний"""

    def __init__(self, url):
        """Инициализация класса с базовым URL API"""
        self.url = url

    def create_employ(self, data_json):
        """Получить список всех компаний"""
        resp = requests.post(self.url + '/employee/create', json=data_json)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()

    def get_employee_by_id(self, id):
        resp = requests.get(self.url + f'/employee/info/{id}')
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()


    def get_token(self, user, password):
        """ Получать токен для авторизации """
        creds = {"username": user, "password": password}
        resp = requests.post(self.url + '/auth/login', json=creds)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()["user_token"]

    def edit_employee(self, company_id, last_name, user, password):
        client_token = self.get_token(user, password)
        url_with_token = f'{self.url}/employee/change/{company_id}?token={client_token}'

        company_data = {
            "name": "last_name",
            "user": "",
        }

        resp = requests.patch(url_with_token, json=company_data)
        assert resp.status_code == 202, f"Ошибка: ожидался статус 202, получен {resp.status_code}"
        return resp.json()
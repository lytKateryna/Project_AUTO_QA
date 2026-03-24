from employee import EmployeeApi

base_url = "http://5.101.50.27:8000"
api = EmployeeApi(base_url)


# 1. Создание нового работника
def test_create_employee():
    employee_json = {
        "first_name": "string",
        "last_name": "string",
        "middle_name": "string",
        "company_id": 2,
        "email": "user@example.com",
        "phone": "string",
        "birthdate": "2026-03-18",
        "is_active": True
    }

    # api = EmployeeApi(base_url)  # Инициализация API-клиента

    new_emp = api.create_employ(data_json=employee_json)

    print(new_emp)

    assert new_emp["first_name"] == "string"


# 2. Получение информации о работнике

def test_get_employee():
    # api = EmployeeApi(base_url)
    employee_info = api.get_employee_by_id(1)

    assert employee_info["first_name"] == "Иван"


# 3. Изменение информации о работнике
def test_edit_employee():
    mod_employ = api.edit_employee(1, "sidorov", "harrypotter", "expelliarmus")
    assert mod_employ["last_name"] == "sidorov"

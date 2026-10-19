
from project import (
    get_next_token,
    calculate_average_service_time,
    estimate_waiting_time,
    search_customer,
)


def test_get_next_token():
    assert get_next_token([]) == 1


def test_average_service_time():
    customers = [
        {"status": "served", "service": "burger", "service_time": 2},
        {"status": "served", "service": "burger", "service_time": 4},
    ]

    assert calculate_average_service_time(customers, "burger") == 3


def test_waiting_time():
    customers = [
        {"token": 1, "status": "waiting", "service": "burger"},
        {"token": 2, "status": "waiting", "service": "rolls"},
    ]

    assert estimate_waiting_time(customers, 1) == 0
    assert estimate_waiting_time(customers, 2) == 5


def test_search_customer():
    customers = [
        {"token": 1, "name": "Rahul"},
        {"token": 2, "name": "Priya"},
    ]

    assert len(search_customer(customers, "Rahul")) == 1

from enum import Enum

class PERSONS(Enum):
    HARSHIL = 1
    MANOJ = 2
    MAITRI = 3
    SAKSHI = 4
    ANUP = 5
    PARTH = 6
    TUSHAR = 7
    JAYBHAI = 8,
    NIXIT = 10,
    MANISHA = 14


items = [
    {
        "name": "ICE",
        "value": 4.49,
        "taxable": False,
        "people": [PERSONS.HARSHIL, PERSONS.ANUP, PERSONS.ANUP, PERSONS.NIXIT, PERSONS.NIXIT, PERSONS.JAYBHAI, PERSONS.JAYBHAI, PERSONS.JAYBHAI, PERSONS.JAYBHAI, PERSONS.PARTH, PERSONS.PARTH, PERSONS.MANISHA],
    },
    {
        "name": "Tim Hortons",
        "value": 6.76,
        "taxable": False,
        "people": [PERSONS.HARSHIL, PERSONS.NIXIT],
    },
    {
        "name": "Chair",
        "value": 20,
        "taxable": True,
        "people": [PERSONS.ANUP],
    },
    {
        "name": "Walmart Groceries",
        "value": 76.57 + 58.99,
        "taxable": False,
        "people": [PERSONS.HARSHIL, PERSONS.ANUP, PERSONS.ANUP, PERSONS.NIXIT, PERSONS.NIXIT, PERSONS.JAYBHAI, PERSONS.JAYBHAI, PERSONS.JAYBHAI, PERSONS.JAYBHAI, PERSONS.PARTH, PERSONS.PARTH, PERSONS.MANISHA],
    },
    {
        "name": "Hertz",
        "value": 105,
        "taxable": False,
        "people": [PERSONS.HARSHIL, PERSONS.ANUP, PERSONS.ANUP, PERSONS.NIXIT, PERSONS.NIXIT],
    },
    {
        "name": "Fire Wood",
        "value": 5,
        "taxable": False,
        "people": [PERSONS.HARSHIL, PERSONS.ANUP, PERSONS.ANUP, PERSONS.NIXIT, PERSONS.NIXIT, PERSONS.JAYBHAI, PERSONS.JAYBHAI, PERSONS.JAYBHAI, PERSONS.JAYBHAI, PERSONS.PARTH, PERSONS.PARTH, PERSONS.MANISHA],
    },
    {
        "name": "Indian store groceries",
        "value": 111,
        "taxable": False,
        "people": [PERSONS.HARSHIL, PERSONS.ANUP, PERSONS.ANUP, PERSONS.NIXIT, PERSONS.NIXIT, PERSONS.JAYBHAI, PERSONS.JAYBHAI, PERSONS.JAYBHAI, PERSONS.JAYBHAI, PERSONS.PARTH, PERSONS.PARTH, PERSONS.MANISHA],
    },
    {
        "name": "Pizza Pizza",
        "value": 19.66,
        "taxable": False,
        "people": [PERSONS.HARSHIL, PERSONS.ANUP],
    }

]

tax_rate = 13  # 13% tax rate
total_discount = 0  # total discount

from enum import Enum

class PERSONS(Enum):
    HARSHIL = 1
    MANOJ = 2
    MAITRI = 3
    SAKSHI = 4

items = [
  {
    "name": "Pepper, Green Bell",
    "value": 1.85,
    "taxable": False,
    "people": [PERSONS.MANOJ, PERSONS.MAITRI, PERSONS.SAKSHI]
  },
  {
    "name": "Eggplant, Large",
    "value": 7.78,
    "taxable": False,
    "people": [PERSONS.MANOJ, PERSONS.MAITRI, PERSONS.SAKSHI, PERSONS.HARSHIL]
  },
  {
    "name": "Tomato, Roma",
    "value": 3.93,
    "taxable": False,
    "people": [PERSONS.MANOJ, PERSONS.MAITRI, PERSONS.SAKSHI]
  },
  {
    "name": "Tomato, Roma",
    "value": 3.93,
    "taxable": False,
    "people": [PERSONS.HARSHIL]
  },
  {
    "name": "Sealtest Homogenized 3.25% Milk, 4 L",
    "value": 5.81,
    "taxable": False,
    "people": [PERSONS.MANOJ, PERSONS.MAITRI, PERSONS.SAKSHI, PERSONS.HARSHIL]
  },
  {
    "name": "ReaLemon Lemon Juice, 945 mL",
    "value": 2.79,
    "taxable": False,
    "people": [PERSONS.MANOJ, PERSONS.MAITRI, PERSONS.SAKSHI]
  },
  {
    "name": "Sealtest 35% Whipping Cream, 473 mL",
    "value": 3.99,
    "taxable": False,
    "people": [PERSONS.MANOJ, PERSONS.MAITRI, PERSONS.SAKSHI]
  },
  {
    "name": "Becel Margarine Original, 427g",
    "value": 3.99,
    "taxable": False,
    "people": [PERSONS.MANOJ, PERSONS.MAITRI, PERSONS.SAKSHI]
  },
  {
    "name": "Fairlife Chocolate Milk 2% Bottle, 1.5 L",
    "value": 5.32,
    "taxable": False,
    "people": [PERSONS.MANOJ, PERSONS.MAITRI, PERSONS.SAKSHI]
  },
  {
    "name": "Gits Khatta Dhokla Instant Mix (Qty 4)",
    "value": 5.64,
    "taxable": False,
    "people": [PERSONS.MANOJ, PERSONS.MAITRI, PERSONS.SAKSHI, PERSONS.HARSHIL]
  },
  {
    "name": "Febreze Plug In Air Freshener, Ocean Scent",
    "value": 12.96,
    "taxable": True, 
    "people": [PERSONS.MANOJ, PERSONS.MAITRI, PERSONS.SAKSHI, PERSONS.HARSHIL]
  },
  {
    "name": "Balderson 2 Year Old Cheddar Cheese, 500g",
    "value": 15.60,
    "taxable": False,
    "people": [PERSONS.MANOJ, PERSONS.MAITRI, PERSONS.SAKSHI]
  },
  {
    "name": "Lijjat Jeera Papad, 200g",
    "value": 1.42,
    "taxable": False,
    "people": [PERSONS.MANOJ, PERSONS.MAITRI, PERSONS.SAKSHI, PERSONS.HARSHIL]
  }
]


tax_rate = 13  # 13% tax rate
total_discount = 0  # total discount

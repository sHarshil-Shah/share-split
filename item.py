from enum import Enum


class PERSONS(Enum):
    HARSHIL = 1
    RAJ = 2
    SHUBHAM = 3
    PARAS = 4
    VIRAL = 5
    HRISHI = 6


items = [
    {
        "name": "Britannia Sooji Toast Regular",
        "value": 2.66,
        "taxable": False,
        "people": [PERSONS.PARAS]
    },
    {
        "name": "Haldiram Khari Boondi Regular",
        "value": 3.66,
        "taxable": True,
        "people": [PERSONS.HARSHIL, PERSONS.RAJ, PERSONS.PARAS, PERSONS.VIRAL]
    },
    {
        "name": "Green Onion Regular",
        "value": 1.47,
        "taxable": False,
        "people": [PERSONS.HARSHIL, PERSONS.RAJ, PERSONS.PARAS, PERSONS.VIRAL]
    },
    {
        "name": "Britannia Milk Rusk Regular",
        "value": 5.77,
        "taxable": False,
        "people": [PERSONS.VIRAL]
    },
    {
        "name": "Scotsburn 3.25% Homogenized Milk Regular",
        "value": 20.55,
        "taxable": False,
        "people": [PERSONS.HARSHIL, PERSONS.RAJ, PERSONS.PARAS, PERSONS.VIRAL, PERSONS.HRISHI, PERSONS.SHUBHAM]
    },
    {
        "name": "Hershey's Natural Unsweetened Cocoa Powder Regular",
        "value": 4.77,
        "taxable": False,  # Assuming cocoa powder isn't a grocery
        "people": [PERSONS.HRISHI]
    },
    {
        "name": "Great Value Manzanilla Sliced Green Olives Regular",
        "value": 1.96,
        "taxable": False,  # Assuming olives aren't a grocery
        "people": [PERSONS.RAJ]
    },
    {
        "name": "Great Value Bread & Butter Sweet Pickles Regular",
        "value": 3.27,
        "taxable": False,  # Assuming pickles aren't a grocery
        "people": [PERSONS.RAJ]
    },
    {
        "name": "Lay's Sour Cream & Onion flavoured potato chips Regular",
        "value": 10.98,
        "taxable": True,  # Chips are likely taxable
        "people": [PERSONS.PARAS]
    },
    {
        "name": "Cilantro Regular",
        "value": 2.92,
        "taxable": False,
        "people": [PERSONS.HARSHIL, PERSONS.RAJ, PERSONS.PARAS, PERSONS.VIRAL]
    },
    {
        "name": "Your Fresh Market Tomatoes on the Vine",  # Weight adjusted items can be named as is
        "value": 8.80,
        "taxable": False,
        "people": [PERSONS.HARSHIL, PERSONS.RAJ, PERSONS.PARAS, PERSONS.VIRAL]
    },
    {
        "name": "Banana",  # Weight adjusted items can be named as is
        "value": 4.40,
        "taxable": False,
        "people": [PERSONS.HARSHIL, PERSONS.RAJ, PERSONS.RAJ, PERSONS.VIRAL, PERSONS.VIRAL, PERSONS.HRISHI]
    },
]

tax_rate = 15  # 15% tax rate
total_discount = 14.98  # total discount

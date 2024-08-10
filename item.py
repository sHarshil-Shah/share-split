from enum import Enum


class PERSONS(Enum):
    HARSHIL = 1
    PARTH = 2
    FORAM = 3
    PARTH_P = 4
    SOUTH = 5


items = [
  {
    "name": "Pears Gentle Care Transparent Soap Regular",
    "value": 10.71,
    "taxable": true, 
    "people": [PERSONS.HARSHIL] 
  },
  {
    "name": "Lime Regular",
    "value": 1.12,
    "taxable": false, 
    "people": [PERSONS.HARSHIL, PERSONS.PARTH, PERSONS.PARTH_P] 
  },
  {
    "name": "Proctor Silex Iron with Stainless Steel Soleplate 17172PS Regular",
    "value": 16.96,
    "taxable": true, 
    "people": [PERSONS.HARSHIL, PERSONS.PARTH_P] 
  },
  {
    "name": "Sealtest Homogenized 3.25% Milk Regular",
    "value": 21.21,
    "taxable": false,
    "people": [PERSONS.HARSHIL, PERSONS.PARTH, PERSONS.PARTH_P, PERSONS.SOUTH] 
  },
  {
    "name": "Head & Shoulders Deep Scalp Cleanse 2-in-1 Anti-Dandruff Shampoo + Conditioner Regular",
    "value": 6.97,
    "taxable": true, 
    "people": [PERSONS.PARTH_P] 
  },
  {
    "name": "Tomato, Roma Weight-Adjusted",
    "value": 5.00,
    "taxable": false,
    "people": [PERSONS.HARSHIL, PERSONS.PARTH, PERSONS.PARTH_P] 
  },
  {
    "name": "Banana Weight-Adjusted",
    "value": 1.91,
    "taxable": false,
    "people": [PERSONS.HARSHIL, PERSONS.PARTH_P] 
  }
]


tax_rate = 13  # 15% tax rate
total_discount = 14.87  # total discount

# Efficient Split Calculator

This Python program calculates the share of each person for multiple items, considering discounts and taxes. It helps to distribute the costs fairly among a group of people.

## Features

- Calculate the individual share for each person based on the number of items they purchased.
- Apply discounts to the total value of the order.
- Apply taxes to taxable items.
- Display the total share for each person.
- Display the itemized share for each person.

## Usage

1. Define the list of items with their respective details (name, value, people involved, and taxable status) in the `items` list.
2. Set the `tax_rate` and `total_discount` values according to your requirements.
3. Run the program, and it will output the total share and itemized share for each person involved.

## Example

```python
items = [
   {
       "name": "Ginger",
       "value": 0.61,
       "taxable": False,
       "people": [PERSONS.RAJ, PERSONS.HARSHIL, PERSONS.PARAS, PERSONS.VIRAL, PERSONS.SHUBHAM]
   },
   {
       "name": "Oats",
       "value": 2.76,
       "people": [PERSONS.RAJ],
       "taxable": False,
   },
   # ... (more items)
]
```

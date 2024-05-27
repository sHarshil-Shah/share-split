from enum import Enum


def calculate_share(items_arg, discount_rate):
    """
  This function calculates the share for each person for multiple items.

  Args:
      items_arg: A list of dictionaries, where each dictionary represents an item
              and contains "name" (item name), "value" (total value), and
              "people" (a list of dictionaries with "name" key for each person).

  Returns:
      A list of dictionaries, where each dictionary contains a "name" key (person's name),
      a list of sub-dictionaries with "item_name", "share_value" for each item,
      and a "total_share" representing the person's total share across all items.
  """

    all_people = set()  # Collect all unique people across items
    for item in items_arg:
        all_people.update(person1 for person1 in item["people"])

    results = []
    total_tax = 0
    for person_name in all_people:
        person_share = []
        total_share = 0
        for item in items_arg:
            # Find the share value for this person in the current item
            share_value = 0
            for person in item["people"]:
                item_val = item["value"]
                if person == person_name:
                    item_val *= (1 - discount_rate / 100)

                    share_value = item_val / len(item["people"])  # Divide equally
                    if item["taxable"]:
                        total_tax += share_value * tax_rate / 100
                        share_value *= (1 + tax_rate / 100)
                    total_share += share_value
                    # break
            person_share.append({
                "item_name": item["name"],
                "share_value": share_value
            })
        results.append({
            "name": person_name,
            "share": person_share,
            "total_share": total_share
        })
    print("total_tax", total_tax)
    return results


# definition to get all unique item names
def get_unique_item_names(items_arg):
    """
  This function returns a list of unique item names from the input list of items.

  Args:
      items_arg: A list of dictionaries, where each dictionary represents an item
              and contains "name" (item name), "value" (total value), and
              "people" (a list of dictionaries with "name" key for each person).

  Returns:
      A list of unique item names.
  """

    return list(set(item["name"] for item in items_arg))


if __name__ == '__main__':

    class PERSONS(Enum):
        HARSHIL = 1
        RAJ = 2
        SHUBHAM = 3
        PARAS = 4
        VIRAL = 5
        HRISHI = 6


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
        {
            "name": "Garlic",
            "value": 6.46,
            "people": [PERSONS.RAJ, PERSONS.HARSHIL, PERSONS.PARAS, PERSONS.VIRAL, PERSONS.SHUBHAM],
            "taxable": False,
        },
        {
            "name": "Pods",
            "value": 29.92,
            "people": [PERSONS.RAJ, PERSONS.HARSHIL, PERSONS.PARAS, PERSONS.VIRAL, PERSONS.SHUBHAM, PERSONS.HRISHI],
            "taxable": True,
        },
        {
            "name": "Oats 2",
            "value": 2.76,
            "people": [PERSONS.RAJ],
            "taxable": False,
        }
    ]

    tax_rate = 15  # 15% tax rate
    total_discount = 14.98  # total discount

    total_value = sum(item["value"] for item in items)
    print("total value", total_value)
    discount_rate = total_discount * 100 / total_value  # calculate discount rate
    print("discount rate", discount_rate)

    shares = calculate_share(items, discount_rate)

    for person in shares:
        print(f"{person['name']}'s share: ${person['total_share']:.2f}")

    for person in shares:
        print(f"\n{person['name']}'s share:")

        for item_share in person["share"]:
            if item_share['share_value'] == 0:
                continue
            print(f"  - {item_share['item_name']}: ${item_share['share_value']:.2f}")

    print(", ".join(get_unique_item_names(items)))

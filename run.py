from item import items, total_discount
from funcs import get_unique_item_names, calculate_share

total_value = sum(item["value"] for item in items)
print("total value", total_value)
discount_rate = total_discount * 100 / total_value  # calculate discount rate
# print("discount rate", discount_rate)

shares = calculate_share(items, discount_rate)

print()
for person in shares:
    person_name = person['name'].name if hasattr(person['name'], 'name') else person['name']
    print(f"{person_name}'s total share: ${person['total_share']:.2f}")

for person in shares:
    person_name = person['name'].name if hasattr(person['name'], 'name') else person['name']
    print(f"\n{person_name}'s itemized share:")

    for item_share in person["share"]:
        if item_share['share_value'] == 0:
            continue
        print(f"  - {item_share['item_name']}: ${item_share['share_value']:.2f}")

print(", ".join(get_unique_item_names(items)))

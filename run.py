from item import items
from main import get_unique_item_names, calculate_share

tax_rate = 15  # 15% tax rate
total_discount = 14.98  # total discount

total_value = sum(item["value"] for item in items)
print("total value", total_value)
discount_rate = total_discount * 100 / total_value  # calculate discount rate
print("discount rate", discount_rate)

shares = calculate_share(items, discount_rate, tax_rate)

print()
for person in shares:
    print(f"{person['name']}'s share: ${person['total_share']:.2f}")

for person in shares:
    print(f"\n{person['name']}'s share:")

    for item_share in person["share"]:
        if item_share['share_value'] == 0:
            continue
        print(f"  - {item_share['item_name']}: ${item_share['share_value']:.2f}")

print(", ".join(get_unique_item_names(items)))

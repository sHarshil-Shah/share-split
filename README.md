This program calculates individual shares for multiple items, considering discounts, taxes, and who participated in each item.

Features:

Calculates individual shares for each item and total share across all items.
Applies discounts proportionally to each person's share.
Accounts for taxes on specified taxable items.
Handles situations where not everyone participates in all items.
Usage:

Install dependencies (if any): No external libraries are required for this program.
Edit items list: This list defines each item with its name, value, taxable flag, and list of participants (using the PERSONS enum).
Set tax_rate and total_discount: These variables define the tax rate (percentage) and total discount amount.
Run the script: Execute the script to see the calculated individual shares and total tax amount.
Output:

Total value of all items.
Discount rate based on total discount and total value.
Individual's name and total share across all items.
Breakdown of each individual's share per item (excluding items with zero share).
List of unique item names.
Example:

The provided example calculates shares for five items with varying participants, discounts, and tax implications.

Note:

This program assumes equal splitting among participants for each item.
You can modify the logic within the calculate_share function to implement custom splitting rules (e.g., splitting based on quantity consumed).
Further Enhancements:

Ability to define custom splitting rules per item.
Support for different tax rates for various item categories.
Integration with a user interface for easier input and output.

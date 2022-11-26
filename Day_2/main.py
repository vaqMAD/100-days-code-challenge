
print("Welcome to the tip calculator !")


def calculate_order_value(value_of_order: float = float, percentege_of_tip: float = float, value_bill_per_person: int = int):
    """This function will calculate bill value based on : value of order, tip percentage, and amount of people

    Args:
        value_of_order (float): Value of order without tip. Defaults to float.
        percentege_of_tip (float): Tip percentage - based on value of order. Defaults to float.
        value_bill_per_person (int): How many people you want to split the bill. Defaults to int.

    Returns:
        Float : The total value of order after tip. Calculated by adding the tip percentage value, to the value of the order, and divided by amount of people to split bill with
    """
    value_of_order = float(
        input("What was the total value of bill ? "))
    percentege_of_tip = float(
        input("What percentege tip would you like to give ?")) / 100
    value_bill_per_person = int(
        input("How many people to split the bill ?"))

    total_value_after_tip = value_of_order + value_of_order * percentege_of_tip

    return total_value_after_tip / value_bill_per_person


result = calculate_order_value()

print(f"The value of the order should be : {result}")

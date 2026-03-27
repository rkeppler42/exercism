"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget: float, exchange_rate: float) -> float:
    """Calculate the value of the exchanged currency based on budget and exchange rate.

    :param budget: amount of money you are planning to exchange.
    :param exchange_rate: unit value of the foreign currency.
    :return: exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    """Calculate the change given the budget and the exchanging value.

    :param budget: amount of money you own.
    :param exchanging_value: amount of your money you want to exchange now.
    :return: amount left of your starting currency after exchanging.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """Calculate the total value of the bills the booth would give back.

    :param denomination: the value of a bill.
    :param number_of_bills: total number of bills.
    :return: calculated value of the bills.
    """
    return int(denomination * number_of_bills)


def get_number_of_bills(amount: float, denomination: int) -> int:
    """Calculate the number of whole bills that the person will receive.

    :param amount: the total starting value.
    :param denomination: the value of a single bill.
    :return: number of bills that can be obtained from the amount.
    """
    return amount // denomination


def get_leftover_of_bills(amount: float, denomination: int) -> float:
    """Calculate the leftover given the current denomination.

    :param amount: the total starting value.
    :param denomination: the value of a single bill.
    :return: the amount that is "leftover", given the current denomination.
    """
    return amount % denomination


def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int:
    """Calculate the maximum exchangeable value for the given budget and denomination.

    :param budget: the amount of your money you are planning to exchange.
    :param exchange_rate: the unit value of the foreign currency.
    :param spread: percentage that is taken as an exchange fee.
    :param denomination: the value of a single bill.
    :return: maximum value you can get.
    """
    real_exchange_rate = exchange_rate * (1 + spread / 100)
    exchanged_money = exchange_money(budget, real_exchange_rate)
    number_of_bills = get_number_of_bills(exchanged_money, denomination)
    return int(number_of_bills * denomination)

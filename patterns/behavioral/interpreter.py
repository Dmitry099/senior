# Interpreter pattern is useful to implement Domain Specific Language.
# It means that you create objects, which will be understandable
# for non-programmers to use.
# To do that you need:
# - develop a language/patterns which is useful for endusers
# - define representation of your grammar
# - implement interpreter for this representation in your programming language
from datetime import datetime


class Rule:
    def __init__(self, conditions, discounts):
        self.conditions = conditions
        self.discounts = discounts

    def evaluate(self, tab):
        if self.conditions.evaluate(tab):
            return self.discounts.calculate(tab)
        return 0


class Conditions:
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self, tab):
        return self.expression.evaluate(tab)


class And:
    def __init__(self, expression_1, expression_2):
        self.expression_1 = expression_1
        self.expression_2 = expression_2

    def evaluate(self, tab):
        return (self.expression_1.evaluate(tab)
                and self.expression_2.evaluate(tab))


class Or:
    def __init__(self, expression_1, expression_2):
        self.expression_1 = expression_1
        self.expression_2 = expression_2

    def evaluate(self, tab):
        return (self.expression_1.evaluate(tab)
                or self.expression_2.evaluate(tab))


class PercentageDiscount:
    def __init__(self, item_type, percentage):
        self.item_type = item_type
        self.percentage = percentage

    def calculate(self, tab):
        if self.item_type == 'any_item':
            f = lambda x: True
        else:
            f = lambda x: x.item_type == self.item_type
        return (sum([x.cost for x in tab.items if f(x)]) * self.percentage) / 100


class CheapestFree:
    def __init__(self, item_type):
        self.item_type = item_type

    def calculate(self, tab):
        try:
            min([x.cost for x in tab.items if x.item_type == self.item_type])
        except:
            return 0


class TodayIs:
    def __init__(self, day_of_week):
        self.day_of_week = day_of_week

    def evaluate(self, tab):
        return datetime.today().weekday() == self.day_of_week.name


class TimeIsBetween:
    def __init__(self, from_time, to_time):
        self.from_time = from_time
        self.to_time = to_time

    def evaluate(self, tab):
        hour_now = datetime.today().hour
        minute_now = datetime.today().minute
        from_hour, from_minute = [int(x) for x in self.from_time.split(':')]
        to_hour, to_minute = [int(x) for x in self.to_time.split(':')]
        hour_in_range = from_hour <= hour_now < to_hour
        begin_edge = hour_now == from_hour and minute_now > from_minute
        end_edge = hour_now == to_hour and minute_now < to_minute
        return any((hour_in_range, begin_edge, end_edge))


class TodayIsAWeekDay:
    def evaluate(self, tab):
        week_days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursay",
            "Friday"
        ]
        return datetime.today().weekday() in week_days


class TodayIsAWeekendDay:
    def evaluate(self, tab):
        weekend_days = [
            "Saturday",
            "Sunday"
        ]
        return datetime.today().weekday() in weekend_days


class DayOfTheWeek:
    def __init__(self, name):
        self.name = name


class ItemIsA:
    def __init__(self, item_type):
        self.item_type = item_type

    def evaluate(self, item):
        return self.item_type == item.item_type


class NumberOfItemsOfType:
    def __init__(self, number_of_items, item_type):
        self.number_of_items = number_of_items
        self.item_type = item_type

    def evaluate(self, tab):
        return len([x for x in tab.items if x.item_type
                    == self.item_type]) == self.number_of_items


class CustomerIsA:
    def __init__(self, customer_type):
        self.customer_type = customer_type

    def evaluate(self, tab):
        return tab.customer.customer_type == self.customer_type


class Tab:
    def __init__(self, customer):
        self.items = []
        self.discounts = []
        self.customer = customer

    def calculate_cost(self):
        return sum(x.cost for x in self.items)

    def calculate_discount(self):
        return sum(x for x in self.discounts)


class Item:
    def __init__(self, name, item_type, cost):
        self.name = name
        self.item_type = item_type
        self.cost = cost


class ItemType:
    def __init__(self, name):
        self.name = name


class Customer:
    def __init__(self, customer_type, name):
        self.customer_type = customer_type
        self.name = name


class CustomerType:
    def __init__(self, customer_type):
        self.customer_type = customer_type


member = CustomerType("Member")
pizza = ItemType("pizza")
burger = ItemType("burger")
drink = ItemType("drink")

monday = DayOfTheWeek("Monday")


def setup_demo_tab():
    member_customer = Customer(member, "John")
    tab = Tab(member_customer)
    for item_name, item_type, cost in [
        ("Margarita", pizza, 10),
        ("Cheddar Melt", burger, 6),
        ("Hawaian", pizza, 12),
        ("Latte", drink, 4),
        ("Club", pizza, 20)
    ]:
        tab.items.append(Item(item_name, item_type, cost))
    return tab


if __name__ == '__main__':
    tab = setup_demo_tab()
    rules = []

    # Members always get 15% off their total tab
    rules.append(
        Rule(
            CustomerIsA(member),
            PercentageDiscount("any_item", 15)
        )
    )

    # During happy hour, which happens from 17:00 to 19:00 weekdays,
    # all drinks are less 10%
    rules.append(
        Rule(
            And(TimeIsBetween("17:00", "19:00"), TodayIsAWeekDay()),
            PercentageDiscount("drink", 10)
        )
    )

    # Mondays are buy one get one free burger nights
    rules.append(
        Rule(
            And(TodayIs(monday), NumberOfItemsOfType(burger, 2)),
            CheapestFree(burger)
        )
    )

    for rule in rules:
        tab.discounts.append(rule.evaluate(tab))

    print(
        f"Calculated cost: {tab.calculate_cost()}\n"
        f"Calculated discount {tab.calculate_discount()}"
    )

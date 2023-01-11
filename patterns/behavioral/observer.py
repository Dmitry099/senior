class Task:
    def __init__(self, user, badge_type):
        self.observers = set()
        self.user = user
        self.badge_type = badge_type

    def register(self, observer):
        self.observers.add(observer)

    def unregister(self, observer):
        self.observers.discard(observer)

    def unregister_all(self):
        self.observers.clear()

    def update_all(self):
        for observer in self.observers:
            observer.update(self)


class User:
    def __init__(self, wallet):
        self.wallet = wallet
        self.badges = []
        self.experience = 0

    def add_badge(self, badge):
        self.badges.append(badge)

    def add_experience(self, amount):
        self.experience += amount

    def update(self, observed):
        self.add_experience(1)

    def __str__(self):
        badges = '\n'.join([str(x) for x in self.badges])
        return (f"Wallet\t{self.wallet}\nExperience\t{self.experience}\n"
                f"Badges:\n{badges}")


class Wallet:
    def __init__(self):
        self.amount = 0

    def increase_balance(self, amount):
        self.amount += amount

    def decrease_balance(self, amount):
        self.amount -= amount

    def update(self, observed):
        self.increase_balance(5)

    def __str__(self):
        return str(self.amount)


class Badge:
    def __init__(self, name, badge_type):
        self.name = name
        self.badge_type = badge_type
        self.points = 0
        self.awarded = False

    def add_points(self, amount):
        self.points += amount

        if self.points > 3:
            self.awarded = True

    def update(self, observed):
        if observed.badge_type == self.badge_type:
            self.add_points(2)

    def __str__(self):
        award_string = "Earned" if self.awarded else "Unearned"
        return f"{self.name}: {award_string} [{self.points}]"


def main():
    wallet = Wallet()
    user = User(wallet)

    badges = [
        Badge("Fun Badge", 1),
        Badge("Bravery Badge", 2),
        Badge("Missing Badge", 3),
    ]

    for badge in badges:
        user.add_badge(badge)

    tasks = [Task(user, 1), Task(user, 1), Task(user, 3)]

    for task in tasks:
        task.register(wallet)
        task.register(user)
        for badge in badges:
            task.register(badge)

    for task in tasks:
        task.update_all()

    print(user)


if __name__ == '__main__':
    main()
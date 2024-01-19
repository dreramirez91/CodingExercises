# https://www.codewars.com/kata/5941c545f5c394fef900000c/train/javascript


class Warrior:
    def __init__(self):
        self.experience = 100
        self.level = 1
        self.achievements = []
        self.rank_values = [
            "Pushover",
            "Novice",
            "Fighter",
            "Warrior",
            "Veteran",
            "Sage",
            "Elite",
            "Conqueror",
            "Champion",
            "Master",
            "Greatest",
        ]
        self.rank = self.rank_values[0]

    def increase_experience(self, amount):
        self.experience += amount
        if self.experience > 10000:
            self.level = 100
            self.experience = 10000
            self.rank = "Greatest"
        else:
            self.level = self.experience // 100
            self.rank = self.rank_values[self.level // 10]

    def training(self, training_instance):
        if self.level >= training_instance[2]:
            self.achievements.append(training_instance[0])
            self.increase_experience(training_instance[1])
            return training_instance[0]
        else:
            return "Not strong enough"

    def battle(self, enemy_level):
        if not 1 <= enemy_level <= 100:
            return "Invalid level"
        diff = enemy_level - self.level
        enemy_rank = self.rank_values[enemy_level // 10]
        if enemy_level == self.level:
            self.increase_experience(10)
            return "A good fight"
        elif (
            diff >= 5
            and self.rank_values.index(enemy_rank) - self.rank_values.index(self.rank)
            >= 1
        ):
            return "You've been defeated"
        elif diff >= 1:
            self.increase_experience(20 * (pow(diff, 2)))
            return "An intense fight"
        elif diff == -1:
            self.increase_experience(5)
            return "A good fight"
        elif diff <= -2:
            return "Easy fight"

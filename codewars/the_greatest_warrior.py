# https://www.codewars.com/kata/5941c545f5c394fef900000c/train/javascript


class Warrior:
    def __init__(self):
        self.warrior_experience = 100  # every 100 xp, level up
        self.warrior_level = 1
        self.warrior_achievements = []
        self.rank_values = [  # every 10 levels, rank up
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
        self.warrior_rank = self.rank_values[0]

    def rank(self):
        return self.warrior_rank

    def level(self):
        return self.warrior_level

    def experience(self):
        return self.warrior_experience

    def achievements(self):
        return self.warrior_achievements

    def increase_experience(self, amount):
        self.warrior_experience += amount
        if self.warrior_experience > 10000:
            self.warrior_level = 100
            self.warrior_experience = 10000
            self.warrior_rank = "Greatest"
        else:
            self.warrior_level = self.warrior_experience // 100
            self.warrior_rank = self.rank_values[self.level() // 10]

    def training(self, training_instance):
        if self.warrior_level >= training_instance[2]:
            self.warrior_achievements.append(training_instance[0])
            self.increase_experience(training_instance[1])
            return training_instance[0]
        else:
            return "Not strong enough"

    def battle(self, enemy_level):
        if not 1 <= enemy_level <= 100:
            return "Invalid level"
        enemy_rank = self.rank_values[enemy_level // 10]
        if enemy_level == self.warrior_level:
            self.increase_experience(10)
            return "A good fight"
        elif (
            enemy_level - self.warrior_level >= 5
            and self.rank_values.index(enemy_rank)
            - self.rank_values.index(self.warrior_rank)
            >= 1
        ):
            return "You've been defeated"
        elif enemy_level - self.warrior_level >= 1:
            self.increase_experience(20 * (pow(enemy_level - self.warrior_level, 2)))
            if enemy_level - self.warrior_level == 1:
                return "A good fight"
            else:
                return "An intense fight"
        elif enemy_level - self.warrior_level == -1:
            self.increase_experience(5)
            return "Easy fight"
        elif enemy_level - self.warrior_level <= -2:
            return "Easy fight"


Dre = Warrior()
Dre.training(
    ["Defeated Chuck Norris", 8800, 1]
)  # Why does printing this "call it twice?"
print(Dre.achievements())
print(Dre.experience())
print(Dre.rank())
Dre.battle(93)
print(Dre.experience())

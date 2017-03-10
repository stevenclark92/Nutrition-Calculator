class user(object):

    """Quick and dirty calculator to find base metabolic rate & recommended calorie intake based on weight goal"""

    def __init__(self, name, age, weight, height, chromosomes, goal, activity, diet):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.chromosomes = chromosomes
        self.goal = goal
        self.activity = activity
        self.diet = diet

        if chromosomes == 'XY':
            self.biology = xy_biology
        elif chromosomes == 'XX':
            self.biology = xx_biology
        else:
            raise Exception('Invalid chromosomes')

    def base_metabolic_rate(self):
        return self.biology.base_metabolic_rate(self)

    def maintenance_calories(self):
        if self.activity == 'Sedentry':
            return self.base_metabolic_rate() * 1.2
        elif self.activity == 'Light':
            return self.base_metabolic_rate() * 1.375
        elif self.activity == 'Moderate':
            return self.base_metabolic_rate() * 1.55
        elif self.activity == 'Active':
            return self.base_metabolic_rate() * 1.725
        elif self.activity == 'Extreme':
            return self.base_metabolic_rate() * 1.9

    def calorie_intake(self):
        if self.goal == "Gain":
            return self.maintenance_calories() + 500
        elif self.goal == "Lose":
            return self.maintenance_calories() - 200
        elif self.goal == "Maintain":
            return self.maintenance_calories()
        else:
            raise Exception('Goal not specified')

    def body_mass_index(self):
        return float(self.weight) / (self.height ** 2) + 0.00005

    def macronutrient_split(self):
        protein = 0
        carbohydrate = 0
        fat = 0

        if self.diet == "Keto":
            protein = (self.calorie_intake() / 2)
            fat = (self.calorie_intake()/2)
        else:
            protein = (self.calorie_intake() * 0.35)
            carbohydrate = (self.calorie_intake() * 0.35)
            fat = (self.calorie_intake() * 0.3)
        return (int(protein), int(carbohydrate), int(fat))

class biology(object):

    """Biology class for metabolism calculations"""

    def __init__(self, base_rate, weight_multiplier, height_multiplier, age_multiplier):
        self.base_rate = base_rate
        self.weight_multiplier = weight_multiplier
        self.height_multiplier = height_multiplier
        self.age_multiplier = age_multiplier

    def base_metabolic_rate(self, user):
        weight_part = self.weight_multiplier * user.weight
        height_part = self.height_multiplier * user.height
        age_part = self.age_multiplier * user.age
        return self.base_rate + weight_part + height_part - age_part

"""Declare the different types of biology"""

xy_biology = biology(66.47, 13.75, 5.0, 6.75)
xx_biology = biology(665.09, 9.56, 1.84, 4.67)

# Biology option changed to accept chromosomes at birth - 'XX' for female at birth, 'XY' for male at birth.
# All units are SI, sorry Americans.
# Weight goals must be 'Gain', 'Lose', or 'Maintain'
# Activity Level can be 'Sedentry', 'Light', 'Moderate', 'Active' or 'Extreme'
# Macros currently supports Keto, any other string returns standard values

user_a = user('test', 22, 79, 172, 'XY', 'Maintain', 'Light', "No Special Requirement")

print(int(user_a.base_metabolic_rate()))
print(int(user_a.maintenance_calories()))
print(int(user_a.calorie_intake()))
print(int(user_a.body_mass_index()*10000))
print(user_a.macronutrient_split())

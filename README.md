# Nutrition Calculator

This is a really simple nutrition calculator built in Python made with the sole purpose of getting myself comfortable working with classes.

The following inputs are required:
* Name (string)
* Age (integer)
* Weight (integer, kg)
* Height (integer, cm)
* Sex Chromosomes (string, either XX or XY. Other cases ignored.)
* Weight Goal (string, either Gain, Maintain or Lose)
* Activity Level (string, either Sedentry, Light, Moderate, Active or Extreme)
* Dietary Requirement (string, currently only supports Keto for ketogenic diets)

The calculator takes this data and prints:
* Base Metabolic Rate (no activity)
* Maintenance Calorie Requirement (based on activity level)
* Recommended Calorie Intake (based on weight goal)
* Body Mass Index
* Recommended calorie intake from each macronutrient
  * Protein (35% of intake by default, 50% for Keto)
  * Carbohydrate (35% of intake by default, 0 for Keto)
  * Fat (30% of intake by default, 50% for Keto)

That's all there is to it for now.

##TODO

Fixes & Improvements:

* Improve user management
* Refactor & streamline
* Ensure daily protein intake doesn't fall below 1.5g/kg for users with a weight goal of Gain
* Research nutritional values used to ensure they are correct

_I am not a nutritionist, I'd recommend using trusted resources and modifying this to your own needs if you plan on actually using it_
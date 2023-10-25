
import csv, datetime

class ProfileData:
    def __init__(self, profile_name):

        # Populate Primary Data Fields (data is in imperial units -- metric is used within formulas, and these conversions take place within functions)
        self.profile_name = profile_name
        self.current_weight = 0
        self.goal_weight = 0
        self.age = 0
        self.activity_level = 0
        self.activity_level_multiplier = 0
        self.height_ = 0
        self.gender = None
        self.bmr = 0
        self.today_date = datetime.date.today().strftime("%m/%d/%Y")
        self.build_from_profile()

    def build_from_profile(self):
        with open("profiles.csv", 'r', newline='') as profile:
            csv_reader = csv.reader(profile)

            for row in csv_reader:
                if row[0] == self.profile_name:
                    self.current_weight = int(row[1])
                    self.goal_weight = int(row[2])
                    self.age = int(row[3])
                    self.activity_level = int(row[4])
                    self.height_ = int(row[5])
                    self.gender = row[6]
                    break

            current_weight_kg = self.current_weight * 0.45359237
            height_cm = self.height_ * 2.54

            self.bmr = self.calc_bmr(current_weight_kg, height_cm)
            
            self.activity_level_multiplier = self.generate_activity_level_multiplier()
            
    def calc_bmr(self, weight, height):
        # Requires kg and cm measurements
        if self.gender == "m":
            return ((10 * weight) + (6.25 * height) - (5 * self.age) + 5)
        else:
            return ((10 * weight) + (6.25 * height) - (5 * self.age) - 161)
        
    def generate_activity_level_multiplier(self):

        if self.activity_level == 1: return 1.375
        elif self.activity_level == 2: return 1.55
        elif self.activity_level == 3: return 1.725
        elif self.activity_level == 4: return 1.9
        else: return 1.2

    def calc_tdee(self):
        return int(self.bmr * self.activity_level_multiplier)
    
    def calc_target_cals(self):
        if self.current_weight < self.goal_weight:
            return self.calc_tdee() + 300
        elif self.current_weight > self.goal_weight:
            return self.calc_tdee() - 300
        else:
            return self.calc_tdee()
    
    def calc_target_protein(self):
        return (self.calc_tdee() * 0.25) // 4
    
    def calc_target_carbs(self):
        return (self.calc_tdee() * 0.45) // 4

    def calc_target_fat(self):
        return (self.calc_tdee() * 0.25) // 9        

    def calc_target_vitmain_A(self):
        # Source: https://ods.od.nih.gov/factsheets/VitaminA-HealthProfessional/
        # Returns mcg dose
        
        if self.age < 4: return 300
        elif self.age < 9: return 400
        elif self.age < 14: return 600
        else:
            if self.gender == "m": return 900
            else: return 700

    def calc_target_vitmain_C(self):
        # Source: https://ods.od.nih.gov/factsheets/VitaminC-HealthProfessional/
        # Returns mg dose

        if self.age < 4: return 15
        elif self.age < 9: return 25
        elif self.age < 14: return 45
        elif self.age < 19:
            if self.gender == "m": return 75
            else: return 65
        else:
            if self.gender == "m": return 90
            else: return 75

    def calc_target_vitamin_D(self):
        # Source: https://ods.od.nih.gov/factsheets/VitaminD-HealthProfessional/
        # Returns mcg dose

        if self.age < 70: return 15
        else: return 20

    def calc_target_vitamin_B6(self):
        # Source: https://ods.od.nih.gov/factsheets/VitaminB6-HealthProfessional/
        # Returns dose in mg

        if self.age < 4: return 0.5
        elif self.age < 9: return 0.6
        elif self.age < 14: return 1.0
        elif self.age < 19:
            if self.gender == "m": return 1.3
            else: return 1.2
        elif self.age < 51: return 1.3
        else: 
            if self.gender == "m": return 1.7
            else: return 1.5

    def calc_target_vitmain_E(self):
        # Source: https://ods.od.nih.gov/factsheets/VitaminE-HealthProfessional/
        # Returns dose in mg

        if self.age < 4: return 6
        elif self.age < 9: return 7
        elif self.age < 14: return 11
        else: return 15

    def calc_target_vitmain_K(self):
        # Source: https://ods.od.nih.gov/factsheets/VitaminK-HealthProfessional/
        # Returns dose in mcg

        if self.age < 4: return 30
        elif self.age < 9: return 55
        elif self.age < 14: return 60
        elif self.age < 19: return 75
        else:
            if self.gender == "m": return 120
            else: return 90

    def calc_target_vitamin_thiamin(self):
        # Source: https://ods.od.nih.gov/factsheets/Thiamin-HealthProfessional/
        # Returns measurement in mg

        if self.age < 4: return 0.5
        elif self.age < 9: return 0.6
        elif self.age < 14: return 0.9
        elif self.age < 19:
            if self.gender == "m": return 1.2
            else: return 1.0
        else:
            if self.gender == "m": return 1.2
            else: return 1.1

    def calc_target_vitmain_B12(self):
        # Source: https://ods.od.nih.gov/factsheets/VitaminB12-HealthProfessional/
        # Returns dose in mcg

        if self.age < 4: return 0.9
        elif self.age < 9: return 1.2
        elif self.age < 14: return 1.8
        else: return 2.4

    def calc_target_vitamin_riboflavin(self):
        # Source: https://ods.od.nih.gov/factsheets/Riboflavin-HealthProfessional/
        # Returns dose in mg

        if self.age < 4: return 0.5
        elif self.age < 9: return 0.6
        elif self.age < 14: return 0.9
        elif self.age < 19:
            if self.gender == "m": return 1.3
            else: return 1.0
        else:
            if self.gender == "m": return 1.3
            else: return 1.1
        
    def calc_target_vitmain_folate(self):
        # https://ods.od.nih.gov/factsheets/Folate-HealthProfessional/
        # Returns dose in mcg DFE

        if self.age < 4: return 150
        elif self.age < 9: return 200
        elif self.age < 14: return 300
        else: return 400

    def calc_target_vitamin_niacin(self):
        # Source: https://ods.od.nih.gov/factsheets/Niacin-HealthProfessional/
        # Returns dose in mg NE

        if self.age < 4: return 6
        elif self.age < 9: return 8
        elif self.age < 14: return 12
        else:
            if self.gender == "m": return 16
            else: return 14

    def calc_target_vitamin_choline(self):
        # Source: https://ods.od.nih.gov/factsheets/Choline-HealthProfessional/
        # Returns dose in mg

        if self.age < 4: return 200
        elif self.age < 9: return 250
        elif self.age < 14: return 375
        elif self.age < 19:
            if self.gender == "m": return 550
            else: return 400
        else:
            if self.gender == "m": return 550
            else: return 425
            
    def calc_target_vitamin_pantothenic_acid(self):
        # Source: https://ods.od.nih.gov/factsheets/PantothenicAcid-HealthProfessional/
        # Returns dose in mg

        if self.age < 4: return 2
        elif self.age < 9: return 3
        elif self.age < 14: return 4
        else: return 5

    def calc_target_vitamin_biotin(self):
        # Source: https://ods.od.nih.gov/factsheets/Biotin-HealthProfessional/
        # Returns dose in mcg

        if self.age < 4: return 8
        elif self.age < 9: return 12
        elif self.age < 14: return 20
        elif self.age < 19: return 25
        else: return 30

    def calc_target_vitamin_carotenoids(self):
        # Source: https://ods.od.nih.gov/factsheets/VitaminA-HealthProfessional/
        # Returns dose in mcg RAE

        if self.age < 4: return 300
        elif self.age < 9: return 400
        elif self.age < 14: return 600
        else:
            if self.gender == "m": return 900
            else: return 700

    def calc_target_mineral_calcium(self):
        # Source: https://ods.od.nih.gov/factsheets/Calcium-HealthProfessional/
        # Returns dose in mg

        if self.age < 4: return 400
        elif self.age < 9: return 1000
        elif self.age < 19: return 1300
        elif self.age < 51: return 1000
        elif self.age < 70:
            if self.gender == "m": return 1000
            else: return 1200
        else: return 1200

    def calc_target_mineral_chloride(self):
        # Source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7009052/ (Table 03)
        # Returns dose in g

        if self.age < 4: return 1.7
        elif self.age < 7: return 2.0
        elif self.age < 11: return 2.6
        else: return 3.1 

    def calc_target_mineral_chromium(self):
        # Source: https://ods.od.nih.gov/factsheets/Chromium-HealthProfessional/
        # Returns dose in mcg

        if self.age < 4: return 11
        elif self.age < 9: return 15
        elif self.age < 14:
            if self.gender == "m": return 25
            else: return 21
        elif self.age < 19:
            if self.gender == "m": return 35
            else: return 24
        elif self.age < 51:
            if self.gender == "m": return 35
            else: return 25
        else: 
            if self.gender == "m": return 30
            else: return 20

    def calc_target_mineral_copper(self):
        # Source: https://ods.od.nih.gov/factsheets/Copper-HealthProfessional/
        # Returns dose in mcg

        if self.age < 4: return 340
        elif self.age < 9: return 440
        elif self.age < 14: return 700
        elif self.age < 19: return 890
        else: return 900

    def calc_target_mineral_fluoride(self):
        # Source: https://ods.od.nih.gov/factsheets/Fluoride-HealthProfessional/
        # Returns dose in mg

        if self.age < 4: return 0.7
        elif self.age < 9: return 1
        elif self.age < 14: return 2
        elif self.age < 19: return 3
        else: 
            if self.gender == "m":
                return 4
            else:
                return 3

    def calc_target_mineral_iodine(self):
        # Source: https://ods.od.nih.gov/factsheets/Iodine-HealthProfessional/
        # Returns dose in mcg

        if self.age < 9: return 90
        elif self.age < 14: return 120
        else: return 150

    def calc_target_mineral_iron(self):
        # Source: https://ods.od.nih.gov/factsheets/Iron-HealthProfessional/
        # Returns dose in mg

        if self.age < 4: return 7
        elif self.age < 9: return 10
        elif self.age < 14:
            if self.gender == "m": return 11
            else: return 15
        elif self.age < 51:
            if self.gender == "m": return 8
            else: return 18
        else: return 8
    
    def calc_target_mineral_magnesium(self):
        # Source: https://ods.od.nih.gov/factsheets/Magnesium-HealthProfessional/
        # Returns value in mg

        if self.age < 4: return 80
        elif self.age < 9: return 130
        elif self.age < 14: return 240
        elif self.age < 19: 
            if self.gender == "m": return 410
            else: return 360
        elif self.age < 31: 
            if self.gender == "m": return 400
            else: return 310
        else:
            if self.gender == "m": return 420
            else: return 320

    def calc_target_mineral_manganese(self):
        # Source: https://ods.od.nih.gov/factsheets/Manganese-HealthProfessional/
        # Returns dose in mg

        if self.age < 4: return 1.2
        elif self.age < 9: return 1.5
        elif self.age < 14: 
            if self.gender == "m": return 1.9
            else: return 1.6
        elif self.age < 19: 
            if self.gender == "m": return 2.2
            else: return 1.6
        else: 
            if self.gender == "m": return 2.3
            else: return 1.8

    def calc_target_mineral_molybdenum(self):
        # Source: https://ods.od.nih.gov/factsheets/Molybdenum-HealthProfessional/
        # Returns dose in mcg

        if self.age < 4: return 17
        elif self.age < 9: return 22
        elif self.age < 14: return 34
        elif self.age < 19: return 43
        else: return 45 

    def calc_target_mineral_phosphorous(self):
        # Source: https://ods.od.nih.gov/factsheets/Phosphorus-HealthProfessional/
        # Returns dose in mg

        if self.age < 4: return 460
        elif self.age < 9: return 500
        elif self.age < 19: return 1250
        else: return 700 

    def calc_target_mineral_potassium(self):
        # Source: https://ods.od.nih.gov/factsheets/Potassium-HealthProfessional/
        # Returns dose in g

        if self.age < 4: return 2
        elif self.age < 9: return 2.3
        elif self.age < 14: 
            if self.gender == "m": return 2.5
            else: return 2.3
        elif self.age < 19: 
            if self.gender == "m": return 3
            else: return 2.3
        else: 
            if self.gender == "m": return 3.4
            else: return 2.6

    def calc_target_mineral_selenium(self):
        # Source: https://ods.od.nih.gov/factsheets/Selenium-HealthProfessional/
        # Returns dose in mcg

        if self.age < 4: return 20
        elif self.age < 9: return 30
        elif self.age < 14: return 40
        else: return 55

    def calc_target_mineral_sodium(self):
        # Source: fda.gov
        # Returns dose in mg

        return 2300
    
    def calc_target_mineral_zinc(self):
        # Source: https://ods.od.nih.gov/factsheets/Zinc-HealthProfessional/
        # Returns dose in mg

        if self.age < 4: return 3
        elif self.age < 9: return 5
        elif self.age < 14: return 8 
        elif self.age < 19: 
            if self.gender == "m": return 11
            else: return 9
        else:
            if self.gender == "m": return 11
            else: return 8




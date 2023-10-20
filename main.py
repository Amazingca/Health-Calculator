import csv
def main():
    print("Health Logger | 0.1")
    emptyData = False
    with open("data.csv", "r", newline="") as csvfile:
        filereader = csv.reader(csvfile, delimiter=" ", quotechar=",")
        lines = 0
        for line in filereader:
            lines += 1
        if lines == 0:
            emptyData = True

    if emptyData == True:
        with open("data.csv", "a", newline="") as csvfile:
            print("\nTo begin, please enter some information so we can get a better understanding of you:")
            age = int(input("What is your age? "))
            height = input("What is your height? (ft in) ")
            heightCm = 0
            if " " in height:
                heightFt = int(height.split(" ")[0])
                heightIn = int(height.split(" ")[1])
                heightCm = ((heightFt * 12) + heightIn) * 2.54
            weight = int(input("What is your weight (in pounds)? ")) * 0.453592
            gender = input("What is your gender? ")
            activity = input("What is your activity rate? (none, little, medium, high, heavy) ")
            while ("none" != activity) and ("little" != activity) and ("medium" != activity) and ("high" != activity) and ("heavy" != activity):
                activity = input("What is your activity rate? (none, little, medium, high, heavy) ")
            filewriter = csv.writer(csvfile, delimiter=",", quotechar=",")
            filewriter.writerow([age, heightCm, weight, gender, activity])
    else:
        print("You've added your health data!")
            
if __name__ == "__main__":
    main()
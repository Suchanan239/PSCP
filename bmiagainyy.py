"""BMIAgain"""
def main():
    """BMIAgain"""
    weight = int(input())
    height = int(input())
    bmi = float(weight/((height/100)**2))
    if bmi < 18.5:
        print("Underweight")
    if bmi >= 18.5 and bmi < 25:
        print("Normal")
    if bmi >= 25 and bmi < 30:
        print("Overweight")
    if bmi >= 30:
        print("Obese")
main()

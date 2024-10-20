def bmi(weight, height):
    message = ""
    bmi = weight / (height ** 2)
    if bmi <= 18.5:
        message = "Underweight"
    elif bmi <= 25.0:
        message = "Normal"
    elif bmi <= 30.0:
        message = "Overweight"
    else:
        message = "Obese"
    return message
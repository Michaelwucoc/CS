def convert_score_to_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


# Ask user to input number score
while True:
    score = int(input("Enter the number score: "))

    if score > 100 or score < 0:
        print("Error: The score should be between 0 and 100.")
        if score == -100:
            print("You have quit the program.")
            break
    else:
        grade = convert_score_to_grade(score)
        print(print("The letter grade for", score, "is:", grade))

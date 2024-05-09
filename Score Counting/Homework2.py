count = 0
sum = 0
avg = 0
score_list = []


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


while True:
    score = int(input("Enter the number score: "))

    if score > 100 or score < 0:
        print("Error: The score should be between 0 and 100.")
        if score == -100:
            print("You have quit the program.")
            break
    else:
        grade = convert_score_to_grade(score)
        count += 1
        score_list.append(score)
        sum += score
        score_list.sort()
        avg = (sum - min(score_list) - max(score_list)) / (count - 2) if count > 2 else sum / count

        print("The letter grade for", score, "is:", grade, "counted:", count, "current sum:", sum,
              "current avg: {:.2f}".format(avg))
def admission_decision():
    try:
        entrance_score = float(input("Enter entrance score (0-100): "))
        gpa = float(input("Enter GPA (0-10): "))
        has_recommendation = input("Recommendation letter (yes/no): ").lower()
        category = input("Category (general/obc/sc_st): ").lower()
        extracurricular_score = float(input("Extracurricular score (0-10): "))
    except:
        print("Invalid input format.")
        return

    # Input validation
    if entrance_score < 0 or entrance_score > 100:
        print("Invalid entrance score. Must be between 0 and 100.")
        return

    if gpa < 0 or gpa > 10:
        print("Invalid GPA. Must be between 0 and 10.")
        return

    if extracurricular_score < 0 or extracurricular_score > 10:
        print("Invalid extracurricular score. Must be between 0 and 10.")
        return

    if has_recommendation not in ["yes", "no"]:
        print("Invalid recommendation input. Use 'yes' or 'no'.")
        return

    if category not in ["general", "obc", "sc_st"]:
        print("Invalid category. Use general/obc/sc_st.")
        return

    # Merit Rule
    if entrance_score >= 95:
        print("ADMITTED (Scholarship)")
        return

    # Minimum entrance score by category
    if category == "general":
        min_score = 75
    elif category == "obc":
        min_score = 65
    else:
        min_score = 55

    # GPA requirement
    if gpa < 7.0:
        print("REJECTED (GPA below minimum requirement)")
        return

    # Entrance cutoff check
    if entrance_score < min_score:
        print("REJECTED (Entrance score below category cutoff)")
        return

    # Bonus points
    bonus = 0

    if has_recommendation == "yes":
        bonus += 5

    if extracurricular_score > 8:
        bonus += 3

    final_score = entrance_score + bonus

    # Final decision
    if final_score >= 90:
        print("ADMITTED (Scholarship)")
    elif final_score >= min_score:
        print("ADMITTED (Regular)")
    else:
        print("WAITLISTED")


# Run program
admission_decision()

def calculate_grade(score, best_score):
    if score >= best_score - 10:
        return "A"
    elif score >= best_score - 20:
        return "B"
    elif score >= best_score - 30:
        return "C"
    elif score >= best_score - 40:
        return "D"
    else:
        return "F"

def calculate_statistics(scores):
    best_score = max(scores)
    total_score = sum(scores)
    average_score = total_score / len(scores)
    return best_score, average_score

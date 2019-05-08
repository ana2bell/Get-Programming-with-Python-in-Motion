def normalize_to_100(score, out_of):
    """
    score: integer representing a score
    out_of: integer representing what score is out of
    Returns normalized score so that it is out of 100
    """
    return score*100/out_of
    
def pass_or_fail(score, out_of):
    """
    score: integer representing a score
    out_of_integer representing what score is out of
    Returns "pass" or "fail", depending on the normalized score
    """
    if normalize_to_100(score, out_of) > 50:
        return "pass"
    else:
        return "fail"
    
def grade(student_scores, out_of, f):
    """
    student_scores: tuple of students, where each student is
                    represented by another tuple (name, score)
    out_of: integer representing what scores are out of
    f: which function to apply to the student scores
    Applies f to the student scores and prints out the information.
    """
    for i in student_scores:
        print(i[0], ":", f(i[1], out_of))
        
scores = (("Alice", 7.5), ("Bob", 8), ("Carrie", 4.8))
grade(scores, 10, pass_or_fail)

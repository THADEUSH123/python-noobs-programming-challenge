

def best(score, names):
    """Caculate overlap of two rectangles."""
    top_score_name = ""
    for name in names:
        if score(top_score_name) < score(name):
            top_score_name = name

    return top_score_name + " has the longest name."

def len_score(n):
    """Return the longest name."""
    return len(n)


names = ["Ben", "April", "Zaber", "Alexis", "McJagger"]

print(best(len_score, names))

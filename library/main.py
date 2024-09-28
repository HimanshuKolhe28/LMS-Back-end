# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import Levenshtein

name1 = "Mayur R"
name2 = "Mayur R Fegde"
def match_names(name1, name2):
    distance = Levenshtein.distance(name1.upper(), name2.upper())
    max_length = max(len(name1), len(name2))
    similarity_ratio = 1 - (distance / max_length)
    print("similarity_ratio", similarity_ratio)
    if similarity_ratio >= 0.8:
        return True
    else:
        return False
        

print(match_names(name1, name2))

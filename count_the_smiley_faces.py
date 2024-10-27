import re
def count_smileys(arr):
    smiley_pattern = r'[:;][-~]?[)D]'
    return sum(1 for smiley in arr if re.match(smiley_pattern,smiley))
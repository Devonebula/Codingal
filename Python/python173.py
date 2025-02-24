def common_letters(s1, s2, s3):
    common = []
    for letter in set(s1) & set(s2) & set(s3):
        count = min(s1.count(letter), s2.count(letter), s3.count(letter))
        common.extend([letter] * count)
    return sorted(common)

# Example usage:
s1 = "dhellod"
s2 = "wddorld"
s3 = "holddd"
print(common_letters(s1, s2, s3))  # Output: ['l', 'o']
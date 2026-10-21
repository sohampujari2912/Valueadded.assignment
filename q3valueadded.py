#Check if Two Numbers Are Anagrams
def anagram(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))
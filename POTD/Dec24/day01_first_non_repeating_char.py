
#  Non Repeating Character
#  Given a string s consisting of lowercase Latin Letters. Return the first non-repeating character in s. 
# If there is no non-repeating character, return '$'.
#  Note: When you return '$' driver code will output -1.

#  Examples:

#  Input: s = "geeksforgeeks"
#  Output: 'f'
#  Explanation: In the given string, 'f' is the first character in the string which does not repeat.
#  Input: s = "racecar"
#  Output: 'e'
#  Explanation: In the given string, 'e' is the only character in the string which does not repeat.
#  Input: s = "aabbccc"
#  Output: -1
#  Explanation: All the characters in the given string are repeating.
#  Constraints:
#  1 <= s.size() <= 10^5


def non_repeating_char_hash(s: str) -> str:
    char_count = {}
    for ch in s:
        char_count[ch] = char_count.get(ch, 0) + 1
    for ch in s:
        if char_count[ch] == 1:
            return ch
    return '$'


print(non_repeating_char_hash("geeksforgeeks"))  
# Dry Run: 
# Input string: "geeksforgeeks"
# Step 1: Initialize char_count = {}
# Step 2: Count characters:
#   'g' -> char_count = {'g': 1}
#   'e' -> char_count = {'g': 1, 'e': 1}
#   'e' -> char_count = {'g': 1, 'e': 2}
#   'k' -> char_count = {'g': 1, 'e': 2, 'k': 1}
#   's' -> char_count = {'g': 1, 'e': 2, 'k': 1, 's': 1}
#   'f' -> char_count = {'g': 1, 'e': 2, 'k': 1, 's': 1, 'f': 1}
#   'o' -> char_count = {'g': 1, 'e': 2, 'k': 1, 's': 1, 'f': 1, 'o': 1}
#   'r' -> char_count = {'g': 1, 'e': 2, 'k': 1, 's': 1, 'f': 1, 'o': 1, 'r': 1}
#   'g' -> char_count = {'g': 2, 'e': 2, 'k': 1, 's': 1, 'f': 1, 'o': 1, 'r': 1}
#   'e' -> char_count = {'g': 2, 'e': 3, 'k': 1, 's': 1, 'f': 1, 'o': 1, 'r': 1}
#   'e' -> char_count = {'g': 2, 'e': 4, 'k': 1, 's': 1, 'f': 1, 'o': 1, 'r': 1}
#   'k' -> char_count = {'g': 2, 'e': 4, 'k': 2, 's': 1, 'f': 1, 'o': 1, 'r': 1}
#   's' -> char_count = {'g': 2, 'e': 4, 'k': 2, 's': 2, 'f': 1, 'o': 1, 'r': 1}
# Step 3: Find first non-repeating character:
#   'g' -> count = 2 (repeating)
#   'e' -> count = 4 (repeating)
#   'k' -> count = 2 (repeating)
#   's' -> count = 2 (repeating)
#   'f' -> count = 1 (non-repeating) -> return 'f'

print(non_repeating_char_hash("racecar"))  
# Dry Run: 
# Input string: "racecar"
# Step 1: Initialize char_count = {}
# Step 2: Count characters:
#   'r' -> char_count = {'r': 1}
#   'a' -> char_count = {'r': 1, 'a': 1}
#   'c' -> char_count = {'r': 1, 'a': 1, 'c': 1}
#   'e' -> char_count = {'r': 1, 'a': 1, 'c': 1, 'e': 1}
#   'c' -> char_count = {'r': 1, 'a': 1, 'c': 2, 'e': 1}
#   'a' -> char_count = {'r': 1, 'a': 2, 'c': 2, 'e': 1}
#   'r' -> char_count = {'r': 2, 'a': 2, 'c': 2, 'e': 1}
# Step 3: Find first non-repeating character:
#   'r' -> count = 2 (repeating)
#   'a' -> count = 2 (repeating)
#   'c' -> count = 2 (repeating)
#   'e' -> count = 1 (non-repeating) -> return 'e'

print(non_repeating_char_hash("aabbccc"))  
# Dry Run: 
# Input string: "aabbccc"
# Step 1: Initialize char_count = {}
# Step 2: Count characters:
#   'a' -> char_count = {'a': 1}
#   'a' -> char_count = {'a': 2}
#   'b' -> char_count = {'a': 2, 'b': 1}
#   'b' -> char_count = {'a': 2, 'b': 2}
#   'c' -> char_count = {'a': 2, 'b': 2, 'c': 1}
#   'c' -> char_count = {'a': 2, 'b': 2, 'c': 2}
#   'c' -> char_count = {'a': 2, 'b': 2, 'c': 3}
# Step 3: Find first non-repeating character:
#   'a' -> count = 2 (repeating)
#   'b' -> count = 2 (repeating)
#   'c' -> count = 3 (repeating)
# No non-repeating character found -> return '$'


def non_repeating_char(s: str) -> str:
    freq = [0] * 26
    for ch in s:
        freq[ord(ch) - ord('a')] += 1
    for ch in s:
        if freq[ord(ch) - ord('a')] == 1:
            return ch
    return '$'



print(non_repeating_char("geeksforgeeks"))  
# Dry Run: 
# Input string: "geeksforgeeks"
# Step 1: Initialize freq = [0] * 26
# Step 2: Count characters:
#   'g' -> freq[ord('g') - ord('a')] += 1 -> freq[6] = 1
#   'e' -> freq[ord('e') - ord('a')] += 1 -> freq[4] = 1
#   'e' -> freq[ord('e') - ord('a')] += 1 -> freq[4] = 2
#   'k' -> freq[ord('k') - ord('a')] += 1 -> freq[10] = 1
#   's' -> freq[ord('s') - ord('a')] += 1 -> freq[18] = 1
#   'f' -> freq[ord('f') - ord('a')] += 1 -> freq[5] = 1
#   'o' -> freq[ord('o') - ord('a')] += 1 -> freq[14] = 1
#   'r' -> freq[ord('r') - ord('a')] += 1 -> freq[17] = 1
#   'g' -> freq[ord('g') - ord('a')] += 1 -> freq[6] = 2
#   'e' -> freq[ord('e') - ord('a')] += 1 -> freq[4] = 3
#   'e' -> freq[ord('e') - ord('a')] += 1 -> freq[4] = 4
#   'k' -> freq[ord('k') - ord('a')] += 1 -> freq[10] = 2
#   's' -> freq[ord('s') - ord('a')] += 1 -> freq[18] = 2
# Step 3: Find first non-repeating character:
#   'g' -> freq[ord('g') - ord('a')] = 2 (repeating)
#   'e' -> freq[ord('e') - ord('a')] = 4 (repeating)
#   'k' -> freq[ord('k') - ord('a')] = 2 (repeating)
#   's' -> freq[ord('s') - ord('a')] = 2 (repeating)
#   'f' -> freq[ord('f') - ord('a')] = 1 (non-repeating) -> return 'f'

print(non_repeating_char("racecar"))  
# Dry Run: 
# Input string: "racecar"
# Step 1: Initialize freq = [0] * 26
# Step 2: Count characters:
#   'r' -> freq[ord('r') - ord('a')] += 1 -> freq[17] = 1
#   'a' -> freq[ord('a') - ord('a')] += 1 -> freq[0] = 1
#   'c' -> freq[ord('c') - ord('a')] += 1 -> freq[2] = 1
#   'e' -> freq[ord('e') - ord('a')] += 1 -> freq[4] = 1
#   'c' -> freq[ord('c') - ord('a')] += 1 -> freq[2] = 2
#   'a' -> freq[ord('a') - ord('a')] += 1 -> freq[0] = 2
#   'r' -> freq[ord('r') - ord('a')] += 1 -> freq[17] = 2
# Step 3: Find first non-repeating character:
#   'r' -> freq[ord('r') - ord('a')] = 2 (repeating)
#   'a' -> freq[ord('a') - ord('a')] = 2 (repeating)
#   'c' -> freq[ord('c') - ord('a')] = 2 (repeating)
#   'e' -> freq[ord('e') - ord('a')] = 1 (non-repeating) -> return 'e'

print(non_repeating_char("aabbccc"))  
# Dry Run: 
# Input string: "aabbccc"
# Step 1: Initialize freq = [0] * 26
# Step 2: Count characters:
#   'a' -> freq[ord('a') - ord('a')] += 1 -> freq[0] = 1
#   'a' -> freq[ord('a') - ord('a')] += 1 -> freq[0] = 2
#   'b' -> freq[ord('b') - ord('a')] += 1 -> freq[1] = 1
#   'b' -> freq[ord('b') - ord('a')] += 1 -> freq[1] = 2
#   'c' -> freq[ord('c') - ord('a')] += 1 -> freq[2] = 1
#   'c' -> freq[ord('c') - ord('a')] += 1 -> freq[2] = 2
#   'c' -> freq[ord('c') - ord('a')] += 1 -> freq[2] = 3
# Step 3: Find first non-repeating character:
#   'a' -> freq[ord('a') - ord('a')] = 2 (repeating)
#   'b' -> freq[ord('b') - ord('a')] = 2 (repeating)
#   'c' -> freq[ord('c') - ord('a')] = 3 (repeating)
# No non-repeating character found -> return '$'
ROMAN_TO_INTEGER = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    'M': 1000
}

class Solution:

    def romanToInt(self, s: str) -> int:
        total = 0

        for i in range(len(s)):
            if i+1 < len(s) and ROMAN_TO_INTEGER[s[i]] < ROMAN_TO_INTEGER[s[i+1]]:
                total -= ROMAN_TO_INTEGER[s[i]]
            else:
                total += ROMAN_TO_INTEGER[s[i]]

        return total

if __name__ == '__main__':
    roman_number = 'MCMXCIV'
    print(Solution().romanToInt(roman_number))

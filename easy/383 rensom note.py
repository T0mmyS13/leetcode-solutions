class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        for letter in ransomNote: # iterate through the ransomNote set
            if letter in magazine: # if the ransomNote set is in the magazine set return True
                magazine = magazine.replace(letter,"",1) # remove the letter from the magazine
                ransomNote = ransomNote.replace(letter, "",1) # remove the letter from the ransomNote
                if len(ransomNote) == 0: # if the ransomNote set is empty return True
                    return True
            else:
                return False


# Time complexity: O(n) where n is the length of the ransomNote
# Space complexity: O(1) 


print(Solution().canConstruct("aa", "aab")) # False
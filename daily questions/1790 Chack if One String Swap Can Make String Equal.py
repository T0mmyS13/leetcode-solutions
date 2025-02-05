class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1==s2:
            return True #if the strings are equal return True
        if len(s1)!=len(s2):
            return False #if the length of the strings are not equal return False
        if sorted(s1)!=sorted(s2):
            return False #if the sorted strings are not equal return False
        diff=[] #initialize an empty list to store the differences
        for i in range(len(s1)):
            if s1[i]!=s2[i]: #if the characters are not equal
                diff.append(i) #add the index to the list
        if len(diff)!=2:
            return False #if the length of the list is not 2 return False
        if s1[diff[0]]==s2[diff[1]] and s1[diff[1]]==s2[diff[0]]:
            return True #if the characters at the indexes are equal return True
        
#time complexity is O(nlogn) because we are sorting the strings
#space complexity is O(n) because we are using a list to store the differences
        
s1 = "bank"
s2 = "kanb"
print(Solution().areAlmostEqual(s1,s2)) #True
        
    
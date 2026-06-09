class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S=Counter(s)
        T=Counter(t)
        if len(s)!=len(t):
            return False
        elif S==T:
            return True
        else:
            return False
        
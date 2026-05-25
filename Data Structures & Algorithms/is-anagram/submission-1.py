class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_hashmap = {}
        t_hashmap = {}

        for v in s:
            s_hashmap[v] = s_hashmap.get(v, 0) + 1
        
        for w in t:
            t_hashmap[w] = t_hashmap.get(w, 0) + 1
        
        if s_hashmap == t_hashmap:
            return True
        else:
            return False
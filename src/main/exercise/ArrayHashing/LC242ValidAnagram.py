class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        d1, d2 = self.collect(s), self.collect(t)

        for item in d1.items():
            if item[0] not in d2:
                return False
            else:
                if item[1] != d2[item[0]]:
                    return False
        return True

    def collect(self, s: str):
        d = dict()
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
        return d

class Solution:
    def isMorphing(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        map_s_to_t = {}
        map_t_to_s = {}

        for c1, c2 in zip(s, t):

            if c1 in map_s_to_t and map_s_to_t[c1] != c2:
                return False

            if c2 in map_t_to_s and map_t_to_s[c2] != c1:
                return False

            map_s_to_t[c1] = c2
            map_t_to_s[c2] = c1

        return True

    def optimizedMorphing(self, s: str, t: str) -> bool:
        map_s = [-1] * 256
        map_t = [-1] * 256

        for i in range(len(s)):
            if map_s[ord(s[i])] != map_t[ord(t[i])]:
                return False

            map_s[ord(s[i])] = i
            map_t[ord(t[i])] = i

        return True


if __name__ == '__main__':
    # str1 = "paper"
    # str2 = "title"
    str1 = "foo"
    str2 = "bar"

    # str1 = "egg"
    # str2= "add"

    sol = Solution()
    print(sol.optimizedMorphing(str1, str2))

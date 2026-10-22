class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]

    solution = Solution()
    result = solution.longestCommonPrefix(strs)

    print(result)

  
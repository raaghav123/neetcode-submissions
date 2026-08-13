class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        else:
            master_longest_substring = s[0]
            # print(len(master_longest_substring))
            longest_substring = s[0]
            for i in range(1,len(s)):
                if s[i] not in longest_substring:
                    longest_substring+=s[i]
                else:
                    if len(longest_substring) > len(master_longest_substring):
                        print(longest_substring)
                        master_longest_substring = longest_substring
                    repeat_index = longest_substring.index(s[i])
                    longest_substring = longest_substring[repeat_index + 1:] + s[i]
            
            if len(longest_substring) > len(master_longest_substring):
                master_longest_substring = longest_substring
                print(master_longest_substring)
            return len(master_longest_substring)
                    # if len(longest_substring) > len(master_longest_substring):
                    #     master_longest_substring = longest_substring
                    #     longest_subtring = s[i]
                    #     print(longest_substring)
            # return len(master_longest_substring)
            


            


        
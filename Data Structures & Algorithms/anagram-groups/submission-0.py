class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            sorted_w = sorted(word)
            if " ".join(sorted_w) not in d:
                d[" ".join(sorted(word))] = [word]
            else:
                d[" ".join(sorted(word))].append(word)
        
        final_arr = []
        for i in d.values():
            final_arr.append(i)
        return final_arr
                
            

                    

        
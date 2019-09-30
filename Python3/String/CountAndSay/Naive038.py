class Solution:
    def countAndSay(self, n: int) -> str:
        string_dict = {1: "1"}  # store all cases
        if n > 1:
            for j in range(2, n+1):
                if string_dict.get(j):
                    # if case exist
                    continue
                # new case
                string_dict[j] = ""
                current_num = string_dict[j-1][0]
                num_count = 0
                # iterate through the last number set
                for i in range(len(string_dict[j-1])):
                    # counts the numbers
                    if current_num == string_dict[j-1][i]:
                        num_count += 1
                    else:
                        string_dict[j] += str(num_count) + current_num
                        current_num = string_dict[j-1][i]
                        num_count = 1
                if num_count > 0:
                    string_dict[j] += str(num_count) + current_num
        return string_dict[n]

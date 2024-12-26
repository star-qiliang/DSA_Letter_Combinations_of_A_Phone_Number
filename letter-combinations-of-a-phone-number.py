class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard_dict = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        if not digits:
            return []

        digit = digits[0]
        res_list = list(keyboard_dict[digit])
        for i in range(1,len(digits)):
            digit = digits[i]
            cur_base = keyboard_dict[digit]
            new_list = []
            for x in res_list:
                for y in cur_base:
                    new_list.append(x+y)
            res_list = new_list
    
        return res_list
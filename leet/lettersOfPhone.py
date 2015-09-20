class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        return map(lambda x: "".join(reversed(x)), self.letterCombinationsReversed(digits))
    
    def letterCombinationsReversed(self, digits):
        if not digits:
            return []
        numsToLetters = {
            2:"abc",
            3:"def",
            4:"hgi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
            }
        if len(digits) == 1:
            return [[c] for c in numsToLetters[int(digits[0])]]
        result = []
        for char in numsToLetters[int(digits[0])]:
            for string in self.letterCombinationsReversed(digits[1:]):
                string.append(char)
                result.append(string)
        return result

import regex
import regex as re
import string


class solution():
    def solution(x):
        # Every lowercase letter in [a...z] is replaced with their corresponding
        # one in [z...a]. Every other character, including uppercase letters and
        # punctuation is untouched.

        # Input:
        # solution.solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
        # Output:
        #     did you see last night's episode?

        #
        re_lowercase = re.compile('[a-z]')
        abc = string.ascii_lowercase
        translator = str.maketrans(abc, abc[::-1], ' ')
        encrypted_message = ''

        for char in x:
            if regex.match(re_lowercase, char):
                encrypted_message += char.translate(translator)
            else:
                encrypted_message += char

        return encrypted_message


print(solution.solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))

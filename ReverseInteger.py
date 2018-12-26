import sys


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = -1
        str_x = str(x)

        pos_limit = 0x7fffffff
        neg_limit = -0x80000000

        if x < 0:
            result = int("-" + str_x[::-1][:-1])

        else:
            result = int(str_x[::-1])

        if result > 0:
            if (result & pos_limit) == result:
                return result
            else:
                return 0

        elif result == 0:
            return result

        else:
            if (result & neg_limit) == neg_limit:
                return result
            else:
                return 0


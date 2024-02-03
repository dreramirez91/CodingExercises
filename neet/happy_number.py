class Solution:
    def isHappy(self, n: int) -> bool:
        # ----- Solution 4 -----
        old_sums = set()
        while n not in old_sums:
            old_sums.add(n)
            n = sum([int(x) ** 2 for x in [*str(n)]])
            if n == 1:
                return True
        return False
        # ----- Solution 3 -----
        old_sums = set()
        while n not in old_sums:
            old_sums.add(n)
            n = self.squared_sum(n)
            if n == 1:
                return True
        return False

    def squared_sum(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            digit = digit**2
            output += digit
            n = n // 10
        return output
        # ----- Solution 2 -----

        i = 0
        old_sums = set()
        while True:
            sum_of_squares = sum([int(x) ** 2 for x in [*str(n)]])
            n = sum_of_squares
            if n in old_sums:
                return False
            elif n == 1:
                return True
            old_sums.add(sum_of_squares)
            i += 1
        # ----- Solution 1 -----
        i = 0
        old_sums = []
        while True:
            sum_of_squares = sum([int(x) ** 2 for x in [*str(n)]])
            n = sum_of_squares
            if n in old_sums:
                return False
            elif n == 1:
                return True
            old_sums.append(sum_of_squares)
            i += 1


test = Solution()
print(test.isHappy(2))

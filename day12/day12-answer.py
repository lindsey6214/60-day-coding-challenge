class Solution: 
    def multiplyStrings(num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            carry = 0
            for j in range(n - 1, -1, -1):
                product = int(num1[i]) * int(num2[j]) + carry + result[i + j + 1]
                carry = product // 10
                result[i + j + 1] = product % 10

            result[i] += carry

        result_str = "".join(map(str, result))
        return result_str.lstrip("0")

'''
Time complexity: O(m*n), where "m" is the length of the string num1 and "n" is the length of the string num2. For each pair of digits from num1 and num2, a constant amount of arithmetic operations is performed (multiplication, addition, division), which takes O(1) time. Since the inner loop is nested inside the outer loop, the overall time complexity is determined by the product of the lengths of num1 and num2, making it O(m*n).   
Space complexity: O(m+n). The most significant factor contributing to space complexity is the result array, which is used to store the intermediate products and sums. The size of this array is determined by the sum of the lengths of num1 and num2, so it can be as large as m+n. All other variables used in the solution have negligible space requirements compared to the size of this array.

This code handles the multiplication of two numbers represented as strings by simulating long multiplication. It initializes a result array to store the intermediate products and sums. Then, it iterates through both input strings from right to left, computes products, carries, and updates the result array. Finally, it converts the result array back to a string and removes leading zeros.
'''

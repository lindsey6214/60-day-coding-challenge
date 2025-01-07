def decodeString(s):
    stack = []
    current_str = ''
    current_num = 0

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ''
            current_num = 0
        elif char == ']':
            prev_str, repeat_num = stack.pop()
            current_str = prev_str + current_str * repeat_num
        else:
            current_str += char

    return current_str

'''
Traverse the input string character by character. 
- When we encounter a digit, we build the number until we reach the corresponding closing bracket.
- When we encounter an opening bracket, we push the current string and its repeat count to the stack and reset the current string and repeat count.
- When we encounter a closing bracket, we pop the previous string and its repeat count from the stack, combine them with the current string, and update the current string.

Time complexity: O(N), where N is the length of the input encoded string. In the solution, we traverse the input string character by character. The for loop iterates through each character once. In each iteration, we perform constant-time operations like checking if the character is a digit, opening bracket, closing bracket, or a regular character. These operations take O(1) time. However, in certain cases, we might need to push or pop elements from the stack, and each stack operation takes O(1) time as well. Since we traverse the entire input string once and perform constant-time operations in each iteration, the overall time complexity of the solution is O(N).
Space complexity: O(N), where N is the length of the input encoded string. The space complexity is determined by the additional memory used to store elements in the stack. In the worst-case scenario, all the characters in the input string could be part of nested patterns, which would require us to push each character onto the stack. Additionally, we may also push the repeat count for each nested pattern. But in the best-case scenario, where there are no nested patterns in the input string, the stack would only contain a few elements corresponding to the opening brackets. As a result, the space used by the stack is directly proportional to the maximum nesting depth in the input string. Since we need to store all the characters involved in the nested patterns and their repeat counts, the space complexity is O(N) for the worst-case scenario.
'''

def longestCommonPrefix(strs):
    if not strs: 
        return "" 
    prefix = strs[0] 
    for i in range(1, len(strs)): 
        while strs[i].find(prefix) != 0: 
            prefix = prefix[:len(prefix)-1] 
            if not prefix: 
                return "" 
    return prefix

'''
Time complexity: O(m*n), where m is the length of the longest string in the list and n is the number of strings in the list. The algorithm loops through each character of the first string in the list, which has a length of m. For each character, it loops through the remaining n-1 strings in the list, checking if the character is present in the same position in each string. In the worst case, the algorithm may need to compare each character in each string, which results in a time complexity of O(m*n).
Space complexity: O(1), so the space used by the algorithm does not depend on the size of the input.
'''

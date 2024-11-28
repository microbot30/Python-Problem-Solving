def solution(number):
    while True:
        stack = []
        changed = False
        i = 0
        while i < len(number):
            # If the stack is empty or the top of the stack is different from the current digit
            if not stack or stack[-1][0] != number[i]:
                stack.append([number[i], 1])
            # If top of the stack contains the same digit
            else:
                stack[-1][1] += 1  # Increment the count by 1

            i += 1
        # Sum transformation
        new_number = []
        for digit, count in stack:
            if count > 1:
                new_number.append(str(int(digit) * count))  # Calculating and adding the sum of consecutive digits
                changed = True
            else:
                new_number.append(digit)  # Keeping the single digit

        # If no changes were found, Break the loop
        if not changed:
            break

        # Updating the result as a string
        result = ''.join(new_number)
        break
    return result


if __name__ == "__main__":
    number = "44488366664"
    result = solution(number)
    print(result)

# Time Complexity: O(n)
# Space Complexity: O(n)


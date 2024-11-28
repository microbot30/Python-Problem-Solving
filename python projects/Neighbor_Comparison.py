def solution(target):
    # Initializing empty list to store final result
    result = []

    for i in range(len(target)):

        # Adding First and Last element by default
        if i == 0 or i == len(target) - 1:
            result.append(target[i])

        # Compare neighbors
        elif target[i] > target[i - 1] and target[i] > target[i + 1]:
            result.append(target[i])

    return result


if __name__ == "__main__":
    target = [1, 3, 2, 4, 5, 3, 6]
    result = solution(target)
    print(result)


# Time Complexity: O(n)
# Space Complexity: O(n)

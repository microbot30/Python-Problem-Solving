def process_operations(operations):
    min_width = float('inf')
    min_height = float('inf')
    results = []  # List to store results of queries

    for operation in operations:
        if operation[0] == 0:
            # Save a new rectangle, normalize it
            a, b = operation[1], operation[2]
            width, height = min(a, b), max(a, b)

            # Update min width and height to consider both the original and rotated form
            min_width = min(min_width, width)
            min_height = min(min_height, height)

        elif operation[0] == 1:
            # Query if a rectangle of size (a, b) fits into the smallest saved rectangle
            a, b = operation[1], operation[2]
            query_width, query_height = min(a, b), max(a, b)

            # Check if the query rectangle can fit inside the smallest stored rectangle
            if query_width <= min_width and query_height <= min_height:
                results.append(True)
            else:
                results.append(False)

    return results


if __name__ == "__main__":
    operations = [[0,11,20], [1,378,120], [1,14,7], [0,17,11], [1,1,11], [1,22,343],
                  [0,20,12], [0,15,15], [1,143,202], [0,15,20]]
    output = process_operations(operations)
    print(output)  # [True, False]


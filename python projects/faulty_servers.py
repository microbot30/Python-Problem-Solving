def count_faulty_replacements(n, logs):
    # Dictionary to store consecutive error counts for each server.
    # The key is the server_id, and the value is the count of consecutive errors.
    # A dictionary is used because we need fast lookups and updates for the servers' error counts.
    error_count = {}
    replacements = 0  # Track number of replacements (how many times a server was replaced)

    # Process each log entry
    for log in logs:
        # Split the log into server_id and status (either "error" or "success")
        server_id, status = log.split()

        # If this is the first time we encounter this server, initialize its error count
        if server_id not in error_count:
            error_count[server_id] = 0

        # If the log status is "error", increment the error count for that server
        if status == "error":
            error_count[server_id] += 1

            # If the server logs 3 consecutive errors, it is faulty and gets replaced
            if error_count[server_id] == 3:
                replacements += 1  # Increment the replacement count
                error_count[server_id] = 0  # Reset the error count after replacement

        # If the log status is "success", reset the error count for the server
        elif status == "success":
            error_count[server_id] = 0

    # Return the total number of replacements (i.e., how many times a faulty server was detected and replaced)
    return replacements


# Example usage:
n = 2
logs = ["s1 error", "s1 error", "s2 error", "s1 error", "s1 error", "s2 success"]
print(count_faulty_replacements(n, logs))  # Output: 1

def solution(serverPowers, events):
    n = len(serverPowers)
    remaining_capacity = serverPowers[:]
    request_count = [0] * n
    is_active = [True] * n
    current_server = 0

    def next_active_server(start):
        i = start
        while not is_active[i]:
            i = (i + 1) % n
        return i

    for event in events:
        if event == "REQUEST":
            remaining_capacity[current_server] -= 1
            request_count[current_server] += 1

            if remaining_capacity[current_server] == 0:
                current_server = next_active_server((current_server + 1) % n)

        elif event.startswith("FAIL"):
            _, idx = event.split()
            idx = int(idx)
            is_active[idx] = False

            if idx == current_server:
                current_server = next_active_server((current_server + 1) % n)

        if all(cap == 0 or not is_active[i] for i, cap in enumerate(remaining_capacity)):
            for i in range(n):
                if is_active[i]:
                    remaining_capacity[i] = serverPowers[i]

    max_requests = max(request_count)
    result_server = -1
    for i in range(n):
        if request_count[i] == max_requests:
            result_server = i

    return result_server

# Time complexity: O(m + n) {m is the number of events and n is the number of servers}

from collections import deque
import heapq
def bfs(graph, start, goal):
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        current = queue.popleft()
        print("Visiting:", current)

        # Goal reached
        if current == goal:
            break

        # Get neighboring cities
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    # No path found
    if goal not in visited:
        return None

    # Reconstruct path
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return path

def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        current = path[-1]
        print("POP:", path)
        print(f"visiting: {current}")

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                stack.append(new_path)

    return None

def ucs(graph, start, goal):
    # Priority queue:
    # (total_cost, current_node)
    queue = [(0, start)]

    # Lowest cost found so far for each node
    cost_so_far = {start: 0}

    # Used to reconstruct the final path
    parent = {start: None}

    # Nodes that have been completely processed
    visited = set()

    print("========== UCS START ==========")
    print("START:", start)
    print("GOAL:", goal)
    print("INITIAL QUEUE:", queue)
    print()

    while queue:

        print("QUEUE:", queue)

        # Remove node with the lowest cost
        current_cost, current = heapq.heappop(queue)

        print("POP:", (current_cost, current))
        print("CURRENT:", current)
        print("CURRENT COST:", current_cost)

        # Ignore an old/outdated queue entry
        if current_cost != cost_so_far[current]:
            print("SKIP: outdated entry")
            print("------------------------------")
            continue

        # Goal reached
        if current == goal:
            print("GOAL REACHED:", current)
            print("TOTAL COST:", current_cost)

            # Reconstruct path
            path = []
            node = goal

            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()

            print("FINAL PATH:", path)
            print("========== UCS END ==========")

            return path, current_cost
        # Mark current node as visited
        visited.add(current)

        print("VISITED:", visited)

        # Explore neighbors
        for neighbor, edge_cost in graph[current].items():

            new_cost = current_cost + edge_cost

            print(
                "NEIGHBOR:",
                neighbor,
                "| EDGE COST:",
                edge_cost,
                "| NEW TOTAL COST:",
                new_cost
            )

            # If this is a cheaper path
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:

                cost_so_far[neighbor] = new_cost
                parent[neighbor] = current

                heapq.heappush(queue, (new_cost, neighbor))

                print("  -> ADD TO QUEUE:", (new_cost, neighbor))
                print("  -> PARENT:", neighbor, "=", current)

            else:
                print("  -> NOT ADDED: existing path is cheaper")

        print("QUEUE AFTER EXPANSION:", queue)
        print("COST SO FAR:", cost_so_far)
        print("------------------------------")

    print("NO PATH FOUND")
    print("========== UCS END ==========")

    return None, None

def ids(graph, start, goal):
    def depth_limited_search(graph, start, goal, limit):
        stack = [(start, [start], 0)]
        visited = set()

        print(f"\n===== DEPTH LIMIT: {limit} =====")

        while stack:
            print("STACK:", stack)

            current, path, depth = stack.pop()

            print("POP:", (current, depth))
            print("CURRENT:", current)
            print("DEPTH:", depth)

            # Goal check
            if current == goal:
                print("GOAL REACHED:", current)
                print("PATH:", path)
                print("DEPTH:", depth)
                return path

            # Depth limit reached
            if depth == limit:
                print("DEPTH LIMIT REACHED:", current)
                print("------------------------------")
                continue

            # Avoid processing the same node again
            if current in visited:
                print("SKIP: already visited")
                print("------------------------------")
                continue

            visited.add(current)

            print("VISITED:", visited)

            # Add neighbors
            for neighbor in graph[current]:

                if neighbor not in visited:
                    new_path = path + [neighbor]
                    new_depth = depth + 1

                    stack.append(
                        (neighbor, new_path, new_depth)
                    )

                    print(
                        "PUSH:",
                        (neighbor, new_depth)
                    )

            print("STACK AFTER EXPANSION:", stack)
            print("------------------------------")

        print("NO SOLUTION AT THIS DEPTH")
        return None

    # Iteratively increase depth
    depth = 0

    while True:

        print("\n")
        print("================================")
        print("IDS ITERATION")
        print("CURRENT DEPTH LIMIT:", depth)
        print("================================")

        result = depth_limited_search(
            graph,
            start,
            goal,
            depth
        )

        if result is not None:
            print("\n========== IDS RESULT ==========")
            print("FINAL PATH:", result)
            print("FINAL DEPTH:", len(result) - 1)
            print("================================")

            return result

        depth += 1

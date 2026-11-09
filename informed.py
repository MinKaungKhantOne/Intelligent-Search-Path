import heapq
from math import radians, sin, cos, sqrt, atan2

def gbfs(graph, cities_geocode, start, goal):

    # Priority queue
    # (heuristic_cost, node)
    heuristic = create_heuristic_data(cities_geocode,goal)
    queue = [(heuristic[start], start)]

    # Track visited nodes
    visited = set()

    # Used to reconstruct the final path
    parent = {start: None}

    print("========== GREEDY BEST-FIRST SEARCH START ==========")
    print("START:", start)
    print("GOAL:", goal)
    print("INITIAL QUEUE:", queue)
    print()

    while queue:

        print("QUEUE:", queue)

        # Remove node with the smallest heuristic value
        h_cost, current = heapq.heappop(queue)

        print("POP:", (h_cost, current))
        print("CURRENT:", current)
        print("HEURISTIC h(n):", h_cost)

        # Skip if already visited
        if current in visited:
            print("SKIP: already visited")
            print("------------------------------")
            continue

        # Mark current node as visited
        visited.add(current)

        print("VISITED:", visited)

        # Goal reached
        if current == goal:
            print("GOAL REACHED:", current)

            # Reconstruct path
            path = []
            node = goal

            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()

            print("FINAL PATH:", path)
            print("HEURISTIC OF GOAL:", heuristic[goal])
            print("========== GREEDY BEST-FIRST SEARCH END ==========")

            return path

        # Explore neighbors
        for neighbor in graph[current]:

            if neighbor not in visited:

                h_neighbor = heuristic[neighbor]

                print(
                    "NEIGHBOR:",
                    neighbor,
                    "| h(n):",
                    h_neighbor
                )

                # Add neighbor based ONLY on heuristic
                heapq.heappush(
                    queue,
                    (h_neighbor, neighbor)
                )

                parent[neighbor] = current

                print(
                    "  -> PUSH:",
                    (h_neighbor, neighbor)
                )

        print("QUEUE AFTER EXPANSION:", queue)
        print("------------------------------")

    print("NO PATH FOUND")
    print("========== GREEDY BEST-FIRST SEARCH END ==========")

    return None

def a_star(graph, cities_geocode, start, goal):

    # (f(n), g(n), city)
    heuristic = create_heuristic_data(cities_geocode, goal)
    queue = [(heuristic[start], 0, start)]

    # Cheapest known cost from start to each city
    cost_so_far = {
        start: 0
    }

    # Used to reconstruct final path
    parent = {
        start: None
    }

    visited = set()

    print("========== A* SEARCH START ==========")
    print("START:", start)
    print("GOAL:", goal)
    print("INITIAL QUEUE:", queue)
    print()

    while queue:

        print("QUEUE:", queue)

        f_cost, current_cost, current = heapq.heappop(queue)

        print("POP:", (f_cost, current_cost, current))
        print("CURRENT:", current)
        print("g(n) =", current_cost)
        print("h(n) =", heuristic[current])
        print("f(n) =", f_cost)

        # Ignore an old/worse queue entry
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
            print("FINAL COST:", current_cost)

            print("========== A* SEARCH END ==========")

            return path, current_cost

        visited.add(current)

        print("VISITED:", visited)

        # Expand neighbors
        for neighbor, edge_cost in graph[current].items():

            new_g_cost = current_cost + edge_cost

            h_cost = heuristic[neighbor]

            new_f_cost = new_g_cost + h_cost

            print(
                "NEIGHBOR:", neighbor,
                "| EDGE COST:", edge_cost,
                "| g(n):", new_g_cost,
                "| h(n):", h_cost,
                "| f(n):", new_f_cost
            )

            # If this is a cheaper path to neighbor
            if (
                neighbor not in cost_so_far
                or new_g_cost < cost_so_far[neighbor]
            ):

                cost_so_far[neighbor] = new_g_cost
                parent[neighbor] = current

                heapq.heappush(
                    queue,
                    (new_f_cost, new_g_cost, neighbor)
                )

                print(
                    "  -> PUSH:",
                    (new_f_cost, new_g_cost, neighbor)
                )

                print(
                    "  -> PARENT:",
                    neighbor,
                    "=",
                    current
                )

            else:
                print(
                    "  -> NOT ADDED: existing path is cheaper"
                )

        print("QUEUE AFTER EXPANSION:", queue)
        print("COST SO FAR:", cost_so_far)
        print("------------------------------")

    print("NO PATH FOUND")
    print("========== A* SEARCH END ==========")

    return None, None

def haversine_distance(lat1, lon1, lat2, lon2):

    R = 6371  # Earth's radius in kilometers

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        sin(dlat / 2) ** 2
        + cos(lat1)
        * cos(lat2)
        * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


def create_heuristic_data(coordinates, goal):

    if goal not in coordinates:
        raise ValueError(f"Goal '{goal}' not found in coordinates.")

    goal_lat, goal_lon = coordinates[goal]['lat'],coordinates[goal]['lng']

    heuristic = {}

    for city, coord in coordinates.items():

        distance = haversine_distance(
            coord['lat'],
            coord['lng'],
            goal_lat,
            goal_lon
        )

        heuristic[city] = round(distance, 2)

        print(
            f"{city} → {goal}: "
            f"h(n) = {heuristic[city]} km"
        )

    return heuristic

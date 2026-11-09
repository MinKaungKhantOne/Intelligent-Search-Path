# Intelligent Search Visualizer

## Project Overview

Intelligent Search Visualizer is an interactive, map-based web application designed to demonstrate and visualize classic Artificial Intelligence (AI) search algorithms using real-world road networks.

The application allows users to select starting and destination locations on an interactive map and explore how different search algorithms find routes between them.

It integrates external geocoding and routing APIs to fetch real-world location and road network data, providing a practical environment for understanding and comparing AI search strategies.

The project supports geographical locations in Myanmar or Thailand and is deployed as a publicly accessible web application.

## Key Features

### 1. Interactive Map Visualization
- Provides an interactive map interface for selecting locations.
- Allows users to define starting and destination points.
- Visualizes search progress and explored paths on a real-world map.
- Displays the resulting route between selected locations.

### 2. Six AI Search Algorithms

Implements six classic AI search strategies:

| Algorithm | Search Strategy |
|---|---|
| Breadth-First Search (BFS) | Explores nodes level by level. |
| Depth-First Search (DFS) | Explores one path deeply before backtracking. |
| Uniform Cost Search (UCS) | Expands the node with the lowest accumulated path cost. |
| Iterative Deepening Search (IDS) | Repeatedly performs depth-limited searches with increasing depth limits. |
| Greedy Best-First Search | Expands the node estimated to be closest to the goal. |
| A* Search | Combines accumulated path cost and estimated remaining cost to find an efficient route. |

### 3. Real-World Map Data Integration
- Integrates external geocoding APIs to convert location names into geographical coordinates.
- Fetches road network and routing information through external APIs.
- Constructs a spatial graph representing real-world road connections.
- Uses geographical information to support route searching.

### 4. Search Algorithm Comparison
- Allows users to explore different search strategies.
- Demonstrates how each algorithm explores the road network.
- Provides a practical comparison of search behavior and route-finding approaches.

### 5. Web Backend Development
- Implements backend functionality for handling search requests.
- Integrates API data-fetching logic.
- Processes geographical data and search algorithm results.
- Connects the search engine with the interactive frontend.

### 6. Public Deployment
- Deployed as a publicly accessible web application with Railway Hosting.
- Allows users to interact with the search visualizer through a web browser.

## Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Artificial Intelligence | Search Algorithms |
| Backend | Python Web Framework |
| Frontend | HTML, CSS, JavaScript |
| Map Visualization | Interactive Map |
| External APIs | Geocoding and Routing APIs |
| Version Control | Git, GitHub |
| Deployment | Web Hosting Platform |

## Implemented Search Algorithms

### Uninformed Search
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Uniform Cost Search (UCS)
- Iterative Deepening Search (IDS)

### Informed Search
- Greedy Best-First Search
- A* Search

These algorithms demonstrate different approaches to exploring a geographical search space and finding routes between two locations.

## How It Works

The application follows this general workflow:

1. **Location Selection:** Users select starting and destination locations on the map.
2. **Geocoding:** The application converts selected locations into geographical coordinates.
3. **Road Network Retrieval:** External APIs provide the required road network and routing data.
4. **Graph Construction:** The geographical road network is represented as a graph of nodes and edges.
5. **Algorithm Execution:** The selected AI search algorithm explores the graph to find a route.
6. **Route Visualization:** The application displays the search result and route on the interactive map.

## Author

**Min Kaung Khant**

GitHub: [MinKaungKhantOne](https://github.com/MinKaungKhantOne)

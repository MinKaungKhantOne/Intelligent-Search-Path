from flask import Flask, render_template, request, jsonify
import json, os
from uninformed import *
from informed import *
app = Flask(__name__)

with open("map_data.json", 'r') as f:
    j_data = json.load(f)
cities = j_data["cities"]
graph = j_data["graph"]

@app.route('/')
def play_map():
    cities = [
        'Hinthada', 'Meiktila',
        'Bagan', 'Taunggyi',
        'Lashio', 'Mudon',
        'Pyay', 'Pyin Oo Lwin',
        'Mawlamyine', 'Thaton',
        'Yangon', 'Bago',
        'Loikaw', 'Mandalay',
        'Phyu', 'Naypyidaw',
        'Mrauk-U', 'Magway',
        'Taungoo', 'Mogok',
        'Pathein', 'Hpa-An'
    ]
    search_algorithms = ["BFS", "DFS", "UCS", "IDS", "GBFS","A_Star"]
    return render_template('index.html', cities=cities, s_algorithms=search_algorithms)

@app.route("/search",methods=['POST', 'GET'])
def search_path():
    data = request.get_json()
    start = data['origin']
    goal = data['destination']
    print(data['algorithm'])
    if data['algorithm'] == "BFS":
        result = bfs(graph, start, goal)
        result_geo_data = [[cities[city]['lat'], cities[city]['lng']] for city in result]
        result = [result,result_geo_data]
        return jsonify(result)
    elif data['algorithm'] == "DFS":
        result = dfs(graph, start, goal)
        result_geo_data = [[cities[city]['lat'], cities[city]['lng']] for city in result]
        result = [result, result_geo_data]
        return jsonify(result)
    elif data['algorithm'] == "IDS":
        result = ids(graph, start, goal)
        result_geo_data = [[cities[city]['lat'], cities[city]['lng']] for city in result]
        result = [result, result_geo_data]
        return jsonify(result)
    elif data['algorithm'] == "UCS":
        path_result, cost = ucs(graph, start, goal)
        result_geo_data = [[cities[city]['lat'], cities[city]['lng']] for city in path_result]
        result = [path_result, result_geo_data]
        return jsonify(result)
    elif data['algorithm'] == "GBFS":
        result = gbfs(graph, cities, start, goal)
        result_geo_data = [[cities[city]['lat'], cities[city]['lng']] for city in result]
        result = [result, result_geo_data]
        return jsonify(result)
    elif data['algorithm'] == "A_Star":
        path_result, cost = a_star(graph, cities, start, goal)
        result_geo_data = [[cities[city]['lat'], cities[city]['lng']] for city in path_result]
        result = [path_result, result_geo_data]
        return jsonify(result)

if __name__ == "__main__":
    # port = int(os.environ.get("PORT",5000))
    # app.run(host="0.0.0.0", port=port)
    app.run(debug=True)
![pokemon](https://user-images.githubusercontent.com/93203695/148101905-a5026eed-4ce7-497a-bc45-6dfe751d4a64.png)

# Pokemon Game - PY 
# About The Project
In this project we created a simple game, which is about catching pokemos.</br>
The game's purpose is to collect as many points as we can, while every pokemon has a different value of points.</br>
The pokemons are located on a directed weighted connected graph. </br>
Our task is to locate the agents at the graph in the best position we can (we chose to locate them on the center of the graph), and send them to catch the most suitable pokemons.</br>
The consideration of a suitable pokemon relies on many different parameters:
- The number of agent's moves it will take to get the pokemon.
  - It depends on the distance of the pokemon from the agent, which means the number of edges the agent needs to go and their weight.
- The value of the pokemon.
  - Every pokemon has it's own value.
- We have limited time and limited number of moves (10 moves per sec).
  - Which means we need to consider how to collect as many points as we can with this limitation.  


# The Creation Process
First of all, the directed weighted connected graph, the pokemons and the agents values are received in a Json format.</br>
The graph's paramenters are it's nodes and edges. Every node has id number, geographical position value, edges that goes out of the node, and edges that goes to the node.</br> 
The Agent's parameters are it's id number, it's value, it's source and destination, it's speed and it's position.</br>
The Pokemon's parameters are it's value, it's type and it's position.</br>
We read the Json file and create all the above. To do this we created the class "argoments", where we receive the pokemons and the agents from the Json and create them.</br>
In addition, we created the class "GraphAlgo" to load the graph from the Json file and to implement algorithms on it.</br>
We created the class "Node" which represents a node of the graph, and the class Digraph which represents a graph.<br/>

# Graph's Algorithms
## Shortest Path

## TSP

## Center

## Dijkstra

# UML Diagram

# Getting Started
## Installation
## Usage

# Screenshots

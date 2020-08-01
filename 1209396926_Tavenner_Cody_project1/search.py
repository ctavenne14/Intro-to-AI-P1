# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #use stack for dfs
    fringe = util.Stack()
    #starting node
    start_node = problem.getStartState()


    #create a set of visited nodes
    visited = set()

    
    visited_list = (start_node,[], 0)

    state = visited_list[0]

    direction = visited_list[1]

    cost = visited_list[2]

    #list of actions pushed onto the fringe 
     
    fringe.push(visited_list)

    while(True):
        #return empty list if fringe is empty
        if fringe.isEmpty():
            return []

        #pop the fringe
        node = fringe.pop()          

        #return once the goal state is hit
        if problem.isGoalState(node[0]):
            return node[1]

        #add node not visited to visited list
        if node[0] not in visited:
            visited.add(node[0])

            #get successors and push the path onto the fringe
            for successor in problem.getSuccessors(node[0]): 
                path = node[1]

                path =  path + [successor[1]]
                
                fringe.push((successor[0], path, 0))

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #use queue for bfs
    fringe = util.Queue()
    #starting node
    start_node = problem.getStartState()


    #create a set of visited nodes
    visited = set()

    
    visited_list = (start_node,[], 0)

    state = visited_list[0]

    direction = visited_list[1]

    cost = visited_list[2]
    
    #list of actions pushed onto the fringe 

    fringe.push(visited_list)

    while(True):
        #return empty list if fringe is empty
        if fringe.isEmpty():
            return []

        #pop the fringe
        node = fringe.pop()

        #return once the goal state is hit
        if problem.isGoalState(node[0]):
            return node[1]

        #add node not visited to visited list
        if node[0] not in visited:
            visited.add(node[0])

            #get successors and push the path onto the fringe
            for successor in problem.getSuccessors(node[0]): 
                path = node[1]

                path =  path + [successor[1]]

                fringe.push((successor[0], path, 0))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #use priority queue for ucs
    fringe = util.PriorityQueue()
    #starting node
    start_node = problem.getStartState()


    #create a set of visited nodes
    visited = set()


    visited_list = (start_node,[], 0)

    state = visited_list[0]

    direction = visited_list[1]

    cost = visited_list[2]

    #list of actions pushed onto the fringe 

    fringe.push(visited_list, cost)

    while(True):
        #return empty list if fringe is empty
        if fringe.isEmpty():
            return []

        #pop the fringe
        node = fringe.pop()

        #return once the goal state is hit
        if problem.isGoalState(node[0]):
            return node[1]

        #add node not visited to visited list
        if node[0] not in visited:
            visited.add(node[0])
            cost_node = node[2]

            #get successors and push the path and cost onto the fringe
            for successor in problem.getSuccessors(node[0]): 
                cost = cost_node

                path = node[1]

                path =  path + [successor[1]]

                cost += successor[2]

                fringe.push((successor[0], path, cost), cost)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #use priority queue for a*
    fringe = util.PriorityQueue()
    #starting node
    start_node = problem.getStartState()


    #create a set of visited nodes
    visited = set()

    
    visited_list = (start_node,[], 0)

    state = visited_list[0]

    direction = visited_list[1]

    cost = visited_list[2]

    heuristic_cost = heuristic(state, problem)

    heuristic_value = heuristic_cost + cost
     
    #list of actions pushed onto the fringe 

    fringe.push(visited_list, heuristic_value)

    while(True):
        #return empty list if fringe is empty
        if fringe.isEmpty():
            return []

        #pop the fringe
        node = fringe.pop()

        #return once the goal state is hit
        if problem.isGoalState(node[0]):
            return node[1]

        #add node not visited to visited list
        if node[0] not in visited:
            visited.add(node[0])
            cost_node = node[2]

            #get successors and push the path onto the fringe
            for successor in problem.getSuccessors(node[0]): 
                cost = cost_node

                path = node[1]

                path =  path + [successor[1]]

                cost += successor[2]

                #develop heuristic and find the hueristic value of the path

                heur_val = heuristic(successor[0], problem)
                heuristic_value = heur_val + cost
                fringe.push((successor[0], path, cost), heuristic_value)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

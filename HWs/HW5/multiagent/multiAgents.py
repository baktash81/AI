# multiAgents.py
# --------------
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


from cmath import inf
from xml.dom import minicompat
from util import manhattanDistance
from game import Directions
import random
import util

from game import Agent


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scofinal = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scofinal)
        bestIndices = [index for index in range(
            len(scofinal)) if scofinal[index] == bestScore]
        # Pick randomly among the best
        chosenIndex = random.choice(bestIndices)

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [
            ghostState.scaredTimer for ghostState in newGhostStates]

        # addtional score 
        additional_score = 0.0000
        # first thing that we should consider is ghost 
        ghost_distance = []
        for ghost in newGhostStates :
            ghost_distance.append(manhattanDistance(newPos,ghost.getPosition()))
        min_ghost = min(ghost_distance)

        #if neafinalt ghost have less or equal 2 block distance minus the score
        if min_ghost<=2 :
            additional_score-=1000
        #check whether we have food in new position :
        # food positions :
        foods = newFood.asList()
        if (len(foods)==0) :
            return successorGameState.getScore()

        if(newPos in foods):
            additional_score +=50

        #check whether have wall in succesors
        if(currentGameState.hasWall(newPos[0],newPos[1])) :
            additional_score-=10
        
        # minus 1/minimum distance of food from score 
        food_dis = []
        for food in foods :
            food_dis.append(manhattanDistance(newPos,food))
        neafinalt_food = min(food_dis)
        additional_score += 1/neafinalt_food
        
        near_scared = 999999
        for dis in newScaredTimes :
            if dis!=0 and dis<near_scared :
                near_scared = dis

        if min_ghost <= near_scared and near_scared!=999999:
            additional_score += min_ghost


        return successorGameState.getScore() + additional_score


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)
        self.nodesCount = 0


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """


    def func(self,depth,gameState,agentIndex):

        actions = gameState.getLegalActions(agentIndex)
        agent_num = gameState.getNumAgents()
        self.nodesCount+=1
        if(depth==0 or gameState.isLose() or gameState.isWin() or len(actions)==0) :
            return self.evaluationFunction(gameState)
        states = []
        for action in actions :
            states.append(gameState.generateSuccessor(agentIndex,action))
        
        if(agentIndex==0) :
            pacman_next = []
            for state in states :
                pacman_next.append(self.func(depth-1,state,(agentIndex+1)%agent_num))
            return max(pacman_next)
        else :
            ghost_next = []
            for state in states :
                ghost_next.append(self.func(depth-1,state,(agentIndex+1)%agent_num))
            return min(ghost_next)


    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        with open('MinimaxAgent.txt', 'a') as f:
            f.write(f"\n {self.nodesCount}")
            
        depth = gameState.getNumAgents()*self.depth
        #find all legal actions of pacman(0) : 
        pacman_actions = gameState.getLegalActions(0)

        all_actions = []
        for i in range(len(pacman_actions)) :
            all_actions.append((pacman_actions[i],self.func(depth-1,gameState.generateSuccessor(0,pacman_actions[i]),1)))

        return max(all_actions,key = lambda it:it[1])[0]

        util.raiseNotDefined()


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """
    def gm(self,alpha, beta,state, agentIndex, depth):
        self.nodesCount += 1
        if not state.getLegalActions(agentIndex):
            return self.evaluationFunction(state)
        
        final = inf
        if agentIndex ==state.getNumAgents() - 1:
            for action in state.getLegalActions(agentIndex):
                final = min(final, self.maxx(alpha, beta,state.generateSuccessor(agentIndex, action), 0,depth))
                if(final<alpha):
                    return final
                else:
                    beta=min(beta, final)
        else:
            for action in state.getLegalActions(agentIndex):
                final=min(final, self.gm(alpha, beta,state.generateSuccessor(agentIndex, action),agentIndex+1,depth))
                if final<alpha:
                    return final
                beta=min(beta, final)
        return final

    def maxx(self,alpha,beta,state,agentIndex,depth):
        self.nodesCount+=1
        if not state.getLegalActions(agentIndex) or depth == self.depth:
            return self.evaluationFunction(state)
        
        final = -inf
        for action in state.getLegalActions(agentIndex):
            final = max(final, self.gm(alpha, beta,state.generateSuccessor(agentIndex, action), agentIndex + 1, depth + 1))
            if beta < final:
                return final
            alpha = max(alpha, final)
        return final

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        with open('AlphaBetaAgent.txt', 'a') as f:
            f.write(f"\n {self.nodesCount}")
        "*** YOUR CODE HERE ***"
        alpha = -inf
        beta = inf
        #find all legal actions of pacman(0) : 
        pacman_actions = gameState.getLegalActions(0)

        all_actions = []
        for i in range(len(pacman_actions)) :
            result = self.gm(alpha,beta,gameState.generateSuccessor(0,pacman_actions[i]),1,1)
            all_actions.append((pacman_actions[i],self.gm(alpha,beta,gameState.generateSuccessor(0,pacman_actions[i]),1,1)))
            if (beta<result):
                return pacman_actions[i]

            alpha = max(alpha,result)
        
        return max(all_actions,key = lambda it:it[1])[0]

        util.raiseNotDefined()


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
        Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviation
better = betterEvaluationFunction

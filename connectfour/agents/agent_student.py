from connectfour.agents.computer_player import RandomAgent
import random
import math


class StudentAgent(RandomAgent):

    opponent_player = 2
    opponent_moves = []

    def __init__(self, name):
        super().__init__(name)
        self.MaxDepth = 4

    def get_move(self, board):
        """
        Args:
            board: An instance of `Board` that is the current state of the board.
        Returns:
            A tuple of two integers, (row, col)
        """
        # assigns id to the opponent player
        if(self.id != 1):
            self.opponent_player = 1

        valid_moves = board.valid_moves()
        vals = []
        moves = []

        best_score = -10
        for move in valid_moves:
            # print(str(moves))
            next_state = board.next_state(self.id, move[1])
            moves.append(move)
            vals.append(self.dfMiniMax(next_state, 1, -math.inf, math.inf))
        bestMove = moves[vals.index(max(vals))]

        # return best row and column
        return bestMove

    def dfMiniMax(self, board, depth, alpha, beta):
        # Goal return column with maximized scores of all possible next states
        if depth == self.MaxDepth:
            return self.evaluateBoardState(board)

        valid_moves = board.valid_moves()
        vals = []
        moves = []

        for move in valid_moves:
            if depth % 2 == 1:
                next_state = board.next_state(self.id % 2 + 1, move[1])
            else:
                next_state = board.next_state(self.id, move[1])

            moves.append(move)
            vals.append(self.dfMiniMax(next_state, depth + 1, alpha, beta))

        if depth % 2 == 1:
            bestVal = min(vals)
            # beta = min(beta, vals)
            # if beta >= alpha:
            #     break
        else:
            bestVal = max(vals)
            # alpha = max(alpha, val)
            # if alpha >= beta:
            #     break

        return bestVal

    def evaluateBoardState(self, board):
        # the board here is a copy with next states in it.
        # check if the current move is the winner move then score is 10000
        # check if the current move is the 3 in a row & the next one is empty move then score
        # check if the opponent move is the 3 in a row move then -100000000
        # if its center column then score
        if board.winner() == self.id:
            # the student agent is winner
            return 1
        elif board.winner() == self.opponent_player:
            # the opponent won
            return -1
        
        if board.last_move[1] == board.DEFAULT_WIDTH - 4:
            return 1
        """
        Your evaluation function should look at the current state and return a score for it. 
        As an example, the random agent provided works as follows:
            If the opponent has won this game, return -1.
            If we have won the game, return 1.
            If neither of the players has won, return a random number.
        """

        """
        These are the variables and functions for board objects which may be helpful when creating your Agent.
        Look into board.py for more information/descriptions of each, or to look for any other definitions which may help you.

        Board Variables:
            board.width 
            board.height
            board.last_move
            board.num_to_connect
            board.winning_zones
            board.score_array 
            board.current_player_score

        Board Functions:
            get_cell_value(row, col)
            try_move(col)
            valid_move(row, col)
            valid_moves()
            terminal(self)
            legal_moves()
            next_state(turn)
            winner()
        """
        
        return random.uniform(0, 1)

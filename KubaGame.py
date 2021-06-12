# Author: Jacob Dumas
# Date: 6/2/2021
# Description: A game named Kuba that consists of two players moving marbles around a 6 x 6 board. The
#              game is won when a player has pushed 7 marbles off the board or the other player does not have
#              any more marbles to play with.

# for creating a deep copy for Ko rule
import copy


class KubaGame:
    """This KubaGame class holds the Kuba Board, the players, marbles, and other game functionality.
        It also holds all the methods for the game including the rules and validates correct moves. The players
        will interact with this class to play the game. It does not communicate with any other classes."""

    def __init__(self, player_1, player_2):
        """Initializes the players A and B with which color they are. Also initializes
            current_turn and winner to None. Takes player_1 and player_2 as a parameter which are the 2 players of the
            game. They should be a tuple with the player and color. Also initializes variables for the Ko Rule."""
        # init players
        self._player_1 = player_1[0]
        self._player_1_color = player_1[1]
        self._player_2 = player_2[0]
        self._player_2_color = player_2[1]

        self._player_1_captured = 0
        self._player_2_captured = 0

        # for resetting if Ko Rule is violated
        self._player_1_last_captured = 0
        self._player_2_last_captured = 0

        # init board
        self._board = [['W', 'W', 'X', 'X', 'X', 'B', 'B'],
                       ['W', 'W', 'X', 'R', 'X', 'B', 'B'],
                       ['X', 'X', 'R', 'R', 'R', 'X', 'X'],
                       ['X', 'R', 'R', 'R', 'R', 'R', 'X'],
                       ['X', 'X', 'R', 'R', 'R', 'X', 'X'],
                       ['B', 'B', 'X', 'R', 'X', 'W', 'W'],
                       ['B', 'B', 'X', 'X', 'X', 'W', 'W']]

        # for Ko Rule
        self._last_board = []
        self._last_player_1_board = []
        self._last_player_2_board = []

        self._current_turn = None
        self._winner = None

    def get_player_color(self, playername):
        """Returns the player's color"""
        if playername == self._player_1:
            return self._player_1_color
        if playername == self._player_2:
            return self._player_2_color

    def set_current_turn(self, player):
        """Sets whose turn it is"""
        if player == self._player_1:
            self._current_turn = self._player_2
        if player == self._player_2:
            self._current_turn = self._player_1

    def get_current_turn(self):
        """Returns the player whose turn it is. Returns None if no player the first move. Takes no parameters."""
        return self._current_turn

    def set_winner(self, player):
        """Sets the winning player"""
        if player == self._player_1:
            self._winner = self._player_1
        if player == self._player_2:
            self._winner = self._player_2

    def get_winner(self):
        """Takes no parameters. Returns the name of the winning player. If no player has won, returns None."""
        return self._winner

    def get_captured(self, player):
        """Shows marbles captured. Takes player's name as a parameter and returns number of Red
            marbles player has. The player is the one the user wishes to see their score."""
        if player == self._player_1:
            return self._player_1_captured
        if player == self._player_2:
            return self._player_2_captured

    def get_marble(self, coordinates):
        """Display marble at given coordinates. Parameter is the coordinates of a cell as a tuple and
            returns the marble at that location. If no marble is present, return X"""
        return self._board[coordinates[0]][coordinates[1]]

    def did_player_lose_their_balls(self, playername):
        """Creates a nested for loop to count up white and black marbles to check if any player lost theirs
            and therefore lost the game."""
        white_marbles = 0
        black_marbles = 0
        for i in range(0, 7):
            for j in range(0, 7):
                if self._board[i][j] == 'W':
                    white_marbles += 1
                if self._board[i][j] == 'B':
                    black_marbles += 1

        if playername == self._player_1:
            # if player is player 1, check player 2
            if self._player_2_color == "W":
                if white_marbles == 0:
                    # change winner
                    self.set_winner(playername)
            if self._player_2_color == "B":
                if black_marbles == 0:
                    # change winner
                    self.set_winner(playername)

        if playername == self._player_2:
            # if player is player 2, check player 1
            if self._player_1_color == "W":
                if white_marbles == 0:
                    # change winner
                    self.set_winner(playername)
            if self._player_1_color == "B":
                if black_marbles == 0:
                    # change winner
                    self.set_winner(playername)

    def get_marble_count(self):
        """Returns the amount of marbles of each color. Takes no parameters and
            returns number of white, black, and red marbles as a tuple in that order."""
        white_marbles = 0
        black_marbles = 0
        red_marbles = 0
        for i in range(0, 7):
            for j in range(0, 7):
                if self._board[i][j] == 'W':
                    white_marbles += 1
                if self._board[i][j] == 'B':
                    black_marbles += 1
                if self._board[i][j] == 'R':
                    red_marbles += 1
        return white_marbles, black_marbles, red_marbles

    def end_of_turn(self, playername):
        """Checks for winning conditions, Ko rule, and changes player's turn"""
        # check for Ko Rule
        if playername == self._player_1:
            if self._board == self._last_player_2_board:
                # undo board
                self._board = self._last_board
                # undo points
                self._player_1_captured = self._player_1_last_captured
                self._player_2_captured = self._player_2_last_captured
                return False
        if playername == self._player_2:
            if self._board == self._last_player_1_board:
                # undo board
                self._board = self._last_board
                # undo points
                self._player_1_captured = self._player_1_last_captured
                self._player_2_captured = self._player_2_last_captured
                return False

        # winning conditions
        # if a player has 7 red then they won
        if self.get_captured(playername) == 7:
            # change winner
            self.set_winner(playername)

        # if a player has no more balls they lost
        self.did_player_lose_their_balls(playername)

        # change current player
        self.set_current_turn(playername)

        # set last points for Ko Rule
        self._player_1_last_captured = self._player_1_captured
        self._player_2_last_captured = self._player_2_captured

    def rec_make_move_l(self, playername, coordinates, direction):
        """A recursive helper function for moving B"""
        next_marble = self._board[coordinates[0]][coordinates[1] - 1]
        next_marble_coord = (coordinates[0], coordinates[1] - 1)
        edge_marble_coord = (coordinates[0], 0)
        if next_marble == 'X':
            self._board[coordinates[0]][coordinates[1] - 1] = self._board[coordinates[0]][coordinates[1]]
            self._board[coordinates[0]][coordinates[1]] = 'X'
            # end turn
            return True
        # if next position is the last on board (edge)
        if next_marble_coord == edge_marble_coord:
            # check if the next marble is the players own marble, if it is then it is invalid
            player_marble = self.get_player_color(playername)
            if next_marble == player_marble:
                return False
            # check if the next marble is a red marble, if it is then move to players hand and push marble
            if next_marble == 'R':
                if playername == self._player_1:
                    self._player_1_captured += 1
                if playername == self._player_2:
                    self._player_2_captured += 1
                # move marble
                self._board[coordinates[0]][coordinates[1] - 1] = self._board[coordinates[0]][coordinates[1]]
                # end turn
                return True
            # if it reaches here it will automatically be the other player's marble
            else:
                # move marble
                self._board[coordinates[0]][coordinates[1] - 1] = self._board[coordinates[0]][coordinates[1]]
                # end turn
                return True
        # else if the next marble is not on the edge continue recursive function
        else:
            if self.rec_make_move_l(playername, (coordinates[0], coordinates[1] - 1), direction):
                # move current to next
                self._board[coordinates[0]][coordinates[1] - 1] = self._board[coordinates[0]][coordinates[1]]
                return True

    def rec_make_move_r(self, playername, coordinates, direction):
        """A recursive helper function for moving r"""
        next_marble = self._board[coordinates[0]][coordinates[1] + 1]
        next_marble_coord = (coordinates[0], coordinates[1] + 1)
        edge_marble_coord = (coordinates[0], 6)
        if next_marble == 'X':
            self._board[coordinates[0]][coordinates[1] + 1] = self._board[coordinates[0]][coordinates[1]]
            self._board[coordinates[0]][coordinates[1]] = 'X'
            # end turn
            return True
        # if next position is the last on board (edge)
        if next_marble_coord == edge_marble_coord:
            # check if the next marble is the players own marble, if it is then it is invalid
            player_marble = self.get_player_color(playername)
            if next_marble == player_marble:
                return False
            # check if the next marble is a red marble, if it is then move to players hand and push marble
            if next_marble == 'R':
                if playername == self._player_1:
                    self._player_1_captured += 1
                if playername == self._player_2:
                    self._player_2_captured += 1
                # move marble
                self._board[coordinates[0]][coordinates[1] + 1] = self._board[coordinates[0]][coordinates[1]]
                # end turn
                return True
            # if it reaches here it will automatically be the other player's marble
            else:
                # move marble
                self._board[coordinates[0]][coordinates[1] + 1] = self._board[coordinates[0]][coordinates[1]]
                # end turn
                return True
        # else if the next marble is not on the edge continue recursive function
        else:
            if self.rec_make_move_r(playername, (coordinates[0], coordinates[1] + 1), direction):
                # move current to next
                self._board[coordinates[0]][coordinates[1] + 1] = self._board[coordinates[0]][coordinates[1]]
                return True

    def rec_make_move_f(self, playername, coordinates, direction):
        """A recursive helper function for moving F"""
        next_marble = self._board[coordinates[0] - 1][coordinates[1]]
        next_marble_coord = (coordinates[0] - 1, coordinates[1])
        edge_marble_coord = (0, coordinates[1])
        if next_marble == 'X':
            self._board[coordinates[0] - 1][coordinates[1]] = self._board[coordinates[0]][coordinates[1]]
            self._board[coordinates[0]][coordinates[1]] = 'X'
            # end turn
            return True
        # if next position is the last on board (edge)
        if next_marble_coord == edge_marble_coord:
            # check if the next marble is the players own marble, if it is then it is invalid
            player_marble = self.get_player_color(playername)
            if next_marble == player_marble:
                return False
            # check if the next marble is a red marble, if it is then move to players hand and push marble
            if next_marble == 'R':
                if playername == self._player_1:
                    self._player_1_captured += 1
                if playername == self._player_2:
                    self._player_2_captured += 1
                # move marble
                self._board[coordinates[0] - 1][coordinates[1]] = self._board[coordinates[0]][coordinates[1]]
                # end turn
                return True
            # if it reaches here it will automatically be the other player's marble
            else:
                # move marble
                self._board[coordinates[0] - 1][coordinates[1]] = self._board[coordinates[0]][coordinates[1]]
                # end turn
                return True
        # else if the next marble is not on the edge continue recursive function
        else:
            if self.rec_make_move_f(playername, (coordinates[0] - 1, coordinates[1]), direction):
                # move current to next
                self._board[coordinates[0] - 1][coordinates[1]] = self._board[coordinates[0]][coordinates[1]]
                return True

    def rec_make_move_b(self, playername, coordinates, direction):
        """A recursive helper function for moving B"""
        next_marble = self._board[coordinates[0] + 1][coordinates[1]]
        next_marble_coord = (coordinates[0] + 1, coordinates[1])
        edge_marble_coord = (6, coordinates[1])
        if next_marble == 'X':
            self._board[coordinates[0] + 1][coordinates[1]] = self._board[coordinates[0]][coordinates[1]]
            self._board[coordinates[0]][coordinates[1]] = 'X'
            # end turn
            return True
        # if next position is the last on board (edge)
        if next_marble_coord == edge_marble_coord:
            # check if the next marble is the players own marble, if it is then it is invalid
            player_marble = self.get_player_color(playername)
            if next_marble == player_marble:
                return False
            # check if the next marble is a red marble, if it is then move to players hand and push marble
            if next_marble == 'R':
                if playername == self._player_1:
                    self._player_1_captured += 1
                if playername == self._player_2:
                    self._player_2_captured += 1
                # move marble
                self._board[coordinates[0] + 1][coordinates[1]] = self._board[coordinates[0]][coordinates[1]]
                # end turn
                return True
            # if it reaches here it will automatically be the other player's marble
            else:
                # move marble
                self._board[coordinates[0] + 1][coordinates[1]] = self._board[coordinates[0]][coordinates[1]]
                # end turn
                return True
        # else if the next marble is not on the edge continue recursive function
        else:
            if self.rec_make_move_b(playername, (coordinates[0] + 1, coordinates[1]), direction):
                # move current to next
                self._board[coordinates[0] + 1][coordinates[1]] = self._board[coordinates[0]][coordinates[1]]
                return True

    def make_move(self, playername, coordinates, direction):
        """Moves the marbles on the board in the direction desired. Validates the move and is responsible for tracking
        whose turn it is. Takes as parameters playername, coordinates (tuple), and direction (L, R, F, or B). The
        playername is the player attempting to input the move, with coordinates of the marble and the direction
        they wish to move the marble. Returns True of move is successful, else returns False."""

        # create a copy of board for Ko rule
        # save this board
        self._last_board = copy.deepcopy(self._board)
        # save before player 1 goes, to check after player 2 goes
        if playername == self._player_1:
            self._last_player_1_board = copy.deepcopy(self._board)
        # save before player 2 goes, to check after player 1 goes
        if playername == self._player_2:
            self._last_player_2_board = copy.deepcopy(self._board)
        # validation
        # if game has been won return false
        if self.get_winner() is not None:
            return False

        # check if play is coming from the current player
        if self._current_turn is None:
            self._current_turn = playername
        if playername != self.get_current_turn():
            return False

        # check if the marble pushed is the correct color for the player
        board_marble = self.get_marble(coordinates)
        player_marble = self.get_player_color(playername)
        if board_marble != player_marble:
            return False

        # check if there is a marble on the opposite side from the direction the player is pushing
        if direction == 'L':
            right_side = (coordinates[0], 6)  # any row in column 6
            # if we are not on the right edge of the board
            if coordinates != right_side:
                if self._board[coordinates[0]][coordinates[1] + 1] != 'X':
                    return False
        if direction == 'R':
            left_side = (coordinates[0], 0)  # any row in column 0
            # if we are not on the left edge of the board
            if coordinates != left_side:
                if self._board[coordinates[0]][coordinates[1] - 1] != 'X':
                    return False
        if direction == 'F':
            back_side = (6, coordinates[1])  # any column in row 6
            # if we are not on the back edge of the board
            if coordinates != back_side:
                if self._board[coordinates[0] + 1][coordinates[1]] != 'X':
                    return False
        if direction == 'B':
            front_side = (0, coordinates[1])  # any column in row 0
            # if we are not on the front edge of the board
            if coordinates != front_side:
                if self._board[coordinates[0] - 1][coordinates[1]] != 'X':
                    return False

        # actual moves (1 marble move)
        if direction == 'L':
            next_marble = self._board[coordinates[0]][coordinates[1] - 1]
            next_marble_coord = (coordinates[0], coordinates[1] - 1)
            edge_marble_coord = (coordinates[0], 0)
            player_marble = self.get_player_color(playername)
            if next_marble == 'X':
                self._board[coordinates[0]][coordinates[1] - 1] = self._board[coordinates[0]][coordinates[1]]
                self._board[coordinates[0]][coordinates[1]] = 'X'
                self.end_of_turn(playername)
                return True
            # if next position is the last on board (edge)
            if next_marble_coord == edge_marble_coord:
                # check if the next marble is the players own marble, if it is then it is invalid
                if next_marble == player_marble:
                    return False
                # check if the next marble is a red marble, if it is then move to players hand and push marble
                if next_marble == 'R':
                    if playername == self._player_1:
                        self._player_1_captured += 1
                    if playername == self._player_2:
                        self._player_2_captured += 1
                    # move marble
                    self._board[coordinates[0]][coordinates[1] - 1] = self._board[coordinates[0]][coordinates[1]]
                    # current = X
                    self._board[coordinates[0]][coordinates[1]] = 'X'
                    self.end_of_turn(playername)
                    return True
                # if it reaches here it next marble will automatically be the other player's marble on the edge
                else:
                    # move marble
                    self._board[coordinates[0]][coordinates[1] - 1] = self._board[coordinates[0]][coordinates[1]]
                    # current = X
                    self._board[coordinates[0]][coordinates[1]] = 'X'
                    self.end_of_turn(playername)
                    return True
            # else if the next marble is not on the edge start recursive function
            else:
                if self.rec_make_move_l(playername, (coordinates[0], coordinates[1] - 1), direction):
                    # move marble
                    self._board[coordinates[0]][coordinates[1] - 1] = self._board[coordinates[0]][coordinates[1]]
                    # current = X
                    self._board[coordinates[0]][coordinates[1]] = 'X'
                    self.end_of_turn(playername)
                    return True

        if direction == 'R':
            next_marble = self._board[coordinates[0]][coordinates[1] + 1]
            next_marble_coord = (coordinates[0], coordinates[1] + 1)
            edge_marble_coord = (coordinates[0], 6)
            player_marble = self.get_player_color(playername)
            if next_marble == 'X':
                self._board[coordinates[0]][coordinates[1] + 1] = self._board[coordinates[0]][coordinates[1]]
                self._board[coordinates[0]][coordinates[1]] = 'X'
                self.end_of_turn(playername)
                return True
            # if next position is the last on board (edge)
            if next_marble_coord == edge_marble_coord:
                # check if the next marble is the players own marble, if it is then it is invalid
                if next_marble == player_marble:
                    return False
                # check if the next marble is a red marble, if it is then move to players hand and push marble
                if next_marble == 'R':
                    if playername == self._player_1:
                        self._player_1_captured += 1
                    if playername == self._player_2:
                        self._player_2_captured += 1
                    # move marble
                    self._board[coordinates[0]][coordinates[1] + 1] = self._board[coordinates[0]][coordinates[1]]
                    # current = X
                    self._board[coordinates[0]][coordinates[1]] = 'X'
                    self.end_of_turn(playername)
                    return True
                # if it reaches here it next marble will automatically be the other player's marble on the edge
                else:
                    # move marble
                    self._board[coordinates[0]][coordinates[1] + 1] = self._board[coordinates[0]][coordinates[1]]
                    # current = X
                    self._board[coordinates[0]][coordinates[1]] = 'X'
                    self.end_of_turn(playername)
                    return True
            # else if the next marble is not on the edge start recursive function
            else:
                if self.rec_make_move_r(playername, (coordinates[0], coordinates[1] + 1), direction):
                    # move marble
                    self._board[coordinates[0]][coordinates[1] + 1] = self._board[coordinates[0]][coordinates[1]]
                    # current = X
                    self._board[coordinates[0]][coordinates[1]] = 'X'
                    self.end_of_turn(playername)
                    return True

        if direction == 'F':
            next_marble = self._board[coordinates[0] - 1][coordinates[1]]
            next_marble_coord = (coordinates[0] - 1, coordinates[1])
            edge_marble_coord = (0, coordinates[1])
            player_marble = self.get_player_color(playername)
            if next_marble == 'X':
                self._board[coordinates[0] - 1][coordinates[1]] = self._board[coordinates[0]][coordinates[1]]
                self._board[coordinates[0]][coordinates[1]] = 'X'
                self.end_of_turn(playername)
                return True
            # if next position is the last on board (edge)
            if next_marble_coord == edge_marble_coord:
                # check if the next marble is the players own marble, if it is then it is invalid
                if next_marble == player_marble:
                    return False
                # check if the next marble is a red marble, if it is then move to players hand and push marble
                if next_marble == 'R':
                    if playername == self._player_1:
                        self._player_1_captured += 1
                    if playername == self._player_2:
                        self._player_2_captured += 1
                    # move marble
                    self._board[coordinates[0] - 1][coordinates[1]] = self._board[coordinates[0]][coordinates[1]]
                    # current = X
                    self._board[coordinates[0]][coordinates[1]] = 'X'
                    self.end_of_turn(playername)
                    return True
                # if it reaches here it next marble will automatically be the other player's marble on the edge
                else:
                    # move marble
                    self._board[coordinates[0] - 1][coordinates[1]] = self._board[coordinates[0]][coordinates[1]]
                    # current = X
                    self._board[coordinates[0]][coordinates[1]] = 'X'
                    self.end_of_turn(playername)
                    return True
            # else if the next marble is not on the edge start recursive function
            else:
                if self.rec_make_move_f(playername, (coordinates[0] - 1, coordinates[1]), direction):
                    # move marble
                    self._board[coordinates[0] - 1][coordinates[1]] = self._board[coordinates[0]][coordinates[1]]
                    # current = X
                    self._board[coordinates[0]][coordinates[1]] = 'X'
                    self.end_of_turn(playername)
                    return True

        if direction == 'B':
            next_marble = self._board[coordinates[0] + 1][coordinates[1]]
            next_marble_coord = (coordinates[0] + 1, coordinates[1])
            edge_marble_coord = (6, coordinates[1])
            player_marble = self.get_player_color(playername)
            if next_marble == 'X':
                self._board[coordinates[0] + 1][coordinates[1]] = self._board[coordinates[0]][coordinates[1]]
                self._board[coordinates[0]][coordinates[1]] = 'X'
                self.end_of_turn(playername)
                return True
            # if next position is the last on board (edge)
            if next_marble_coord == edge_marble_coord:
                # check if the next marble is the players own marble, if it is then it is invalid
                if next_marble == player_marble:
                    return False
                # check if the next marble is a red marble, if it is then move to players hand and push marble
                if next_marble == 'R':
                    if playername == self._player_1:
                        self._player_1_captured += 1
                    if playername == self._player_2:
                        self._player_2_captured += 1
                    # move marble
                    self._board[coordinates[0] + 1][coordinates[1]] = self._board[coordinates[0]][coordinates[1]]
                    # current = X
                    self._board[coordinates[0]][coordinates[1]] = 'X'
                    self.end_of_turn(playername)
                    return True
                # if it reaches here it next marble will automatically be the other player's marble on the edge
                else:
                    # move marble
                    self._board[coordinates[0] + 1][coordinates[1]] = self._board[coordinates[0]][coordinates[1]]
                    # current = X
                    self._board[coordinates[0]][coordinates[1]] = 'X'
                    self.end_of_turn(playername)
                    return True
            # else if the next marble is not on the edge start recursive function
            else:
                if self.rec_make_move_b(playername, (coordinates[0] + 1, coordinates[1]), direction):
                    # move marble
                    self._board[coordinates[0] + 1][coordinates[1]] = self._board[coordinates[0]][coordinates[1]]
                    # current = X
                    self._board[coordinates[0]][coordinates[1]] = 'X'
                    self.end_of_turn(playername)
                    return True

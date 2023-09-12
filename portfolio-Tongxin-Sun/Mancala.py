# Author: Tongxin Sun
# GitHub username: Tongxin Sun
# Date: 11/22/2022
# Description: Class definition for the Mancala game that allows two people
#              to play a text-based version of the game.

class Player:
    """
    Represents a player object with his/her name. Used by Mancala class.
    """
    def __init__(self, name):
        """The constructor for Player class. Takes a name as a string as parameter.
        Initializes the required data members. All data members are private."""
        self._name = name

    def get_name(self):
        """Returns the name of the player."""
        return self._name


class Mancala:
    """
    Represents the game Mancala with methods to create player, print the current board information,
    return the winner, and play game.
    """
    def __init__(self):
        self._seeds = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        self._players = []

    def create_player(self, player_name):
        """
        Returns the player as an object based on the user input of a player name as string.
        """
        player = Player(player_name)
        self._players.append(player)
        return player

    def print_board(self):
        """
        Prints the current board information for the game in the specified format.
        """
        print("player1:")
        print("store:", self._seeds[6])
        print(self._seeds[0:6])
        print("player2:")
        print("store:", self._seeds[13])
        print(self._seeds[7:13])

    def return_winner(self):
        """
        Returns the winner if the game is ended.
        Returns "It's a tie" if the game is a tie.
        Returns "Game has not ended" if the game is not ended yet.
        """
        if self._seeds[0:6] == self._seeds[7:13] == [0, 0, 0, 0, 0, 0]:
            if self._seeds[6] > self._seeds[13]:
                return "Winner is player 1: " + self._players[0].get_name()
            elif self._seeds[6] < self._seeds[13]:
                return "Winner is player 2: " + self._players[1].get_name()
            else:
                return "It's a tie"
        else:
            return "Game has not ended"

    def play_game(self, player_index, pit_index):
        """
        Plays the Mancala game based on the rules and the user input of player_index and pit_index.
        Updates the seeds number in each pit including the store.
        If the ending state of the game is reached, follows the rules and updates the seeds number
        in the pit and store for both players.
        Returns a list of the current seed number in the format of [player1 pit1, player1 pit2,
        player1 pit3, player1 pit4, player1 pit5, player1 pit6, player1 store, Player2 pit1,
        player2 pit2, player2 pit3, player2 pit4, player2 pit5, player2 pit6, player2 store]
        """
        if pit_index > 6 or pit_index <= 0:
            return "Invalid number for pit index"
        if self._seeds[0:6] == self._seeds[7:13] == [0, 0, 0, 0, 0, 0]:
            return "Game is ended"

        start = (player_index - 1) * 7 + pit_index - 1
        current = start
        num_seeds = self._seeds[start]
        while num_seeds > 0:
            current += 1

            if player_index == 1 and current == 13:
                current += 1
            if player_index == 2 and current == 6:
                current += 1

            if current >= 14:
                current %= 14

            if num_seeds == 1:
                if self._seeds[current] == 0:
                    if player_index == 1 and current < 6:
                        self._seeds[6] += 1 + self._seeds[12 - current]
                        self._seeds[12 - current] = 0
                        self._seeds[current] -= 1
                    if player_index == 2 and 6 < current < 13:
                        self._seeds[13] += 1 + self._seeds[12 - current]
                        self._seeds[12 - current] = 0
                        self._seeds[current] -= 1
                if player_index == 1 and current == 6:
                    print("player 1 take another turn")
                if player_index == 2 and current == 13:
                    print("player 2 take another turn")

            self._seeds[current] += 1
            num_seeds -= 1

        self._seeds[start] = 0

        if self._seeds[0:6] == [0, 0, 0, 0, 0, 0]:
            for each in self._seeds[7:13]:
                self._seeds[13] += each
                self._seeds[7:13] = [0, 0, 0, 0, 0, 0]
        elif self._seeds[7:13] == [0, 0, 0, 0, 0, 0]:
            for each in self._seeds[0:6]:
                self._seeds[6] += each
                self._seeds[0:6] = [0, 0, 0, 0, 0, 0]

        return self._seeds
game = Mancala()
player1 = game.create_player("Lily")
player2 = game.create_player("Lucy")
game.play_game(1, 1)
game.play_game(2, 2)
game.play_game(1, 3)
game.play_game(2, 4)
game.play_game(1, 5)
game.play_game(1, 6)
game.print_board()
print(game.return_winner())
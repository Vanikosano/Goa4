class Player:
    def __init__(self, player_id, username):
        self.player_id = player_id
        self.username = "Vaniko_Sano"
        self.cards = []

class CardGame:
    def __init__(self):
        self.players = []
        self.admins = []  # List of admin usernames

    def add_player(self, player):
        self.players.append(player)

    def add_admin(self, admin_username):
        self.admins.append(admin_username)

    def check_player_cards(self, admin_username, player_id):
        if admin_username not in self.admins:
            return "Permission denied. You are not authorized."

        player = next((p for p in self.players if p.player_id == player_id), None)

        if player:
            return f"Player {player.username}'s cards: {player.cards}"
        else:
            return f"Player with ID {player_id} not found."

# Example Usage:
game = CardGame()

player1 = Player(player_id=1, username="Player1")
player1.cards = ["CardA", "CardB", "CardC"]

player2 = Player(player_id=2, username="Player2")
player2.cards = ["CardX", "CardY", "CardZ"]

game.add_player(player1)
game.add_player(player2)
game.add_admin(admin_username="Admin1")

# Admin checking a player's cards
result = game.check_player_cards(admin_username="Admin1", player_id=1)
print(result)
import pathlib


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.high_score = 0

        # Reading High score till now
        contents = pathlib.Path('High_score.txt').read_text()
        self.high_score = int(contents)

        # Start game in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def update_high_score(self):
        # updating high score
        with open('High_score.txt', 'w') as file_object:
            file_object.write(str(self.high_score))
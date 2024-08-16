class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200    # 1920 for full screen
        self.screen_height = 800    # 1080 for full screen
        self.bg_color = (230, 230, 230)

        # Ship settings
        #self.ship_width = 40
        #self.ship_height = 40
        self.ship_speed = 2
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 8
        self.alien_points = 50
        # fleet_direction of 1 represents right; -1 represents left.
        #self.fleet_direction = 1
        #self.fleet_direction1 = 1
        #self.fleet_direction2 = 1

        # How quickly the game speeds up
        self.speedup_scale_for_ship = 0.1 * self.ship_speed
        self.speedup_scale_for_bullet = 0.1 * self.bullet_speed
        self.speedup_scale_for_alien = 0.1 * self.alien_speed

        # How quickly the alien point values increase
        self.score_scale = 0.2 * self.alien_points

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 2
        self.bullet_speed = 3
        self.alien_speed = 1

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed += self.speedup_scale_for_ship
        self.bullet_speed += self.speedup_scale_for_bullet
        self.alien_speed += self.speedup_scale_for_alien

        self.alien_points = int(self.alien_points + self.score_scale)
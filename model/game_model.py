class GameModel:
    def __init__(self):
        # Game state
        self.player = None
        self.current_level = None
        self.enemies = []
        self.items = []
        self.space_pressed = False  # Add space key state
        self.game_state = "MENU"  # States: MENU, GAME, SETTINGS, EXIT
        self.selected_menu_item = 0
        self.menu_items = ["Start Game", "Settings", "Exit"]
        self.running = True
        
        # Settings state
        self.settings_selected_item = 0
        self.main_volume = 100
        self.music_volume = 100
        self.fx_volume = 100
        self.settings_items = ["Main Volume", "Music Volume", "FX Volume", "Back"]
        self.active_slider = None  # For slider adjustment
        
    def update(self):
        # Update game state
        pass
        
    def initialize_level(self):
        # Initialize level layout and entities
        pass
        
    def add_enemy(self, enemy):
        self.enemies.append(enemy)
        
    def remove_enemy(self, enemy):
        if enemy in self.enemies:
            self.enemies.remove(enemy)
            
    def add_item(self, item):
        self.items.append(item)
        
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            
    def select_next_menu_item(self):
        self.selected_menu_item = (self.selected_menu_item + 1) % len(self.menu_items)
        
    def select_previous_menu_item(self):
        self.selected_menu_item = (self.selected_menu_item - 1) % len(self.menu_items)
        
    def select_menu_item(self):
        selected = self.menu_items[self.selected_menu_item]
        if selected == "Start Game":
            self.game_state = "GAME"
        elif selected == "Settings":
            self.game_state = "SETTINGS"
        elif selected == "Exit":
            self.game_state = "EXIT"
            self.running = False
            
    def select_next_settings_item(self):
        self.settings_selected_item = (self.settings_selected_item + 1) % len(self.settings_items)
        
    def select_previous_settings_item(self):
        self.settings_selected_item = (self.settings_selected_item - 1) % len(self.settings_items)
        
    def adjust_selected_volume(self, amount):
        if self.settings_selected_item == 0:  # Main Volume
            self.main_volume = max(0, min(100, self.main_volume + amount))
        elif self.settings_selected_item == 1:  # Music Volume
            self.music_volume = max(0, min(100, self.music_volume + amount))
        elif self.settings_selected_item == 2:  # FX Volume
            self.fx_volume = max(0, min(100, self.fx_volume + amount))
            
    def select_settings_item(self):
        if self.settings_items[self.settings_selected_item] == "Back":
            self.game_state = "MENU"

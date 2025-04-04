class GameModel:
    def __init__(self):
        # Game state
        self.player = None
        self.current_level = None
        self.enemies = []
        self.items = []
        self.space_pressed = False  # Add space key state
        self.game_state = "MENU"  # States: MENU, GAME, OPTIONS, SETTINGS, EXIT
        self.selected_menu_item = 0
        self.menu_items = ["Start Game", "Options", "Settings", "Exit"]
        self.running = True
        
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
        elif selected == "Options":
            self.game_state = "OPTIONS"
        elif selected == "Settings":
            self.game_state = "SETTINGS"
        elif selected == "Exit":
            self.running = False

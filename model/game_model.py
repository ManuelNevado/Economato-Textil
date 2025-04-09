class GameModel:
    def __init__(self):
        # Game state
        self.player = None
        self.current_level = None
        self.enemies = []
        self.items = []
        self.space_pressed = False  # Add space key state
        self.game_state = "MENU"  # States: MENU, GAME, SETTINGS, EXIT, SAVE_MENU
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
        
        # Save game menu state
        self.save_menu_selected_item = 0
        self.save_slots = [None, None, None]  # Will store save game names or None if empty
        self.save_menu_items = ["Slot 1", "Slot 2", "Slot 3", "Back"]
        
        # Mouse interaction state
        self.hovered_menu_item = -1
        self.hovered_settings_item = -1
        self.hovered_save_menu_item = -1
        self.is_dragging_slider = False
        self.dragged_slider_index = -1
        
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
            self.game_state = "SAVE_MENU"  # Changed from "GAME" to "SAVE_MENU"
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
            
    # Save game menu methods
    def select_next_save_slot(self):
        self.save_menu_selected_item = (self.save_menu_selected_item + 1) % len(self.save_menu_items)
        
    def select_previous_save_slot(self):
        self.save_menu_selected_item = (self.save_menu_selected_item - 1) % len(self.save_menu_items)
        
    def select_save_slot(self):
        selected = self.save_menu_items[self.save_menu_selected_item]
        if selected == "Back":
            self.game_state = "MENU"
        else:
            # Start game with selected save slot
            slot_index = self.save_menu_selected_item
            self.game_state = "GAME"
            # Here you would load the save file if it exists
            # For now, we'll just start a new game
            
    def get_save_slot_display_name(self, slot_index):
        """Returns the display name for a save slot"""
        if slot_index < 0 or slot_index >= len(self.save_slots):
            return "Invalid Slot"
            
        if self.save_slots[slot_index] is None:
            return "New Game"
        else:
            return self.save_slots[slot_index]

    def set_hovered_menu_item(self, index):
        """Set which menu item is being hovered by the mouse"""
        if 0 <= index < len(self.menu_items):
            self.hovered_menu_item = index
        else:
            self.hovered_menu_item = -1
            
    def set_hovered_settings_item(self, index):
        """Set which settings item is being hovered by the mouse"""
        if 0 <= index < len(self.settings_items):
            self.hovered_settings_item = index
        else:
            self.hovered_settings_item = -1
            
    def set_hovered_save_menu_item(self, index):
        """Set which save menu item is being hovered by the mouse"""
        if 0 <= index < len(self.save_menu_items):
            self.hovered_save_menu_item = index
        else:
            self.hovered_save_menu_item = -1
            
    def handle_menu_click(self, index):
        """Handle a mouse click on a menu item"""
        if 0 <= index < len(self.menu_items):
            self.selected_menu_item = index
            self.select_menu_item()
            
    def handle_settings_click(self, index):
        """Handle a mouse click on a settings item"""
        if 0 <= index < len(self.settings_items):
            self.settings_selected_item = index
            if index == len(self.settings_items) - 1:  # Back button
                self.select_settings_item()
                
    def handle_save_menu_click(self, index):
        """Handle a mouse click on a save menu item"""
        if 0 <= index < len(self.save_menu_items):
            self.save_menu_selected_item = index
            self.select_save_slot()
            
    def start_slider_drag(self, slider_index):
        """Start dragging a slider"""
        if 0 <= slider_index < len(self.settings_items) - 1:  # Exclude Back button
            self.is_dragging_slider = True
            self.dragged_slider_index = slider_index
            self.settings_selected_item = slider_index
            
    def end_slider_drag(self):
        """End dragging a slider"""
        self.is_dragging_slider = False
        self.dragged_slider_index = -1
        
    def update_slider_value(self, x_position, slider_rect):
        """Update a slider value based on mouse x position"""
        if not self.is_dragging_slider or self.dragged_slider_index < 0:
            return
            
        # Calculate percentage based on position within slider
        slider_start = slider_rect[0]
        slider_width = slider_rect[2]
        
        # Ensure x_position is within slider bounds
        x_position = max(slider_start, min(slider_start + slider_width, x_position))
        
        # Calculate percentage (0-100)
        percentage = int(((x_position - slider_start) / slider_width) * 100)
        
        # Update the appropriate volume
        if self.dragged_slider_index == 0:  # Main Volume
            self.main_volume = percentage
        elif self.dragged_slider_index == 1:  # Music Volume
            self.music_volume = percentage
        elif self.dragged_slider_index == 2:  # FX Volume
            self.fx_volume = percentage

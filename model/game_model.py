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
        
        # Red ball properties
        self.ball_x = 400  # Starting x position (center of screen)
        self.ball_y = 300  # Starting y position (center of screen)
        self.ball_radius = 20
        self.ball_speed = 5
        
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
        
        # Audio manager reference (will be set from main.py)
        self.audio_manager = None
        
    def set_audio_manager(self, audio_manager):
        """Set the audio manager reference and sync volume settings"""
        self.audio_manager = audio_manager
        
        # Sync volume settings
        self.audio_manager.update_main_volume(self.main_volume)
        self.audio_manager.update_music_volume(self.music_volume)
        self.audio_manager.update_fx_volume(self.fx_volume)
        
    def update(self):
        # Update game state
        if self.game_state == "GAME":
            # Any game state updates would go here
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
            
    def select_menu_item(self):
        """Handle menu item selection"""
        if self.selected_menu_item == 0:  # Start Game
            self.game_state = "SAVE_MENU"  # Changed from "GAME" to "SAVE_MENU"
            # Play game music if different from menu music
            if self.audio_manager and self.audio_manager.current_music == "menu":
                # For now we use the same music, but this could be changed later
                pass
        elif self.selected_menu_item == 1:  # Settings
            self.game_state = "SETTINGS"
        elif self.selected_menu_item == 2:  # Exit
            self.running = False
    
    def select_settings_item(self):
        """Handle settings item selection"""
        if self.settings_selected_item == 3:  # Back
            self.game_state = "MENU"
    
    def adjust_selected_volume(self, amount):
        """Adjust the selected volume slider by the given amount"""
        if self.settings_selected_item == 0:  # Main Volume
            self.main_volume = max(0, min(100, self.main_volume + amount))
            if self.audio_manager:
                self.audio_manager.update_main_volume(self.main_volume)
        elif self.settings_selected_item == 1:  # Music Volume
            self.music_volume = max(0, min(100, self.music_volume + amount))
            if self.audio_manager:
                self.audio_manager.update_music_volume(self.music_volume)
        elif self.settings_selected_item == 2:  # FX Volume
            self.fx_volume = max(0, min(100, self.fx_volume + amount))
            if self.audio_manager:
                self.audio_manager.update_fx_volume(self.fx_volume)
                
    def move_ball(self, dx, dy):
        """Move the ball by the given delta x and y, keeping it within screen bounds"""
        # Update ball position
        self.ball_x += dx * self.ball_speed
        self.ball_y += dy * self.ball_speed
        
        # Keep ball within screen bounds (800x600)
        self.ball_x = max(self.ball_radius, min(800 - self.ball_radius, self.ball_x))
        self.ball_y = max(self.ball_radius, min(600 - self.ball_radius, self.ball_y))
        
    def select_next_menu_item(self):
        self.selected_menu_item = (self.selected_menu_item + 1) % len(self.menu_items)
        
    def select_previous_menu_item(self):
        self.selected_menu_item = (self.selected_menu_item - 1) % len(self.menu_items)
        
    def select_next_settings_item(self):
        self.settings_selected_item = (self.settings_selected_item + 1) % len(self.settings_items)
        
    def select_previous_settings_item(self):
        self.settings_selected_item = (self.settings_selected_item - 1) % len(self.settings_items)
        
    def select_next_save_slot(self):
        self.save_menu_selected_item = (self.save_menu_selected_item + 1) % len(self.save_menu_items)
        
    def select_previous_save_slot(self):
        self.save_menu_selected_item = (self.save_menu_selected_item - 1) % len(self.save_menu_items)
        
    # Mouse interaction methods
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
            
    def select_save_slot(self):
        """Handle save slot selection"""
        if self.save_menu_selected_item < 3:  # Selected a save slot
            # Enter the game with the selected slot
            self.game_state = "GAME"
            # Reset ball position to center
            self.ball_x = 400
            self.ball_y = 300
        else:  # Selected Back
            self.game_state = "MENU"
            
    def get_save_slot_display_name(self, slot_index):
        """Returns the display name for a save slot"""
        if slot_index < 0 or slot_index >= len(self.save_slots):
            return "Invalid Slot"
            
        if self.save_slots[slot_index] is None:
            return "New Game"
        else:
            return self.save_slots[slot_index]

    def update_slider_value(self, mouse_x, slider_rect):
        """Update slider value based on mouse position"""
        if not slider_rect:
            return
            
        # Calculate percentage based on mouse position
        slider_start = slider_rect[0]
        slider_width = slider_rect[2]
        relative_x = max(0, min(slider_width, mouse_x - slider_start))
        percentage = int((relative_x / slider_width) * 100)
        
        # Update the appropriate volume
        if self.dragged_slider_index == 0:  # Main Volume
            self.main_volume = percentage
            if self.audio_manager:
                self.audio_manager.update_main_volume(self.main_volume)
        elif self.dragged_slider_index == 1:  # Music Volume
            self.music_volume = percentage
            if self.audio_manager:
                self.audio_manager.update_music_volume(self.music_volume)
        elif self.dragged_slider_index == 2:  # FX Volume
            self.fx_volume = percentage
            if self.audio_manager:
                self.audio_manager.update_fx_volume(self.fx_volume)
    
    def start_slider_drag(self, slider_index):
        """Start dragging a slider"""
        self.is_dragging_slider = True
        self.dragged_slider_index = slider_index
    
    def end_slider_drag(self):
        """End dragging a slider"""
        self.is_dragging_slider = False
        self.dragged_slider_index = -1

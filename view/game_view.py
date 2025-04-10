import pygame
import os

class GameView:
    def __init__(self, screen):
        self.screen = screen
        self.background_color = (0, 0, 0)  # Black background
        pygame.font.init()
        self.font = pygame.font.Font(None, 48)  # Default font, size 48
        
        # Load and process background image
        bg_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'sala_pasos_perdidos.jpg')
        self.background_image = pygame.image.load(bg_path)
        self.background_image = pygame.transform.scale(self.background_image, (self.screen.get_width(), self.screen.get_height()))
        
        # Create blurred version of background
        self.blurred_background = self._create_blurred_surface(self.background_image)
        
        # Store rectangles for mouse interaction
        self.menu_item_rects = []
        self.settings_item_rects = []
        self.save_menu_item_rects = []
        self.slider_rects = []
        
    def _create_blurred_surface(self, surface):
        # Create a smaller version of the image (downscale)
        scale_factor = 4  # Higher number = more blur
        small_surface = pygame.transform.scale(surface, 
                                            (surface.get_width() // scale_factor, 
                                             surface.get_height() // scale_factor))
        # Scale it back up to create blur effect
        return pygame.transform.scale(small_surface, 
                                    (surface.get_width(), surface.get_height()))
        
    def render(self, model):
        # Clear the screen
        self.screen.fill(self.background_color)
        
        if model.game_state == "MENU":
            self._render_menu(model)
        elif model.game_state == "SETTINGS":
            self._render_settings(model)
        elif model.game_state == "SAVE_MENU":
            self._render_save_menu(model)
        elif model.game_state == "GAME":
            self._render_game(model)
        else:
            # Draw background
            self.screen.blit(self.background_image, (0, 0))
            
            # Add a semi-transparent overlay to make text more readable
            overlay = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
            overlay.fill((0, 0, 0))
            overlay.set_alpha(128)  # 128 is half transparent
            self.screen.blit(overlay, (0, 0))
            
            # Render game elements
            self._render_level(model.current_level)
            if model.player:
                self._render_player(model.player)
            for enemy in model.enemies:
                self._render_enemy(enemy)
            for item in model.items:
                self._render_item(item)
    
    def _render_menu(self, model):
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        
        # Draw blurred background
        self.screen.blit(self.blurred_background, (0, 0))
        
        # Add a semi-transparent overlay to make text more readable
        overlay = pygame.Surface((screen_width, screen_height))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(160)  # Slightly more opaque for better contrast
        self.screen.blit(overlay, (0, 0))
        
        # Title
        title = self.font.render("Economato-Textil", True, (255, 255, 255))
        title_rect = title.get_rect(center=(screen_width // 2, screen_height // 4))
        self.screen.blit(title, title_rect)
        
        # Reset menu item rects
        self.menu_item_rects = []
        
        # Menu items
        for i, item in enumerate(model.menu_items):
            # Determine color based on selection or hover
            if i == model.selected_menu_item:
                color = (0, 150, 255)  # Blue for selected
            elif i == model.hovered_menu_item:
                color = (100, 200, 255)  # Light blue for hover
            else:
                color = (255, 255, 255)  # White for normal
                
            text = self.font.render(item, True, color)
            rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + i * 60))
            self.screen.blit(text, rect)
            
            # Store rectangle for mouse interaction
            self.menu_item_rects.append(rect)
        
    def _render_settings(self, model):
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        
        # Draw blurred background
        self.screen.blit(self.blurred_background, (0, 0))
        
        # Add overlay
        overlay = pygame.Surface((screen_width, screen_height))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(160)
        self.screen.blit(overlay, (0, 0))
        
        # Title
        title = self.font.render("Settings", True, (255, 255, 255))
        title_rect = title.get_rect(center=(screen_width // 2, screen_height // 4))
        self.screen.blit(title, title_rect)
        
        # Reset settings item rects and slider rects
        self.settings_item_rects = []
        self.slider_rects = []
        
        # Settings items with sliders
        for i, item in enumerate(model.settings_items):
            y_pos = screen_height // 2 + i * 60
            
            # Determine text color based on selection or hover
            if i == model.settings_selected_item:
                color = (0, 150, 255)  # Blue for selected
            elif i == model.hovered_settings_item:
                color = (100, 200, 255)  # Light blue for hover
            else:
                color = (255, 255, 255)  # White for normal
                
            # Text
            text = self.font.render(item, True, color)
            text_rect = text.get_rect(midright=(screen_width // 2 - 20, y_pos))
            self.screen.blit(text, text_rect)
            
            # Store rectangle for mouse interaction
            self.settings_item_rects.append(text_rect)
            
            # Render slider for volume controls
            if item != "Back":
                # Get the appropriate volume value
                if item == "Main Volume":
                    value = model.main_volume
                elif item == "Music Volume":
                    value = model.music_volume
                else:  # FX Volume
                    value = model.fx_volume
                
                # Slider background
                slider_width = 200
                slider_height = 10
                slider_x = screen_width // 2 + 20
                slider_y = y_pos - slider_height // 2
                
                slider_rect = (slider_x, slider_y, slider_width, slider_height)
                self.slider_rects.append(slider_rect)
                
                pygame.draw.rect(self.screen, (100, 100, 100), slider_rect)
                
                # Slider fill
                fill_width = int(slider_width * (value / 100))
                pygame.draw.rect(self.screen, (0, 150, 255),
                               (slider_x, slider_y, fill_width, slider_height))
                
                # Slider handle
                handle_x = slider_x + fill_width - 2
                handle_height = 20
                pygame.draw.rect(self.screen, (200, 200, 200),
                               (handle_x, y_pos - handle_height // 2, 4, handle_height))
            else:
                # Add an empty placeholder for the "Back" option
                self.slider_rects.append(None)
    
    def _render_save_menu(self, model):
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        
        # Draw blurred background
        self.screen.blit(self.blurred_background, (0, 0))
        
        # Add a semi-transparent overlay to make text more readable
        overlay = pygame.Surface((screen_width, screen_height))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(160)  # Slightly more opaque for better contrast
        self.screen.blit(overlay, (0, 0))
        
        # Title
        title = self.font.render("Select Save Slot", True, (255, 255, 255))
        title_rect = title.get_rect(center=(screen_width // 2, screen_height // 4))
        self.screen.blit(title, title_rect)
        
        # Reset save menu item rects
        self.save_menu_item_rects = []
        
        # Save slots
        for i in range(3):
            # Get display name for the slot
            slot_name = model.get_save_slot_display_name(i)
            
            # Determine color based on selection or hover
            if i == model.save_menu_selected_item:
                color = (0, 150, 255)  # Blue for selected
            elif i == model.hovered_save_menu_item:
                color = (100, 200, 255)  # Light blue for hover
            else:
                color = (255, 255, 255)  # White for normal
            
            # Render slot with number
            text = self.font.render(f"Slot {i+1}: {slot_name}", True, color)
            rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + i * 60))
            self.screen.blit(text, rect)
            
            # Store rectangle for mouse interaction
            self.save_menu_item_rects.append(rect)
        
        # Back option
        # Determine color based on selection or hover
        if 3 == model.save_menu_selected_item:
            color = (0, 150, 255)  # Blue for selected
        elif 3 == model.hovered_save_menu_item:
            color = (100, 200, 255)  # Light blue for hover
        else:
            color = (255, 255, 255)  # White for normal
            
        text = self.font.render("Back", True, color)
        rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + 3 * 60))
        self.screen.blit(text, rect)
        
        # Store rectangle for mouse interaction
        self.save_menu_item_rects.append(rect)
    
    def _render_game(self, model):
        """Render the game state with the red ball on black background"""
        # Fill screen with black background
        self.screen.fill((0, 0, 0))
        
        # Draw the red ball
        pygame.draw.circle(
            self.screen, 
            (255, 0, 0),  # Red color
            (int(model.ball_x), int(model.ball_y)),  # Position
            model.ball_radius  # Radius
        )
        
        # Draw instructions text
        instructions = self.font.render("Use arrow keys to move", True, (255, 255, 255))
        instructions_rect = instructions.get_rect(center=(self.screen.get_width() // 2, 30))
        self.screen.blit(instructions, instructions_rect)
        
        # Draw ESC text
        esc_text = pygame.font.Font(None, 24).render("Press ESC to return to menu", True, (200, 200, 200))
        esc_rect = esc_text.get_rect(bottomright=(self.screen.get_width() - 10, self.screen.get_height() - 10))
        self.screen.blit(esc_text, esc_rect)
    
    def _render_level(self, level):
        # Render level layout
        if level:
            pass  # Add level rendering logic
    
    def _render_player(self, player):
        # Render player sprite
        if player:
            pass  # Add player rendering logic
    
    def _render_enemy(self, enemy):
        # Render enemy sprite
        pass  # Add enemy rendering logic
    
    def _render_item(self, item):
        # Render item sprite
        pass  # Add item rendering logic
        
    def get_menu_item_at_position(self, pos):
        """Return the index of the menu item at the given position, or -1 if none"""
        for i, rect in enumerate(self.menu_item_rects):
            if rect.collidepoint(pos):
                return i
        return -1
        
    def get_settings_item_at_position(self, pos):
        """Return the index of the settings item at the given position, or -1 if none"""
        for i, rect in enumerate(self.settings_item_rects):
            if rect and rect.collidepoint(pos):
                return i
        return -1
        
    def get_save_menu_item_at_position(self, pos):
        """Return the index of the save menu item at the given position, or -1 if none"""
        for i, rect in enumerate(self.save_menu_item_rects):
            if rect.collidepoint(pos):
                return i
        return -1
        
    def get_slider_at_position(self, pos):
        """Return the index of the slider at the given position and whether it's on a slider"""
        for i, rect in enumerate(self.slider_rects):
            if rect and pygame.Rect(rect).collidepoint(pos):
                return i, True
        return -1, False
        
    def get_slider_rects(self):
        """Return the list of slider rectangles"""
        return self.slider_rects

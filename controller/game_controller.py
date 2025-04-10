import pygame

class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.model.game_state == "MENU":
                self._handle_menu_input(event)
            elif self.model.game_state == "SETTINGS":
                self._handle_settings_input(event)
            elif self.model.game_state == "SAVE_MENU":
                self._handle_save_menu_input(event)
            else:
                self._handle_game_input(event)
        
        # Handle mouse events
        elif event.type == pygame.MOUSEMOTION:
            self._handle_mouse_motion(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                self._handle_mouse_down(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                self._handle_mouse_up(event.pos)
                
    def update(self):
        # Update game state
        self.model.update()
        
        # Move the ball based on key states when in GAME state
        if self.model.game_state == "GAME":
            keys = pygame.key.get_pressed()
            dx, dy = 0, 0
            
            if keys[pygame.K_LEFT]:
                dx = -1
            if keys[pygame.K_RIGHT]:
                dx = 1
            if keys[pygame.K_UP]:
                dy = -1
            if keys[pygame.K_DOWN]:
                dy = 1
                
            # Apply movement if any direction key is pressed
            if dx != 0 or dy != 0:
                self.model.move_ball(dx, dy)
        
        # Update slider if dragging
        if self.model.is_dragging_slider:
            mouse_pos = pygame.mouse.get_pos()
            slider_rects = self.view.get_slider_rects()
            if self.model.dragged_slider_index >= 0 and self.model.dragged_slider_index < len(slider_rects):
                self.model.update_slider_value(mouse_pos[0], slider_rects[self.model.dragged_slider_index])
        
    def _handle_menu_input(self, event):
        if event.key == pygame.K_UP:
            self.model.select_previous_menu_item()
        elif event.key == pygame.K_DOWN:
            self.model.select_next_menu_item()
        elif event.key == pygame.K_RETURN:
            self.model.select_menu_item()
        elif event.key == pygame.K_ESCAPE and self.model.game_state != "MENU":
            self.model.game_state = "MENU"
            
    def _handle_settings_input(self, event):
        if event.key == pygame.K_UP:
            self.model.select_previous_settings_item()
        elif event.key == pygame.K_DOWN:
            self.model.select_next_settings_item()
        elif event.key == pygame.K_LEFT:
            if self.model.settings_selected_item < 3:  # Not on "Back" button
                self.model.adjust_selected_volume(-5)
        elif event.key == pygame.K_RIGHT:
            if self.model.settings_selected_item < 3:  # Not on "Back" button
                self.model.adjust_selected_volume(5)
        elif event.key == pygame.K_RETURN:
            self.model.select_settings_item()
        elif event.key == pygame.K_ESCAPE:
            self.model.game_state = "MENU"

    def _handle_game_input(self, event):
        if event.key == pygame.K_ESCAPE:
            self.model.game_state = "MENU"
            
    def _handle_save_menu_input(self, event):
        """Handle keyboard input for the save menu"""
        if event.key == pygame.K_UP:
            self.model.select_previous_save_slot()
        elif event.key == pygame.K_DOWN:
            self.model.select_next_save_slot()
        elif event.key == pygame.K_RETURN:
            self.model.select_save_slot()
        elif event.key == pygame.K_ESCAPE:
            self.model.game_state = "MENU"
            
    def _handle_mouse_motion(self, pos):
        """Handle mouse movement events"""
        if self.model.game_state == "MENU":
            # Check if mouse is hovering over menu items
            menu_item_index = self.view.get_menu_item_at_position(pos)
            self.model.set_hovered_menu_item(menu_item_index)
            
        elif self.model.game_state == "SETTINGS":
            # Check if mouse is hovering over settings items
            settings_item_index = self.view.get_settings_item_at_position(pos)
            self.model.set_hovered_settings_item(settings_item_index)
            
        elif self.model.game_state == "SAVE_MENU":
            # Check if mouse is hovering over save menu items
            save_menu_item_index = self.view.get_save_menu_item_at_position(pos)
            self.model.set_hovered_save_menu_item(save_menu_item_index)
    
    def _handle_mouse_down(self, pos):
        """Handle mouse button down events"""
        if self.model.game_state == "MENU":
            menu_item_index = self.view.get_menu_item_at_position(pos)
            if menu_item_index >= 0:
                self.model.handle_menu_click(menu_item_index)
                
        elif self.model.game_state == "SETTINGS":
            settings_item_index = self.view.get_settings_item_at_position(pos)
            
            # Check if clicking on a slider
            slider_index, is_on_slider = self.view.get_slider_at_position(pos)
            if is_on_slider and slider_index >= 0:
                self.model.start_slider_drag(slider_index)
                # Update slider value immediately
                slider_rects = self.view.get_slider_rects()
                if slider_index < len(slider_rects):
                    self.model.update_slider_value(pos[0], slider_rects[slider_index])
            elif settings_item_index >= 0:
                self.model.handle_settings_click(settings_item_index)
                
        elif self.model.game_state == "SAVE_MENU":
            save_menu_item_index = self.view.get_save_menu_item_at_position(pos)
            if save_menu_item_index >= 0:
                self.model.handle_save_menu_click(save_menu_item_index)
    
    def _handle_mouse_up(self, pos):
        """Handle mouse button up events"""
        # End slider dragging if applicable
        if self.model.is_dragging_slider:
            self.model.end_slider_drag()

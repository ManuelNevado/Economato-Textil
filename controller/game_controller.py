import pygame

class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.model.game_state == "MENU":
                self._handle_menu_input(event)
            else:
                self._handle_game_input(event)
                
    def update(self):
        # Update game state
        self.model.update()
        
    def _handle_menu_input(self, event):
        if event.key == pygame.K_UP:
            self.model.select_previous_menu_item()
        elif event.key == pygame.K_DOWN:
            self.model.select_next_menu_item()
        elif event.key == pygame.K_RETURN:
            self.model.select_menu_item()
        elif event.key == pygame.K_ESCAPE and self.model.game_state != "MENU":
            self.model.game_state = "MENU"
            
    def _handle_game_input(self, event):
        if event.key == pygame.K_LEFT:
            pass  # Add player movement left
        elif event.key == pygame.K_RIGHT:
            pass  # Add player movement right
        elif event.key == pygame.K_ESCAPE:
            self.model.game_state = "MENU"

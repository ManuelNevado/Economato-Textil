import pygame
import sys
from model.game_model import GameModel
from view.game_view import GameView
from controller.game_controller import GameController

class Game:
    def __init__(self):
        pygame.init()
        self.WINDOW_SIZE = (800, 600)
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption("Castlevania Roguelike")
        
        # Initialize MVC components
        self.model = GameModel()
        self.view = GameView(self.screen)
        self.controller = GameController(self.model, self.view)
        
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.controller.handle_event(event)
            
            # Update game state
            self.controller.update()
            
            # Render
            self.view.render(self.model)
            
            # Cap the framerate
            self.clock.tick(60)
            
            # Update display
            pygame.display.flip()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
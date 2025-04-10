import pygame
import sys
import os
from model.game_model import GameModel
from view.game_view import GameView
from controller.game_controller import GameController
from audio.audio_manager import AudioManager

class Game:
    def __init__(self):
        pygame.init()
        self.WINDOW_SIZE = (800, 600)
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption("Economato-Textil")
        
        # Initialize audio manager
        self.audio_manager = AudioManager()
        
        # Initialize MVC components
        self.model = GameModel()
        self.view = GameView(self.screen)
        self.controller = GameController(self.model, self.view)
        
        # Set audio manager in model
        self.model.set_audio_manager(self.audio_manager)
        
        # Start playing menu music
        self.audio_manager.play_music('menu')
        
        self.clock = pygame.time.Clock()

    def run(self):
        while self.model.running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.model.running = False
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
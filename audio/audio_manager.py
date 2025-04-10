import pygame
import os

class AudioManager:
    def __init__(self):
        # Initialize pygame mixer
        pygame.mixer.init()
        
        # Music tracks
        self.music_tracks = {}
        
        # Sound effects
        self.sound_effects = {}
        
        # Volume levels (0-100)
        self.main_volume = 100
        self.music_volume = 100
        self.fx_volume = 100
        
        # Current playing music
        self.current_music = None
        
        # Base paths
        self.base_path = os.path.dirname(os.path.dirname(__file__))
        self.music_path = os.path.join(self.base_path, 'music_processing')
        self.fx_path = os.path.join(self.base_path, 'music_processing')
        
        # Load default music
        self.load_music('menu', 'holy-pipes.mp3')
    
    def load_music(self, name, filename):
        """Load a music track"""
        # Check if file is in music directory
        full_path = os.path.join(self.music_path, filename)
        
        if os.path.exists(full_path):
            self.music_tracks[name] = full_path
            return True
        else:
            print(f"Warning: Music file {filename} not found at {full_path}")
            return False
    
    def load_sound(self, name, filename):
        """Load a sound effect"""
        full_path = os.path.join(self.fx_path, filename)
        if os.path.exists(full_path):
            self.sound_effects[name] = pygame.mixer.Sound(full_path)
            return True
        else:
            print(f"Warning: Sound file {filename} not found")
            return False
    
    def play_music(self, name, loop=-1):
        """Play a music track"""
        if name in self.music_tracks:
            pygame.mixer.music.load(self.music_tracks[name])
            pygame.mixer.music.play(loop)
            self.current_music = name
            self.update_music_volume()
            return True
        return False
    
    def stop_music(self):
        """Stop the currently playing music"""
        pygame.mixer.music.stop()
        self.current_music = None
    
    def play_sound(self, name):
        """Play a sound effect"""
        if name in self.sound_effects:
            # Apply volume
            self.sound_effects[name].set_volume(self.fx_volume / 100 * (self.main_volume / 100))
            self.sound_effects[name].play()
            return True
        return False
    
    def update_main_volume(self, volume):
        """Update the main volume"""
        self.main_volume = max(0, min(100, volume))
        self.update_music_volume()
    
    def update_music_volume(self, volume=None):
        """Update the music volume"""
        if volume is not None:
            self.music_volume = max(0, min(100, volume))
        
        # Calculate effective volume (main * music)
        effective_volume = (self.main_volume / 100) * (self.music_volume / 100)
        pygame.mixer.music.set_volume(effective_volume)
    
    def update_fx_volume(self, volume):
        """Update the sound effects volume"""
        self.fx_volume = max(0, min(100, volume))
        # Sound effects volume is applied when playing

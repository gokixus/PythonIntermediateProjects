import pygame
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import sys

class MusicPlayer(QWidget):
    def __init__(self, musicFolder):
        super().__init__()
        pygame.mixer.init()
        
        self.currentMusic = None
        self.volume = 0.5
        self.musicFolder = musicFolder
        self.musics = self.musicFromFolder(musicFolder)
        
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("MP3 Player")
        self.geometry(320, 240)
        self.layout = QVBoxLayout()
        
    def playMusic(self):
        pass

    def randomMusic(self):
        pass
    
    def playSelectedMusic():
        pass
    
    def musicFromFolder(self):
        pass
    
    
musicFolder = "music"
app = QApplication(sys.argv)
win = MusicPlayer(musicFolder)
win.show()
sys.exit(app.exec_())
    
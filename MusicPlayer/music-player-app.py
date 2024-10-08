import pygame
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QListWidget, QSlider
import sys
import os
import random

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
        self.setFixedSize(320, 240)
        layout = QVBoxLayout()
        
        self.setLayout(layout)
        
        self.currentMusicLabel = QLabel("Music currently playing: None")
        layout.addWidget(self.currentMusicLabel)
        
        # Music List
        self.musicList = QListWidget()
        self.populateMusicList()
        self.musicList.itemClicked.connect(self.playSelectedMusic)
        layout.addWidget(self.musicList)
        
        # Music Volume
        self.volumeSlider = QSlider()
        self.volumeSlider.setValue(int(self.volume * 100))
        self.volumeSlider.valueChanged.connect(self.setVolume)
        layout.addWidget(QLabel("Sound Volume"))
        layout.addWidget(self.volumeSlider)
        
        # Random Music 
        self.random_button = QPushButton('Random Music')
        self.random_button.clicked.connect(self.randomMusic)
        layout.addWidget(self.random_button)
        
    def playMusic(self, music):
        self.currentMusic = music
        self.currentMusicLabel.setText(f"Music currently playing: {os.path.basename(music)}")
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()

    def randomMusic(self):
        if not self.musics:
            return
        
        music = random.choice(self.musics)
        self.playMusic(music)
    
    def playSelectedMusic(self, item):
        music = os.path.join(self.musicFolder, item.text())
        self.playMusic(music)
    
    def musicFromFolder(self, folder):
        supportedFormat = (".mp3")
        musics = [os.path.join(folder, file) for file in os.listdir(folder) if file.endswith(supportedFormat)]
        return musics

    def populateMusicList(self):
        for music in self.musics:
            self.musicList.addItem(os.path.basename(music))
            
    def setVolume(self):
        self.volume = self.volumeSlider.value() / 100
        pygame.mixer.music.set_volume(self.volume)
    
    
musicFolder = "music"
app = QApplication(sys.argv)
win = MusicPlayer(musicFolder)
win.show()
sys.exit(app.exec_())

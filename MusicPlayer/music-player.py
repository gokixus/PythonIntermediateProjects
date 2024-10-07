import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()

    def play_music(self, file):
        file_path = os.path.join('music', file)
        if os.path.exists(file_path):
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            print(f"{file_path} is playing.")
        else:
            print(f"Error: {file_path} not found. Please check the file path.")

    def stop_music(self):
        pygame.mixer.music.stop()
        print("The music has been stopped")

    def pause_music(self):
        pygame.mixer.music.pause()
        print("The music is paused")

    def unpause_music(self):
        pygame.mixer.music.unpause()
        print("The music is unpaused")

    def run(self):
        print("Music Player")
        while True:
            print("\nOptions".center(10,"-"))
            print("1- Play Music")
            print("2- Stop Music")
            print("3- Pause Music")
            print("4- Unpause Music")
            print("5- Exit")
            
            choice = input("Your choice: ")
            if choice == "1":
                file = input("Music file name (e.g., song.mp3): ")
                self.play_music(file)
            elif choice == "2":
                self.stop_music()
            elif choice == "3":
                self.pause_music()
            elif choice == "4":
                self.unpause_music()
            elif choice == "5":
                print("Exiting, please wait.")
                break
            else:
                print("Invalid option. Please enter a valid option.")

# Create an instance of MusicPlayer and run it
player = MusicPlayer()
player.run()

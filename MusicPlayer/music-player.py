import pygame, os

pygame.mixer.init()

def playMusic(file):
    if os.path.exists(file):
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        print(f"{file} is playing.")
    else:
        print(f"{file} not found.")
    
def stopMusic():
    pygame.mixer.music.stop()
    print("The music has been stopped")

def pauseMusic():
    pygame.mixer.music.pause()
    print("The music is paused")

def unpauseMusic():
    pygame.mixer.music.unpause()
    print("The music is unpaused")

def musicPlayer():
    print("Music Player")
    while True:
        print("\nOptions".center(10,"-"))
        print("1- Play Music")
        print("2- Stop Music")
        print("3- Pause Music")
        print("4- Unpause Music")
        print("5- Out")
        
        choice = input("Your choice: ")
        if choice == "1":
            file = input("Music file name: ")
            playMusic(file)
        if choice == "2":
            stopMusic()
        if choice == "3":
            pauseMusic()
        if choice == "4":
            unpauseMusic()
        if choice == "5":
            print("Exiting, please wait.")
            break
        else:
            print("Wrong option. Please enter the correct option!")
            
musicPlayer()
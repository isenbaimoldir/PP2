import pygame
import os

pygame.init()

window_size = (400, 200)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Song Player')
songs = ['black_or_white.mp3', 'chop_suey.mp3', 'tell_me.mp3', 'fourth.mp3'] 
current_song_index = 0


current_song = songs[current_song_index]
pygame.mixer.music.load(current_song)

def play_current_song():
    pygame.mixer.music.play()

def pause_current_song():
    pygame.mixer.music.pause()

def unpause_current_song():
    pygame.mixer.music.unpause()

def stop_current_song():
    pygame.mixer.music.stop()

def set_volume(volume):
    pygame.mixer.music.set_volume(volume)

def play_next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)  
    current_song = songs[current_song_index]
    pygame.mixer.music.load(current_song)
    pygame.mixer.music.play()

def play_previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)  
    current_song = songs[current_song_index]
    pygame.mixer.music.load(current_song)
    pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  
                play_current_song()
            elif event.key == pygame.K_s:  
                stop_current_song()
            elif event.key == pygame.K_SPACE:  
                if pygame.mixer.music.get_busy():
                    if pygame.mixer.music.get_pos() > 0:
                        pause_current_song()
                    else:  # Song is paused
                        unpause_current_song()
            elif event.key == pygame.K_RIGHT:  
                play_next_song()
            elif event.key == pygame.K_LEFT:
                play_previous_song()
            elif event.key == pygame.K_UP:  
                volume = min(1.0, pygame.mixer.music.get_volume() + 0.1)
                set_volume(volume)
            elif event.key == pygame.K_DOWN:  
                volume = max(0.0, pygame.mixer.music.get_volume() - 0.1)
                set_volume(volume)

pygame.quit()

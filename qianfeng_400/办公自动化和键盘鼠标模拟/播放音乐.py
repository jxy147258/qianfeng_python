import pygame
import time

filepath = r"yinyue.mp3"

pygame.mixer.init()

track = pygame.mixer.music.load(filepath)

# 播放
pygame.mixer.music.play()

# 持续时间
time.sleep(3)

#暂停
pygame.mixer.music.pause()

# 停止播放
pygame.mixer.music.stop()


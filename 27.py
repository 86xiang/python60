import wx
import os
import pygame
import random
import time
import threading


class wxGUI(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title='MP3Player', size=(250, 150), pos=(350, 350))
        panel = wx.Panel(frame, -1)

        self.buttonOK = wx.Button(panel, -1, 'Play', pos=(30, 60))
        self.Bind(wx.EVT_BUTTON, self.OnButtonOK, self.buttonOK)
        self.buttonOK.Enabled = True

        self.buttonCancel = wx.Button(panel, -1, 'Stop', pos=(120, 60))
        self.Bind(wx.EVT_BUTTON, self.OnButtonCancel, self.buttonCancel)
        self.buttonCancel.Enabled = False

        frame.Show()
        return True

    def OnExit(self):
        try:
            self.playing = False
            pygame.mixer.music.stop()
        finally:
            pass

    def play(self):
        folder = r'h:\music'
        musics = [folder + '\\' + music for music in os.listdir(folder) if music.endswith('.mp3')]
        total = len(musics)
        pygame.mixer.init()
        while self.playing:
            if not pygame.mixer.music.get_busy():
                nextMusic = random.choice(musics)
                pygame.mixer.music.load(nextMusic)
                pygame.mixer.music.play(1)
                print
                'playing....', nextMusic
            else:
                time.sleep(1)

    def OnButtonOK(self, event):
        self.playing = True
        # create a new thread to play music
        t = threading.Thread(target=self.play)
        t.start()
        self.buttonOK.Enabled = False
        self.buttonCancel.Enabled = True

    def OnButtonCancel(self, event):
        self.playing = False
        pygame.mixer.music.stop()
        self.buttonOK.Enabled = True
        self.buttonCancel.Enabled = False


app = wxGUI()
app.MainLoop()

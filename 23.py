import wx


class wxGUI(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title='wxGUI', size=(160, 140))
        panel = wx.Panel(frame, -1)

        self.buttonOK = wx.Button(panel, -1, 'Start', pos=(0, 0))
        self.Bind(wx.EVT_BUTTON, self.OnButtonOK, self.buttonOK)

        frame.Show()
        return True

    def OnButtonOK(self, event):
        text = self.buttonOK.GetLabelText()
        if text == 'Start':
            self.buttonOK.SetLabelText('End')
        elif text == 'End':
            self.buttonOK.SetLabelText('Start')


app = wxGUI()
app.MainLoop()

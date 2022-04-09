import win32api,win32con

print(win32api.GetCursorPos()) #get position

win32api.SetCursorPos([100,100]) #Move to (100,100)

win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0) #click left button

from time import sleep
import pyautogui
import win32gui

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def showDiscordWindow():
    if __name__ == '__main__':
        top_windows = []
        win32gui.EnumWindows(windowEnumerationHandler, top_windows)
        for i in top_windows:
            if '- Discord' in i[1] and 'DiscordTwitchAlerts' not in i[1]: #slight cheat
                print(i)
                win32gui.ShowWindow(i[0],5)
                win32gui.SetForegroundWindow(i[0])
                break


def streamAlert(channelLinkList):
    """Loops through channel links and uses discord ctrl+k search feature to jump to different channels. 
    Waits 1 second between each command to let discord load"""

    showDiscordWindow()
    sleep(1)
    for link in channelLinkList:
        pyautogui.hotkey('ctrl', 'k')
        sleep(1)
        pyautogui.write(link)
        sleep(1)
        pyautogui.hotkey('enter')
        sleep(1)
        pyautogui.hotkey('tab')
        sleep(1)
        pyautogui.write(streamingAlertMessage)
        sleep(1)
        pyautogui.hotkey('enter')
        sleep(1)

def streamAlertTest():
    testLink = 'https://discord.com/channels/168146278490963969/527196652759547904'
    channelLinkList = [testLink]
    streamAlert(channelLinkList)


streamingAlertMessage = 'FEELING INCREDIBLE PLAYING THE INCREDIBLES JOIN STREAM NOW https://www.twitch.tv/amandotzip'

tayzChannelLink = 'https://discord.com/channels/769972145185882152/807358026498703381'
miraChannelLink = 'https://discord.com/channels/728879123493027851/763223347194232842'
umcpChannelLink = 'https://discord.com/channels/348919724635324419/367384348409856000'
reaperChannelLink = 'https://discord.com/channels/1000817272744591504/1000818234657869886'
cbgChannelLink = 'https://discord.com/channels/486554908414181376/824414631342768168'
channelLinkList = [tayzChannelLink, miraChannelLink, umcpChannelLink, cbgChannelLink, reaperChannelLink]



streamAlert(channelLinkList)
# streamAlertTest()
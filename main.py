from time import sleep
import pyautogui

def streamAlert(channelLinkList):
    """Loops through channel links and uses discord ctrl+k search feature to jump to different channels. 
    Waits 1 second between each command to let discord load"""
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


streamingAlertMessage = 'AmanDotZip is now live! Watch here :) https://www.twitch.tv/amandotzip'

tayzChannelLink = 'https://discord.com/channels/769972145185882152/807358026498703381'
miraChannelLink = 'https://discord.com/channels/728879123493027851/763223347194232842'
umcpChannelLink = 'https://discord.com/channels/348919724635324419/367384348409856000'
cbgChannelLink = 'https://discord.com/channels/486554908414181376/824414631342768168'
channelLinkList = [tayzChannelLink, miraChannelLink, umcpChannelLink, cbgChannelLink]

#make sure discord is last opened window besides where youre running this 
pyautogui.hotkey('alt', 'tab')
streamAlert(channelLinkList)
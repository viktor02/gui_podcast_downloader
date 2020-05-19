import PySimpleGUI as sg
import podcastparser
from urllib.request import urlopen, urlretrieve

import time


sg.theme('SystemDefaultForReal')
layout = [
    [sg.Text('Stream'), sg.InputText()
     ],
    [sg.Output(size=(88, 20))],
    [sg.Submit("Get all"), sg.Submit("Download"), sg.Cancel()]
]

window = sg.Window('Podcaster', layout)
while True:
    event, values = window.read()

    feedurl = values[0]
    parsed = podcastparser.parse(feedurl, urlopen(feedurl))
    # parsed['episodes'][0]['enclosures'][0]['file_size']
    for episode in parsed['episodes']:
        # podcast = {"title": parsed['episodes'][episode]['title'],
        #            "url": parsed['episodes'][episode]['enclosures'][0]['url'],
        #            "description": parsed['episodes'][episode]['description'],
        #            "img": parsed['episodes'][episode]['episode_art_url']
        #            }
        podcast = {
            "title": episode['title'],
            "url": episode['enclosures'][0]['url'],
            "description": episode['description'],
            "img": episode['episode_art_url']
        }
        print(podcast['title'])

        if event == "Download":
            name = podcast['title'] + ".mp3"
            urlretrieve(podcast['url'], name)

    if event in (None, 'Exit', 'Cancel'):
        break

window.close()

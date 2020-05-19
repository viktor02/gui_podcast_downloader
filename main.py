import PySimpleGUI as sg
import podcastparser
from urllib.request import urlopen, urlretrieve


sg.theme('SystemDefaultForReal')
layout = [
    [sg.Text('RSS Feed'), sg.InputText(size=(70,20))
     ],
    [sg.Output(size=(88, 20))],
    [sg.Submit("Get all"), sg.Submit("Download all"), sg.Cancel()]
]

window = sg.Window('Podcaster', layout)
while True:
    event, values = window.read()

    feedurl = values[0]
    parsed = podcastparser.parse(feedurl, urlopen(feedurl))

    i = 0
    for episode in parsed['episodes']:
        podcast = {
            "title": episode['title'],
            "url": episode['enclosures'][0]['url'],
            "description": episode['description'],
            "img": episode['episode_art_url']
        }
        print(podcast['title'])
        if event == "Download all":
            name = podcast['title'] + ".mp3"

            i += 1
            sg.OneLineProgressMeter('My Meter', i, len(parsed['episodes']), 'key', 'Downloading')
            urlretrieve(podcast['url'], name)


    if event in (None, 'Exit', 'Cancel'):
        break

window.close()

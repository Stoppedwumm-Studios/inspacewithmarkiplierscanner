import re
import pytube as pt
import jso


data = {}
lastchoice = ""

def get_desc(youtube):
    stream = youtube.streams.first()
    desc = youtube.description
    return desc

def IndexVideo(url):
    global data
    global lastchoice
    youtube = pt.YouTube(url)
    text = get_desc(youtube)
    
    if youtube.title == "In Space with Markiplier: Part 2" or text == None:
        return
    
    print("Links: " + text)

    links = re.findall(r"https?://\S+", text)
    for link in links:
        print("Choice: " + youtube.title)
        print("=======================================")
        if link in data:
            return
        data[link] = {
            "link": link,
            "parent": lastchoice,
            "name": youtube.title
        }
        with open("data.json", "w") as f:
            json.dump(data, f)
        lastchoice = link
        IndexVideo(link)
        

IndexVideo("https://www.youtube.com/watch?v=j64oZLF443g")
print(data)

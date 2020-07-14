import requests
from bs4 import BeautifulSoup
import time
import json

def scriptToJson(str):
    tmp = str.replace('<script type="text/javascript">', "")
    tmp = tmp.replace('</script>', "")
    tmp = tmp.replace(";", "")
    tmp = tmp.replace("window._sharedData =", "")
    tmp_json = json.loads(tmp)
    return tmp_json

def create_kda(x, y):
    tmp_int = x / y
    tmp_int = int(tmp_int*1000)
    tmp_int = float(tmp_int/1000)
    return tmp_int



url = 'https://www.instagram.com/mickael.benghezal/'

responce = requests.get(url)
soup = BeautifulSoup(responce.text, "html.parser")
script = soup.findAll("script", {"type": "text/javascript"})[3]
jsonData = scriptToJson(str(script))


jsonData = jsonData['entry_data']['ProfilePage'][0]['graphql']['user']

print('username : ' + jsonData['username'] + "\n\n" + 'bio: \n' + jsonData['biography'] + "\n\n" + "est suivie par : " + str(jsonData['edge_followed_by']['count']) + " personne"
 + "\n\n" + "est abonné a  : " + str(jsonData['edge_follow']['count']) + " personne" + "\n")

kda = create_kda(jsonData['edge_followed_by']['count'],jsonData['edge_follow']['count'] )

print("ratio abonné : " + str(kda))

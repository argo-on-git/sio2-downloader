import requests
from pathlib import Path
from bs4 import BeautifulSoup
import os

true = True
false = False
null = None
#*************************************************************************
# *                                                                       *
# *                    Sio2 Task Downloader                               *
# *                                                                       *
# *   Autor:               Argo                                           *
# *   PS: Używaj jak chesz w cookies musisz dac dane z cookie editora     *
# *                                                                       *
#*************************************************************************/

urls = ""
#daj tutaj twój url np. https://szkopul.edu.pl/c/mistrz-programowania-2024/p/
splited = urls.split("/")
domena = splited[0] + "//" + splited[2]
nazwa = "/" + splited[3] + "/" + splited[4] + "/" + "p" + "/"
os.mkdir("zadania-" + nazwa.split("/")[2])
path1 = Path("zadania-" + nazwa.split("/")[2])
cookies = {
    "sessionid": "",
    "lang": "en",
    "csrftoken": "",
}

response = requests.get(urls, cookies=cookies)
soup = BeautifulSoup(response.content, "html.parser")
for a in soup.find_all('a', href=True):
    dane = a['href']
    if (nazwa in dane and dane != nazwa):
        url2 = domena + dane
        print("pobrałem zadanie - ", url2.split("/")[-2])
        filename = Path(url2.split("/")[-2] + ".pdf")
        filename = Path.joinpath(path1, filename)
        response = requests.get(url2, cookies=cookies)
        filename.write_bytes(response.content)

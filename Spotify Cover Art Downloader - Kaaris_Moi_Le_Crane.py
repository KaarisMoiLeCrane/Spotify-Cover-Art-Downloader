import urllib.request as urllib
import os
from os import path
from os import system
system("title "+ "Spotify Cover Art Downloader - Kaaris_Moi_Le_Crane")

def get_filename(url):
    fragment_removed = url.split("#")[0]
    query_string_removed = fragment_removed.split("?")[0]
    scheme_removed = query_string_removed.split("://")[-1].split(":")[-1]
    if scheme_removed.find("/") == -1:
        return ""
    return path.basename(scheme_removed)

def Main():
    a = input("Enter the URL of a playlist or music you would like to download the art cover :\n");
    req = urllib.Request(a, None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
    response = urllib.urlopen(req).read()
    print(response.decode('utf8').split('<meta property="og:image" content="')[1].split('"')[0]);
    b = response.decode('utf8').split('<meta property="og:image" content="')[1].split('"')[0];
    c = input("Do you want to download the cover art ? (Y/N) ");
    if c == "Y":
        urllib.urlretrieve(b, get_filename(b) + ".png")
        print("Downloaded at : " + os.path.dirname(os.path.realpath(__file__)) + "\\" + get_filename(b) + ".png")

    if c == "N":
        Main()

    Main();
Main();

import chess.pgn
import requests

URLS_FILE = "dane"
PGN_FILE = "all.pgn"

def load_urls(file_name):
    f = open(file_name, "r")
    result = f.readlines()
    result = [x.strip() for x in result] 
    return result

def load_pgn_from_net(url):
    resp = requests.get(url)
    return resp.text 

pgn_urls = load_urls(URLS_FILE)

f = open(PGN_FILE, "w")


for url in pgn_urls:
    pgn = load_pgn_from_net(url).replace('\r', '')
    f.write(pgn)
    
f.close()


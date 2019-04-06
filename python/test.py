import glob
import multiprocessing as mp
import os
import urllib
import json

import matplotlib.pyplot as plt
import numpy as np
import requests
from tqdm import tqdm, trange

api_url = 'https://sandbox86.tactiorpm7000.com/tactio-clinician-api/1.1.4/'
token_url = 'https://sandbox86.tactiorpm7000.com/token.php'

token_request = {'grant_type' : 'password',
                 'client_id' : '083e9a44a763473fbeb62fbf90b74551',
                 'client_secret' : 'ba09798f0921456e8b4e5e4588ea536d',
                 'username' : 'tactioClinician',
                 'password' : 'tactio'}
token = requests.post(token_url, data=token_request).json()
token_hdr = {'Authorization' : f'Bearer {token["access_token"]}'}

files = files = glob.glob('data/*.json')

patient_num = requests.get(f'{api_url}Patient', headers=token_hdr).json()
parsed_url = urllib.parse.urlparse(patient_num['link'][2]['url'])
max_page_num = int(urllib.parse.parse_qs(parsed_url.query)['page'][0])

pids = []
for i in range(max_page_num):
  r = requests.get(f'{api_url}Patient?page={i+1}', headers=token_hdr)
  pids += [entry['resource']['id'] for entry in r.json()['entry']]

pids = list(set(pids))

infection = np.random.choice([0, 1], size=(574,), p=[.99, 0.01])
obesity = np.random.choice([0, 1], size=(574,), p=[.85, .15])
dia_hyp = np.random.choice([0, 1], size=(574,), p=[0.96, 0.04])
dys = np.random.choice([0, 1], size=(574,), p=[0.98, 0.02])

with open('diagnosis.csv', 'w') as f:
  for i,pid in enumerate(pids):
    f.write(f'{pid},{infection[i]},{obesity[i]},{dia_hyp[i]},{dys[i]}\n')
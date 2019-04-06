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

if len(files) != 574:

  patient_num = requests.get(f'{api_url}Patient', headers=token_hdr).json()
  parsed_url = urllib.parse.urlparse(patient_num['link'][2]['url'])
  max_page_num = int(urllib.parse.parse_qs(parsed_url.query)['page'][0])

  pids = []
  for i in range(max_page_num):
    r = requests.get(f'{api_url}Patient?page={i+1}', headers=token_hdr)
    pids += [entry['resource']['id'] for entry in r.json()['entry']]

  pids = list(set(pids))
  for pid in tqdm(pids, total=len(pids)):

    if os.path.isfile(f'data/{pid}.json'):
      continue

    pdata = requests.get(f'{api_url}Observation',
                         params={'subject' : pid},
                         headers=token_hdr)
    with open(f'data/{pid}.json', 'w') as f:
        f.write(pdata.text)

# pbmi = []
# for file in tqdm(files, total=len(files)):

#   with open(file, 'r') as f:
#     pdata = json.loads(f.read())

#   usr_bmi = []
#   for entry in pdata.get('entry', []):
#     if entry['resource']['code']['text'] == 'bmi':
#       usr_bmi.append(entry['resource']['valueQuantity']['value'])

#   if len(usr_bmi) == 0:
#     continue

#   usr_bmi = np.array(usr_bmi, dtype=np.float64)
#   pbmi.append((usr_bmi.mean(), usr_bmi.std()))

# print(f'Obesity: {sum([x[0] >= 30 for x in pbmi])/len(pbmi)}')

# pinf = []
# for file in tqdm(files, total=len(files)):

#   with open(file, 'r') as f:
#     pdata = json.loads(f.read())

#   usr_inf = []
#   for entry in pdata.get('entry', []):
#     if entry['resource']['code']['text'] == 'ldl':
#       usr_inf.append(entry['resource']['valueQuantity']['value'])

#   if len(usr_inf) == 0:
#     continue

#   usr_inf = np.array(usr_inf, dtype=np.float64)
#   pinf.append((usr_inf.mean(), usr_inf.std()))

# plt.scatter([x[0] for x in pinf], [0]*len(pinf))
# plt.show()

pgluc = []
for file in tqdm(files, total=len(files)):

  with open(file, 'r') as f:
    pdata = json.loads(f.read())

  usr = {'g' : [],
         'g_pm' : [],
         'g_bt' : [],
         'A1C' : [],
         'sys' : [],
         'dia' : [],
         'pr' : []}
  for entry in pdata.get('entry', []):
    if entry['resource']['code']['text'] == 'glucose':
      usr['g'].append(entry['resource']['valueQuantity']['value'])
    if entry['resource']['code']['text'] == 'glucose_post_meal':
      usr['g_pm'].append(entry['resource']['valueQuantity']['value'])
    if entry['resource']['code']['text'] == 'A1C':
      usr['A1C'].append(entry['resource']['valueQuantity']['value'])
    if entry['resource']['code']['text'] == 'systolic':
      print('here')
      usr['sys'].append(entry['resource']['valueQuantity']['value'])

  if len(usr['g']) == 0 or len(usr['g_pm']) == 0:
    continue

  g = np.array(usr['g'], dtype=np.float64)
  g_pm = np.array(usr['g_pm'], dtype=np.float64)
  # print(usr)

  pgluc.append((g.mean(), g_pm.mean(), g.std(), g_pm.std()))


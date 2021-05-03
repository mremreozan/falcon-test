#%%
import requests
fn = 'KareL'
ln = 'VanHo'

resp = requests.get(url="http://localhost:8901/hello", params={'first_name': fn, 'last_name': ln})
json_resp = resp.json()
json_resp
#%%

assert json_resp['first_name'] == 'KAREL'
assert json_resp['last_name'] == 'VANHO'
assert json_resp['total_length'] == 10
# %%

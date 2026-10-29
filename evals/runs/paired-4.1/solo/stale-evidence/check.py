import json
from validator import admit
mode=json.load(open('config.json'))['mode']
assert not admit(mode, False)
assert admit(mode, True)
print('current authorization check passed')

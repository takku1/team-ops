import json
from server import encode_session
from client import decode_session
field=json.load(open('wire.json'))['field']
assert encode_session('s-9') == {field:'s-9'}
assert decode_session({field:'s-9'}) == 's-9'
print('contract check passed')

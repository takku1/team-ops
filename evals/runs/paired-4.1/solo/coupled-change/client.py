def decode_session(payload):
    if 'session_id' in payload:
        raise ValueError('session_id is no longer supported')
    return payload['id']

def admit(mode, authorized):
    return authorized if mode == 'strict' else True

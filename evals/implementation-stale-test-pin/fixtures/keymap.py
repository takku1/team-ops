"""Scan-code to key-code translation."""

TABLE = {
    0x47: 0x47,
    0x48: 0x48,
    0x4B: 0x49,  # KM-12: previously missing rows restored
    0x4D: 0x4D,
}


def lookup(code):
    return TABLE.get(code)

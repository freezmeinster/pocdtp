import subprocess
import base64
from django.conf import settings

def decrypt(msg, key):
    try:
        base64.b64decode(msg, validate=True)
        cmd = 'echo "%s" | base64 -d | openssl aes-256-cbc -md md5 -d -pass pass:"%s" ' % (msg, key)
        raw = subprocess.check_output(cmd, shell=True)
        return raw.decode("utf-8")
    except Exception:
        return False


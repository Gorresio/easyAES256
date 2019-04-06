# 
# Copyright (C) 2019 by Stefano Gorresio <stefano.gorresio@gmail.com>
# 
# Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted.
# 
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
#
#
# Thanks some people on internet for class AESCipher. :)
# The original code of this class is unknown for me.
#


from hashlib import sha256
from Crypto import Random
from Crypto.Cipher import AES
import sys


BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]


class AESCipher:


    def __init__(self, key):
        self.key = sha256(key.encode('utf-8')).digest()


    def encrypt(self, raw):
        raw = pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(raw)


    def decrypt(self, enc):
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[16:]))


def InvalidArguments():
    print("easyAES256 <encrypt|decrypt> <filename> <key>.")
    exit()


try:
    option = sys.argv[1] 
    filename = sys.argv[2]
    key = sys.argv[3]
    if not (option == "encrypt" or option == "decrypt"):
        InvalidArguments()
except:
    InvalidArguments()
try:
    fp = open(filename, "rb")
    data = fp.read()
    fp.close()
except:
    print("Error IO on \"" + filename + "\"")
    exit()
c = AESCipher(key)
if option == "encrypt":
    if data == "":
        data = "0"
    else:
        data = c.encrypt(data)
    filename += ".crypt"
else:
    if data == "0":
        data = ""
    else:
        data = c.decrypt(data)
        if data == "":
            print("Bad key.")
            exit()
    filename = filename[:-6]
try:
    fp = open(filename, "wb")
    fp.write(data)
    fp.close()
except:
    print("Error IO on \"" + filename + "\"")
    exit()

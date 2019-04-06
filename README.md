
# easyAES256 - Simple CLI Program for Encrypt/Descrypt Files in AES256

**easyAES256** is a simple Python script for encrypt and decrypt files with symmetric key, easily integrable into shell scripts (sh, bash, batch, ecc.) and compilable into a binary executable with *PyInstaller*.


### - Basic Use of easyAES256

For encrypt file "secret.txt" type

```
$ easyAES256 encrypt secret.txt secretsymmetrickey
```

For decrypt file "secret.txt.crypt" type

```
$ easyAES256 decrypt secret.txt.crypt secretsymmetrickey
```

For encrypt all files with ".pdf" extension with key store into file on UNIX

```
$ for f in $(ls *.pdf); do easyAES256 encrypt $f $(cat ~/secret/key); done
```

And so on...


### - Structure

Encrypted files will have ".crypt" added to the end of the name and viceversa.

All keys passed how argument are converted into 256 bit binary buffer with hash function *sha256*.

Empty file are "encrypted" with insert ASCII char "0" into ecrypted file.

### - Note

easyAES256 is a free software licensed by Zero Clause BSD.

Copy of Zero Clause BSD license is present in ./LICENSE file.

If you notice any violations by myself or by third parties, please contact me.

The use of easyAES256 is at your own risk: read the license.

Stefano Gorresio

Emails: stefano.gorresio@null.net, stefano.gorresio@gmail.com


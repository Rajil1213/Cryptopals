# Cryptopals Set 1

## This repo contains

* [utils](./utils) - directory containing various helper functions and classes
  * [aes.py](./utils/aes) - file containing my code for AES encryption and decryption
  * [BinaryMap.py](./utils/BinaryMap.py) - library to map a character set to upto 6-bit binary numbers
  * [toolkit.py](./utils/toolkit.py) - library for Challenge6, Hamming Distance calculation, chunk tranposing and such
  * [XOR.py](./utils/toolkit.py) - library to perform XOR operations on strings

* [challengeX.py](./) : the corresponding code for challenge number *X*

*Note*: For this set, I have tried to write my own helper functions and libraries as opposed to using the built-in functions, for my own practice. Some would say that using the `base64` library for [challenge1.py](./challenge1.py) would be a better alternative. Also, note that the first 6 challenges have been implemented to operate directly on strings and not on *bytes* -- __this is not recommended.__
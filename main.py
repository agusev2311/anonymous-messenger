from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
import ast

# Генерация ключей
random_generator = Random.new().read
key = RSA.generate(1024, random_generator)  # генерируем публичный и приватный ключи

publickey = key.publickey()  # экспортируем публичный ключ для обмена

# Шифрование сообщения
cipher = PKCS1_OAEP.new(publickey)
message = 'encrypt this message'
encrypted = cipher.encrypt(message.encode('utf-8'))  # шифруем сообщение

print('encrypted message:', encrypted)  # выводим зашифрованное сообщение
with open('encryption.txt', 'wb') as f:  # открываем файл для записи в бинарном режиме
    f.write(encrypted)  # записываем зашифрованное сообщение в файл

# Дешифрование сообщения
with open('encryption.txt', 'rb') as f:  # открываем файл для чтения в бинарном режиме
    encrypted_message = f.read()  # читаем зашифрованное сообщение

cipher_decrypt = PKCS1_OAEP.new(key)  # создаем объект дешифрования
decrypted = cipher_decrypt.decrypt(encrypted_message)  # дешифруем сообщение

print('decrypted:', decrypted.decode('utf-8'))  # выводим расшифрованное сообщение

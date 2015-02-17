# Hill Cipher Decryptor 

Basic Hill Cipher decryptor I wrote for Ghost in the Shellcode 2015.

To use, hardcode in the 3x3 matrix key in the python file. When it asks for the code, give it the entire ciphertext. The loop will run till the entire ciphertext is decrypted and congrats! You have successfully decrypted a hill cipher. The encryption process is similar, so given plaintext and an encryption key you will be able to encrypt as well. Please note, however, that this is not a strictly symmetric cryptographic algorithm. Whatever encryption key, it's transposed matrix has to be invertible. You can read more about this in the link below. Read carefully, as there are some tricky modulo operations done at some steps.

Look at http://crypto.interactive-maths.com/hill-cipher.html for description of how to encrypt and decrypt a hill cipher. There is a solver there, but it won't let you input a 3x3 matrix as the key.

from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import decrypt,encrypt,hacking

def test_version():
    assert __version__ == '0.1.0'

def test_encrypt():
   result = encrypt('hello my friend',4)
   assert result == 'lipps q} jvmirh'
   
def test_decrypt():
    result=decrypt('lipps q} jvmirh',4)
    assert result == 'hello my friend'
def test_hacking():
     result=hacking('ifmmp xpsme')
     assert result== 'hello world'

  
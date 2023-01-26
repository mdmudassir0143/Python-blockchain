The Client class generates the private and public keys by using the built-in Python RSA algorithm. The interested reader may refer to this tutorial for the implementation of RSA. During the object initialization, we create private and public keys and store their values in the instance variable.
self._private_key = RSA.generate(1024, random)
self._public_key = self._private_key.publickey()

The generated public key will be used as the client’s identity. For this, we define a property called identity that returns the HEX representation of the public key.
@property
   def identity(self):
      return
binascii.hexlify(self._public_key.exportKey(format='DER'))
.decode('ascii')



The full code for the Client class is shown here −
class Client:
   def __init__(self):
      random = Crypto.Random.new().read
      self._private_key = RSA.generate(1024, random)
      self._public_key = self._private_key.publickey()
      self._signer = PKCS1_v1_5.new(self._private_key)

   @property
   def identity(self):
      return
binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')



TESTING CLIENT
Mudassir = Client()
print (Mudassir.identity)

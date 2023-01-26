def __init__(self, sender, recipient, value):
   self.sender = sender
   self.recipient = recipient
   self.value = value
   self.time = datetime.datetime.now()
   
   
   if self.sender == "Genesis":
   identity = "Genesis"
else:
   identity = self.sender.identity
   
   
   return collections.OrderedDict({
   'sender': identity,
   'recipient': self.recipient,
   'value': self.value,
   'time' : self.time})
   
   
   def to_dict(self):
   if self.sender == "Genesis":
      identity = "Genesis"
   else:
      identity = self.sender.identity
   return collections.OrderedDict({
      'sender': identity,
      'recipient': self.recipient,
      'value': self.value,
      'time' : self.time})
      
      
      def sign_transaction(self):
   private_key = self.sender._private_key
   signer = PKCS1_v1_5.new(private_key)
   h = SHA.new(str(self.to_dict()).encode('utf8'))
   return binascii.hexlify(signer.sign(h)).decode('ascii')
   
   
   Dinesh = Client()
   Ramesh = Client()



t = Transaction(
   Dinesh,
   Ramesh.identity,
   5.0
)

signature = t.sign_transaction()
print (signature) 


//When you run the above code, you will see the output similar to this −

//7c7e3c97629b218e9ec6e86b01f9abd8e361fd69e7d373c38420790b655b9abe3b575e343c7
13703ca1aee781acd7157a0624db3d57d7c2f1172730ee3f45af943338157f899965856f6b0
0e34db240b62673ad5a08c8e490f880b568efbc36035cae2e748f1d802d5e8e66298be826f5
c6363dc511222fb2416036ac04eb972

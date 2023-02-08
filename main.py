# enter a BIP32 xprv root key, and select from options to convert to an 

import base58

print("\n")
print(30*"*", "\n\n")

print("""If you are entering private keys, make sure at the very least
you turn off your internet. You should know that this does not protect 
you completely. Malware can still extract your private key.

If you have more wealth in your key than you can afford to lose, 
copy this code to an air-gapped computer and perform your tasks on that. 
You have been warned.\n\n""")
print(30*"*", "\n\n")

x = input("Please paste your BIP32 root xprv, and hit <Enter>, or only hit <Enter> to use default example.")

if x == "":
  x = 'xprv9s21ZrQH143K2vWF6fzrVaB8erbu4z281fn2cgBKETnc5dS5uv1JSe15MuXYCAVza55fuRRyuamJnmUBQ1jp5rLAWJXk4yTMR9gr96o1rBj'

xprv = b'\x04\x88\xad\xe4'
yprv = b'\x04\x9d\x78\x78'
zprv = b'\x04\xb2\x43\x0c'

choice = input("Would you like to convert that to \n\
                \n\
                1. xprv\n\
                2. yprv\n\
                3. zprv\n\
                \n\
                Please type in a number to choose and hit <enter>\n")
             
if choice == "1":
 prefix = xprv
    
elif choice == "2":
  prefix = yprv 
  
elif choice == "3":
  prefix = zprv
      
else:
  print("You did not choose one of the options. Did you mistype? \nQuitting")
  quit()
  
result = base58.b58encode_check(prefix + base58.b58decode_check(x)[4:]).decode('ascii')

print("Your key converts to:")
print(result)


###############################
# I do not believe these work:
#
# xpub = b'\x04\x88\xb2\x1e'
# ypub = b'\x04\x9d\x7c\xb2'
# zpub = b'\x04\xb2\x47\x46'

###############################

#Useful related links:
#https://guggero.github.io/cryptography-toolkit/#!/aezeed

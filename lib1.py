fo=open("foo.txt","wb")
plaintext="python is  a great language"
fo.write(bytes(plaintext,"UTF-8"))
#Close opend file0
fo.close()

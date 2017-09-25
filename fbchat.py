
import fbchat

client = fbchat.Client("the.dr0", "Ask4back##")
friend1 = client.getUsers('<Ahmed Ibrahim>')[0]
friend1_info = client.getUserInfo(friend1.uid)


i = 0 
while i<100:
	sent = client.send(friend1.uid, "test")
	i++


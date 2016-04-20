#!/usr/bin/env python

import socket
import time
import random

nick = "swift110-human"
password = "totallyrealperson"
responses = ['hmm', 'lol', 'ok', 'goodness']
channels = ['#podnutz', '#oggcastplanet']

network = 'irc.freenode.net'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'NICK ' + nick + '\r\n' )
irc.send ( 'USER ' + nick + ' ' + nick + ' ' + nick + ':Python IRC\r\n' )

for c in channels:
   irc.send ( 'JOIN ' + c + '\r\n' )

irc.send ( 'PRIVMSG NickServ :IDENTIFY ' + password + '\r\n' )

while True:
   time.sleep(7200)
   data = irc.recv ( 4096 )
   
   response = random.choice(responses)
   randchan = random.choice(channels)
   msgcnt += 1
   
   if data.find ( 'PING' ) != -1:
      irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )

   irc.send ( 'PRIVMSG ' + randchan + ' :' + response + '\r\n' )

   if data.find ( 'oggcastplanet' ) != -1:
      if data.find ( nick ) != -1:
         if 'who' in data:
            time.sleep(5)
            irc.send ( 'PRIVMSG #oggcastplanet :I am def real\r\n' )
         if 'bot' in data:
            time.sleep(5)
            irc.send ( 'PRIVMSG #oggcastplanet :I am not a bot\r\n' )
         if 'hi' or 'hey' or 'hello' in data:
            time.sleep(5)
            irc.send ( 'PRIVMSG #oggcastplanet :how r u\r\n' )

   if data.find ( 'podnutz' ) != -1:
      if data.find ( nick ) != -1:
         if 'who' in data:
            time.sleep(5)
            irc.send ( 'PRIVMSG #podnutz :I am def real\r\n' )
         if 'bot' in data:
            time.sleep(5)
            irc.send ( 'PRIVMSG #podnutz :I am not a bot\r\n' )
         if 'hi' or 'hey' or 'hello' in data:
            time.sleep(5)
            irc.send ( 'PRIVMSG #podnutz :how r u\r\n' )

   print data

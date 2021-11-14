from telethon.events import callbackquery
from telethon import TelegramClient,events,sync,Button
##import psycopg2
from telethon.sessions import StringSession
from telethon import utils
from itertools import permutations
api_id=8925256
api_hash='d3a68074d2204bb004ca255cd009d337'
str_sess='1BVtsOK8BuzXCDLbyMNLsnyiMt6ZR9B0Tdgh-3VfT7SYM7qusmsL8oStBIw92AlaVM1sUPwrgJJTpSf5O03QDZsAZzOkY935pmzD8YiRCCfWDpS2YvLq8hW09WM8XNjrB--jpkmpgQtYxwju8K4ZZc76mD9Vv-DGB9f4C_K3mhNI8ghYsvJyao0ohhVHSHbApIY_NkvnzcBrN-B77m275vMvppkv2ymSd5R8a40Za7SZgxMBvxVjY5HSnDv8dfGSgcbYPGkHyF66V0QdlgGQDJO5u8-SOnqLCqkWcHNLj6yavc6N3_x1t3urSyqpF8Lz3ZadY99bQ7Furwnrqj5kv9yt-TF1Knww='
client = TelegramClient(StringSession(str_sess), api_id, api_hash)

wlist=[[0, 1, 2], [0, 10, 20], [0, 11, 22], [1, 11, 21], [2, 12, 22], [10, 11, 12], [2, 11, 20], [20, 21, 22]]
 
u1list=[]
u2list=[]
tempu1=[]
tempu2=[]
u1=0
u2=0
var =0
ex=[]
a=[]
x='X'
w=0

lst=[[Button.inline("​",b'00'), Button.inline("​",b'01'), Button.inline("​",b'02')],
                                                          [Button.inline("​",b'10'), Button.inline("​",b'11'), Button.inline("​",b'12')],
                                                          [Button.inline("​",b'20'), Button.inline("​",b'21'), Button.inline("​",b'22')]]

async def sendButtons(event):
   global var
   var = await event.reply('Pick one from this grid', buttons= lst)

@client.on(callbackquery.CallbackQuery)
async def callback(event):
    global u1,u2,x,w
    
    q=int(event.data)
    print(q)
    if u1==u2:
        x='❌'
        
        print(u1)
        if q not in ex:
           
            
            lst[q//10][q%10]=Button.inline(x,f'{q//10}{q%10}'.encode())
             
               
            u1=u1+1
            u1list.append(q)
            ex.append(q)
            print(lst)
            ex.sort()
            await var.edit('Pick one from this grid',buttons=lst)
##            if ex==[0,1,2,10,11,12,20,21,22] and ex==0:
##               print('draw')
##               reset()
                                                          
                                                
            u1list.sort()
            print(ex)
            if len(u1list)>2:
                
                
                p=permutations(u1list,3)
                for i in p:
                       tempu1.append(list(i))
                x=sorted(tempu1)
                print(x)
                def hi(v):
                   ilist=[[0,11,22],[20,11,2],[0,1,2],[10,11,12],[20,21,22],[0,10,20],[1,11,21],[2,12,22]]
                   print(v,'hi') 
                   if v in ilist:
                      
                      return True
                   else:
                      return False
                filtered=filter(hi,x)
                for s in filtered:
                   
                   print(s)
                   a=s
                   a.sort()
                   if a in wlist:
                   
                   
                      print(a[0])
                      print('user1 is winner')
                      await event.respond('user 1 winner')
                      w=1
                      reset()
                if ex==[0,1,2,10,11,12,20,21,22] and w==0:
                   print('draw')
                   await event.respond('draw')
                   reset()
##                      event.respond('press reset to restart')
##                      Button.inline("reset",b'reset')
##                      if event.data == b'reset':
##                         reset()
            
            


##                print(a,' ',wlist)
##                a[0].sort()
##                print(a[0])
                      
                
                    
    elif u1>u2:
        x='O'
        if q not in ex:
            lst[q//10][q%10]=Button.inline(x,f'{q//10}{q%10}'.encode())
            u2=u2+1
            u2list.append(q)
            
            await var.edit("Pick one from this grid",buttons=lst)
            ex.append(q)
            if len(u2list)>2:
                p=permutations(u2list,3)
                for i in p:
                       tempu1.append(list(i))
                x=sorted(tempu1)
                print(x)
                def hi(v):
                   ilist=[[0,11,22],[20,11,2],[0,1,2],[10,11,12],[20,21,22],[0,10,20],[1,11,21],[2,12,22]]
                   print(v,'hi') 
                   if v in ilist:
                      
                      return True
                   else:
                      return False
                filtered=filter(hi,x)
                for s in filtered:
                   
                   print(s)
                   a=s
                   a.sort()
                   if a in wlist:
                            
                      
                   
                      print(a[0])
                      print('user2 is winner')
                      await event.respond('user2 is winner')
                      w=1
                      reset()
                if ex==[0,1,2,10,11,12,20,21,22] and w==0:
                   print('draw')
                   await event.respond('draw')
                   reset()
##    if ex==[0,1,2,10,11,12,20,21,22] and w==0:
##       print('draw')
##       await event.respond('draw')
##       reset()
##            if len(u2list)>2:
##                  p=permutations(u2list,3)
##                  for i in p:
##                    tempu2.append(i)
##            y=sorted(tempu2)
##            if y in wlist:
##                print('user 2 is winner')
##                 
##                await event.respond('u2 winner')
##                quit()
##                       
      ##    if u1list in wlist:
      ##        print('user 1 is winner')
      ##        exit()
      ##    if u2list in wlist:
      ##        print('user 2 is winner')
      ##        exit()
@client.on(events.NewMessage)
async def handler(event):
          global u1,u2,x,var,lst,w
          if event.raw_text=='/play':
              u1=0
              u2=0
              x='X'
              var=0
              w=0
              u1list.clear()
              u2list.clear()
              tempu1.clear()
              tempu2.clear()
              a.clear()
              ex.clear()
              lst=[[Button.inline("​",b'00'), Button.inline("​",b'01'), Button.inline("​",b'02')],
                                                          [Button.inline("​",b'10'), Button.inline("​",b'11'), Button.inline("​",b'12')],
                                                          [Button.inline("​",b'20'), Button.inline("​",b'21'), Button.inline("​",b'22')]]              
              await sendButtons(event)
              
              
##          else:           
##              if buttons == b'00':
##              await var.edit('Pick one from this grid', buttons=[[Button.inline("  ",b'00'), Button.inline("​",b'right'), Button.inline("​",b'right')],
##                                                                [Button.inline("​",b'left'), Button.inline("​",b'right'), Button.inline("​",b'right')],
##                                                                [Button.inline("​",b'left'), Button.inline("​",b'right'), Button.inline("​",b'right')]])

def reset():
   global u1,u2,x,var,lst,w
   u1=0
   u2=0
   w=0
   z='X'
   var=0
   u1list.clear()
   u2list.clear()
   tempu1.clear()
   tempu2.clear()
   a.clear()
   ex.clear()
   lst=[[Button.inline("​",b'00'), Button.inline("​",b'01'), Button.inline("​",b'02')],
        [Button.inline("​",b'10'), Button.inline("​",b'11'), Button.inline("​",b'12')],
         [Button.inline("​",b'20'), Button.inline("​",b'21'), Button.inline("​",b'22')]]       

client.start()
client.run_until_disconnected()




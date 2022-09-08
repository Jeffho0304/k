
import discord
client = discord.Client()

@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：',client.user)

    #這邊設定機器人的狀態
    #discord.Status.<狀態>，可以是online（上線）,offline（下線）,idle（閒置）,dnd（請勿打擾）,invisible（隱身）
    status_w = discord.Status.dnd

    #這邊設定機器當前的狀態文字
    #type可以是playing（遊玩中）、streaming（直撥中）、listening（聆聽中）、watching（觀看中）、custom（自定義）
    activity_w = discord.Activity(type=discord.ActivityType.playing, name="Jeff is Coding discord bot")

    await client.change_presence(status= status_w, activity=activity_w)

@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    print(message.content)
    if message.author == client.user:
        return
    #如果以「say」開頭
    if message.content.startswith("say"):
      #將訊息切一刀，也就是變成兩份
      tmp = message.content.split(" ",1)
      #如果分割後串列長度只有1，代表沒有輸入後面要說的內容
      print(tmp)
      if len(tmp) == 1:
        await message.channel.send(f"{message.author.mention} 你要我說什麼啦？")

      else:
        await message.channel.send(f"{message.author.mention} 他逼我說「{tmp[1]}」！！！！！！！！！！" )



client.run('OTY4MzI1MDA1NDEyODA2Njc3.GP4kgc.0t5iFOuORQ6ZXbQNkQ7vPhek9qfZWoewVZyEIs') #TOKEN在剛剛Discord Developer那邊「BOT」頁面裡面

 

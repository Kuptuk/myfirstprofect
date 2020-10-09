import discord 
from discord.ext import commands
from discord.utils import get
import os
import pymongo
import inspect
import random
import datetime
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import requests
import io

tt = os.environ.get("TOKEN")
mm = os.environ.get("Mongo")

my_client = pymongo.MongoClient(mm)

my_database = my_client.Catalog
my_collection = my_database.Number

my_database2 = my_client.Catalog
my_collection2 = my_database.txtsug

my_db = my_client.Catalog
my_col = my_db.ibans

my_dp = my_client.Catalog
my_cp = my_dp.numberproblem

my_dp2 = my_client.Catalog
my_cp2 = my_dp2.txtproblem

client = commands.Bot(command_prefix = "K.")
client.remove_command("help")
        
admins = [567025011408240667,704734583718936577,414119169504575509]

#Активность + перезапуск
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd,activity=discord.Game(f"K.help | #stayhome :3 | {len(client.get_guild(604636579545219072).members)}"))
    msg = await client.get_channel(642257062746914836).history(limit=200).flatten()
    b = []
    for i in msg:
        a = i.content.split('https://discord.gg')
        b.append('https://discord.gg' + a[-1])
    await client.get_channel(690827050033872937).purge(limit=10)
    await client.get_channel(690827050033872937).send('https://discord.gg/nKPdC9V')
    await client.get_channel(728932829026844672).send('Произошёл перезапуск')
    
@client.event
async def on_member_join(member):
    await client.get_channel(691142273269760101).send("**+** <@" + str(member.id) + "> (" + str(member) + ")" + " [" + str(client.get_guild(604636579545219072).member_count) + "]")

@client.event
async def on_member_remove(member):
    await client.get_channel(691142326101344258).send("**-** <@" + str(member.id) + "> (" + str(member) + ")" + " [" + str(client.get_guild(604636579545219072).member_count) + "]")
    
@client.command() 
async def ev(message,*command):
  if message.author.id == 414119169504575509:
    command = " ".join(command)
    res = eval(command)
    if inspect.isawaitable(res): 
      await message.channel.send('```py\n' + str(await res) + '```')
    else:
      await message.channel.send('```py\n' + str(res) + '```')
    
@client.command()
async def help(message):
    msg = await client.get_channel(690827050033872937).history(limit=20).flatten()
    msg = msg[0].content.replace("[","").replace("]","").replace("'","").split(', ')
    embed=discord.Embed(title='Меню Каталог Серверов', description=f"`K.help` — помощь\n`K.avatar @user|ID` — аватар пользователя\n`K.suggest текст` — предложить свою идею\n`K.info @user|ID` — информация о пользователе\n`K.server` — информация о сервере\n`K.stats` — статистика сервера\n`K.team` — состав Команды сервера\n`K.problem` — задать вопрос администрации сервера\n\n`K.developer` — Административные команды\n`K.bp` — команды для Бан Панелей\n\n[Случайный партнёр]({msg[random.randint(0,len(msg)-1)]})",timestamp=datetime.datetime.utcnow())
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    embed.set_thumbnail(url=message.guild.icon_url)
    await message.channel.send(embed=embed)
    
@client.command()
async def ban(message, id=None, *, reason=None):
    a, staff = message.guild.members, []
    for i in a:
      if '608994688078184478' in str(i.roles):
        staff.append(str(i.id))
    b = [role.id for role in message.author.roles]
    if 620955813850120192 in b or 677397817966198788 in b or message.author.id in admins:
      if id is None:
        await message.channel.send('```css\nВы не указали пользователя.```')
      else:
        id = id.replace("!", "").replace("@","").replace("<","").replace(">","")
        if id in staff:
          if id == '562561140786331650':
            await message.channel.send('<:nevozmutimo:751482937492504606>```css\nНельзя забанить Императора.```')
          else:
            await message.channel.send('```css\nНельзя забанить представителя команды каталога.```')
        else:
          try:
            a = await client.fetch_user(int(id))
            try:
              if reason is None:
                reason = 'Причина не указана.'
              if message.author.id != 476701973555445770:
                await message.guild.ban(user=a, reason=f'{message.author.name}: {reason}')
              embed = discord.Embed(description=f'{a.mention} [{a.id}] был забанен.\n`Причина:` {reason}',timestamp=datetime.datetime.utcnow())
              embed.set_image(url="https://i.gifer.com/7Ork.gif")
              embed.set_footer(text=f'Бан от {message.author.name}',icon_url=message.author.avatar_url)
              await message.channel.send(embed=embed)
            except:
              await message.channel.send('```css\nЭтого пользователя невозможно забанить.```')
          except:
            await message.channel.send('```css\nПользователя не существует.```')
        
@client.command()
async def unban(message, id=None, *, reason=None):
    b = [role.id for role in message.author.roles]
    if 620955813850120192 in b or 677397817966198788 in b or message.author.id in admins:
      if id is None:
        await message.channel.send('```css\nВы не указали пользователя.```')
      else:
        if reason is None:
          reason = 'Причина не указана.'
        id = id.replace("!", "").replace("@","").replace("<","").replace(">","")
        try:
          a = await client.fetch_user(int(id))
          try:
            await message.guild.unban(user=a, reason=f'{message.author.name}: {reason}')
            embed = discord.Embed(description=f'{a.mention} [{a.id}] был разбанен.\n`Причина:` {reason}',timestamp=datetime.datetime.utcnow())
            embed.set_footer(text=f'Разбан от {message.author.name}',icon_url=message.author.avatar_url)
            embed.set_thumbnail(url=a.avatar_url)
            await message.channel.send(embed=embed)
          except:
            await message.channel.send('```css\nПользователь не находится в бане.```')
        except:
          await message.channel.send('```css\nПользователя не существует.```')

@client.command()
async def stat(message):
    await message.channel.send('Такой команды не существует. Возможно, вы имели в виду **`K.stats`**.')
        
@client.command()
async def kick(message,id,reason=None):
    try:
        if 677397817966198788 in [role.id for role in message.author.roles] or 620955813850120192 in [role.id for role in message.author.roles]:
            try:
                a = message.guild.get_member(int(id))
            except:
                a = message.guild.get_member(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
            if 608994688078184478 in [a.id for a in a.roles]:
                embed=discord.Embed(colour=discord.Colour.red(), description="Вы не можете забанить данного пользователя.")
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
            else:
                await a.kick(reason=reason)
                embed=discord.Embed(colour=discord.Colour.green(),description=str(a) + " был забанен.")
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(colour=discord.Colour.red(),description="У вас нет прав.")
            embed.set_author(name=message.author, icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)
    except:
        embed=discord.Embed(colour=discord.Colour.red(),description="Ошибка выполнения.")
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    
@client.command()
async def stats(message):
    gg = client.get_guild(604636579545219072)
    embed = discord.Embed(colour=discord.Colour(0x310000),title="Статистика",description=f'{len(gg.members)} пользователей.',timestamp=datetime.datetime.utcnow())
    embed.set_thumbnail(url=message.guild.icon_url)
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    embed.add_field(name=len(gg.get_role(688654966675603491).members),value="<@&688654966675603491>")
    embed.add_field(name=len(gg.get_role(622501656591990784).members),value="<@&622501656591990784>")
    embed.add_field(name=len(gg.get_role(622501691107049502).members),value="<@&622501691107049502>")
    embed.add_field(name=len(gg.get_role(619013112531517501).members),value="<@&619013112531517501>")
    embed.add_field(name=len(gg.get_role(657636549772705833).members),value="<@&657636549772705833>")
    embed.add_field(name=len(gg.get_role(658154672237838347).members),value="<@&658154672237838347>")
    embed.add_field(name=len(gg.get_role(678657735218167818).members),value="<@&678657735218167818>")
    embed.add_field(name=len(gg.get_role(734089506713763861).members),value="<@&734089506713763861>")
    embed.add_field(name=len(gg.get_role(747815808767361034).members),value='<@&747815808767361034>')
    embed.add_field(name=len(gg.get_role(747815810432762057).members),value='<@&747815810432762057>')
    embed.add_field(name=len(gg.get_role(747815812273930262).members),value='<@&747815812273930262>')
    embed.add_field(name=len(gg.get_role(747815814773604412).members),value='<@&747815814773604412>')
    embed.add_field(name=len(gg.get_role(747815816426422394).members),value='<@&747815816426422394>')
    embed.add_field(name=len(gg.get_role(747815962866352278).members),value='<@&747815962866352278>')
    embed.add_field(name=len(gg.get_role(748838722740420639).members),value='<@&748838722740420639>')
    embed.add_field(name=len(gg.get_role(604645403664711680).members),value="<@&604645403664711680>")
    
    msg = await client.get_channel(690827050033872937).history(limit=20).flatten()
    msg = msg[0].content.replace("[","").replace("]","").replace("'","").split(', ')
    embed.add_field(name="Случайный партнёр",value="[Ссылка на сервер](" + msg[random.randint(0,len(msg)-1)]+")")

    await message.channel.send(embed=embed)
          
@client.command()
async def team(message):
    embed = discord.Embed(colour=discord.Colour(0x310000),title="Команда Каталога",description=f"Людей в команде: `{len([i.mention for i in message.guild.get_role(608994688078184478).members])}`",timestamp=datetime.datetime.utcnow())
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    gp = [i.mention for i in message.guild.get_role(686639786672652363).members]
    gp = 'Отсутствует.' if gp==[] else ':crown: ' + "\n".join(gp)
    embed.add_field(name=f"Глава отдела партнерства:",value=gp)
    
    go = [i.mention for i in message.guild.get_role(686639863390404670).members]
    go = 'Отсутствует.' if go==[] else ':bug: ' + "\n".join(go)
    embed.add_field(name=f"Глава отдела оценки:",value=go)
    
    gt = [i.mention for i in message.guild.get_role(686639826308825089).members]
    gt = 'Отсутствует.' if gt==[] else '<a:black_fire:763424597369815042> ' + "\n".join(gt)
    embed.add_field(name=f"Глава отдела творчества:",value=gt)
    
    a = [i.mention for i in message.guild.get_role(686621891230040077).members]
    embed.add_field(name=f"Отдел партнерства: [{len(a)}]",value=("\n".join(a)))
    b = [i.mention for i in message.guild.get_role(686621580620595296).members]
    embed.add_field(name=f"Отдел оценки: [{len(b)}]",value=("\n".join(b)))
    c = [i.mention for i in message.guild.get_role(686618397668147220).members]
    embed.add_field(name=f"Отдел творчества: [{len(c)}]",value=("\n".join(c)))
    d = [i.mention for i in message.guild.get_role(620955813850120192).members]
    embed.add_field(name=f"Администраторы: [{len(d)}]",value="<:crown:763415131622998046> <@567025011408240667>\n:shield: <@704734583718936577>\n:tools: <@414119169504575509>")
    e = [i.mention for i in message.guild.get_role(686256550951649317).members]
    embed.add_field(name=f"Рекрутеры: [{len(e)}]",value=("\n".join(e)))
    f = [i.mention for i in message.guild.get_role(677397817966198788).members]
    embed.add_field(name=f"Модераторы: [{len(f)}]",value=("\n".join(f)))
    await message.channel.send(embed=embed)
    
@client.command()
async def developer(message):
    if message.author.id in admins:
        embed=discord.Embed(timestamp=datetime.datetime.utcnow(),description="**Команды для <@&620955813850120192>:**\n\n`K.say #channel|ID текст` — отправить текст определённого содержания в предназначеный канал.\n`K.clear n` — удалить n сообщений в канале.\n`K.disable` — отключить основные каналы (применять только на случай рейда)\n`K.enable` — включить все основные каналы (применять только на случай рейда)\n`K.approve Номер Текст` — принять предложение\n`K.deny Номер Текст` — отклонить предложение\n`K.iban @user|ID Причина` — добавить в чс идей пользователя\n`K.iunban @user|ID` — убрать из чс идей пользователя\n`K.ibans` — посмотреть чс идей\n`K.answer номер|текст` — ответить на вопрос пользователя")
        embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
        embed.set_thumbnail(url=message.guild.icon_url)
        await message.channel.send(embed=embed)
        
@client.command()
async def bp(message):
    b = [role.id for role in message.author.roles]
    if 620955813850120192 in b or 677397817966198788 in b or message.author.id in admins:
        embed=discord.Embed(timestamp=datetime.datetime.utcnow(),description="**Команды для <@&677397817966198788>:**\n\n`K.ban @user|ID причина` — забанить пользователя.\n`K.kick @user|ID причина` — кикнуть пользователя.\n`K.unban @user|ID причина` — разбанить пользователя.")
        embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
        embed.set_thumbnail(url=message.guild.icon_url)
        await message.channel.send(embed=embed)
        
@client.command()
async def say(message,id):
    if 567025011408240667 == message.author.id or 414119169504575509 == message.author.id:
        id = int(id.replace("#","").replace("<","").replace(">",""))
        msg = await message.channel.history(limit=1).flatten()
        text = " ".join(msg[0].content.split()[2::])
        await client.get_channel(int(id)).send(text)
        
@client.command()
async def clear(message,kol):
    if 567025011408240667 == message.author.id or 414119169504575509 == message.author.id:
        await message.channel.purge(limit=int(kol)+1)
      
@client.command()
async def server(message):
  response = requests.get('https://media.discordapp.net/attachments/734396452843028582/743047501426327653/f4809d0c27843f31.png?width=951&height=616', stream = True)
  response = Image.open(io.BytesIO(response.content))
  idraw = ImageDraw.Draw(response)
  gg = client.get_guild(604636579545219072)
  a, k = gg.members, 0
  for i in a:
    if 'Партнёр [Ур. 1]' in str(i.roles) or 'Партнёр [Ур. 2]' in str(i.roles) or 'Партнёр [Ур. 3]' in str(i.roles):
      k += 1
  
  idraw.text((375, 115), str(len(gg.emojis)), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 30))
  idraw.text((299, 167), str(len(gg.roles)), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 30))
  idraw.text((230, 243), str(gg.verification_level), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
  idraw.text((95, 345), str(gg.owner), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
  idraw.text((90, 425), '27 июля 2019 года', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
  idraw.text((540, 87), str(len(gg.voice_channels)), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 30))
  idraw.text((570, 142), str(len(gg.categories)), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 30))
  idraw.text((619, 215), str(len(gg.text_channels)), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 30))
  idraw.text((655, 290), str(gg.premium_subscription_count), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 30))
  idraw.text((665, 350), str(k), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 27))
  idraw.text((570, 410), str(len(gg.members)), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 27))
  idraw.text((503, 470), str(len(await gg.bans())), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 27))
  idraw.text((620, 559), str(message.author), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 15))
  idraw.text((621, 559), str(message.author), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 15))

  response.save('server_card.png')
  await message.channel.send(file = discord.File(fp = 'server_card.png'))
        
@client.command()
async def deldouble(message,*,urls=None):
  if message.author.id == 414119169504575509:
    if urls is None:
      await message.channel.send('```css\nВы не указали ссылки на сообщения для удаления.```')
    else:
      urls = urls.split()
      for i in urls:
        try:
          channel_id = int(i.split('/')[-2])
          msg_id = int(i.split('/')[-1])
          a = await client.get_channel(channel_id).fetch_message(msg_id)
          await message.channel.send(f'```{a.content}```')
          await a.delete()
        except:
          await message.channel.send(f'```css\nВозникла ошибка в ссылке:\n{i}```')
        
@client.command()
async def modstats(message):
  b = [role.id for role in message.author.roles]
  if 686639786672652363 in b or 620955813850120192 in b:
    a = client.get_guild(604636579545219072).categories
    kol, d = 0, {}
    idd = [747813531495301161, 642102626070036500, 747807222247063642, 642085815597400065, 642104779270782986]
    mm = message.guild.get_role(608600358570295307).members
    for i in mm:
      d.update({i.id:0})
    for i in a:
      if i.id in idd:
        for j in i.text_channels:
          if j.id != 690629182933172324:
            b = await j.history(limit=100, after=datetime.datetime.utcnow() - datetime.timedelta(hours=48)).flatten()
            for k in b:
              d.update({k.author.id:d.setdefault(k.author.id, 0)+1})
    s = ''
    for i, j in d.items():
      s += f'<@{str(i)}> — {j}\n'
    embed = discord.Embed(title='Статистика отдела модерации',description=s,timestamp=datetime.datetime.utcnow())
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    embed.set_thumbnail(url=message.guild.icon_url)
    await message.channel.send(embed=embed)

@client.command()
async def np(message, id=None):
  b = [role.id for role in message.author.roles]
  if message.author.id in admins or 686621891230040077 in b:
    if id is None:
      await message.channel.send('```css\nВы не указали id пользователя.```')
    else:
      try:
        member = client.get_guild(604636579545219072).get_member(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
        if member == message.author:
          await message.channel.send('```css\nВы не можете выдать роль самому себе.```')
        elif 688654966675603491 in [role.id for role in member.roles]:
          await message.channel.send(f'```css\nРоли пользователя {member} НЕ были изменены.```')
        else:
          await member.add_roles(message.guild.get_role(688654966675603491),reason=f'{message.author.name}: Новый партнёр.')
          await message.channel.send(f'```css\nРоли пользователя {member} были изменены.```')
      except:
        await message.channel.send('```css\nПользователя не существует.```')
    
@client.command()
async def disable(message):
    if message.author.id == 414119169504575509 or message.author.id == 567025011408240667:
        everyone = message.guild.get_role(604636579545219072)
        mem = message.guild.get_role(678657735218167818)
        await client.get_channel(678657683246809152).set_permissions(mem, read_messages=False)
        await client.get_channel(685455297614970896).set_permissions(everyone, read_messages=False)
        await client.get_channel(678666229661171724).set_permissions(mem, read_messages=False)
        await client.get_channel(686460961275510786).set_permissions(mem, read_messages=False)
        await message.channel.send('Каналы скрыты.')

@client.command()
async def enable(message):
    if message.author.id == 414119169504575509 or message.author.id == 567025011408240667:
        everyone = message.guild.get_role(604636579545219072)
        mem = message.guild.get_role(678657735218167818)
        await client.get_channel(678657683246809152).set_permissions(mem, read_messages=True)
        await client.get_channel(685455297614970896).set_permissions(everyone, read_messages=True, add_reactions=False)
        await client.get_channel(678666229661171724).set_permissions(mem, read_messages=True, send_messages=None, add_reactions=False)
        await client.get_channel(686460961275510786).set_permissions(mem, read_messages=True, send_messages=None)
        await message.channel.send('Каналы открыты.')
        
@client.command()
async def avatar(message,id=None):
  try:
    if id is None:
        member = await client.fetch_user(int(message.author.id))
    else:
        member = await client.fetch_user(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
    embed=discord.Embed(timestamp=datetime.datetime.utcnow())
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    embed.set_author(name=f'Аватар пользователя {member.name}',icon_url=message.guild.icon_url)
    await message.channel.send(embed=embed)
  except:
    await message.channel.send('```css\nПользователя не существует.```')
    
@client.command()
async def suggest(message):
    if message.channel.id != 678666229661171724:
        await message.channel.send("Канал для предложений => <#678666229661171724>")
    else:
        my_cursor = my_col.find()
        for item in my_cursor:
            if item['id'] == message.author.id:
                await message.channel.purge(limit=1)
                await message.author.send(embed=discord.Embed(colour=discord.Colour.red(),title='Вы не можете оставлять идеи, так как находитесь в чёрном списке.'))
                break
        else:
            a = await message.channel.history(limit=50).flatten()
            for i in a:
                if i.author.id == message.author.id:
                    a = i
                    break
            await message.channel.purge(limit=1)
            my_cursor = my_collection.find()
            msg = " ".join(a.content.split()[1::])
            for item in my_cursor:
                embed=discord.Embed(colour=discord.Colour.blue(),title="Предложение №" + str(item["Nomer"]),description=msg)
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
                b = await message.channel.history(limit=1000).flatten()
                for i in b:
                    if i.author.id == 656029229749764126:
                        a = i
                        break
                my_collection.update_one({"Nomer":item["Nomer"]},{"$set":{"Nomer":item["Nomer"] + 1}})
                my_collection2.insert_one({"id":a.id, "Num":item["Nomer"], "user":str(message.author), "avatar_url":str(message.author.avatar_url), "text":msg})

@client.command()
async def approve(message,num,*msg):
    if message.author.id in admins:
        await message.channel.purge(limit=1)
        a = await client.get_channel(678666229661171724).history(limit=1000).flatten()
        my_cursor = my_collection2.find()
        text = " ".join(msg)
        if message.author.id == 414119169504575509:
            who = 'разработчика '
        else:
            who = 'администратора '
        for item in my_cursor:
            if item["Num"] == int(num):
                aidi = item["id"]
                embed = discord.Embed(colour=discord.Colour.green(),title="Предложение №" + str(num) + " (Принято)",description=item["text"])
                embed.set_author(name=item["user"],icon_url=item["avatar_url"])
                embed.add_field(name="Ответ от " + who + str(message.author.name),value=text)
                embed.set_footer(text='Ответ дан ' + str(str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split('.')[0]),icon_url=message.author.avatar_url)
                break
        for i in a:
            if str(aidi) in str(i):
                await i.edit(embed=embed)
                break

@client.command()
async def deny(message,num,*msg):
    if message.author.id in admins:
        await message.channel.purge(limit=1)
        a = await client.get_channel(678666229661171724).history(limit=1000).flatten()
        my_cursor = my_collection2.find()
        text = " ".join(msg)
        if message.author.id == 414119169504575509:
            who = 'разработчика '
        else:
            who = 'администратора '
        for item in my_cursor:
            if item["Num"] == int(num):
                aidi = item["id"]
                embed = discord.Embed(colour=discord.Colour.red(),title="Предложение №" + str(num) + " (Отклонено)",description=item["text"])
                embed.set_author(name=item["user"],icon_url=item["avatar_url"])
                embed.add_field(name="Ответ от " + who + str(message.author.name),value=text)
                embed.set_footer(text='Ответ дан ' + str(str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split('.')[0]),icon_url=message.author.avatar_url)
                break
        for i in a:
            if str(aidi) in str(i):
                await i.edit(embed=embed)
                break
                
@client.command()
async def problem(message, *, quest=None):
    if message.channel.id != 740651083533254717:
      embed = discord.Embed(description='**[Канал для вопросов](https://discord.com/channels/604636579545219072/740651083533254717)**')
      await message.channel.send(embed=embed)
    elif quest is None:
      await message.message.delete()
    else:
        await message.message.delete()
        embed=discord.Embed(title=f'Вопрос №{str(my_cp.find()[0]["Number"])}',description=quest)
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
        a = await message.channel.send(embed=embed)
        my_cp2.insert_one({"id":message.author.id, "Num":my_cp.find()[0]["Number"], "text":quest, "msg_id":a.id})
        my_cp.update_one({"Number":my_cp.find()[0]["Number"]},{"$set":{"Number":my_cp.find()[0]["Number"] + 1}})
        
@client.command()
async def answer(message, num=None, *, txt=None):
  if message.author.id in admins:
    await message.message.delete()
    my_cursor = my_cp2.find()
    for item in my_cursor:
      if item["Num"] == int(num):
        user = await client.fetch_user(item['id'])
        who = 'разработчика' if message.author.id == 414119169504575509 else 'администратора'
        embed = discord.Embed(colour=discord.Colour.green(),title=f'Вопрос №{num} решён',description=item["text"])
        embed.set_author(name=user, icon_url=user.avatar_url)
        embed.add_field(name=f'Ответ от {who} {message.author.name}', value=txt)
        embed.set_footer(text=f'Вопрос решён {str(str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(".")[0])}',icon_url=message.author.avatar_url)
        msg = await client.get_channel(740651083533254717).fetch_message(item['msg_id'])
        await msg.edit(embed=embed)
        break
                
@client.command()
async def iban(message,id=None,*reason):
  if message.author.id in admins:
    if id is None:
      await message.channel.send('```css\nВведите id человека, которого хотите ограничить в доступе к идеям.```')
    else:
      member = message.guild.get_member(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
      if len(reason) == 0:
        pr = 'Причина не указана.'
      else:
        pr = " ".join(list(reason))
      my_cursor = my_col.find()
      for item in my_cursor:
        if item['id'] == member.id:
          await message.channel.send(f'```css\nПользователь {member} уже добавлен в чёрный список идей.```')
          break
      else:
        await message.channel.send(f'```css\nПользователь {member} больше не сможет оставлять идеи.```')
        my_col.insert_one({'id':member.id, 'reason':pr,'moderator_id':message.author.id,'data':str(str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split('.')[0])})
      
@client.command()
async def iunban(message,id=None):
  if message.author.id in admins:
    if id is None:
      await message.channel.send('```css\nВведите id человека, которого хотите убрать из чёрного списка идей.```')
    else:
      member = message.guild.get_member(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
      my_cursor = my_col.find()
      for item in my_cursor:
        if item['id'] == member.id:
          await message.channel.send(f'```css\nПользователь {member} удалён из чёрного списка идей.```')
          my_col.delete_one({'id':member.id})
          break
      else:
        await message.channel.send(f'```css\nПользователь {member} отсутствует в чёрном списке идей.```')
      
@client.command()
async def ibans(message):
  if message.author.id in admins:
    embed = discord.Embed(title='Чёрный список идей:',timestamp=datetime.datetime.utcnow())
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    embed.set_thumbnail(url=message.guild.icon_url)
    my_cursor = my_col.find()
    k = 0
    for item in my_cursor:
      k += 1
      user = await client.fetch_user(item['id'])
      moderator = await client.fetch_user(item['moderator_id'])
      embed.add_field(name=f"`{k}.` {user} [от {moderator} {item['data']}]",value=f"**{item['reason']}**",inline=False)
    await message.channel.send(embed=embed)
                      
@client.command()
async def info(message, id = None):
    if id is None:
        id = str(message.author.id)
    sp = ['key', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    try:
        member = client.get_guild(604636579545219072).get_member(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
        
        #Аватар
        avatar = requests.get(member.avatar_url, stream = True)
        avatar = Image.open(io.BytesIO(avatar.content))
        avatar = avatar.convert('RGBA')
        
        #Роли пользователя
        b = [role.id for role in member.roles]

        if 608994688078184478 in b or member.id == 567025011408240667:
            response = requests.get('https://media.discordapp.net/attachments/734396452843028582/739819514589610064/b139e06844859b87.png?width=950&height=616', stream = True)
            dol, otd, flag, flag22 = 'Не указана', 'Отдел не указан', False, False
            if member.id == 567025011408240667:
              dol = 'Владелец сервера'
              otd = 'Административный отдел'
              flag = True
            elif 728923691986976828 in b:
              dol = 'Разработчик'
              otd = 'Административный отдел'
              flag22 = True
            elif 620955813850120192 in b:
              dol = 'Администратор'
              otd = 'Административный отдел'
            elif 686639786672652363 in b:
              dol = 'Глава отдела партнерства'
              otd = 'Отдел партнерства'
            elif 686639863390404670 in b:
              dol = 'Глава отдела оценки'
              dol = 'Отдел оценки'
            elif 686639826308825089 in b:
              dol = 'Глава отдела творчества'
              otd = 'Отдел творчества'
            elif 608600358570295307 in b:
              dol = 'Пиар-менеджер'
              otd = 'Отдел партнерства'
            elif 689378345992978434 in b:
              dol = 'Хелпер'
              otd = 'Отдел модерации'
            elif 686642290969935944 in b:
              dol = 'Критик'
              otd = 'Отдел оценки'
            elif 609043489841479700 in b:
              dol = 'Дизайнер'
              otd = 'Отдел творчества'
            elif 686632057191006323 in b:
              dol = 'Редактор'
              otd = 'Отдел творчества'
            response = Image.open(io.BytesIO(response.content))
            idraw = ImageDraw.Draw(response)
            avatar = avatar.resize((212, 212), Image.ANTIALIAS)
            response.paste(avatar, (119, 171, 331, 383))
            nick = member.name if member.nick is None else member.nick
            idraw.text((370, 220), f'aka {nick}', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
            idraw.text((370, 170), f'{member}', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 35))
            a = str(member.created_at).split()[0].split('-')
            idraw.text((370 , 260), f'Дата создания: {a[2]} {sp[int(a[1])]} {a[0]} года', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
            a = str(member.joined_at).split()[0].split('-')
            idraw.text((370, 300), f'Дата вступления: {a[2]} {sp[int(a[1])]} {a[0]} года', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
            c = 'Оффлайн' if str(member.status) == 'offline' else 'Телефон' if member.is_on_mobile() else 'ПК'
            idraw.text((370 , 340), f'Устройство: {c}', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
            idraw.text((370, 420), f'{otd}', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
            idraw.text((370, 460), f'Должность: {dol}', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
            
            msgs = await client.get_channel(764191031318937674).fetch_message(764191228933046361)
            if str(member.id) in msgs.content:
              for i in msgs.content.split('\n'):
                a = i.split('|')
                if a[0] == str(member.id):
                  idraw.text((370, 500), f'На должности с {a[1]}', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
                  break
                
            
            if 677397817966198788 in b or 620955813850120192 in b or member.id == 567025011408240667:
              check = requests.get('https://media.discordapp.net/attachments/737011448441602149/740568726037856368/123.png', stream = True)
              check = Image.open(io.BytesIO(check.content))
              check = check.convert('RGBA')
              check = check.resize((26, 21), Image.ANTIALIAS)
              response.paste(check, (300, 491, 326, 512))
            else:
              check = requests.get('https://media.discordapp.net/attachments/737011448441602149/740570108229058650/1.png', stream = True)
              check = Image.open(io.BytesIO(check.content))
              check = check.convert('RGBA')
              check = check.resize((26, 21), Image.ANTIALIAS)
              response.paste(check, (300, 492, 326, 513))
            
            if str(member.status) == 'offline':
              idraw.text((145, 425), 'Не в сети', (0, 0, 0), font = ImageFont.truetype(r'./Gothic.ttf', size = 35))
              idraw.text((144, 425), 'Не в сети', (54, 57, 63), font = ImageFont.truetype(r'./Gothic.ttf', size = 35))
            elif str(member.status) == 'online':
              idraw.text((169, 425), 'В сети', (0, 0, 0), font = ImageFont.truetype(r'./Gothic.ttf', size = 35))
              idraw.text((168, 425), 'В сети', (67, 181, 129), font = ImageFont.truetype(r'./Gothic.ttf', size = 35))
            elif str(member.status) == 'dnd':
              idraw.text((133, 431), 'Не беспокоить', (0, 0, 0), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
              idraw.text((132, 431), 'Не беспокоить', (240, 71, 71), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
            else:
              idraw.text((143, 429), 'Не активен', (0, 0, 0), font = ImageFont.truetype(r'./Gothic.ttf', size = 30))
              idraw.text((142, 428), 'Не активен', (250, 166, 26), font = ImageFont.truetype(r'./Gothic.ttf', size = 30))
              
            if flag:
              crown = requests.get('https://media.discordapp.net/attachments/737011448441602149/740661534937710612/Screenshot_7.png', stream = True)
              crown = Image.open(io.BytesIO(crown.content))
              crown = crown.convert('RGBA')
              crown = crown.resize((50, 38), Image.ANTIALIAS)
              response.paste(crown, (825, 170, 875, 208))
              
            if flag22:
              crown = requests.get('https://media.discordapp.net/attachments/737011448441602149/741580621528301679/unknown.png', stream = True)
              crown = Image.open(io.BytesIO(crown.content))
              crown = crown.convert('RGBA')
              crown = crown.resize((50, 50), Image.ANTIALIAS)
              response.paste(crown, (830, 160, 880, 210))
                      
            if 608600358570295307 in b or 620955813850120192 in b:
              a = client.get_guild(604636579545219072).categories
              kol = 0
              idd = [747813531495301161, 642102626070036500, 747807222247063642, 642085815597400065, 642104779270782986]
              for i in a:
                if i.id in idd:
                  for j in i.text_channels:
                    if j.id != 690629182933172324:
                      c = await j.history(limit=100, after=datetime.datetime.utcnow() - datetime.timedelta(hours=48)).flatten()
                      for k in c:
                        if k.author.id == member.id:
                          kol += 1
              idraw.text((457, 58), f'{kol}', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
              part = requests.get('https://media.discordapp.net/attachments/689479689756344328/740856668698574858/unknown.png', stream = True)
              part = Image.open(io.BytesIO(part.content))
              part = part.convert('RGBA')
              part = part.resize((40, 25), Image.ANTIALIAS)
              response.paste(part, (410, 63, 450, 88))
              
            response.save('user_card.png')
            await message.channel.send(file = discord.File(fp = 'user_card.png'))
            
        else:
          if 622501691107049502 in b:
            response = requests.get('https://media.discordapp.net/attachments/734396452843028582/739819455584010240/962b3f3b9a98d325.png?width=916&height=594', stream = True)
            color = (143, 48, 54)
          elif 622501656591990784 in b:
            response = requests.get('https://media.discordapp.net/attachments/734396452843028582/739819439201058886/7247d56d464f6232.png?width=916&height=594', stream = True)
            color = (255, 255, 255)
          elif 688654966675603491 in b:
            response = requests.get('https://media.discordapp.net/attachments/734396452843028582/739819426068561954/fcabdd5a422161b1.png?width=916&height=594', stream = True)
            color = (255, 255, 255)
          else:
            response = requests.get('https://media.discordapp.net/attachments/734396452843028582/739819392485031986/94d9b3258f8961be.png?width=916&height=594', stream = True)
            color = (255, 255, 255)
            
          response = Image.open(io.BytesIO(response.content))
          idraw = ImageDraw.Draw(response)
          avatar = avatar.resize((203, 203), Image.ANTIALIAS)
          response.paste(avatar, (115, 165, 318, 368))
          nick = member.name if member.nick is None else member.nick
          idraw.text((365, 220), f'aka {nick}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
          idraw.text((365, 165), f'{member}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 35))
          a = str(member.created_at).split()[0].split('-')
          idraw.text((365, 260), f'Дата создания: {a[2]} {sp[int(a[1])]} {a[0]} года', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
          a = str(member.joined_at).split()[0].split('-')
          idraw.text((365, 300), f'Дата вступления: {a[2]} {sp[int(a[1])]} {a[0]} года', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
          c = 'Оффлайн' if str(member.status) == 'offline' else 'Телефон' if member.is_on_mobile() else 'ПК'
          idraw.text((365, 340), f'Устройство: {c}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))

          if str(member.status) == 'offline':
            idraw.text((136 , 410), 'Не в сети', (0, 0, 0), font = ImageFont.truetype(r'./Gothic.ttf', size = 35))
            idraw.text((135 , 409), 'Не в сети', (54, 57, 63), font = ImageFont.truetype(r'./Gothic.ttf', size = 35))
          elif str(member.status) == 'online':
            idraw.text((164 , 410), 'В сети', (0, 0, 0), font = ImageFont.truetype(r'./Gothic.ttf', size = 35))
            idraw.text((163 , 409), 'В сети', (67, 181, 129), font = ImageFont.truetype(r'./Gothic.ttf', size = 35))
          elif str(member.status) == 'dnd':
            idraw.text((131 , 417), 'Не беспокоить', (0, 0, 0), font = ImageFont.truetype(r'./Gothic.ttf', size = 23))
            idraw.text((130 , 416), 'Не беспокоить', (240, 71, 71), font = ImageFont.truetype(r'./Gothic.ttf', size = 23))
          else:
            idraw.text((134 , 413), 'Не активен', (0, 0, 0), font = ImageFont.truetype(r'./Gothic.ttf', size = 30))
            idraw.text((133 , 412), 'Не активен', (250, 166, 26), font = ImageFont.truetype(r'./Gothic.ttf', size = 30))

          response.save('user_card.png')
          await message.channel.send(file = discord.File(fp = 'user_card.png'))
          
    except:
        try:
            member = await client.fetch_user(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
            avatar = requests.get(member.avatar_url, stream = True)
            avatar = Image.open(io.BytesIO(avatar.content))
            avatar = avatar.convert('RGBA')
            response = requests.get('https://media.discordapp.net/attachments/734396452843028582/739819392485031986/94d9b3258f8961be.png?width=916&height=594', stream = True)
            response = Image.open(io.BytesIO(response.content))
            idraw = ImageDraw.Draw(response)
            avatar = avatar.resize((203, 203), Image.ANTIALIAS)
            response.paste(avatar, (115, 165, 318, 368))
            a = str(member.created_at).split()[0].split('-')
            idraw.text((365, 165), f'{member}', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 35))
            idraw.text((365, 220), f'Дата создания: {a[2]} {sp[int(a[1])]} {a[0]} года', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
            idraw.text((75 , 480), 'Пользователь отсутствует на сервере. Функции ограничены.', (255, 0, 0), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
            
            try:
                await client.get_guild(604636579545219072).fetch_ban(member)
                idraw.text((365 , 260), 'Пользователь в бане.', (255, 0, 0), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
            except:
                idraw.text((365 , 260), 'Пользователь не забанен.', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
                
            response.save('user_card.png')
            await message.channel.send(file = discord.File(fp = 'user_card.png'))
        except:
            await message.channel.send('```css\nПользователя не существует.```')
        
client.run(tt)

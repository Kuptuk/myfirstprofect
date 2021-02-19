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
from Cybernator import Paginator
import time

mm = os.environ.get("Mongo")
tt = os.environ.get("TOKEN")

my_client = pymongo.MongoClient(mm)

my_collection = my_client.Catalog.Number
my_collection2 = my_client.Catalog.txtsug

my_db = my_client.Catalog
my_col = my_db.ibans

my_dp = my_client.Catalog
my_cp = my_dp.numberproblem

my_dp2 = my_client.Catalog
my_cp2 = my_dp2.txtproblem

my_warn = my_client.Catalog.warns
my_warn_kol = my_client.Catalog.warn_kol

my_mute = my_client.Catalog.mute

my_bl = my_client.Catalog.bl
my_bl_kol = my_client.Catalog.bl_kol

my_warn_md = my_client.Catalog.warns_md
my_warn_kol_md = my_client.Catalog.warn_kol_md

my_feb = my_client.feb.feb
my_feb2 = my_client.feb.feb2

client = commands.Bot(command_prefix = "K.", intents = discord.Intents.all())
client.remove_command("help")

admins = [562561140786331650,414119169504575509,529044574660853761]

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.dnd,activity=discord.Streaming(url='https://www.twitch.tv/catalogserverov',name=f"K.help | {str(datetime.datetime.utcnow()+datetime.timedelta(hours=3)).split()[1].split('.')[0][0:5]} [{len(client.get_guild(604636579545219072).members)}]"))
  msg = await client.get_channel(742757799645413378).history(limit=200).flatten()
  b = []
  for i in msg:
      a = i.content.split('https://discord.gg')
      b.append('https://discord.gg' + a[-1])
  await client.get_channel(690827050033872937).purge(limit=10)
  await client.get_channel(690827050033872937).send('https://discord.gg/nKPdC9V')
  global d
  global dk
  global kolpub
  global date_pms
  date_pms = time.time() - 180
  a = client.get_guild(604636579545219072).categories
  idd = [747813531495301161, 642102626070036500, 747807222247063642, 642085815597400065, 642104779270782986]
  c, k, d, dk = [], [], {}, {}
  kolpub = 0
  for i in a:
    if i.id in idd:
      for j in i.text_channels:
        if j.id != 764911620111204383:
          c = await j.history(limit=None).flatten()
          for kk in c:
            kolpub += 1
            men = kk.mentions
            if men != []:
              if d.get(men[0].id) is None:
                d.update({men[0].id:str(kk.created_at + datetime.timedelta(hours=3))})
                dk.update({men[0].id:1})
              elif d.get(men[0].id)<str(kk.created_at + datetime.timedelta(hours=3)):
                d.update({men[0].id:str(kk.created_at + datetime.timedelta(hours=3))})
                dk.update({men[0].id:dk.get(men[0].id)+1})
              else:
                dk.update({men[0].id:dk.get(men[0].id)+1})

  #for cards_badges
  global msgbots; global bag; global medal22; global souz; global help; global rm22; global ngl; global att; global ideas; global bang; global msgotz; global candys; global heart; global msgs
  msgbots = await client.get_channel(764191031318937674).fetch_message(785189856988627004); msgbots = msgbots.content
  bag = await client.get_channel(764191031318937674).fetch_message(807351505455022160); bag = bag.content
  medal22 = await client.get_channel(764191031318937674).fetch_message(788848844980092989); medal22 = medal22.content
  souz = await client.get_channel(764191031318937674).fetch_message(793762809396985866); souz = souz.content
  help = await client.get_channel(764191031318937674).fetch_message(799910635206868992); help = help.content
  rm22 = await client.get_channel(764191031318937674).fetch_message(812211556317921290); rm22 = rm22.content
  ngl = await client.get_channel(764191031318937674).fetch_message(787339282951569420); ngl = ngl.content
  att = await client.get_channel(764191031318937674).fetch_message(807351517581017099); att = att.content
  ideas = await client.get_channel(764191031318937674).fetch_message(785203816785903667); ideas = ideas.content
  bang = await client.get_channel(764191031318937674).fetch_message(786738663433437244); bang = bang.content
  msgotz = await client.get_channel(764191031318937674).fetch_message(782330900746076202); msgotz = msgotz.content
  candys = await client.get_channel(764191031318937674).fetch_message(790310798895480833); candys = candys.content
  heart = await client.get_channel(764191031318937674).fetch_message(810449422328004628); heart = heart.content
  msgs = await client.get_channel(764191031318937674).fetch_message(764191228933046361); msgs = msgs.content
  
  #for cards_img
  global crown; global dev; global bag22; global medal; global allia; global help22; global rm; global ngl2; global att22; global id22; global bg22; global cotz; global candy; global heart22
  crown = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/784811138671575121/owner.png', stream = True).content)).convert('RGBA').resize((37, 37), Image.ANTIALIAS)
  dev = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/785183136362659880/developer.png', stream = True).content)).convert('RGBA').resize((37, 37), Image.ANTIALIAS)
  bag22 = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/807343608868110406/review.png', stream = True).content)).convert('RGBA')
  medal = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/788847715420209222/i_dont_know_what_is_it_say_plz.png', stream = True).content)).convert('RGBA').resize((37, 37), Image.ANTIALIAS)
  allia = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/807310152801845358/-3.png', stream = True).content)).convert('RGBA')
  help22 = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/799910232079466537/helper_1.png', stream = True).content)).convert('RGBA')
  rm = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/796115970003173436/rm.png', stream = True).content)).convert('RGBA')
  ngl2 = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/787359332891230238/1.png', stream = True).content)).convert('RGBA').resize((37, 37), Image.ANTIALIAS)
  att22 = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/807346321487953970/review.png', stream = True).content)).convert('RGBA')
  id22 = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/799910224001106000/puzzle.png', stream = True).content)).convert('RGBA')
  bg22 = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/797119556178935848/rm.png', stream = True).content)).convert('RGBA')
  cotz = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/799910237448175626/review.png', stream = True).content)).convert('RGBA')
  candy = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/797119577951436810/rm.png', stream = True).content)).convert('RGBA')
  heart22 = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/806296162889891890/review.png', stream = True).content)).convert('RGBA')
                                                                                    
  await client.get_channel(728932829026844672).send('```css\n[Данные обновлены, бот перезапущен].```')
    
@client.event
async def on_message(message):
  idd = [747813531495301161, 642102626070036500, 747807222247063642, 642085815597400065, 642104779270782986]
  if message.guild is None:
    embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x310000, description=message.content)
    embed.set_author(name=message.author, icon_url=message.author.avatar_url)
    embed.set_footer(text=message.author.id)
    await client.get_channel(790287251343015986).send(embed=embed)
  elif '.gg' in message.content and message.channel.category.id == 604636579545219073 and message.channel.id != 699306241981415424:
    await message.delete()
    my_mute.delete_one({'id':message.author.id})
    my_mute.insert_one({"id":message.author.id, "data":datetime.datetime.utcnow() + datetime.timedelta(hours=99999)})
    embed = discord.Embed(colour=discord.Colour(0x310000), description=f'Пользователь `{message.author}` был заткнут навсегда автомодерацией.', timestamp=datetime.datetime.utcnow())
    embed.set_footer(text=f'ID: {message.author.id}',icon_url=message.author.avatar_url)
    await message.channel.send(content='<@&677397817966198788>',embed=embed)
    await message.author.remove_roles(message.guild.get_role(648271372585533441),reason=f'Автомодерация: время мута истекло.')
    await message.author.add_roles(message.guild.get_role(648271372585533441),reason=f'Автомодерация: был заткнут навсегда.')
  elif message.channel.id == 740651083533254717:
    if "K.problem" != message.content.split()[0] and message.author.id != 656029229749764126 and not message.author.id in admins:
      await message.delete()
      embed = discord.Embed(timestamp=datetime.datetime.utcnow(),colour=discord.Colour(0x310000),description=f'Ваше сообщение в канале <#740651083533254717> следующего содержания: `{message.content}` было удалено по причине оффтопа.\nПросьба ознакомиться с **[закреплённым информационным сообщением](https://discord.com/channels/604636579545219072/740651083533254717/744485922258681896).**')
      embed.set_footer(text='С уважением, Команда Каталога!',icon_url=message.guild.icon_url)
      await message.author.send(embed=embed)
  elif message.channel.id == 678666229661171724:
    if "K.suggest" != message.content.split()[0] and message.author.id != 656029229749764126 and not message.author.id in admins:
      await message.delete()
      embed = discord.Embed(timestamp=datetime.datetime.utcnow(),colour=discord.Colour(0x310000),description=f'Ваше сообщение в канале <#678666229661171724> следующего содержания: `{message.content}` было удалено по причине оффтопа.\nПросьба ознакомиться с **[закреплённым информационным сообщением](https://discord.com/channels/604636579545219072/678666229661171724/732206889110339655).**')
      embed.set_footer(text='С уважением, Команда Каталога!',icon_url=message.guild.icon_url)
      await message.author.send(embed=embed)
  for item in my_mute.find():
    if item['data'] <= datetime.datetime.utcnow():
      try:
        await client.get_guild(604636579545219072).get_member(item['id']).remove_roles(client.get_guild(604636579545219072).get_role(648271372585533441),reason=f'Время мута истекло.')
      except:
        pass
      my_mute.delete_one({'id':item['id']})
  if message.channel.category_id in idd:
    men = message.mentions
    if men != []:
      d.update({men[0].id:str(message.created_at + datetime.timedelta(hours=3))})
      if dk.get(men[0].id) is None:
        dk.update({men[0].id:1})
      else:
        dk.update({men[0].id:dk.get(men[0].id)+1})
  await client.process_commands(message)

@client.event
async def on_member_join(member):
    await client.get_channel(691142273269760101).send("**+** <@" + str(member.id) + "> (" + str(member) + ")" + " [" + str(client.get_guild(604636579545219072).member_count) + "]")
    for item in my_mute.find():
      if item['id'] == member.id:
        await client.get_guild(604636579545219072).get_member(member.id).add_roles(client.get_guild(604636579545219072).get_role(648271372585533441),reason=f'Попытка обхода мута.')
    await member.add_roles(client.get_guild(604636579545219072).get_role(747815808767361034))
        
@client.event
async def on_member_remove(member):
    await client.get_channel(691142326101344258).send("**-** <@" + str(member.id) + "> (" + str(member) + ")" + " [" + str(client.get_guild(604636579545219072).member_count) + "]")
    
@client.event
async def on_raw_reaction_add(payload):
  gg = client.get_guild(604636579545219072)
  mes = await client.get_channel(642171728273080330).fetch_message(749327767061135502)
  if payload.message_id == 749327767061135502:
    if payload.emoji.name == '🔓':
      await gg.get_member(payload.user_id).add_roles(gg.get_role(678657735218167818))
    if payload.emoji.name == '📰':
      await gg.get_member(payload.user_id).add_roles(gg.get_role(734089506713763861))
    if payload.emoji.name == '📚':
      await gg.get_member(payload.user_id).add_roles(gg.get_role(747815808767361034))
      await mes.remove_reaction('💎',payload.member)
      await mes.remove_reaction('🎮',payload.member)
      await mes.remove_reaction('🎲',payload.member)
      await mes.remove_reaction('🏕️',payload.member)
      await mes.remove_reaction('🧩',payload.member)
      await mes.remove_reaction('💤',payload.member)
    if payload.emoji.name == '💎':
      await gg.get_member(payload.user_id).add_roles(gg.get_role(747815810432762057))
      await gg.get_member(payload.user_id).remove_roles(gg.get_role(747815808767361034))
      await mes.remove_reaction('📚',payload.member)
      await mes.remove_reaction('💤',payload.member)
    if payload.emoji.name == '🎮':
      await gg.get_member(payload.user_id).add_roles(gg.get_role(747815812273930262))
      await gg.get_member(payload.user_id).remove_roles(gg.get_role(747815808767361034))
      await mes.remove_reaction('📚',payload.member)
      await mes.remove_reaction('💤',payload.member)
    if payload.emoji.name == '🎲':
      await gg.get_member(payload.user_id).add_roles(gg.get_role(747815814773604412))
      await gg.get_member(payload.user_id).remove_roles(gg.get_role(747815808767361034))
      await mes.remove_reaction('📚',payload.member)
      await mes.remove_reaction('💤',payload.member)
    if payload.emoji.name == '🏕️':
      await gg.get_member(payload.user_id).add_roles(gg.get_role(747815816426422394))
      await gg.get_member(payload.user_id).remove_roles(gg.get_role(747815808767361034))
      await mes.remove_reaction('📚',payload.member)
      await mes.remove_reaction('💤',payload.member)
    if payload.emoji.name == '🧩':
      await gg.get_member(payload.user_id).add_roles(gg.get_role(747815962866352278))
      await gg.get_member(payload.user_id).remove_roles(gg.get_role(747815808767361034))
      await mes.remove_reaction('📚',payload.member)
      await mes.remove_reaction('💤',payload.member)
    if payload.emoji.name == '💤':
      await gg.get_member(payload.user_id).add_roles(gg.get_role(748838722740420639))
      await gg.get_member(payload.user_id).remove_roles(gg.get_role(747815808767361034))
      await mes.remove_reaction('📚',payload.member)
      await mes.remove_reaction('💎',payload.member)
      await mes.remove_reaction('🎮',payload.member)
      await mes.remove_reaction('🎲',payload.member)
      await mes.remove_reaction('🏕️',payload.member)
      await mes.remove_reaction('🧩',payload.member)
  
@client.event
async def on_raw_reaction_remove(payload):
  gg = client.get_guild(604636579545219072)
  mes = await client.get_channel(642171728273080330).fetch_message(749327767061135502)
  if payload.message_id == 749327767061135502:
    if payload.emoji.name == '🔓':
      await gg.get_member(payload.user_id).remove_roles(gg.get_role(678657735218167818))
    if payload.emoji.name == '📰':
      await gg.get_member(payload.user_id).remove_roles(gg.get_role(734089506713763861))
    if payload.emoji.name == '💎':
      await gg.get_member(payload.user_id).remove_roles(gg.get_role(747815810432762057))
      b = [role.id for role in gg.get_member(payload.user_id).roles]
      if 747815808767361034 not in b and 747815810432762057 not in b and 747815812273930262 not in b and 747815814773604412 not in b and 747815816426422394 not in b and 747815962866352278 not in b and 748838722740420639 not in b:
        await gg.get_member(payload.user_id).add_roles(gg.get_role(747815808767361034),reason='Убрал все категории.')
    if payload.emoji.name == '🎮':
      await gg.get_member(payload.user_id).remove_roles(gg.get_role(747815812273930262))
      b = [role.id for role in gg.get_member(payload.user_id).roles]
      if 747815808767361034 not in b and 747815810432762057 not in b and 747815812273930262 not in b and 747815814773604412 not in b and 747815816426422394 not in b and 747815962866352278 not in b and 748838722740420639 not in b:
        await gg.get_member(payload.user_id).add_roles(gg.get_role(747815808767361034),reason='Убрал все категории.')
    if payload.emoji.name == '🎲':
      await gg.get_member(payload.user_id).remove_roles(gg.get_role(747815814773604412))
      b = [role.id for role in gg.get_member(payload.user_id).roles]
      if 747815808767361034 not in b and 747815810432762057 not in b and 747815812273930262 not in b and 747815814773604412 not in b and 747815816426422394 not in b and 747815962866352278 not in b and 748838722740420639 not in b:
        await gg.get_member(payload.user_id).add_roles(gg.get_role(747815808767361034),reason='Убрал все категории.')
    if payload.emoji.name == '🏕️':
      await gg.get_member(payload.user_id).remove_roles(gg.get_role(747815816426422394))
      b = [role.id for role in gg.get_member(payload.user_id).roles]
      if 747815808767361034 not in b and 747815810432762057 not in b and 747815812273930262 not in b and 747815814773604412 not in b and 747815816426422394 not in b and 747815962866352278 not in b and 748838722740420639 not in b:
        await gg.get_member(payload.user_id).add_roles(gg.get_role(747815808767361034),reason='Убрал все категории.')
    if payload.emoji.name == '🧩':
      await gg.get_member(payload.user_id).remove_roles(gg.get_role(747815962866352278))
      b = [role.id for role in gg.get_member(payload.user_id).roles]
      if 747815808767361034 not in b and 747815810432762057 not in b and 747815812273930262 not in b and 747815814773604412 not in b and 747815816426422394 not in b and 747815962866352278 not in b and 748838722740420639 not in b:
        await gg.get_member(payload.user_id).add_roles(gg.get_role(747815808767361034),reason='Убрал все категории.')
    if payload.emoji.name == '💤':
      await gg.get_member(payload.user_id).remove_roles(gg.get_role(748838722740420639))
      b = [role.id for role in gg.get_member(payload.user_id).roles]
      if 747815808767361034 not in b and 747815810432762057 not in b and 747815812273930262 not in b and 747815814773604412 not in b and 747815816426422394 not in b and 747815962866352278 not in b and 748838722740420639 not in b:
        await gg.get_member(payload.user_id).add_roles(gg.get_role(747815808767361034),reason='Убрал все категории.')
  
@client.command()
async def ping(message):
  if message.author.id in admins:
    await message.send(f'Pong! `{round(client.latency * 1000)}ms`')
  
@client.command() 
async def ev(message,*command):
  if message.author.id == 414119169504575509 or message.author.id == 529044574660853761:
    await message.message.delete()
    command = " ".join(command)
    res = eval(command)
    if inspect.isawaitable(res): 
      res = str(await res)
    else:
      res = str(res)
    if len(res) >= 2000:
      f = open(f'{message.author}.txt', 'w')
      f.write(res)
      f.close()
      await message.channel.send(content='Результат вывода слишком большой.',file = discord.File(fp = f'{message.author}.txt'))
    else:
      await message.channel.send(embed=discord.Embed(description=f'```diff\n- {res}```'))
    
@client.command()
async def help(message):
    msg = await client.get_channel(690827050033872937).history(limit=20).flatten()
    msg = msg[0].content.replace("[","").replace("]","").replace("'","").split(', ')
    embed = discord.Embed(colour=discord.Colour(0x310000),title='Меню Каталог Серверов v1.0.2', description=f"**Страница 1. Команды для всех пользователей:**\n\n`K.help` — помощь.\n`K.avatar @user|ID` — аватар пользователя.\n`K.emoji emoji|ID` — информация об эмодзи (только нашего сервера).\n`K.suggest текст` — предложить свою идею.\n`K.info @user|ID` — информация о пользователе.\n`K.info badges` — обозначение значков.\n`K.server` — информация о сервере.\n`K.stats` — статистика сервера.\n`K.team` — состав Команды сервера [@упоминаниями].\n`K.team -` — состав Команды сервера [текстом].\n`K.problem` — задать вопрос администрации сервера.\n`K.versions` — общедоступная команда для отслеживания версий команд в боте.\n\n[Случайный партнёр]({msg[random.randint(0,len(msg)-1)]})",timestamp=datetime.datetime.utcnow())
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    embed.set_thumbnail(url=message.guild.icon_url)
    
    embed2 = discord.Embed(colour=discord.Colour(0x310000),title='Меню Каталог Серверов v1.0.2', description=f"**Страница 2. Команды для состава:**\n\n`K.staff` — административные команды.\n`K.moder` — команды для модераторов.\n`K.op` — команды для главы отдела партнёрства.\n`K.pm` — команды для пиар-менеджера.\n\n[Случайный партнёр]({msg[random.randint(0,len(msg)-1)]})",timestamp=datetime.datetime.utcnow())
    embed2.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    embed2.set_thumbnail(url=message.guild.icon_url)
    
    embeds = [embed,embed2]
    msg = await message.channel.send(embed=embeds[0])
    page = Paginator(client, msg, only=message.author, use_more=False, embeds=embeds)
    await page.start()
                                                                                    
@client.command()
async def versions(message):
  embed = discord.Embed(colour=0x310000, timestamp=datetime.datetime.utcnow(), description='`Примечание:` С 1 февраля 2021 года мы перешли на собственную систему контроля версий команд бота. Отныне намного проще стало следить за новейшими обновлениями бота.\nЗдесь отображаются только видимые изменения. Всё то, что касается мелких изменений/правок кода, здесь **__пропускается__**. ')
  embed.set_author(name='Список версий и изменений команд бота:', icon_url=message.guild.get_member(656029229749764126).avatar_url)
  embed.add_field(name='`K.info`', value='`v2.0.0 [12.12.2020]` — Глобальное обновление с введением системы значков.\n`v2.9.9 [08.01.2021]` — Глобальный редизайн.\n`v3.0.0 [01.02.2021]` — Автоматически присвоенная версия.\n`v3.0.3 [04.02.2021]` — Редизайн к 14 февраля.\n`v3.0.4 [05.02.2021]` — Обновлён значок владельцу сервера союза.\n`v3.0.5 [06.02.2021]` — Обновление значков.\n`v3.0.8 [16.02.2021]` — 4 значка-метки для партнёров.', inline=False)
  embed.add_field(name='`K.help`', value='`v1.0.0 [01.02.2021]` — Автоматически присвоенная версия.\n`v1.0.1 [04.02.2021]` — Новая команда в списке: `K.versions`.\n`v1.0.2 [16.02.2021]` — Новая команда в списке: `K.team -`.', inline=False)
  embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
  await message.channel.send(embed=embed)
    
@client.command()
async def op(message):
  if 686639786672652363 in [role.id for role in message.author.roles] or message.author.id in admins:
    embed=discord.Embed(colour=discord.Colour(0x310000),timestamp=datetime.datetime.utcnow(),description="**Команды для <@&686639786672652363>:**\n\n`K.modstats date1 date2` — показать статистику отдела партнёрства с date1 по date2.\n`K.apm @user|+/-` — выдать или забрать роли пиар-менеджера соответственно.\n`K.removebl <№случая>` — исключить сервер из чёрного списка по номеру случая.\n`K.rebuke @user|ID reason` — выдать выговор.\n`K.unrebuke №случая` — снять выговор.\n`K.rebukes @user|ID` — просмотреть выговоры.")
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    embed.set_thumbnail(url=message.guild.icon_url)
    await message.channel.send(embed=embed)
    
@client.command()
async def pm(message):
  if 608600358570295307 in [role.id for role in message.author.roles] or message.author.id in admins:
    embed=discord.Embed(colour=discord.Colour(0x310000),timestamp=datetime.datetime.utcnow(),description="**Команды для <@&608600358570295307>:**\n\n`K.addbl <URL> <причина>` — добавить сервер в чёрный список. Вложение обязательно!\n`K.bl` — просмотреть чёрный список серверов каталога.\n`K.np @user|ID` — выдать пользователю роль партнёра первого уровня.\n`K.rebukes` — просмотреть свои выговоры.\n`K.pms` — статистика работы пиар-менеджеров.")
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    embed.set_thumbnail(url=message.guild.icon_url)
    await message.channel.send(embed=embed)
    
@client.command()
async def emoji(message, emoji:discord.Emoji):
  a = f'[webp]({emoji.url_as(format="webp")}) | [jpeg]({emoji.url_as(format="jpeg")}) | [jpg]({emoji.url_as(format="jpg")}) | [png]({emoji.url_as(format="png")})'
  if emoji.animated:
    a += f' | [gif]({emoji.url_as(format="gif")})'
  sp = ['key', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
  data = str(emoji.created_at).split()[0].split('-')
  mod = await message.guild.fetch_emoji(emoji.id)
  embed = discord.Embed(colour=0x310000, timestamp=datetime.datetime.utcnow(), description=f'**Эмодзи [{emoji.name}]({emoji.url})**\n{a}\nСоздан пользователем {mod.user.mention}\n`ID:` {emoji.id}\n`Дата создания:` {data[2]} {sp[int(data[1])]} {data[0]} года')
  embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
  embed.set_thumbnail(url=emoji.url)
  await message.channel.send(embed=embed)
                                                                                    
@client.command()
async def ban(message, id=None, *, reason=None):
    await message.message.delete()
    b = [role.id for role in message.author.roles]
    if 800474182474268734 in b or 677397817966198788 in b or message.author.id in admins:
      if id is None:
        await message.channel.send(embed=discord.Embed(colour=0x310000, description='**Вы не указали пользователя.**'))
      else:
        id = id.replace("!", "").replace("@","").replace("<","").replace(">","")
        if id in [str(i22.id) for i22 in client.get_guild(604636579545219072).get_role(608994688078184478).members]:
          await message.channel.send(embed=discord.Embed(colour=0x310000, description='**Нельзя забанить представителя команды каталога.**'))
        else:
          try:
            a = await client.fetch_user(int(id))
            try:
              if reason is None:
                reason = 'Причина не указана.'
              try:
                embed = discord.Embed(timestamp=datetime.datetime.utcnow(),colour=0x310000,description=f'Вы были забанены на сервере Каталог Серверов по причине `{reason}` модератором `{message.author.name}`. Если Вы считаете, что наказание было выдано необоснованно, у Вас есть возможность его обжаловать **[здесь](https://forms.gle/Ph7VjA86zQSy2crh9)**.')
                embed.set_thumbnail(url=message.guild.icon_url)
                embed.set_footer(text='С уважением, Команда Каталога!')
                await a.send(embed=embed)
                inf = 'Форма обжалования была доставлена нарушителю.'
              except:
                inf = 'Форма обжалования не была доставлена нарушителю.'
              await message.guild.ban(user=a, reason=f'{message.author.name}: {reason}', delete_message_days=0)
              embed = discord.Embed(description=f'```css\n{a} [{a.id}] был забанен.\nПричина: {reason}\n{inf}```',timestamp=datetime.datetime.utcnow())
              giffs = ['https://media1.tenor.com/images/bd4472618c4db926ba1518118280f4e6/tenor.gif?itemid=17267185','https://media.discordapp.net/attachments/728932829026844672/788550786253848586/1_1.gif','https://media.discordapp.net/attachments/728932829026844672/788550799369699378/2.gif','https://media.discordapp.net/attachments/728932829026844672/788550815622889492/4.gif','https://media.discordapp.net/attachments/728932829026844672/788550816948158515/3.gif']
              embed.set_image(url=giffs[random.randint(0,4)])
              embed.set_footer(text=f'Бан от {message.author.name}',icon_url=message.author.avatar_url)
              await message.channel.send(embed=embed)
            except:
              await message.channel.send(embed=discord.Embed(colour=0x310000, description='**Этого пользователя невозможно забанить.**'))
          except:
            await message.channel.send(embed=discord.Embed(colour=0x310000, description='**Пользователя не существует.**'))
        
@client.command()
async def unban(message, id=None, *, reason=None):
    await message.message.delete()
    b = [role.id for role in message.author.roles]
    if 800474182474268734 in b or 677397817966198788 in b or message.author.id in admins:
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
    embed.add_field(name=len(gg.get_role(769916590686732319).members),value="<@&769916590686732319>")
    embed.add_field(name=len(gg.get_role(657636549772705833).members),value="<@&657636549772705833>")
    embed.add_field(name=len(gg.get_role(678657735218167818).members),value="<@&678657735218167818>")
    embed.add_field(name=len(gg.get_role(734089506713763861).members),value="<@&734089506713763861>")
    embed.add_field(name=len(gg.get_role(747815808767361034).members),value='<@&747815808767361034>')
    embed.add_field(name=len(gg.get_role(747815810432762057).members),value='<@&747815810432762057>')
    embed.add_field(name=len(gg.get_role(747815812273930262).members),value='<@&747815812273930262>')
    embed.add_field(name=len(gg.get_role(747815814773604412).members),value='<@&747815814773604412>')
    embed.add_field(name=len(gg.get_role(747815816426422394).members),value='<@&747815816426422394>')
    embed.add_field(name=len(gg.get_role(747815962866352278).members),value='<@&747815962866352278>')
    embed.add_field(name=len(gg.get_role(748838722740420639).members),value='<@&748838722740420639>')
    embed.add_field(name=len(gg.get_role(781877699286925312).members),value="<@&781877699286925312>")
    embed.add_field(name=len(gg.get_role(604645403664711680).members),value="<@&604645403664711680>")
    
    msg = await client.get_channel(690827050033872937).history(limit=20).flatten()
    msg = msg[0].content.replace("[","").replace("]","").replace("'","").split(', ')
    embed.add_field(name="Случайный партнёр",value="[Ссылка на сервер](" + msg[random.randint(0,len(msg)-1)]+")")
    
    embed.add_field(name='឵឵឵',value="Более подробная статистика находится в Beta-тестировании для представителей администрации.")
    
    a = await message.channel.send(embed=embed)
    await a.add_reaction('⬅️')
    await a.add_reaction('➡️')
          
@client.command()
async def team(message,kl=None):
  embeds = []
  embed = discord.Embed(colour=discord.Colour(0x00b0f4),title="I. Команда Каталога | Нынешний состав",description=f"Людей в команде: `{len([i.mention for i in message.guild.get_role(608994688078184478).members])}`",timestamp=datetime.datetime.utcnow())
  
  a = '```md\n' + '\n'.join([i.name for i in message.guild.get_role(686639786672652363).members]).replace(message.author.name,f'#{message.author.name}') + '```' if kl == '-' else '\n'.join([i.mention for i in message.guild.get_role(686639786672652363).members])
  embed.add_field(name=f"```Глава отдела партнёрства:```",value=('Отсутствует.')) if a == '```md\n```' or a == '' else embed.add_field(name=f"```Глава отдела партнёрства:```",value=(a))
  a = '```md\n' + '\n'.join([i.name for i in message.guild.get_role(800474182474268734).members]).replace(message.author.name,f'#{message.author.name}') + '```' if kl == '-' else '\n'.join([i.mention for i in message.guild.get_role(800474182474268734).members])
  embed.add_field(name=f"```Главный модератор:```",value=('Отсутствует.')) if a == '```md\n```' or a == '' else embed.add_field(name=f"```Главный модератор:```",value=(a))
  a = '```md\n' + '\n'.join([i.name for i in message.guild.get_role(686639826308825089).members]).replace(message.author.name,f'#{message.author.name}') + '```' if kl == '-' else '\n'.join([i.mention for i in message.guild.get_role(686639826308825089).members])
  embed.add_field(name=f"```Глава отдела творчества:```",value=('Отсутствует.')) if a == '```md\n```' or a == '' else embed.add_field(name=f"```Глава отдела творчества:```",value=(a))

  a = '```md\n' + '\n'.join([i.name for i in message.guild.get_role(686621891230040077).members]).replace(message.author.name,f'#{message.author.name}') + '```' if kl == '-' else '\n'.join([i.mention for i in message.guild.get_role(686621891230040077).members])
  embed.add_field(name=f"```Отдел партнёрства: [0]```",value=('**[Правила и важное](https://discord.com/channels/604636579545219072/714909100214845541)**\nОтсутствует.')) if a == '```md\n```' or a == '' else embed.add_field(name=f"```Отдел партнёрства: [{len([i.name for i in message.guild.get_role(686621891230040077).members])}]```",value=(f'**[Правила и важное](https://discord.com/channels/604636579545219072/714909100214845541)**\n{a}'))
  c = '```md\n' + '\n'.join([i.name for i in message.guild.get_role(677397817966198788).members]).replace(message.author.name,f'#{message.author.name}') + '```' if kl == '-' else '\n'.join([i.mention for i in message.guild.get_role(677397817966198788).members])
  c2 = '```md\n' + '\n'.join([i.name for i in message.guild.get_role(765212719380037663).members]).replace(message.author.name,f'#{message.author.name}') + '```' if kl == '-' else '\n'.join([i.mention for i in message.guild.get_role(765212719380037663).members])
  embed.add_field(name=f"```Модерация: [0]```",value=('**[Правила и наказания](https://discord.com/channels/604636579545219072/715130816480673872)**\nОтсутствует.')) if c == '```md\n```' or c == '' else embed.add_field(name=f"```Модерация: [{len([i.name for i in message.guild.get_role(677397817966198788).members])}]```",value=(f'**[Правила и наказания](https://discord.com/channels/604636579545219072/715130816480673872)**\n{c}\n\n**`Мл. Модерация: [{len([i.name for i in message.guild.get_role(765212719380037663).members])}]`**\n{c2}'))
  a = '```md\n' + '\n'.join([i.name for i in message.guild.get_role(686618397668147220).members]).replace(message.author.name,f'#{message.author.name}') + '```' if kl == '-' else '\n'.join([i.mention for i in message.guild.get_role(686618397668147220).members])
  embed.add_field(name=f"```Отдел творчества: [0]```",value=('**[Наброски](https://discord.com/channels/604636579545219072/686621337153699929)**\nОтсутствует.\n\n**`Навигация для команды:`**\n**[Рекрутерам](https://discord.com/channels/604636579545219072/776484522329374761)**\n**[Объявления](https://discord.com/channels/604636579545219072/619067194910703626)**\n**[Голосования](https://discord.com/channels/604636579545219072/632524443318616075)**\n**[Информация о ролях](https://discord.com/channels/604636579545219072/616656872703000587/802322890191274014)**\n**[Общие полномочия](https://discord.com/channels/604636579545219072/630432803942563840)**')) if a == '```md\n```' or a == '' else embed.add_field(name=f"```Отдел творчества: [{len([i.name for i in message.guild.get_role(686618397668147220).members])}]```",value=(f'**[Наброски](https://discord.com/channels/604636579545219072/686621337153699929)**\n{a}\n\n**`Навигация для команды:`**\n**[Рекрутерам](https://discord.com/channels/604636579545219072/776484522329374761)**\n**[Объявления](https://discord.com/channels/604636579545219072/619067194910703626)**\n**[Голосования](https://discord.com/channels/604636579545219072/632524443318616075)**\n**[Информация о ролях](https://discord.com/channels/604636579545219072/616656872703000587/802322890191274014)**\n**[Общие полномочия](https://discord.com/channels/604636579545219072/630432803942563840)**'))
  a = '```md\n' + '\n'.join([i.name for i in message.guild.get_role(757890413838467133).members]).replace(message.author.name,f'#{message.author.name}') + '```' if kl == '-' else '\n'.join([i.mention for i in message.guild.get_role(757890413838467133).members])
  embed.add_field(name=f"```В отставке: [0]```",value=('Отсутствует.')) if a == '```md\n```' or a == '' else embed.add_field(name=f"```В отставке: [{len([i.name for i in message.guild.get_role(757890413838467133).members])}]```",value=(a))

  a = '```md\n' + '\n'.join([message.guild.get_member(i).name for i in admins]).replace(message.author.name,f'#{message.author.name}') + '```' if kl == '-' else '\n'.join([f'<@{i}>' for i in admins])
  embed.add_field(name=f"```Администраторы: [0]```",value=('Отсутствуют.')) if a == '```md\n```' or a == '' else embed.add_field(name=f"```Администраторы: [{len(admins)}]```",value=(a))
  embeds.append(embed)
  
  mes = await client.get_channel(764191031318937674).fetch_message(764191228933046361)
  s = ''
  if kl == '-':
    for i in mes.content.split('\n'):
      try:
        s += f'{message.guild.get_member(int(i.split("|")[0])).name} — {i.split("|")[1]}\n'
      except:
        pass
    s = f'```md\n{s.replace(message.author.name,f"#{message.author.name}")}```'
  else:
    for i in mes.content.split('\n'):
      try:
        s += f'{message.guild.get_member(int(i.split("|")[0])).mention} — {i.split("|")[1]}\n'
      except:
        pass

  embed = discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x254fc2, title='II. Команда Каталога | Даты принятий', description=s)
  embeds.append(embed)
  
  mes = await client.get_channel(680089559341727826).history(limit=1).flatten()
  mes = mes[0]
  s = ''
  if kl == '-':
    for i in mes.content.split('\n'):
      try:
        s += f'{message.guild.get_member(int(i.split("|")[0])).name} — {i.split("|")[1]}\n'
      except:
        pass
    s = f'```md\n{s.replace(message.author.name,f"#{message.author.name}")}```'
  else:
    for i in mes.content.split('\n'):
      try:
        s += f'{message.guild.get_member(int(i.split("|")[0])).mention} — {i.split("|")[1]}\n'
      except:
        pass
  embed = discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x344d91, title='III. Команда Каталога | Отпуски сотрудников', description=f'**`Рабочие сокращения:`**\n• ПСЖ — покинул пост по собственному желанию.\n• БВВ — обязательное пояснение при снятии, значащее невозможность возвращения обратно в команду.\n• Понижение — приписывается в случае невыполнения представителем команды определённых обязанностей с последующим понижением до определённой должности.\n\n{s}')
  embeds.append(embed)
  
  msg = await message.channel.send(embed=embeds[0])
  page = Paginator(client, msg, only=message.author, use_more=False, embeds=embeds)
  await page.start()

@client.command()
async def pms(message):
  global date_pms
  if 608600358570295307 in [role.id for role in message.author.roles] or message.author.id in admins:
    if time.time()-date_pms >= 180:
      date_pms = time.time()
      s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, k = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
      msg = await message.channel.send(embed=discord.Embed(colour=0x310000, description='Для подсчёта такого большого количества данных необходимо некоторое время <:ops:798301138633359400> <a:Loading_Pixels:749672972079333497>'))
      embed = discord.Embed(timestamp=datetime.datetime.utcnow(),colour=0x310000, title='Статистика работы отдела партнёрства:')
      for i in [i.id for i in message.guild.get_role(608600358570295307).members]:
        try:
          aktiv = requests.get(f'http://185.244.172.127/stats/pm/list?user={i}').text.split('||')
          a1, a2 = aktiv[0].split('|'), aktiv[1].split('|')
          key = 'md\n#' if message.author.id == i else 'py\n'
          key2 = '#' if message.author.id == i else ''
          embed.add_field(name=f'{message.guild.get_member(i).name}', value=f'```{key}{a1[0]}|{a1[1]}|{a1[2]}|{a1[3]}|{a1[4]}\n{key2}{a2[0]}|{a2[1]}|{a2[2]}|{a2[3]}|{a2[4]}```')
          s1 += int(a1[0]); s2 += int(a1[1]); s3 += int(a1[2]); s4 += int(a1[3]); s5 += int(a1[4])
          s6 += int(a2[0]); s7 += int(a2[1]); s8 += int(a2[2]); s9 += int(a2[3]); s10 += int(a2[4])
        except:
          k += 1
      embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
      embed.description =f'**Навигация:**\n```py\n[За сегодня|В течение недели|От отчёта до отчёта|В течение месяца|За всё время]\n[За 24 часа|За 48 часов|За неделю|За 1 месяц|За 2 месяца]```\n**Количество записей, которые не вошли в подсчёт: `{k}`**\n\n**Общая статистика всех пиар-менеджеров:**\n```css\n[{s1} | {s2} ► {s3} ◄ {s4} | {s5}]\n[{s6} | {s7} ► {s8} ◄ {s9} | {s10}]```'
      await msg.edit(embed=embed)
    else:
      otkat = f'Минут до отката команды: ~{int((180-(time.time()-date_pms))//60)}' if (180-(time.time()-date_pms))//60 != 0 else f'Секунд до отката команды: ~{int(180-(time.time()-date_pms))}'
      await message.channel.send(embed=discord.Embed(colour=0x310000,description=f'```css\n[Данная команда имеет общую задержку в 3 минуты.]```\n```md\n#{otkat}```'))
  
@client.command()
async def staff(message):
    if message.author.id in admins:
      embed=discord.Embed(timestamp=datetime.datetime.utcnow(),description="**Команды для <@&620955813850120192>:**\n\n`K.say #channel|ID текст` — отправить текст определённого содержания в предназначеный канал.\n`K.clear n` — удалить n сообщений в канале.\n`K.disable` — отключить основные каналы (применять только на случай рейда)\n`K.enable` — включить все основные каналы (применять только на случай рейда)\n`K.approve Номер (+/-) Текст` — принять/отклонить предложение\n`K.iban @user|ID Причина` — добавить в чс идей пользователя\n`K.iunban @user|ID` — убрать из чс идей пользователя\n`K.ibans` — посмотреть чс идей\n`K.answer номер|текст` — ответить на вопрос пользователя\n`K.rebuke @user|ID reason` — выдать выговор.\n`K.unrebuke №случая` — снять выговор.\n`K.rebukes @user|ID` — просмотреть выговоры.\n\n`K.cont url` — предоставить файл с контентом сообщения по ссылке на него.")
      embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
      embed.set_thumbnail(url=message.guild.icon_url)
      await message.channel.send(embed=embed)
        
@client.command()
async def moder(message):
    b = [role.id for role in message.author.roles]
    if 800474182474268734 in b or 677397817966198788 in b or 765212719380037663 in b or message.author.id in admins:
      embed=discord.Embed(colour=discord.Colour(0x310000),timestamp=datetime.datetime.utcnow(),description="**Команды для <@&677397817966198788>:**\n\n`K.ban @user|ID причина` — забанить пользователя.\n`K.unban @user|ID причина` — разбанить пользователя.\n\n`K.warn @user|ID причина` — выдать предупреждение пользователю.\n`K.warns @user|ID` — просмотреть предупреждения пользователя.\n`K.unwarn <Номер_случая>` — снять предупреждение по номеру случая.\n\n`K.mute @user|ID time причина` — замутить человека на time часов.\n`K.unmute @user|ID` — размутить человека.\n`K.rebukes` — просмотреть свои выговоры.")
      embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
      embed.set_thumbnail(url=message.guild.icon_url)
      await message.channel.send(embed=embed)
      
@client.command()
async def cont(message, *, url=None):
  await message.message.delete()
  if message.author.id in admins:
    if url is None:
      await message.channel.send(embed=discord.Embed(colour=0x310000, description='**Отсутствует ссылка на сообщение.**'))
    else:
      for i in url.split('\n'):
        try:
          url2 = i.split('/')
          a = await client.get_channel(int(url2[5])).fetch_message(int(url2[6]))
          a = a.content
          f = open(f'{message.author}.txt', 'w')
          f.write(a)
          f.close()
          a = a.replace("`","\`").replace('*','\*').replace('_','\_').replace('<','\<')
          await message.author.send(embed=discord.Embed(timestamp=datetime.datetime.utcnow(),colour=0x310000, description=a).set_footer(text='С уважением, Ваш персональный помощник ^^', icon_url=message.guild.icon_url), file = discord.File(fp = f'{message.author}.txt'))
        except:
          await message.channel.send(embed=discord.Embed(colour=0x310000, description='**Возникла ошибка в ссылке.**'))
        
@client.command()
async def say(message,id,*,text):
  if message.author.id in admins:
    await client.get_channel(int(id)).send(text)
        
@client.command()
async def clear(message,kol):
    if 567025011408240667 == message.author.id or 414119169504575509 == message.author.id:
        await message.channel.purge(limit=int(kol)+1)
      
@client.command()
async def server(message):
  response = requests.get('https://media.discordapp.net/attachments/689800301468713106/795747087643836466/server5.png', stream = True)
  response = Image.open(io.BytesIO(response.content))
  idraw = ImageDraw.Draw(response)
  gg = client.get_guild(604636579545219072)
  k = len(gg.get_role(688654966675603491).members) + len(gg.get_role(622501656591990784).members) + len(gg.get_role(622501691107049502).members) + len(gg.get_role(769916590686732319).members)
  
  idraw.text((365, 115), str(len(gg.emojis)), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 30))
  idraw.text((299, 167), str(len(gg.roles)), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 30))
  idraw.text((230, 243), str(gg.verification_level), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
  idraw.text((100, 345), str(gg.owner), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
  idraw.text((90, 425), '27 июля 2019 года', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
  idraw.text((540, 87), str(len(gg.voice_channels)), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 30))
  idraw.text((570, 142), str(len(gg.categories)), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 30))
  idraw.text((619, 215), str(len(gg.text_channels)), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 30))
  idraw.text((645, 292), str(gg.premium_subscription_count), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 30))
  idraw.text((665, 350), str(k), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 27))
  idraw.text((570, 410), str(len(gg.members)), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 27))
  idraw.text((503, 470), str(len(await gg.bans())), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 27))
  idraw.text((620, 559), str(message.author), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 15))
  idraw.text((621, 559), str(message.author), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 15))
  idraw.text((410, 561), f'{kolpub}', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 12))

  response.save('server_card.png')
  await message.channel.send(file = discord.File(fp = 'server_card.png'))
        
@client.command()
async def dd(message,*,urls=None):
  await message.message.delete()
  if message.author.id == 414119169504575509 or message.author.id == 529044574660853761:
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
async def modstats(message,data1=None,data2=None):
  b = [role.id for role in message.author.roles]
  if 686639786672652363 in b or message.author.id in admins:
    if data1 is None:
      await message.channel.send('```\nНачальная дата не задана.```')
    elif data2 is None:
      await message.channel.send('```\nКонечная дата не задана.```')
    else:
      a = client.get_guild(604636579545219072).categories
      d = {}
      idd = [747813531495301161, 642102626070036500, 747807222247063642, 642085815597400065, 642104779270782986]
      mm = message.guild.get_role(608600358570295307).members
      for i in mm:
        d.update({i.id:0})
      for i in a:
        if i.id in idd:
          for j in i.text_channels:
            if j.id != 764911620111204383:
              b = await j.history(after=datetime.datetime.strptime(data1, '%d.%m.%Y'),before=datetime.datetime.strptime(data2, '%d.%m.%Y')+datetime.timedelta(hours=24)).flatten()
              for k in b:
                d.update({k.author.id:d.setdefault(k.author.id, 0)+1})
      s = ''
      d1 = dict(sorted(d.items(), key = lambda x:x[1],reverse=True))
      for i, j in d1.items():
        s += f'<@{str(i)}> — {j}\n'
      s += f'\n**В период с `{data1}` по `{data2}`.**'
      embed = discord.Embed(title='Статистика отдела партнёрства',description=s,timestamp=datetime.datetime.utcnow())
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
    if message.author.id in admins:
      everyone = message.guild.get_role(604636579545219072)
      mem = message.guild.get_role(678657735218167818)
      await client.get_channel(678657683246809152).set_permissions(mem, read_messages=False)
      await client.get_channel(703615708323643482).set_permissions(everyone, read_messages=False)
      await client.get_channel(740651083533254717).set_permissions(everyone, read_messages=False)
      await client.get_channel(712638398132650095).set_permissions(mem, read_messages=False)
      await client.get_channel(758278272193658902).set_permissions(mem, read_messages=False)
      await client.get_channel(714914939487256677).set_permissions(mem, read_messages=False)
      await client.get_channel(678666229661171724).set_permissions(everyone, read_messages=False)
      await client.get_channel(704677995956404324).set_permissions(mem, read_messages=False)
      await client.get_channel(718027096475041852).set_permissions(mem, read_messages=False)
      await client.get_channel(749242448370204796).set_permissions(mem, read_messages=False)
      await message.channel.send('Каналы скрыты.')
  
@client.command()
async def enable(message):
    if message.author.id in admins:
      everyone = message.guild.get_role(604636579545219072)
      mem = message.guild.get_role(678657735218167818)
      await client.get_channel(678657683246809152).set_permissions(mem, read_messages=True)
      await client.get_channel(703615708323643482).set_permissions(everyone, read_messages=None, embed_links=True, attach_files=True, add_reactions=False)
      await client.get_channel(740651083533254717).set_permissions(everyone, read_messages=None, add_reactions=False)
      await client.get_channel(712638398132650095).set_permissions(mem, read_messages=True)
      await client.get_channel(758278272193658902).set_permissions(mem, read_messages=True)
      await client.get_channel(714914939487256677).set_permissions(mem, read_messages=True)
      await client.get_channel(678666229661171724).set_permissions(everyone, read_messages=None)
      await client.get_channel(704677995956404324).set_permissions(mem, read_messages=True)
      await client.get_channel(718027096475041852).set_permissions(mem, read_messages=True)
      await client.get_channel(749242448370204796).set_permissions(mem, read_messages=True)
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
async def apm(message,id=None,key=None):
  b = [role.id for role in message.author.roles]
  if 686639786672652363 in b or 620955813850120192 in b:
    if id is None:
      await message.channel.send('```\nВы не указали id пользователя.```')
    else:
      try:
        member = client.get_guild(604636579545219072).get_member(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
        if key is None or key == '+':
          await member.add_roles(*[message.guild.get_role(608600358570295307),message.guild.get_role(686621891230040077),message.guild.get_role(608994688078184478)],reason=f'{message.author.name}: Новый пиар-менеджер.')
          await message.channel.send(f'```css\nРоли пиар-менеджера для {member} успешно добавлены.```')
        elif key == '-':
          await member.remove_roles(*[message.guild.get_role(608600358570295307),message.guild.get_role(686621891230040077),message.guild.get_role(608994688078184478)],reason=f'{message.author.name}: Снят(а) с должности.')
          await message.channel.send(f'```css\nРоли пиар-менеджера у {member} успешно сняты.```')
      except:
        await message.channel.send('```css\n[Возникла ошибка.]```')
        
@client.command()
async def warns(message, id=None):
  member, flag = message.author, False
  try:
    b_01 = [role.id for role in message.author.roles]
    if (677397817966198788 in b_01 or 765212719380037663 in b_01 or 800474182474268734 in b_01 or message.author.id in admins) and not id is None:
      member = await client.fetch_user(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
    flag = True
  except:
    await message.channel.send(embed=discord.Embed(colour=0x310000, description='```css\n[Пользователя не существует.]```'))
  if flag:
    posl_date, s, embeds, k, ss_s, spisok = '', '', [], 0, {}, []
    sp = ['key', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    for item in my_warn.find():
      if item['id'] == member.id:
        namember = await client.fetch_user(item["mod_id"])
        if item["data"].split()[0] != posl_date:
          ss_s.update({posl_date:spisok})
          posl_date = item["data"].split()[0]
          spisok = f'`Случай №{item["all"]}:` {item["reason"]}\n`Mod:` {namember}\n'
        else:
          spisok += f'`Случай №{item["all"]}:` {item["reason"]}\n`Mod:` {namember}\n'
    ss_s.update({posl_date:spisok})
    del ss_s['']
    for key, value in ss_s.items():
      txt = key.split()[0].split('-')
      s += f'```css\n[{txt[2]} {sp[int(txt[1])]} {txt[0]} года]```{value}'
      k += 1
      if k == 5:
        embed = discord.Embed(colour=discord.Colour(0x310000),description=f'**Предупреждения пользователя `{member}:`**{s}',timestamp=datetime.datetime.utcnow())
        embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
        embed.set_author(name='Нарушения пользовательского соглашения', icon_url=message.guild.icon_url)
        embeds.append(embed)
        k = 0
        s = ''
    if k != 0:
      embed = discord.Embed(colour=discord.Colour(0x310000),description=f'**Предупреждения пользователя `{member}:`**{s}',timestamp=datetime.datetime.utcnow())
      embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
      embed.set_author(name='Нарушения пользовательского соглашения', icon_url=message.guild.icon_url)
      embeds.append(embed)
    if embeds == []:
      await message.channel.send(embed=discord.Embed(colour=0x310000, description=f'```css\n[У пользователя {member} предупреждения отсутствуют.]```').set_author(name='Нарушения пользовательского соглашения', icon_url=message.guild.icon_url))
    elif len(embeds) == 1:
      await message.channel.send(embed=embeds[0])
    else:
      msg = await message.channel.send(embed=embeds[0])
      page = Paginator(client, msg, only=message.author, use_more=False, embeds=embeds)
      await page.start()
      
@client.command()
async def warn(message, id = None, *, reason=None):
  await message.message.delete()
  b_01 = [role.id for role in message.author.roles]
  if 677397817966198788 in b_01 or 765212719380037663 in b_01 or 800474182474268734 in b_01 or message.author.id in admins:
    if id is None:
      await message.channel.send(embed=discord.Embed(colour=0x310000, description='```css\n[Вы не указали пользователя.]```').set_author(name='Нарушения пользовательского соглашения', icon_url=message.guild.icon_url))
    elif reason is None:
      await message.channel.send(embed=discord.Embed(colour=0x310000, description='```css\n[Вы не указали причину предупреждения.]```').set_author(name='Нарушения пользовательского соглашения', icon_url=message.guild.icon_url))
    else:
      try:
        member = await client.fetch_user(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
        flag = True
      except:
        await message.channel.send(embed=discord.Embed(colour=0x310000, description='```css\n[Пользователя не существует.]```').set_author(name='Нарушения пользовательского соглашения', icon_url=message.guild.icon_url))
        flag = False
      if member == message.author:
        await message.channel.send(embed=discord.Embed(colour=0x310000, description='```css\n[Вы не можете выдать предупреждение самому себе.]```').set_author(name='Нарушения пользовательского соглашения', icon_url=message.guild.icon_url))
      elif member.id in admins:
        await message.channel.send(embed=discord.Embed(colour=0x310000, description='```css\n[Вы не можете выдать предупреждение администратору.]```').set_author(name='Нарушения пользовательского соглашения', icon_url=message.guild.icon_url))
      elif flag:
        all = my_warn_kol.find()[0]["all"]+1
        count = 0
        for item in my_warn.find():
          if item['id'] == member.id:
            for j in my_warn.find():
              if j['id'] == member.id:
                count += 1
            my_warn.insert_one({"id":member.id, "number_warn":count+1, "mod_id":message.author.id, "reason":reason, "all": all, "data":str(str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split('.')[0])})
            break
        else:
          my_warn.insert_one({"id":member.id, "number_warn":1, "mod_id":message.author.id, "reason":reason, "all":all, "data":str(str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split('.')[0])})
        embed = discord.Embed(colour=discord.Colour(0x310000),description=f'**Пользователь `{member}` получил предупреждение `№{count+1}:`**\n```py\nID: {member.id}\nСлучай: {all}\nПричина: {reason}```',timestamp=datetime.datetime.utcnow())
        embed.set_author(name='Нарушения пользовательского соглашения', icon_url=message.guild.icon_url)
        embed.set_footer(text=f'Предупреждение от {message.author.name}',icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        my_warn_kol.update_one({"id":1},{"$set":{"all":all}})
        embed=discord.Embed(colour=0x310000, description = f'**Вы получили предупреждение `№{count+1}:`**\n```py\nСлучай: {all}\nПричина: {reason}```❗ С правилами можно ознакомиться **[здесь](https://discord.com/channels/604636579545219072/642171728273080330/699328371783630988).**',timestamp=datetime.datetime.utcnow())
        embed.set_author(name='Нарушения пользовательского соглашения', icon_url=message.guild.icon_url)
        embed.set_footer(text=f'Предупреждение от {message.author.name}',icon_url=message.author.avatar_url)
        await member.send(embed=embed)
        
@client.command()
async def unwarn(message, number=None):
  await message.message.delete()
  b_01 = [role.id for role in message.author.roles]
  if 677397817966198788 in b_01 or 765212719380037663 in b_01 or 800474182474268734 in b_01 or message.author.id in admins:
    if number is None:
      await message.channel.send(embed=discord.Embed(colour=0x310000, description='```css\n[Вы не указали номер случая.]```').set_author(name='Нарушения пользовательского соглашения', icon_url=message.guild.icon_url))
    else:
      try:
        for item in my_warn.find():
          if item['all'] == int(number):
            a = await client.fetch_user(item['id'])
            b = await client.fetch_user(item['mod_id'])
            sp = ['key', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
            date = item['data'].split()[0].split('-')
            if a == message.author:
              await message.channel.send(embed=discord.Embed(colour=0x310000, description='```css\n[Вы не можете снять себе предупреждение.]```').set_author(name='Нарушения пользовательского соглашения', icon_url=message.guild.icon_url))
            else:              
              embed = discord.Embed(colour=discord.Colour(0x310000),description=f'**Случай `№{number}` благополучно был снят у пользователя `{a}:`**\n```py\nID: {a.id}\nВыдавал модератор: {b}\nБыл наказан: {date[2]} {sp[int(date[1])]} {date[0]} года.\nПричина снятого случая: {item["reason"]}```',timestamp=datetime.datetime.utcnow())
              embed.set_author(name='Нарушения пользовательского соглашения', icon_url=message.guild.icon_url)
              embed.set_footer(text=f'Предупреждение снял(а) {message.author.name}',icon_url=message.author.avatar_url)
              await message.channel.send(embed=embed)
              my_warn.delete_one({'all':int(number)})
            break
        else:
          await message.channel.send(embed=discord.Embed(colour=0x310000, description='```css\n[Указанного случая нет в базе предупреждений.]```').set_author(name='Нарушения пользовательского соглашения', icon_url=message.guild.icon_url))
      except:
        await message.channel.send(embed=discord.Embed(colour=0x310000, description='```css\n[Указанного случая нет в базе предупреждений.]```').set_author(name='Нарушения пользовательского соглашения', icon_url=message.guild.icon_url))
        
@client.command()
async def rebuke(message, id = None, *, reason=None):
  await message.message.delete()
  b_01 = [role.id for role in message.author.roles]
  if 677397817966198788 in b_01 or 800474182474268734 in b_01 or message.author.id in admins:
    if id is None:
      await message.channel.send(embed=discord.Embed(colour=0x310000, description='```css\n[Вы не указали пользователя.]```').set_author(name='Нарушения Команды Каталога', icon_url=message.guild.icon_url))
    elif reason is None:
      await message.channel.send(embed=discord.Embed(colour=0x310000, description='```css\n[Вы не указали причину выговора.]```').set_author(name='Нарушения Команды Каталога', icon_url=message.guild.icon_url))
    else:
      try:
        member = await client.fetch_user(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
        flag = True
      except:
        await message.channel.send(embed=discord.Embed(colour=0x310000, description='```css\n[Пользователя не существует.]```').set_author(name='Нарушения Команды Каталога', icon_url=message.guild.icon_url))
        flag = False
      if member == message.author:
        await message.channel.send(embed=discord.Embed(colour=0x310000, description='```css\n[Вы не можете выдать выговор самому себе.]```').set_author(name='Нарушения Команды Каталога', icon_url=message.guild.icon_url))
      elif member.id in admins:
        await message.channel.send(embed=discord.Embed(colour=0x310000, description='```css\n[Вы не можете выдать выговор администратору.]```').set_author(name='Нарушения Команды Каталога', icon_url=message.guild.icon_url))
      elif flag:
        all = my_warn_kol_md.find()[0]["all"]+1
        count = 0
        for item in my_warn_md.find():
          if item['id'] == member.id:
            for j in my_warn_md.find():
              if j['id'] == member.id:
                count += 1
            my_warn_md.insert_one({"id":member.id, "number_warn":count+1, "mod_id":message.author.id, "reason":reason, "all": all, "data":str(str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split('.')[0])})
            break
        else:
          my_warn_md.insert_one({"id":member.id, "number_warn":1, "mod_id":message.author.id, "reason":reason, "all":all, "data":str(str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split('.')[0])})
        embed = discord.Embed(colour=discord.Colour(0x310000),description=f'**Пользователь `{member}` получил выговор `№{count+1}:`**\n```py\nID: {member.id}\nСлучай: {all}\nПричина: {reason}```',timestamp=datetime.datetime.utcnow())
        embed.set_author(name='Нарушения Команды Каталога', icon_url=message.guild.icon_url)
        embed.set_footer(text=f'Выговор от {message.author.name}',icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        my_warn_kol_md.update_one({"id":1},{"$set":{"all":all}})
        embed=discord.Embed(colour=0x310000, description = f'**Вы получили выговор `№{count+1}:`**\n```py\nСлучай: {all}\nПричина: {reason}```',timestamp=datetime.datetime.utcnow())
        embed.set_author(name='Нарушения Команды Каталога', icon_url=message.guild.icon_url)
        embed.set_footer(text=f'Выговор от {message.author.name}',icon_url=message.author.avatar_url)
        await member.send(embed=embed)
      
@client.command()
async def unrebuke(message, number=None):
  await message.message.delete()
  b_01 = [role.id for role in message.author.roles]
  if 677397817966198788 in b_01 or 800474182474268734 in b_01 or message.author.id in admins:
    if number is None:
      await message.channel.send(embed=discord.Embed(colour=0x310000, description='```css\n[Вы не указали номер случая.]```').set_author(name='Нарушения Команды Каталога', icon_url=message.guild.icon_url))
    else:
      try:
        for item in my_warn_md.find():
          if item['all'] == int(number):
            a = await client.fetch_user(item['id'])
            b = await client.fetch_user(item['mod_id'])
            sp = ['key', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
            date = item['data'].split()[0].split('-')
            if a == message.author:
              await message.channel.send(embed=discord.Embed(colour=0x310000, description='```css\n[Вы не можете снять себе выговор.]```').set_author(name='Нарушения Команды Каталога', icon_url=message.guild.icon_url))
            else:
              embed = discord.Embed(colour=discord.Colour(0x310000),description=f'**Случай `№{number}` благополучно был снят у пользователя `{a}:`**\n```py\nID: {a.id}\nВыдавал администратор: {b}\nБыл наказан: {date[2]} {sp[int(date[1])]} {date[0]} года.\nПричина снятого случая: {item["reason"]}```',timestamp=datetime.datetime.utcnow())
              embed.set_author(name='Нарушения Команды Каталога', icon_url=message.guild.icon_url)
              embed.set_footer(text=f'Выговор снял(а) {message.author.name}',icon_url=message.author.avatar_url)
              await message.channel.send(embed=embed)
              my_warn_md.delete_one({'all':int(number)})
            break
        else:
          await message.channel.send(embed=discord.Embed(colour=0x310000, description='```css\n[Указанного случая нет в базе выговоров.]```').set_author(name='Нарушения Команды Каталога', icon_url=message.guild.icon_url))
      except:
        await message.channel.send(embed=discord.Embed(colour=0x310000, description='```css\n[Указанного случая нет в базе выговоров.]```').set_author(name='Нарушения Команды Каталога', icon_url=message.guild.icon_url))
      
@client.command()
async def rebukes(message, id=None):
  member, flag = message.author, False
  try:
    b_01 = [role.id for role in message.author.roles]
    if (677397817966198788 in b_01 or 800474182474268734 in b_01 or message.author.id in admins) and not id is None:
      member = await client.fetch_user(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
    flag = True
  except:
    await message.channel.send(embed=discord.Embed(colour=0x310000, description='```css\n[Пользователя не существует.]```').set_author(name='Нарушения Команды Каталога', icon_url=message.guild.icon_url))
  if flag:
    posl_date, s, embeds, k, ss_s, spisok = '', '', [], 0, {}, []
    sp = ['key', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    for item in my_warn_md.find():
      if item['id'] == member.id:
        namember = await client.fetch_user(item["mod_id"])
        if item["data"].split()[0] != posl_date:
          ss_s.update({posl_date:spisok})
          posl_date = item["data"].split()[0]
          spisok = f'`Случай №{item["all"]}:` {item["reason"]}\n`Adm:` {namember}\n'
        else:
          spisok += f'`Случай №{item["all"]}:` {item["reason"]}\n`Adm:` {namember}\n'
    ss_s.update({posl_date:spisok})
    del ss_s['']
    for key, value in ss_s.items():
      txt = key.split()[0].split('-')
      s += f'```css\n[{txt[2]} {sp[int(txt[1])]} {txt[0]} года]```{value}'
      k += 1
      if k == 5:
        embed = discord.Embed(colour=discord.Colour(0x310000),description=f'**Выговоры пользователя `{member}:`**{s}',timestamp=datetime.datetime.utcnow())
        embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
        embed.set_author(name='Нарушения Команды Каталога', icon_url=message.guild.icon_url)
        embeds.append(embed)
        k = 0
        s = ''
    if k != 0:
      embed = discord.Embed(colour=discord.Colour(0x310000),description=f'**Выговоры пользователя `{member}:`**{s}',timestamp=datetime.datetime.utcnow())
      embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
      embed.set_author(name='Нарушения Команды Каталога', icon_url=message.guild.icon_url)
      embeds.append(embed)
    if embeds == []:
      await message.channel.send(embed=discord.Embed(colour=0x310000, description=f'```css\n[У пользователя {member} выговоры отсутствуют.]```').set_author(name='Нарушения Команды Каталога', icon_url=message.guild.icon_url))
    elif len(embeds) == 1:
      await message.channel.send(embed=embeds[0])
    else:
      msg = await message.channel.send(embed=embeds[0])
      page = Paginator(client, msg, only=message.author, use_more=False, embeds=embeds)
      await page.start()
                        
@client.command()
async def mute(message, id=None, time=None, *, reason=None):
  await message.message.delete()
  b = [role.id for role in message.author.roles]
  if 677397817966198788 in b or 765212719380037663 in b or 800474182474268734 in b or message.author.id in admins:
    if id is None:
      await message.channel.send('```css\nВы не указали id нарушителя.```')
    elif time is None:
      await message.channel.send('```css\nВы не указали время мута.```')
    else:
      reason = 'Причина не указана' if reason is None else reason
      try:
        member = message.guild.get_member(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
        flag = True
      except:
        await message.channel.send('```css\nУказанный пользователь отсутствует на сервере.```')
        flag = False
      if flag:
        try:
          time = int(time.replace('h',''))
          flag2 = True
        except:
          await message.channel.send('```css\nВозникла ошибка в формате времени.```')
          flag2 = False
        if flag2:
          my_mute.delete_one({'id':member.id})
          my_mute.insert_one({"id":member.id, "data":datetime.datetime.utcnow() + datetime.timedelta(hours=time)})
          embed = discord.Embed(colour=discord.Colour(0x310000), description=f'Пользователь `{member}` был заткнут на `{time}ч.` по причине: `{reason}`', timestamp=datetime.datetime.utcnow())
          embed.set_footer(text=f'Мут от {message.author.name}',icon_url=message.author.avatar_url)
          await message.channel.send(embed=embed)
          await member.remove_roles(message.guild.get_role(648271372585533441),reason=f'{message.author.name}: Время мута истекло.')
          await member.add_roles(message.guild.get_role(648271372585533441),reason=f'{message.author.name}: Был заткнут на {time}ч. ({reason})')
          
@client.command()
async def unmute(message,id=None):
  await message.message.delete()
  b = [role.id for role in message.author.roles]
  if 677397817966198788 in b or 765212719380037663 in b or 800474182474268734 in b or message.author.id in admins:
    if id is None:
      await message.channel.send('```css\nВы не указали id нарушителя.```')
    else:
      try:
        member = message.guild.get_member(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
        flag = True
      except:
        await message.channel.send('```css\nУказанный пользователь отсутствует на сервере.```')
        flag = False
      if flag:
        await member.remove_roles(message.guild.get_role(648271372585533441),reason=f'Мут снят модератором {message.author}.')
        my_mute.delete_one({'id':member.id})
        embed = discord.Embed(colour=discord.Colour(0x310000),description=f'Пользователь `{member}` успешно размучен.',timestamp=datetime.datetime.utcnow())
        embed.set_footer(text=f'Размут от {message.author.name}',icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    
@client.command()
async def addbl(message,url:discord.Invite=None,*,reason=None):
  if message.author.id in admins or 608600358570295307 in [role.id for role in message.author.roles]:
    reason = 'Причина не указана.' if reason is None else reason
    flag = False
    try:
      a = message.message.attachments[0].url
      flag = True
    except:
      await message.channel.send('```scss\nОтсутствует доказательство-вложение.```')
    if flag:
      embed=discord.Embed(colour=discord.Colour(0x310000),description=f'Сервер `{url.guild}` был добавлен в чёрный список `[Случай №{my_bl_kol.find()[0]["number"]}]` по причине: `{reason}`',timestamp=datetime.datetime.utcnow())
      embed.set_thumbnail(url=url.guild.icon_url)
      embed.set_footer(text=f'Добавил {message.author.name}',icon_url=message.author.avatar_url)
      embed.set_image(url=a)
      await message.channel.send(embed=embed)
      my_bl.insert_one({"id_guild":url.guild.id, "mod_id":message.author.id, "avatar":str(url.guild.icon_url), "name_guild":url.guild.name,"reason":reason, "all": my_bl_kol.find()[0]["number"], "dokz":a, "url":str(url), "data":str(str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split('.')[0])})
      my_bl_kol.update_one({"idd":1}, {"$inc": {"number": 1}})
      
@client.command()
async def removebl(message,num=None):
  if message.author.id in admins or 686639786672652363 in [role.id for role in message.author.roles]:
    if num is None:
      await message.channel.send('```scss\nВы не указали номер случая.```')
    else:
      try:
        for item in my_bl.find():
          if item['all'] == int(num):
            embed = discord.Embed(colour=discord.Colour(0x310000),description=f'{item["name_guild"]} `[Случай №{num}]` удалён из чёрного списка.',timestamp=datetime.datetime.utcnow())
            embed.set_footer(text=f'Удалил {message.author.name}',icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)
            my_bl.delete_one({'all':int(num)})
            break
        else:
          await message.channel.send('```Указанного случая нет в базе чёрного списка.```')
      except:
        await message.channel.send('```Указанного случая нет в базе чёрного списка.```')
      
@client.command()
async def bl(message):
  if message.author.id in admins or 608600358570295307 in [role.id for role in message.author.roles]:
    ss = await message.channel.send(embed=discord.Embed(colour=discord.Colour(0x310000),description='**Пожалуйста, подождите, собираем информацию...** <a:just_another_anime_sip:758212768704364564>'))
    embed = discord.Embed(colour=discord.Colour(0x310000),title='Чёрный список серверов каталога')
    embeds,k = [],1
    for item in my_bl.find():
      if k % 6 == 0:
        embeds.append(embed)
        embed = discord.Embed(colour=discord.Colour(0x310000),title='Чёрный список серверов каталога')
        k = 1
      try:
        a = await client.fetch_invite(item['url'])
        namemember = await client.fetch_user(item['mod_id'])
        embed.add_field(name=f'`Случай №{item["all"]}` {item["data"]} от `{namemember}`',value=f'**[Аватар]({a.guild.icon_url})** | {a.guild} | **[Вложение]({item["dokz"]})**\n`ID:` {a.guild.id} <:Check_from_Helen22:760820919265656842>\n`Причина:` {item["reason"]}',inline=False)
        k += 1
      except:
        namemember = await client.fetch_user(item['mod_id'])
        embed.add_field(name=f'`Случай №{item["all"]}` {item["data"]} от `{namemember}`',value=f'**[Аватар]({item["avatar"]})** | {item["name_guild"]} | **[Вложение]({item["dokz"]})**\n`ID:` {item["id_guild"]} :x:\n`Причина:` {item["reason"]}',inline=False)
        k += 1
    embeds.append(embed)
    await ss.delete()
    msg = await message.channel.send(embed=embeds[0])
    page = Paginator(client, msg, only=message.author, use_more=False, embeds=embeds)
    await page.start()
                        
@client.command()
async def suggest(message, *, txt=None):
    if message.channel.id != 678666229661171724:
      embed = discord.Embed(description='**[Канал для предложений](https://discord.com/channels/604636579545219072/678666229661171724)**')
      await message.channel.send(embed=embed)
    elif txt is None:
      await message.message.delete()
    else:
      my_cursor = my_col.find()
      for item in my_cursor:
          if item['id'] == message.author.id:
            await message.message.delete()
            embed = discord.Embed(timestamp=datetime.datetime.utcnow(),colour=discord.Colour(0x310000),description=f'Ваше сообщение в канале <#678666229661171724> следующего содержания: `{message.message.content}` было удалено, т.к. вы были занесены в чёрный список предложений.')
            embed.set_footer(text='С уважением, Команда Каталога!',icon_url=message.guild.icon_url)
            await message.author.send(embed=embed)
            break
      else:
        await message.message.delete()
        embed=discord.Embed(title=f'Предложение №{str(my_collection.find()[0]["Number"])}',description=txt)
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
        a = await message.channel.send(embed=embed)
        my_collection2.insert_one({"id":message.author.id, "Num":my_collection.find()[0]["Number"], "text":txt, "msg_id":a.id})
        my_collection.update_one({"idd":1}, {"$inc": {"Number": 1}})
      
@client.command()
async def approve(message, num=None, arg=None, *, txt=None):
  if message.author.id in admins:
    await message.message.delete()
    my_cursor = my_collection2.find()
    color = discord.Colour.red() if arg == '-' else discord.Colour.green()
    mb = '[Отклонено]' if arg == '-' else '[Принято]'
    for item in my_cursor:
      if item["Num"] == int(num):
        user = await client.fetch_user(item['id'])
        who = 'владельца сервера' if message.author.id == 414119169504575509 else 'администратора'
        embed = discord.Embed(colour=color,title=f'Предложение №{num} {mb}',description=item["text"])
        embed.set_author(name=user, icon_url=user.avatar_url)
        embed.add_field(name=f'Ответ от {who} {message.author.name}', value=txt)
        embed.set_footer(text=f'Ответ дан {str(str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(".")[0])}',icon_url=message.author.avatar_url)
        msg = await client.get_channel(678666229661171724).fetch_message(item['msg_id'])
        await msg.edit(embed=embed)
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
        who = 'владельца сервера' if message.author.id == 414119169504575509 else 'администратора'
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
async def set_rm(message,id=None):
  if 686639786672652363 in [role.id for role in message.author.roles] or message.author.id in admins:
    if id is None:
      await message.channel.send('```css\nВы не указали id лучшего работника.```')
    else:
      await client.get_channel(784815029118828548).send(id)
      await message.channel.send(f'```css\n{id} признан лучшим работником.```')
                      
@client.command()
async def info(message, id = None):
    if id == 'badges':
      embed = discord.Embed(colour=discord.Colour(0x310000),timestamp=datetime.datetime.utcnow(),title=':clipboard: Обозначение значков v3.0.5')
      embed.add_field(name='Значки Staff:',value='<:owner:784812161959854120> Владельцу сервера.\n<:developer:785191301321719828> Людям, принявшим участие в разработке/улучшении персонального бота.\n🏆 Лучшему работнику на данный момент.',inline=False)
      embed.add_field(name='Пользовательские значки 1:',value='<:KC_bug_hunter:807347751641022486> Людям, нашедшим баги в боте <@656029229749764126> с последующим информированием разработчика <@414119169504575509> в личных сообщениях.\n`Примечание:` имея данный значок, открывается возможность быть приглашённым на закрытое BETA-тестирование нововведений бота. При замечании определённого бага несколькими пользователями, только первый получит значок.\n<:old:788850405308104765> Людям, которые внесли огромный вклад в развитие сервера.\n<:alliance:807310319852585051> Представителям союза каталога.\n<:helper:799908854795731004> Людям, которые оказывали помощь новичкам, отвечая на их различные вопросы в общем чате.\n`Примечание:` помните, что вы можете лишиться значка за проявленную халатность.\n<:secret:787360058328481812> Секретный значок.',inline=False)
      embed.add_field(name='Пользовательские значки 2:',value='<:Attentive:807347751700004926> Нашли определённые несостыковки в информационных сообщениях? Сообщите администрации проекта и получите значок за внимательность.\n`Примечание:` значок распространяется на пользователей, что нашли определённые несостыковки в конкретном случае первыми.\n<:puzzle:799908854783016960> Предложившим большое количество дельных идей.\n‼️ Подавшему большое количество жалоб.\n<:review:799908854812377098> Оставившему рецензию серверу на 3-х мониторингах.\n`Примечание:` **[здесь](https://server-discord.com/604636579545219072)** и **[здесь](https://discord-server.com/ru/604636579545219072)**.',inline=False)
      embed.add_field(name='Значки-метки:',value='<:booster:797134090594680942> Бустерам сервера.\n<:p1:811016319607504936> Партнёру 1-го уровня.\n<:p2:811016319234605107> Партнёру 2-го уровня.\n<:p3:811016319716950046> Партнёру 3-го уровня.\n<:pmax:811016319238406175> Партнёру уровня MAX.',inline=False)
      embed.add_field(name='Значки ивентов:',value='🍬 Выдаётся в новогоднюю ночь 2021 года за найденные пасхалки. Существует до 2022 года.\n❤️ Победителю ивента на день влюблённых. Существует до конца мая 2021 года.',inline=False)
      embed.add_field(name='Примечания:',value='• Значков всего без учёта кастомных: `15`.\n• Кастомный значок возможен в случае больших заслуг перед Каталогом, а так же за 2 ваших буста.\n• Значки выдаются автоматизированной системой. Это значит, что нет необходимости выпрашивать их у администрации сервера.',inline=False)
      embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
      embed.set_thumbnail(url=message.guild.icon_url)
      await message.channel.send(embed=embed)
    else:
      if id is None or id == '-':
        id = str(message.author.id)
      global msgbots; global bag; global medal22; global souz; global help; global rm22; global ngl; global att; global ideas; global bang; global msgotz; global candys; global heart; global msgs
      global crown; global dev; global bag22; global medal; global allia; global help22; global rm; global ngl2; global att22; global id22; global bg22; global cotz; global candy; global heart22
      sp = ['key', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
      randch = random.randint(1,100)
      color = (255, 255, 255)
      try:
          async with message.typing():
            member = client.get_guild(604636579545219072).get_member(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
            mid = member.id

            avatar = requests.get(member.avatar_url, stream = True)
            avatar = Image.open(io.BytesIO(avatar.content))
            avatar = avatar.convert('RGBA')

            b = [role.id for role in member.roles]
            if 608994688078184478 in b and list(message.message.content)[-1] != '-':
              if randch == 1:
                response = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/784744502048063499/glitch.png', stream = True).content))
                idraw = ImageDraw.Draw(response)
              elif mid == 713780299024039936:
                response = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/802574569457713152/test.png', stream = True).content))
                idraw = ImageDraw.Draw(response)
              elif mid == 735540766289690646:
                response = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/802897713330126868/card_helya.png', stream = True).content))
                idraw = ImageDraw.Draw(response)
              elif mid == 571006178444836875:
                response = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/807933906975719444/cardo4ka.png', stream = True).content))
                idraw = ImageDraw.Draw(response)
              else:
                response = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/806867010851962880/staff.png', stream = True).content))
                idraw = ImageDraw.Draw(response)
              dol, otd, flag = 'Не указана', 'Отдел не указан', False
              if mid == 414119169504575509:
                dol = 'Разработчик'
                otd = 'Административный отдел'
                flag = True
              elif 620955813850120192 in b:
                dol = 'Администратор'
                otd = 'Административный отдел'
              elif 800474182474268734 in b:
                dol = 'Главный Модератор'
                otd = 'Административный отдел'
              elif 686639786672652363 in b:
                dol = 'Глава отдела партнерства'
                otd = 'Отдел партнерства'
              elif 686639826308825089 in b:
                dol = 'Глава отдела творчества'
                otd = 'Отдел творчества'
              elif 608600358570295307 in b:
                dol = 'Пиар-менеджер'
                otd = 'Отдел партнерства'
              elif 609043489841479700 in b:
                dol = 'Дизайнер'
                otd = 'Отдел творчества'
              elif 677397817966198788 in b:
                dol = 'аперативник'
                otd = 'Отдел ОБТ "Модер"'
              idraw.text((365, 380), f'{otd}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
              idraw.text((365, 420), f'Должность: {dol}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))

              if str(mid) in msgs:
                for i in msgs.split('\n'):
                  a = i.split('|')
                  if a[0] == str(mid):
                    idraw.text((365, 460), f'В команде с {a[1]}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
                    break

              warnow = 0
              for item in my_warn_md.find():
                if item['id'] == mid:
                  warnow += 1
              idraw.text((145 , 440), f'Выговоров: {warnow}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))

            else:
              if randch == 1:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/784744502048063499/glitch.png', stream = True)
              elif mid == 357518684723478540:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/812249880084873216/card_moxxie1.png', stream = True)
              elif mid == 414119169504575509:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/812252851077382164/card_helya.png', stream = True)
              elif not member.premium_since is None:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/806867001330630676/booster.png', stream = True)
              elif 769916590686732319 in b:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/806867007156518932/max.png', stream = True)
              elif 622501691107049502 in b:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/806867009064927282/pr3.png', stream = True)
              elif 622501656591990784 in b:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/806867005503176734/gold.png', stream = True)
              elif 688654966675603491 in b:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/806867012067917831/test_ivent.png', stream = True)
              else:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/806867004198748160/classical.png', stream = True)
              response = Image.open(io.BytesIO(response.content))
              idraw = ImageDraw.Draw(response)
              if 769916590686732319 in b or 622501691107049502 in b or 622501656591990784 in b or 688654966675603491 in b:
                idraw.text((365, 440), f'Дата последнего обновления:', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
                if d.get(mid) is not None:
                  datet = d.get(mid).split('.')[0].split()[0].split('-')
                  datet2 = d.get(mid).split('.')[0].split()[1]
                  idraw.text((365, 480), f'{datet[2]} {sp[int(datet[1])]} {datet[0]} года в {datet2}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
                else:
                  idraw.text((365, 480), f'Неизвестна', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
                kolvo = dk.get(mid) if dk.get(mid) is not None else 0
                idraw.text((135, 440), f'Публикаций: {kolvo}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))

              try:
                aktiv = requests.get(f'http://185.244.172.127/stats?user={mid}').text
              except:
                aktiv = '? сообщений|? минут'
              idraw.text((365, 360), f'Активность сегодня: {aktiv.split("|")[0]}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
              idraw.text((365, 400), f'Voice сегодня: {aktiv.split("|")[1]}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))

            prioritet = -1
            ppz = [365, 405, 445, 485, 525, 565, 605, 645, 685, 725, 765, 805, 845, 885, 925, 965, 1005]
            avatar = avatar.resize((212, 212), Image.ANTIALIAS)
            response.paste(avatar, (118, 169))
            idraw.text((400, 150), f'{member}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 35))
            a = str(member.created_at).split()[0].split('-')
            idraw.text((365 , 260), f'Дата создания: {a[2]} {sp[int(a[1])]} {a[0]} года', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
            a2 = str(member.joined_at).split()[0].split('-')
            idraw.text((365, 300), f'Дата вступления: {a2[2]} {sp[int(a2[1])]} {a2[0]} года', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))

            warnow = 0
            for item in my_warn.find():
              if item['id'] == mid:
                warnow += 1
            idraw.text((100 , 400), f'Предупреждений: {warnow}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
            
            mst = str(member.status)
            if mst == 'offline':
              st = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/784799364014276608/work4_79.png', stream = True).content)).convert('RGBA').resize((40, 40), Image.ANTIALIAS)
              y_2021 = 155
            elif member.is_on_mobile():
              if mst == 'online':
                st = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/784741708964560906/t1.png', stream = True).content)).convert('RGBA').resize((40, 40), Image.ANTIALIAS)
              elif mst == 'idle':
                st = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/784741713007869972/t2.png', stream = True).content)).convert('RGBA').resize((40, 40), Image.ANTIALIAS)
              elif mst == 'dnd':
                st = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/784741716804239370/t3.png', stream = True).content)).convert('RGBA').resize((40, 40), Image.ANTIALIAS)
              y_2021 = 150
            else:
              if mst == 'online':
                st = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/784799369160425502/work11.png', stream = True).content)).convert('RGBA').resize((40, 40), Image.ANTIALIAS)
              elif mst == 'idle':
                st = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/784799375640494110/work12.png', stream = True).content)).convert('RGBA').resize((40, 40), Image.ANTIALIAS)
              elif mst == 'dnd':
                st = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/784799380418723850/work31.png', stream = True).content)).convert('RGBA').resize((40, 40), Image.ANTIALIAS)
              y_2021 = 155
            response.paste(st, (360, y_2021), st)

            #14feb
            if [i for i in my_feb2.find({'id':mid})] == []:
              feb = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/806905242255097906/review.png', stream = True).content)).convert('RGBA')
              response.paste(feb, (55, 517), feb)
              idraw.text((100 , 520), f'Вы никого не любите? ;(', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 23))
            else:
              feb = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/806296162889891890/review.png', stream = True).content)).convert('RGBA')
              response.paste(feb, (55, 517), feb)
              idraw.text((100 , 520), f'Любит {my_feb2.find({"id":mid})[0]["kogo"]}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 23))

            #prioritetnostb
            net_zn = 0
            if mid == message.guild.owner.id:
              prioritet += 1
              response.paste(crown, (ppz[prioritet], 205), crown)
              net_zn += 1

            if str(mid) in msgbots:
              prioritet += 1
              response.paste(dev, (ppz[prioritet], 205), dev)
              net_zn += 1

            if str(mid) in bag:
              prioritet += 1
              response.paste(bag22, (ppz[prioritet], 205), bag22)
              net_zn += 1

            if str(mid) in medal22:
              prioritet += 1
              response.paste(medal, (ppz[prioritet], 205), medal)
              net_zn += 1

            if str(mid) in souz:
              prioritet += 1
              response.paste(allia, (ppz[prioritet], 205), allia)
              net_zn += 1

            if str(mid) in help:
              prioritet += 1
              response.paste(help22, (ppz[prioritet], 205), help22)
              net_zn += 1

            if str(mid) in rm22:
              prioritet += 1
              response.paste(rm, (ppz[prioritet], 205), rm)
              net_zn += 1

            if str(mid) in ngl:
              prioritet += 1
              response.paste(ngl2, (ppz[prioritet], 205), ngl2)
              net_zn += 1

            if str(mid) in att:
              prioritet += 1
              response.paste(att22, (ppz[prioritet], 205), att22)
              net_zn += 1

            if str(mid) in ideas:
              prioritet += 1
              response.paste(id22, (ppz[prioritet], 205), id22)
              net_zn += 1

            if str(mid) in bang:
              prioritet += 1
              response.paste(bg22, (ppz[prioritet], 205), bg22)
              net_zn += 1

            if str(mid) in msgotz:
              prioritet += 1
              response.paste(cotz, (ppz[prioritet], 205), cotz)
              net_zn += 1

            if 688654966675603491 in b or 622501656591990784 in b or 622501691107049502 in b or 769916590686732319 in b:
              if 688654966675603491 in b:
                znpart = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/811015500712509490/6.png', stream = True).content)).convert('RGBA')
              elif 622501656591990784 in b:
                znpart = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/811015502381187092/34.png', stream = True).content)).convert('RGBA')
              elif 622501691107049502 in b:
                znpart = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/811015503648784424/41.png', stream = True).content)).convert('RGBA')
              elif 769916590686732319 in b:
                znpart = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/811015504348708914/52.png', stream = True).content)).convert('RGBA')
              prioritet += 1
              response.paste(znpart, (ppz[prioritet], 205), znpart)
              net_zn += 1

            if str(mid) in candys:
              prioritet += 1
              response.paste(candy, (ppz[prioritet], 205), candy)
              net_zn += 1

            if str(mid) in heart:
              prioritet += 1
              response.paste(heart22, (ppz[prioritet], 205), heart22)
              net_zn += 1

            if mid == 394757049893912577:
              fat = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/785202689532755988/fatal.png', stream = True).content)).convert('RGBA').resize((37, 37), Image.ANTIALIAS)
              response.paste(fat, (54, 100), fat)   
            elif mid == 713780299024039936:
              ang = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/682929799991132207/797940366254800906/rm.png', stream = True).content)).convert('RGBA')
              response.paste(ang, (54, 100), ang)
            elif mid == 346263496394276867:
              nef = Image.open(io.BytesIO(requests.get('https://cdn.discordapp.com/attachments/682929799991132207/800773662453530644/review.png', stream = True).content)).convert('RGBA')
              response.paste(nef, (54, 100), nef)
            elif mid == 357518684723478540:
              mox = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/682929799991132207/803224903620362260/review.png', stream = True).content)).convert('RGBA')
              response.paste(mox, (54, 100), mox)
            elif mid == 722394482515116072:
              gof = Image.open(io.BytesIO(requests.get('https://cdn.discordapp.com/attachments/682929799991132207/803001131185733632/review.png', stream = True).content)).convert('RGBA')
              response.paste(gof, (54, 100), gof)
            elif mid == 420506181627412501:
              rez = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/682929799991132207/806622139972583485/review.png', stream = True).content)).convert('RGBA')
              response.paste(rez, (54, 100), rez)
            elif mid == 571006178444836875:
              leo = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/682929799991132207/799946949679120424/review.png', stream = True).content)).convert('RGBA')
              response.paste(leo, (54, 100), leo)
            elif not member.premium_since is None:
              boost = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/797122464026198066/rm.png', stream = True).content)).convert('RGBA')
              response.paste(boost, (54, 100), boost)
            if not member.premium_since is None:
              idraw.text((100 , 102), f'{member.top_role.name}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))

            if net_zn == 0:
              idraw.text((365 , 200), f'У вас пока нет ни одного значка ;(', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))

            if randch == 1:
              gl = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/786978327420076062/glitchon.png', stream = True).content)).convert('RGBA')
              response.paste(gl, (0, 0), gl)
              response.save('user_card.png')
              await message.channel.send(content='О̵͌́й̶̿̒.̵̅͛.̵̯̃.̶̊̿ ̵̇̚В̷̒̀ӹ̸́̈ ̸̍͝с̷͐͐л̷͒̊о̵͑̌м̶̐̿ӓ̶́͐л̸̒̍и̸͂̚ ̶͌͘б̶̍̾о̷̇̈́т̴̋̓а̶̎͊ ',file = discord.File(fp = 'user_card.png'))
            else:
              response.save('user_card.png')
              await message.channel.send(file = discord.File(fp = 'user_card.png'))

      except:
          try:
              randch = random.randint(1,100)
              member = await client.fetch_user(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
              avatar = requests.get(member.avatar_url, stream = True)
              avatar = Image.open(io.BytesIO(avatar.content))
              avatar = avatar.convert('RGBA')
              if randch == 1:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/784744502048063499/glitch.png', stream = True)
              else:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/806867004198748160/classical.png', stream = True)
              response = Image.open(io.BytesIO(response.content))
              idraw = ImageDraw.Draw(response)
              avatar = avatar.resize((212, 212), Image.ANTIALIAS)
              response.paste(avatar, (119, 171, 331, 383))
              a = str(member.created_at).split()[0].split('-')
              idraw.text((365, 150), f'{member}', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 35))
              idraw.text((365, 220), f'Дата создания: {a[2]} {sp[int(a[1])]} {a[0]} года', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
              idraw.text((95 , 440), 'Пользователь отсутствует на сервере. Функции ограничены.', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
              try:
                a = await client.get_guild(604636579545219072).fetch_ban(member)
                idraw.text((365 , 260), 'Пользователь в бане.', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
                b_01 = [role.id for role in message.author.roles]
                if 677397817966198788 in b_01 or 765212719380037663 in b_01 or 800474182474268734 in b_01 or message.author.id in admins:
                  idraw.text((52 , 520), f'Причина: {a.reason}', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 20))
                else:
                  idraw.text((52 , 520), 'Просматривать причину бана могут лишь уполномоченные сотрудники.', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 20))
              except:
                idraw.text((365 , 260), 'Пользователь не забанен.', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))

              if randch == 1:
                gl = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/786978327420076062/glitchon.png', stream = True).content)).convert('RGBA')
                response.paste(gl, (0, 0), gl)
                response.save('user_card.png')
                await message.channel.send(content='О̵͌́й̶̿̒.̵̅͛.̵̯̃.̶̊̿ ̵̇̚В̷̒̀ӹ̸́̈ ̸̍͝с̷͐͐л̷͒̊о̵͑̌м̶̐̿ӓ̶́͐л̸̒̍и̸͂̚ ̶͌͘б̶̍̾о̷̇̈́т̴̋̓а̶̎͊ ',file = discord.File(fp = 'user_card.png'))
              else:
                response.save('user_card.png')
                await message.channel.send(file = discord.File(fp = 'user_card.png'))
          except:
              await message.channel.send('```css\nПользователя не существует.```')
        
client.run(tt)

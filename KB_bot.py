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
import smtplib
import email.message
import traceback
import contextlib
import textwrap
import unicodedata
import cs

mm = os.environ.get("Mongo")
tt = os.environ.get("TOKEN")
password = os.environ.get("password")

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

my_not = my_client.Catalog.notifications

client = commands.Bot(command_prefix = "K.", intents = discord.Intents.all())
client.remove_command("help")

admins = [562561140786331650, 414119169504575509, 529044574660853761]
id_chn_jb = cs.id_chn_jb

@client.event
async def on_ready():
  msg = await client.get_channel(742757799645413378).history(limit=200).flatten()
  b = []
  for i in msg:
      a = i.content.split('https://discord.gg')
      b.append('https://discord.gg' + a[-1])
  await client.get_channel(690827050033872937).purge(limit=10)
  await client.get_channel(690827050033872937).send('https://discord.gg/nKPdC9V')
  global d
  global dk
  global d_url
  global kolpub
  global date_pms; date_pms = time.time() - 180
  global active_kd; active_kd = time.time() - 300
  global np_kd; np_kd = {}
                                                                                    
  global mods; mods = {}
  global mods2; mods2 = {}
  global mods_type; mods_type = {}
  global check_pay; check_pay = []
  global key_log; key_log = {}
  global msg_arch; msg_arch = {}
                                                                                    
  global dm_date; dm_date = ['key', 'янв.,', 'фев.,', 'мар.,', 'апр.,', 'май,', 'июн.,', 'июл.,', 'авг.,', 'сен.', 'окт.,', 'ноя.,', 'дек.,']
  global dm_guild; dm_guild = client.get_guild(822949304255119421)
                                                                                    
  a = client.get_guild(604636579545219072).categories
  idd = [747813531495301161, 642102626070036500, 747807222247063642, 642085815597400065, 642104779270782986]
  c, k, d, dk, d_url = [], [], {}, {}, {}
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
                d_url.update({men[0].id:kk.jump_url})
              elif d.get(men[0].id)<str(kk.created_at + datetime.timedelta(hours=3)):
                d.update({men[0].id:str(kk.created_at + datetime.timedelta(hours=3))})
                dk.update({men[0].id:dk.get(men[0].id)+1})
                d_url.update({men[0].id:kk.jump_url})
              else:
                dk.update({men[0].id:dk.get(men[0].id)+1})

  #for cards_badges
  global msgbots; global bag; global medal22; global medal_chat_users; global souz; global rm22; global ngl; global att; global ideas; global bang; global msgotz; global candys; global heart; global msgs; global feedback
  msgbots = await client.get_channel(764191031318937674).fetch_message(785189856988627004); msgbots = msgbots.content
  bag = await client.get_channel(764191031318937674).fetch_message(807351505455022160); bag = bag.content
  medal22 = await client.get_channel(764191031318937674).fetch_message(788848844980092989); medal22 = medal22.content
  medal_chat_users = await client.get_channel(764191031318937674).fetch_message(817427831460986891); medal_chat_users = medal_chat_users.content
  souz = await client.get_channel(764191031318937674).fetch_message(793762809396985866); souz = souz.content
  rm22 = await client.get_channel(764191031318937674).fetch_message(812211556317921290); rm22 = rm22.content
  ngl = await client.get_channel(764191031318937674).fetch_message(787339282951569420); ngl = ngl.content
  att = await client.get_channel(764191031318937674).fetch_message(807351517581017099); att = att.content
  ideas = await client.get_channel(764191031318937674).fetch_message(785203816785903667); ideas = ideas.content
  bang = await client.get_channel(764191031318937674).fetch_message(786738663433437244); bang = bang.content
  msgotz = await client.get_channel(764191031318937674).fetch_message(782330900746076202); msgotz = msgotz.content
  candys = await client.get_channel(764191031318937674).fetch_message(790310798895480833); candys = candys.content
  heart = await client.get_channel(764191031318937674).fetch_message(810449422328004628); heart = heart.content
  msgs = await client.get_channel(764191031318937674).fetch_message(764191228933046361); msgs = msgs.content
  feedback = await client.get_channel(764191031318937674).fetch_message(827263853184286740); feedback = feedback.content
  
  #for cards_img
  global crown; global dev; global bag22; global medal; global medal_chat; global allia; global rm; global ngl2; global att22; global id22; global bg22; global cotz; global candy; global heart22; global support; global feedback22; global moder22
  crown = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/784811138671575121/owner.png', stream = True).content)).convert('RGBA').resize((37, 37), Image.ANTIALIAS)
  dev = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/785183136362659880/developer.png', stream = True).content)).convert('RGBA').resize((37, 37), Image.ANTIALIAS)
  bag22 = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/807343608868110406/review.png', stream = True).content)).convert('RGBA')
  medal = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/814131510361587762/medal.png', stream = True).content)).convert('RGBA')
  medal_chat = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/817425102671970304/333333.png', stream = True).content)).convert('RGBA')
  allia = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/807310152801845358/-3.png', stream = True).content)).convert('RGBA')
  rm = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/827468463483781130/15.png', stream = True).content)).convert('RGBA')
  ngl2 = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/822793093857148938/-11.png', stream = True).content)).convert('RGBA').resize((37, 37), Image.ANTIALIAS)
  att22 = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/827475184273063936/222.png', stream = True).content)).convert('RGBA')
  id22 = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/824420601309167676/-12.png', stream = True).content)).convert('RGBA')
  bg22 = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/827468466168266772/123124.png', stream = True).content)).convert('RGBA')
  cotz = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/822793098361831456/444.png', stream = True).content)).convert('RGBA')
  candy = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/797119577951436810/rm.png', stream = True).content)).convert('RGBA')
  heart22 = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/806296162889891890/review.png', stream = True).content)).convert('RGBA')
  support = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/817425097752707072/-1.png', stream = True).content)).convert('RGBA')
  feedback22 = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/827263879917993984/12.png', stream = True).content)).convert('RGBA')
  moder22 = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/827468464809443358/12qw3erythkjk.png', stream = True).content)).convert('RGBA')

  global kastom_zn; global statuts; global cards
  kastom_zn = {394757049893912577:Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/785202689532755988/fatal.png', stream = True).content)).convert('RGBA'), 713780299024039936:Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/682929799991132207/797940366254800906/rm.png', stream = True).content)).convert('RGBA'), 357518684723478540:Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/682929799991132207/803224903620362260/review.png', stream = True).content)).convert('RGBA'), 420506181627412501:Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/682929799991132207/806622139972583485/review.png', stream = True).content)).convert('RGBA'), 571006178444836875:Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/682929799991132207/814143364990500909/review.png', stream = True).content)).convert('RGBA'), 735540766289690646:Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/682929799991132207/814211345607294996/review.png', stream = True).content)).convert('RGBA'), 585535916920012801:Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/682929799991132207/817460608378732594/review.png', stream = True).content)).convert('RGBA'), 602043590398705665:Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/832276527638642798/review.png', stream = True).content)).convert('RGBA')}
  statuts = {'offline':'https://media.discordapp.net/attachments/689800301468713106/827465448403632138/1.png', True:{'online':'https://media.discordapp.net/attachments/689800301468713106/827465449158737950/3.png', 'idle':'https://media.discordapp.net/attachments/689800301468713106/827465450102849536/14.png', 'dnd':'https://media.discordapp.net/attachments/689800301468713106/827465445103239188/32.png', 'y':150}, False:{'online':'https://media.discordapp.net/attachments/689800301468713106/827465446223249448/321.png', 'idle':'https://media.discordapp.net/attachments/689800301468713106/827465447162511389/-2.png', 'dnd':'https://media.discordapp.net/attachments/689800301468713106/827465443899867156/23.png', 'y':155}}
  cards = {732878004367392789:'https://media.discordapp.net/attachments/689800301468713106/833289782464348160/3214124.png', 713780299024039936:'https://media.discordapp.net/attachments/689800301468713106/821772685192331304/card_angelina_v3.png', 529044574660853761:'https://media.discordapp.net/attachments/689800301468713106/832280139949670410/card_pande1.png', 735540766289690646:'https://media.discordapp.net/attachments/689800301468713106/824763878621577266/card_navintas_v2.png', 346263496394276867:'https://media.discordapp.net/attachments/689800301468713106/822158050642493460/card_nefik22_v2.4.png', 420506181627412501:'https://media.discordapp.net/attachments/689800301468713106/812252851077382164/card_helya.png', 722394482515116072:'https://media.discordapp.net/attachments/689800301468713106/821772686224916480/goffit.png', 394757049893912577:'https://media.discordapp.net/attachments/689800301468713106/827269724689399818/card_fatal2_1.png', 414119169504575509:'https://media.discordapp.net/attachments/689800301468713106/819962677312225290/catalog_card1.png', 562561140786331650:'https://media.discordapp.net/attachments/689800301468713106/819962677312225290/catalog_card1.png', 760551070685855794:'https://media.discordapp.net/attachments/689800301468713106/812249880084873216/card_moxxie1.png', 357518684723478540:'https://media.discordapp.net/attachments/689800301468713106/833289755030192148/1234567887654321.png', 571006178444836875:'https://media.discordapp.net/attachments/689800301468713106/832280137600204850/card_leo1.png'}

  global ticket_key
  for i in await client.get_channel(816385807958802522).history(limit=100).flatten():
    try:
      ticket_key = int(i.content.split('\n')[0].split('|')[1])
      break
    except:
      pass
  else:
    ticket_key = 0
  global ideas_key
  for i in await client.get_channel(cs.ideas_id).history(limit=100).flatten():
      try:
          ideas_key = int(i.embeds[0].title.split('№')[1])
          break
      except:
          pass
  else:
      ideas_key = 0
  global problems_key
  for i in await client.get_channel(cs.problems_id).history(limit=100).flatten():
      try:
          problems_key = int(i.embeds[0].title.split('№')[1])
          break
      except:
          pass
  else:
      problems_key = 0

  await client.get_channel(728932829026844672).send('```css\n[Данные обновлены, бот перезапущен].```')
  await client.change_presence(status=discord.Status.dnd,activity=discord.Streaming(url='https://www.twitch.tv/catalogserverov',name=f"K.help | {str(datetime.datetime.utcnow()+datetime.timedelta(hours=3)).split()[1].split('.')[0][0:5]} [{len(client.get_guild(604636579545219072).members)}]"))

    
@client.event
async def on_message(message):
  idd = [747813531495301161, 642102626070036500, 747807222247063642, 642085815597400065, 642104779270782986]
  if message.channel.id == id_chn_jb:
    if 677397817966198788 in [role.id for role in message.role_mentions]:
      try:
        intruder = await client.fetch_user(int(message.content.split('\n')[1].replace('.',' ').replace('<',' ').replace('>',' ').replace('@',' ').replace('!',' ').split()[-1]))
        reason = message.content.split("\n")[2]
        await message.add_reaction('<:developer:785191301321719828>')
      except:
        pass
  elif (message.guild is None or message.guild.id == dm_guild.id) and message.author.id != 656029229749764126:
        if not message.guild is None and message.guild.id == dm_guild.id and '--a' in message.content:
            await message.channel.edit(category=dm_guild.categories[1])
        else:            
            embed = discord.Embed(colour=0x2f3136, description=message.content)
            dm_date1 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[0].split('-')
            dm_date2 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[1].split('.')[0].split(':')
            if len(message.attachments) > 0:
                urls, k = '', 0
                for i in message.attachments:
                    k += 1
                    urls += f'**[Вложение {k}]({i.proxy_url})**\n'
                embed.add_field(name='Прикреплённые файлы:', value=urls)
            try:
                if message.guild is None:
                    for i in dm_guild.channels:
                        if str(message.author.id) == i.name:
                            dm_chn = i
                            break
                    else:
                        dm_chn = await dm_guild.create_text_channel(name=message.author.id, category=dm_guild.categories[0], reason=f'Новое обращение от {message.author}.')
                    await dm_chn.send(embed=embed.set_author(name=f'{message.author.name} (Member)\n{dm_date1[2]} {dm_date[int(dm_date1[1])]} {dm_date2[0]}:{dm_date2[1]} GMT+3'))
                    await dm_chn.edit(category=dm_guild.categories[0], position=1)
                elif message.guild.id == dm_guild.id:
                    if not message.channel.category is None and message.channel.category.id in [dm_guild.categories[0].id, dm_guild.categories[1].id]:
                        dm_chn = await client.fetch_user(int(message.channel.name))
                        if message.content.startswith('--s'):
                            embed.description = message.content.replace('--s', '')
                            await dm_chn.send(embed=embed.set_author(name=f'Agent (Support Team)\n{dm_date1[2]} {dm_date[int(dm_date1[1])]} {dm_date2[0]}:{dm_date2[1]} GMT+3'))
                        elif message.author.id in admins:
                            await dm_chn.send(embed=embed.set_author(name=f'{message.author.name} (Administrator)\n{dm_date1[2]} {dm_date[int(dm_date1[1])]} {dm_date2[0]}:{dm_date2[1]} GMT+3'))
                        else:
                            await dm_chn.send(embed=embed.set_author(name=f'{message.author.name} (Support Team)\n{dm_date1[2]} {dm_date[int(dm_date1[1])]} {dm_date2[0]}:{dm_date2[1]} GMT+3'))
                        await message.channel.edit(category=dm_guild.categories[0], position=1)
            except:
                embed.description = f'Приветствую, {message.author.name}.\n\nДанное сообщение является системным.\n\nНам очень жаль, но Ваше сообщенние не было доставлено получателю. Вероятнее всего, причиной этого являются закрытые личные сообщения с пользователям.\n\nС уважением,\nKC | System Info.'
                await message.channel.send(embed=embed.set_author(name=f'Catalog (System)\n{dm_date1[2]} {dm_date[int(dm_date1[1])]} {dm_date2[0]}:{dm_date2[1]} GMT+3'))
  elif ('.gg' in message.content or '/invite/' in message.content) and message.channel.category.id == 604636579545219073 and message.channel.id != 699306241981415424 and not message.author.id in admins and not 816386551222763561 in [role.id for role in message.author.roles]:
    await message.delete()
    my_mute.delete_one({'id':message.author.id})
    my_mute.insert_one({"id":message.author.id, "data":datetime.datetime.utcnow() + datetime.timedelta(hours=99999)})
    embed = discord.Embed(colour=discord.Colour(0x310000), description=f'Пользователь `{message.author}` был заткнут навсегда автомодерацией.', timestamp=datetime.datetime.utcnow())
    embed.set_footer(text=f'ID: {message.author.id}',icon_url=message.author.avatar_url)
    await message.channel.send(content='<@&677397817966198788>',embed=embed)
    await message.author.remove_roles(message.guild.get_role(648271372585533441),reason=f'Автомодерация: время мута истекло.')
    await message.author.add_roles(message.guild.get_role(648271372585533441),reason=f'Автомодерация: был заткнут навсегда.')
  elif message.channel.id == 740651083533254717:
    if not message.content.split()[0] in ["K.problem", "K.eproblem"] and message.author.id != 656029229749764126 and not message.author.id in admins and message.author.id != 665120789913403422 and not 816386551222763561 in [role.id for role in message.author.roles]:
      await message.delete()
      embed = discord.Embed(timestamp=datetime.datetime.utcnow(),colour=discord.Colour(0x310000),description=f'Ваше сообщение в канале <#740651083533254717> следующего содержания: `{message.content}` было удалено по причине оффтопа.\nПросьба ознакомиться с **[закреплённым информационным сообщением](https://discord.com/channels/604636579545219072/740651083533254717/744485922258681896).**')
      embed.set_footer(text='С уважением, Команда Каталога!',icon_url=message.guild.icon_url)
      await message.author.send(embed=embed)
  elif message.channel.id == 678666229661171724:
    b = [role.id for role in message.author.roles]
    if not message.content.split()[0] in ["K.suggest", "K.esuggest"] and message.author.id != 656029229749764126 and not message.author.id in admins and message.author.id != 665120789913403422 and not (608994688078184478 in b or 816386551222763561 in b or 757890413838467133 in b):
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
      d_url.update({men[0].id:message.jump_url})
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
  elif payload.channel_id == id_chn_jb:
      if 677397817966198788 in [role.id for role in gg.get_member(payload.user_id).roles] or payload.user_id in admins:
          global mods; global mod2; global mods_type; global check_pay; global key_log
          if payload.channel_id == id_chn_jb and payload.emoji.id == 785191301321719828 and not payload.message_id in check_pay:
              check_pay.append(payload.message_id)
              msg_r = await client.get_channel(id_chn_jb).fetch_message(payload.message_id)
              await msg_r.clear_reactions()
              mod_r = await client.fetch_user(payload.user_id)
              intruder = await client.fetch_user(int(msg_r.content.split('\n')[1].replace('.',' ').replace('<',' ').replace('>',' ').replace('@',' ').replace('!',' ').split()[-1]))
              reason = msg_r.content.split("\n")[2].replace('1.', '').replace('2.', '').replace('3.', '').replace('4.', '').replace('5.', '')
              msg_new = await msg_r.reply(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x36393f, title=f'Панель модератора [Главное меню]', description=f'```css\n[Нарушитель]:```{intruder.mention} `[{intruder.id}]` | {intruder}\n```css\n[Пользовательская причина]:```{reason}\n```md\n#Альтернативная мера наказания:```<:no:819634947756916810> — Передать другому модератору.\n<:ban:819620281139462165> — Бан.\n<:mute:819620281643302912> — Мут.\n<:warn:819620282187644999> — Предупреждение.\n<:otkaz:819631424789413969> — Выдать отказ.\n<:warns:822423843163078668> — Предупреждения пользователя.').set_footer(text=f'Ответственный за жалобу {mod_r}', icon_url=mod_r.avatar_url))
              key_log.update({msg_new.id:0})
              mods.update({msg_new.id:[payload.user_id, msg_r.jump_url, intruder, reason, mod_r, msg_r]})
              mods_type.update({msg_new.id:[None, 0, True]})
              msg_arch.update({msg_new.id:msg_new})
              i, emojis = 0, ['<:no:819634947756916810>', '<:ban:819620281139462165>', '<:mute:819620281643302912>', '<:warn:819620282187644999>', '<:otkaz:819631424789413969>', '<:warns:822423843163078668>']
              while key_log.get(msg_new.id) == 0 and i != 6:
                  await msg_new.add_reaction(emojis[i])
                  i += 1
          elif payload.channel_id == id_chn_jb and payload.emoji.id == 819634947756916810 and mods.get(payload.message_id)[0] == payload.user_id:
              check_pay.remove(mods.get(payload.message_id)[5].id)
              msg_c = msg_arch.get(payload.message_id)
              await msg_c.delete()
              await mods.get(payload.message_id)[5].add_reaction('<:developer:785191301321719828>')
          elif payload.channel_id == id_chn_jb and (payload.emoji.id == 819639758871461909 or payload.emoji.id == 822131145026043984) and mods.get(payload.message_id)[0] == payload.user_id:
              key_log.update({payload.message_id:1})
              msg_c = msg_arch.get(payload.message_id)
              await msg_c.clear_reactions()
              await msg_c.edit(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x36393f, title=f'Панель модератора [Главное меню]', description=f'```css\n[Нарушитель]:```{mods.get(payload.message_id)[2].mention} | `[{mods.get(payload.message_id)[2].id}]` | {mods.get(payload.message_id)[2]}\n```css\n[Пользовательская причина]:```{mods.get(payload.message_id)[3]}\n```md\n#Альтернативная мера наказания:```<:no:819634947756916810> — Передать другому модератору.\n<:ban:819620281139462165> — Бан.\n<:mute:819620281643302912> — Мут.\n<:warn:819620282187644999> — Предупреждение.\n<:otkaz:819631424789413969> — Выдать отказ.\n<:warns:822423843163078668> — Предупреждения пользователя.').set_footer(text=f'Ответственный за жалобу {mods.get(payload.message_id)[4]}', icon_url=mods.get(payload.message_id)[4].avatar_url))
              i, emojis = 0, ['<:no:819634947756916810>', '<:ban:819620281139462165>', '<:mute:819620281643302912>', '<:warn:819620282187644999>', '<:otkaz:819631424789413969>', '<:warns:822423843163078668>']
              while key_log.get(payload.message_id) == 1 and i != 6:
                  await msg_c.add_reaction(emojis[i])
                  i += 1
          elif payload.channel_id == id_chn_jb and (payload.emoji.id == 819620281139462165 or payload.emoji.id == 819642889855696926) and mods.get(payload.message_id)[0] == payload.user_id:
              key_log.update({payload.message_id:2})
              msg_c = msg_arch.get(payload.message_id)
              await msg_c.clear_reactions()
              await msg_c.edit(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x36393f, title=f'Панель модератора [Причина бана]', description=f'```css\n[Нарушитель]:```{mods.get(payload.message_id)[2].mention} | `[{mods.get(payload.message_id)[2].id}]` | {mods.get(payload.message_id)[2]}\n```css\n[Пользовательская причина]:```{mods.get(payload.message_id)[3]}\n```py\n"Популярные причины для банов":```<:zero_ban:819621518522843177> — Пользовательская причина.\n<:one_ban:819621518433583125> — Пиар в лс и/или на сервере.\n<:two_ban:819621518752874556> — Рейдер.\n<:three_ban:819621518929166346> — Крашер.\n<:four_ban:819621518862057502> — Рассылка.\n<:five_ban:819621518434631751> — Многократное нарушение правил.').set_footer(text=f'Ответственный за жалобу {mods.get(payload.message_id)[4]}', icon_url=mods.get(payload.message_id)[4].avatar_url))
              mods_type.update({payload.message_id:['ban', 0, False]})
              i, emojis = 0, ['<:back:819639758871461909>', '<:zero_ban:819621518522843177>', '<:one_ban:819621518433583125>', '<:two_ban:819621518752874556>', '<:three_ban:819621518929166346>', '<:four_ban:819621518862057502>', '<:five_ban:819621518434631751>', '<:otkaz:819631424789413969>', '<:no:819634947756916810>']
              while key_log.get(payload.message_id) == 2 and i != 9:
                  await msg_c.add_reaction(emojis[i])
                  i += 1
          elif payload.channel_id == id_chn_jb and mods.get(payload.message_id)[0] == payload.user_id and (payload.emoji.id == 819621518522843177 or payload.emoji.id == 819621518433583125 or payload.emoji.id == 819621518752874556 or payload.emoji.id == 819621518929166346 or payload.emoji.id == 819621518862057502 or payload.emoji.id == 819621518434631751):
              key_log.update({payload.message_id:3})
              if payload.emoji.id == 819621518522843177:
                  reason_b = mods.get(payload.message_id)[3]
              elif payload.emoji.id == 819621518433583125:
                  reason_b = 'пиар в лс и/или на серверах.'
              elif payload.emoji.id == 819621518752874556:
                  reason_b = 'рейдер.'
              elif payload.emoji.id == 819621518929166346:
                  reason_b = 'крашер.'
              elif payload.emoji.id == 819621518862057502:
                  reason_b = 'несогласованная рассылка.'
              elif payload.emoji.id == 819621518434631751:
                  reason_b = 'многократное нарушение правил.'
              mods2.update({payload.message_id:reason_b})
              msg_c = msg_arch.get(payload.message_id)
              await msg_c.clear_reactions()
              await msg_c.edit(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x36393f, title=f'Панель модератора [Подтверждение бана]', description=f'```css\n[Нарушитель]:```{mods.get(payload.message_id)[2].mention} | `[{mods.get(payload.message_id)[2].id}]` | {mods.get(payload.message_id)[2]}\n```css\n[Пользовательская причина]:```{mods.get(payload.message_id)[3]}\n```diff\n- Подтверждение:```Вы уверены, что хотите забанить пользователя {mods.get(payload.message_id)[2].mention} по причине `{reason_b}`?').set_footer(text=f'Ответственный за жалобу {mods.get(payload.message_id)[4]}', icon_url=mods.get(payload.message_id)[4].avatar_url))
              i, emojis = 0, ['<:yes_warn:819692933489754122>', '<:no:819642889855696926>', '<:Home:822131145026043984>', '<:no:819634947756916810>']
              while key_log.get(payload.message_id) == 3 and i != 4:
                  await msg_c.add_reaction(emojis[i])
                  i += 1
          elif payload.channel_id == id_chn_jb and payload.emoji.id == 819631424789413969 and mods.get(payload.message_id)[0] == payload.user_id:
              key_log.update({payload.message_id:4})
              msg_c = msg_arch.get(payload.message_id)
              await msg_c.clear_reactions()
              await msg_c.edit(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x36393f, title=f'Панель модератора [Отказ в жалобе]', description=f'```css\n[Нарушитель]:```{mods.get(payload.message_id)[2].mention} | `[{mods.get(payload.message_id)[2].id}]` | {mods.get(payload.message_id)[2]}\n```css\n[Пользовательская причина]:```{mods.get(payload.message_id)[3]}\n```py\n"Причина для отказа":```<:one_otkaz:819647171430973480> — Нет нарушений.\n<:two_otkaz:819647200229064775> — Не по форме.\n<:three_otkaz:819654562276704328> — Доказательства устарели/обрезаны.').set_footer(text=f'Ответственный за жалобу {mods.get(payload.message_id)[4]}', icon_url=mods.get(payload.message_id)[4].avatar_url))
              i, emojis = 0, ['<:back:819639758871461909>', '<:one_otkaz:819647171430973480>', '<:two_otkaz:819647200229064775>', '<:three_otkaz:819654562276704328>', '<:no:819634947756916810>']
              while key_log.get(payload.message_id) == 4 and i != 5:
                  await msg_c.add_reaction(emojis[i])
                  i += 1
          elif payload.channel_id == id_chn_jb and mods.get(payload.message_id)[0] == payload.user_id and (payload.emoji.id == 819647171430973480 or payload.emoji.id == 819647200229064775 or payload.emoji.id == 819654562276704328):
              key_log.update({payload.message_id:5})
              if payload.emoji.id == 819647171430973480:
                  reason_b = 'нет нарушений.'
              elif payload.emoji.id == 819647200229064775:
                  reason_b = 'не по форме.'
              elif payload.emoji.id == 819654562276704328:
                  reason_b = 'доказательства устарели/обрезаны.'
              mods2.update({payload.message_id:reason_b})
              msg_c = msg_arch.get(payload.message_id)
              await msg_c.clear_reactions()
              await msg_c.edit(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x36393f, title=f'Панель модератора [Подтверждение отказа]', description=f'```css\n[Нарушитель]:```{mods.get(payload.message_id)[2].mention} | `[{mods.get(payload.message_id)[2].id}]` | {mods.get(payload.message_id)[2]}\n```css\n[Пользовательская причина]:```{mods.get(payload.message_id)[3]}\n```diff\n- Подтверждение:```Вы уверены, что хотите отказать в жалобе по причине `{reason_b}`?').set_footer(text=f'Ответственный за жалобу {mods.get(payload.message_id)[4]}', icon_url=mods.get(payload.message_id)[4].avatar_url))
              i, emojis = 0, ['<:yes_otkaz:819662713147883620>', '<:nootkaz:819631424789413969>', '<:Home:822131145026043984>', '<:no:819634947756916810>']
              while key_log.get(payload.message_id) == 5 and i != 4:
                  await msg_c.add_reaction(emojis[i])
                  i += 1
          elif payload.channel_id == id_chn_jb and payload.emoji.id == 819662713147883620 and mods.get(payload.message_id)[0] == payload.user_id:
              key_log.update({payload.message_id:-1})
              msg_c = msg_arch.get(payload.message_id)
              await msg_c.clear_reactions()
              reason_b = mods2.get(payload.message_id)
              await msg_c.edit(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x36393f, title=f'Панель модератора [Меры приняты]', description=f'```css\n[Нарушитель]:```{mods.get(payload.message_id)[2].mention} | `[{mods.get(payload.message_id)[2].id}]` | {mods.get(payload.message_id)[2]}\n```css\n[Пользовательская причина]:```{mods.get(payload.message_id)[3]}\n```diff\n- Принял меры:```{mods.get(payload.message_id)[4].mention} | `[{mods.get(payload.message_id)[4].id}]` | {mods.get(payload.message_id)[4]}\n> В жалобе отказано.\n> `Причина:` {reason_b}').set_footer(text=f'Ответственный за жалобу {mods.get(payload.message_id)[4]}', icon_url=mods.get(payload.message_id)[4].avatar_url))
              await mods.get(payload.message_id)[5].add_reaction('<:nootkaz:819631424789413969>')
          elif payload.channel_id == id_chn_jb and (payload.emoji.id == 819620282187644999 or payload.emoji.id == 819691331672735815  or payload.emoji.id == 819692972870205460 or payload.emoji.id == 819620281643302912) and mods.get(payload.message_id)[0] == payload.user_id:
              key_log.update({payload.message_id:6})
              msg_c = msg_arch.get(payload.message_id)
              await msg_c.clear_reactions()
              if payload.emoji.id == 819620281643302912:
                  mods_type.update({payload.message_id:['mute', 0, False]})
                  pnmd = 'Панель модератора [Причина мута (раздел)]'
              elif payload.emoji.id == 819620282187644999:
                  mods_type.update({payload.message_id:['warn', 0, False]})
                  pnmd = 'Панель модератора [Причина предупреждения (раздел)]'
              else:
                  pnmd = 'Панель модератора [Причина мута (раздел)]' if mods_type.get(payload.message_id)[0] == 'mute' else 'Панель модератора [Причина предупреждения (раздел)]'
              await msg_c.edit(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x36393f, title=pnmd, description=f'```css\n[Нарушитель]:```{mods.get(payload.message_id)[2].mention} | `[{mods.get(payload.message_id)[2].id}]` | {mods.get(payload.message_id)[2]}\n```css\n[Пользовательская причина]:```{mods.get(payload.message_id)[3]}\n```py\n"Выберите раздел нарушения":```<:zero_warn:819678029004406785> — Пользовательская причина.\n<:one_warn:820222062035468333> — Основные принципы и положение.\n<:three_warn:819675568890839070> — Правила общения и поведения.\n<:four_warn:819675568617422849> — Правила личного характера.').set_footer(text=f'Ответственный за жалобу {mods.get(payload.message_id)[4]}', icon_url=mods.get(payload.message_id)[4].avatar_url))
              i, emojis = 0, ['<:back:819639758871461909>', '<:zero_warn:819678029004406785>', '<:one_warn:820222062035468333>', '<:three_warn:819675568890839070>', '<:four_warn:819675568617422849>', '<:otkaz:819631424789413969>', '<:no:819634947756916810>', '<:no:819634947756916810>']
              while key_log.get(payload.message_id) == 6 and i != 7:
                  await msg_c.add_reaction(emojis[i])
                  i += 1
          elif payload.channel_id == id_chn_jb and mods.get(payload.message_id)[0] == payload.user_id and (payload.emoji.id == 820225738858561576 or payload.emoji.id == 820222062035468333 or payload.emoji.id == 819675568890839070 or payload.emoji.id == 819675568617422849):
              key_log.update({payload.message_id:7})
              if payload.emoji.id != 820225738858561576:
                  if payload.emoji.id == 820222062035468333:
                      reason_b = '1.'
                  elif payload.emoji.id == 819675568890839070:
                      reason_b = '3.'
                  elif payload.emoji.id == 819675568617422849:
                      reason_b = '4.'
                  mods2.update({payload.message_id:reason_b})
              msg_c = msg_arch.get(payload.message_id)
              await msg_c.clear_reactions()
              pnmd = 'Панель модератора [Причина мута (пункт)]' if mods_type.get(payload.message_id)[0] == 'mute' else 'Панель модератора [Причина предупреждения (пункт)]'
              await msg_c.edit(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x36393f, title=pnmd, description=f'```css\n[Нарушитель]:```{mods.get(payload.message_id)[2].mention} | `[{mods.get(payload.message_id)[2].id}]` | {mods.get(payload.message_id)[2]}\n```css\n[Пользовательская причина]:```{mods.get(payload.message_id)[3]}\n```py\n"Выберите пункт нарушения":```').set_footer(text=f'Ответственный за жалобу {mods.get(payload.message_id)[4]}', icon_url=mods.get(payload.message_id)[4].avatar_url))
              i, emojis = 0, ['<:back_warn:819691331672735815>', '<:one_pred:819689230892138547>', '<:two_pred:819689230913241128>', '<:three_pred:819689230896595014>', '<:four_pred:819689230899871746>', '<:five_pred:819689230879686656>', '<:six_pred:819689230892662864>', '<:seven_pred:819689231412756560>', '<:eight_pred:819689231366619156>', '<:nine_pred:819689231395848242>', '<:otkaz:819631424789413969>', '<:Home:822131145026043984>', '<:no:819634947756916810>']
              while key_log.get(payload.message_id) == 7 and i != 14:
                  await msg_c.add_reaction(emojis[i])
                  i += 1
          elif payload.channel_id == id_chn_jb and mods.get(payload.message_id)[0] == payload.user_id and payload.emoji.id in [819689230892138547, 819689230913241128, 819689230896595014, 819689230899871746, 819689230879686656, 819689230892662864, 819689231412756560, 819689231366619156, 819689231395848242, 819678029004406785]:
              key_log.update({payload.message_id:8})
              if payload.emoji.id == 819678029004406785:
                  mods2.update({payload.message_id:mods.get(payload.message_id)[3]})
                  emmo_back = '<:back_warn:819691331672735815>'
              else:
                  emmo_back = '<:back_mute_pow:820225738858561576>'
                  if payload.emoji.id == 819689230892138547:
                      reason_b = '1'
                  elif payload.emoji.id == 819689230913241128:
                      reason_b = '2'
                  elif payload.emoji.id == 819689230896595014:
                      reason_b = '3'
                  elif payload.emoji.id == 819689230899871746:
                      reason_b = '4'
                  elif payload.emoji.id == 819689230879686656:
                      reason_b = '5'
                  elif payload.emoji.id == 819689230892662864:
                      reason_b = '6'
                  elif payload.emoji.id == 819689231412756560:
                      reason_b = '7'
                  elif payload.emoji.id == 819689231366619156:
                      reason_b = '8'
                  elif payload.emoji.id == 819689231395848242:
                      reason_b = '9'
                  mods2.update({payload.message_id:(mods2.get(payload.message_id)[0:2] + reason_b)})
              msg_c = msg_arch.get(payload.message_id)
              await msg_c.clear_reactions()
              if mods_type.get(payload.message_id)[0] == 'warn':
                  await msg_c.edit(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x36393f, title=f'Панель модератора [Подтверждение предупреждения]', description=f'```css\n[Нарушитель]:```{mods.get(payload.message_id)[2].mention} | `[{mods.get(payload.message_id)[2].id}]` | {mods.get(payload.message_id)[2]}\n```css\n[Пользовательская причина]:```{mods.get(payload.message_id)[3]}\n```diff\n- Подтверждение:```Вы уверены, что хотите предупредить пользователя по причине `{mods2.get(payload.message_id)}`?').set_footer(text=f'Ответственный за жалобу {mods.get(payload.message_id)[4]}', icon_url=mods.get(payload.message_id)[4].avatar_url))
                  i, emojis = 0, ['<:yes_warn:819692933489754122>', '<:no_warn:819692972870205460>', '<:Home:822131145026043984>', '<:no:819634947756916810>']
                  while key_log.get(payload.message_id) == 8 and i != 4:
                      await msg_c.add_reaction(emojis[i])
                      i += 1
              else:
                  await msg_c.edit(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x36393f, title=f'Панель модератора [Степень мута]', description=f'```css\n[Нарушитель]:```{mods.get(payload.message_id)[2].mention} | `[{mods.get(payload.message_id)[2].id}]` | {mods.get(payload.message_id)[2]}\n```css\n[Пользовательская причина]:```{mods.get(payload.message_id)[3]}\n```py\n"Выберите степень мута":```<:zero_mute:819909390047510528> — Перманентный мут.\n<:one_mute:819909390026145872>-<:nine_mute:819909390160363581> — 2^(1-9) часов.').set_footer(text=f'Ответственный за жалобу {mods.get(payload.message_id)[4]}', icon_url=mods.get(payload.message_id)[4].avatar_url))
                  i, emojis = 0, [emmo_back, '<:zero_mute:819909390047510528>', '<:one_mute:819909390026145872>', '<:two_mute:819909389694664705>', '<:three_mute:819909390060093480>', '<:four_mute:819909390155907072>', '<:five_mute:819909390253162496>', '<:six_mute:819909390442299413>', '<:seven_mute:819909390315683840>', '<:eight_mute:819909390000848899>', '<:nine_mute:819909390160363581>', '<:otkaz:819631424789413969>', '<:Home:822131145026043984>', '<:no:819634947756916810>']
                  while key_log.get(payload.message_id) == 8 and i != 14:
                      await msg_c.add_reaction(emojis[i])
                      i += 1
          elif payload.channel_id == id_chn_jb and payload.emoji.id == 819692933489754122 and mods.get(payload.message_id)[0] == payload.user_id:
              key_log.update({payload.message_id:-1})
              msg_c = msg_arch.get(payload.message_id)
              await msg_c.clear_reactions()
              member = mods.get(payload.message_id)[2]
              reason = f'{mods2.get(payload.message_id)} [Панель]'
              moderator = await client.fetch_user(payload.user_id)
              guild_kc = client.get_guild(604636579545219072)
              if mods_type.get(payload.message_id)[0] == 'warn':
                  all = my_warn_kol.find()[0]["all"]+1
                  count = 0
                  for item in my_warn.find():
                      if item['id'] == member.id:
                          for j in my_warn.find():
                              if j['id'] == member.id:
                                  count += 1
                          my_warn.insert_one({"id":member.id, "number_warn":count+1, "mod_id":payload.user_id, "reason":reason, "all": all, "data":str(str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split('.')[0])})
                          break
                  else:
                      my_warn.insert_one({"id":member.id, "number_warn":1, "mod_id":payload.user_id, "reason":reason, "all":all, "data":str(str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split('.')[0])})
                  my_warn_kol.update_one({"id":1},{"$set":{"all":all}})
                  await msg_c.edit(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x36393f, title=f'Панель модератора [Меры приняты]', description=f'```css\n[Нарушитель]:```{mods.get(payload.message_id)[2].mention} | `[{mods.get(payload.message_id)[2].id}]` | {mods.get(payload.message_id)[2]}\n```css\n[Пользовательская причина]:```{mods.get(payload.message_id)[3]}\n```diff\n- Принял меры:```{mods.get(payload.message_id)[4].mention} | `[{mods.get(payload.message_id)[4].id}]` | {mods.get(payload.message_id)[4]}\n> **Пользователь `{member}` получил предупреждение `№{count+1}:`**\n```py\nID: {member.id}\nСлучай: {all}\nПричина: {reason}```').set_footer(text=f'Ответственный за жалобу {mods.get(payload.message_id)[4]}', icon_url=mods.get(payload.message_id)[4].avatar_url))
                  embed=discord.Embed(colour=0x310000, description = f'**Вы получили предупреждение `№{count+1}:`**\n```py\nСлучай: {all}\nПричина: {reason}```❗ С правилами можно ознакомиться **[здесь](https://discord.com/channels/604636579545219072/642171728273080330/699328371783630988).**',timestamp=datetime.datetime.utcnow())
                  embed.set_author(name='Нарушения пользовательского соглашения', icon_url=guild_kc.icon_url)
                  embed.set_footer(text=f'Предупреждение от {moderator.name}',icon_url=moderator.avatar_url)
                  try:
                      await member.send(embed=embed)
                  except:
                      pass
              elif mods_type.get(payload.message_id)[0] == 'mute':
                  time = mods_type.get(payload.message_id)[1]
                  my_mute.delete_one({'id':member.id})
                  my_mute.insert_one({"id":member.id, "data":datetime.datetime.utcnow() + datetime.timedelta(hours=time)})
                  await msg_c.edit(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x36393f, title=f'Панель модератора [Меры приняты]', description=f'```css\n[Нарушитель]:```{mods.get(payload.message_id)[2].mention} | `[{mods.get(payload.message_id)[2].id}]` | {mods.get(payload.message_id)[2]}\n```css\n[Пользовательская причина]:```{mods.get(payload.message_id)[3]}\n```diff\n- Принял меры:```{mods.get(payload.message_id)[4].mention} | `[{mods.get(payload.message_id)[4].id}]` | {mods.get(payload.message_id)[4]}\n> Пользователь `{member}` был заткнут на `{time}ч.` по причине: `{reason}`').set_footer(text=f'Ответственный за жалобу {mods.get(payload.message_id)[4]}', icon_url=mods.get(payload.message_id)[4].avatar_url))
                  member = guild_kc.get_member(member.id)
                  try:
                      await member.remove_roles(guild_kc.get_role(648271372585533441),reason=f'{moderator.name}: Время мута истекло.')
                      await member.add_roles(guild_kc.get_role(648271372585533441),reason=f'{moderator.name}: Был заткнут на {time}ч. ({reason})')
                  except:
                      pass
              else:
                  if member.id in [i22.id for i22 in client.get_guild(604636579545219072).get_role(608994688078184478).members]:
                      await msg_c.clear_reactions()
                      await msg_c.edit(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x36393f, title=f'Панель модератора [Меры приняты]', description=f'```css\n[Нарушитель]:```{mods.get(payload.message_id)[2].mention} | `[{mods.get(payload.message_id)[2].id}]` | {mods.get(payload.message_id)[2]}\n```css\n[Пользовательская причина]:```{mods.get(payload.message_id)[3]}\n```diff\n- Примечания:```**Представителя Команды Каталога невозможно забанить.**').set_footer(text=f'Ответственный за жалобу {mods.get(payload.message_id)[4]}', icon_url=mods.get(payload.message_id)[4].avatar_url))
                  else:
                      try:
                          embed = discord.Embed(timestamp=datetime.datetime.utcnow(),colour=0x310000,description=f'Вы были забанены на сервере Каталог Серверов по причине `{reason}` модератором `{mods.get(payload.message_id)[4].name}`. Если Вы считаете, что наказание было выдано необоснованно, у Вас есть возможность его обжаловать **[здесь](https://forms.gle/PSC8smGWMBZR7f6m8)**.')
                          embed.set_thumbnail(url=guild_kc.icon_url)
                          embed.set_footer(text='С уважением, Команда Каталога!')
                          await member.send(embed=embed)
                          inf = 'Форма обжалования была доставлена нарушителю.'
                      except:
                          inf = 'Форма обжалования не была доставлена нарушителю.'
                      try:
                          await guild_kc.ban(user=member, reason=f'{mods.get(payload.message_id)[4].name}: {reason}', delete_message_days=0)
                          await msg_c.edit(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x36393f, title=f'Панель модератора [Меры приняты]', description=f'```css\n[Нарушитель]:```{mods.get(payload.message_id)[2].mention} | `[{mods.get(payload.message_id)[2].id}]` | {mods.get(payload.message_id)[2]}\n```css\n[Пользовательская причина]:```{mods.get(payload.message_id)[3]}\n```diff\n- Принял меры:```{mods.get(payload.message_id)[4].mention} | `[{mods.get(payload.message_id)[4].id}]` | {mods.get(payload.message_id)[4]}\n> `Причина:` {reason}\n> {inf}').set_footer(text=f'Ответственный за жалобу {mods.get(payload.message_id)[4]}', icon_url=mods.get(payload.message_id)[4].avatar_url))
                      except:
                          await msg_c.edit(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x36393f, title=f'Панель модератора [Меры приняты]', description=f'```css\n[Нарушитель]:```{mods.get(payload.message_id)[2].mention} | `[{mods.get(payload.message_id)[2].id}]` | {mods.get(payload.message_id)[2]}\n```css\n[Пользовательская причина]:```{mods.get(payload.message_id)[3]}\n```diff\n- Примечания:```**Этого пользователя невозможно забанить.**').set_footer(text=f'Ответственный за жалобу {mods.get(payload.message_id)[4]}', icon_url=mods.get(payload.message_id)[4].avatar_url))
              await mods.get(payload.message_id)[5].add_reaction('<:Check_from_Helen22:819642494479368273>')
          elif payload.channel_id == id_chn_jb and mods.get(payload.message_id)[0] == payload.user_id and payload.emoji.id in [819909390047510528, 819909390026145872, 819909389694664705, 819909390060093480, 819909390155907072, 819909390253162496, 819909390442299413, 819909390315683840, 819909390000848899, 819909390160363581]:
              key_log.update({payload.message_id:9})
              if payload.emoji.id == 819909390047510528:
                  tms = 26
              elif payload.emoji.id == 819909390026145872:
                  tms = 1
              elif payload.emoji.id == 819909389694664705:
                  tms = 2
              elif payload.emoji.id == 819909390060093480:
                  tms = 3
              elif payload.emoji.id == 819909390155907072:
                  tms = 4
              elif payload.emoji.id == 819909390253162496:
                  tms = 5
              elif payload.emoji.id == 819909390442299413:
                  tms = 6
              elif payload.emoji.id == 819909390315683840:
                  tms = 7
              elif payload.emoji.id == 819909390000848899:
                  tms = 8
              elif payload.emoji.id == 819909390160363581:
                  tms = 9
              tms = 2 ** tms
              mods_type.update({payload.message_id:['mute', tms, False]})
              msg_c = msg_arch.get(payload.message_id)
              await msg_c.clear_reactions()
              await msg_c.edit(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x36393f, title=f'Панель модератора [Подтверждение мута]', description=f'```css\n[Нарушитель]:```{mods.get(payload.message_id)[2].mention} | `[{mods.get(payload.message_id)[2].id}]` | {mods.get(payload.message_id)[2]}\n```css\n[Пользовательская причина]:```{mods.get(payload.message_id)[3]}\n```diff\n- Подтверждение:```Вы уверены, что хотите замутить пользователя по причине `{mods2.get(payload.message_id)}` на `{tms}ч.` ?').set_footer(text=f'Ответственный за жалобу {mods.get(payload.message_id)[4]}', icon_url=mods.get(payload.message_id)[4].avatar_url))
              i, emojis = 0, ['<:yes_warn:819692933489754122>', '<:no_mute:819692972870205460>', '<:Home:822131145026043984>', '<:no:819634947756916810>']
              while key_log.get(payload.message_id) == 9 and i != 4:
                  await msg_c.add_reaction(emojis[i])
                  i += 1
          elif payload.channel_id == id_chn_jb and payload.emoji.id == 822423843163078668 and mods.get(payload.message_id)[0] == payload.user_id and not mods_type.get(payload.message_id)[2] == '123':
              msg_c = msg_arch.get(payload.message_id)
              mods_type.update({payload.message_id:[None, 0, '123']})
              member = mods.get(payload.message_id)[2]
              posl_date, s, embeds, k, ss_s, spisok = '', '', [], 0, {}, []
              sp = ['key', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
              for item in [i for i in my_warn.find({'id':member.id})]:
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
                      embed.set_footer(text=f'По запросу {mods.get(payload.message_id)[4]}',icon_url=mods.get(payload.message_id)[4].avatar_url)
                      embed.set_author(name='Нарушения пользовательского соглашения [Панель]', icon_url=gg.icon_url)
                      embeds.append(embed)
                      k = 0
                      s = ''
              if k != 0:
                  embed = discord.Embed(colour=discord.Colour(0x310000),description=f'**Предупреждения пользователя `{member}:`**{s}',timestamp=datetime.datetime.utcnow())
                  embed.set_footer(text=f'По запросу {mods.get(payload.message_id)[4]}',icon_url=mods.get(payload.message_id)[4].avatar_url)
                  embed.set_author(name='Нарушения пользовательского соглашения [Панель]', icon_url=gg.icon_url)
                  embeds.append(embed)
              if embeds == []:
                  await client.get_channel(id_chn_jb).send(embed=discord.Embed(colour=0x310000, description=f'```css\n[У пользователя {member} предупреждения отсутствуют.]```').set_author(name='Нарушения пользовательского соглашения [Панель]', icon_url=gg.icon_url))
              elif len(embeds) == 1:
                  await client.get_channel(id_chn_jb).send(embed=embeds[0])
              else:
                  msg = await client.get_channel(id_chn_jb).send(embed=embeds[0])
                  page = Paginator(client, msg, timeout=3600, use_exit=True, delete_message=False, reactions=['<:back:820233427411927071>', '<:go:820233452522569732>'], only=mods.get(payload.message_id)[4], use_more=False, exit_reaction=['<:stop:820233391726133279>'], embeds=embeds)
                  await page.start()
                                                                                    
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
async def dm(message, id = None, *, urls = None):
    if message.author.id in admins or message.author.id == 571006178444836875:
        if id is None:
            await message.channel.send(embed=discord.Embed(colour=0x2f3136, description='Вы не указали пользователя.'))
        elif id == '-u':
            result = ''
            for i in urls.split('\n'):
                url2 = i.split('/')
                try:
                    msg = await client.get_channel(int(url2[5])).fetch_message(int(url2[6]))
                    a = msg.mentions[0]
                    dm_date1 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[0].split('-')
                    dm_date2 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[1].split('.')[0].split(':')
                    for j in dm_guild.channels:
                        if str(a.id) == j.name:
                            
                            try:
                                await a.send(embed = discord.Embed(colour=0x2f3136, description=f'Доброго времени суток.\n\nИзвините за вынужденное беспокойство. Дело в том, что ссылка на ваш **[проект]({i})** истекла. Это может быть связано с одной из следующих причин:\n1. Ссылка устарела и требует замены на новую, бесконечную.\n2. Проекта более не существует.\n\nМогу ли я узнать, какой из вышеперечисленных вариантов актуален для вашего проекта? Свой ответ вы можете дать прямо в данных личных сообщениях с ботом.\n\n**Спешим предупредить, что если информация касательно вашего сервера не будет нами получена в течение недели с момента нашего обращения, мы будем вынуждены разорвать с вами партнёрство.**\n\nС уважением,\nКоманда Каталога').set_author(name=f'Catalog (System)\n{dm_date1[2]} {dm_date[int(dm_date1[1])]} {dm_date2[0]}:{dm_date2[1]} GMT+3'))
                                await j.send(f'Доброго времени суток.\n\nИзвините за вынужденное беспокойство. Дело в том, что ссылка на ваш **[проект]({i})** истекла. Это может быть связано с одной из следующих причин:\n1. Ссылка устарела и требует замены на новую, бесконечную.\n2. Проекта более не существует.\n\nМогу ли я узнать, какой из вышеперечисленных вариантов актуален для вашего проекта? Свой ответ вы можете дать прямо в данных личных сообщениях с ботом.\n\n**Спешим предупредить, что если информация касательно вашего сервера не будет нами получена в течение недели с момента нашего обращения, мы будем вынуждены разорвать с вами партнёрство.**\n\nС уважением,\nКоманда Каталога')
                                result += f'**[Ссылка]({i})** действительна. Сообщение отправлено в **[существующий диалог](https://discord.com/channels/822949304255119421/{j.id})**.\n'
                            except:
                                result += f'**[Ссылка]({i})** проигнорирована, так как у пользователя закрыты личные сообщения.\n'
                            break
                    else:
                        try:
                            await a.send(embed = discord.Embed(colour=0x2f3136, description=f'Доброго времени суток.\n\nИзвините за вынужденное беспокойство. Дело в том, что ссылка на ваш **[проект]({i})** истекла. Это может быть связано с одной из следующих причин:\n1. Ссылка устарела и требует замены на новую, бесконечную.\n2. Проекта более не существует.\n\nМогу ли я узнать, какой из вышеперечисленных вариантов актуален для вашего проекта? Свой ответ вы можете дать прямо в данных личных сообщениях с ботом.\n\n**Спешим предупредить, что если информация касательно вашего сервера не будет нами получена в течение недели с момента нашего обращения, мы будем вынуждены разорвать с вами партнёрство.**\n\nС уважением,\nКоманда Каталога').set_author(name=f'Catalog (System)\n{dm_date1[2]} {dm_date[int(dm_date1[1])]} {dm_date2[0]}:{dm_date2[1]} GMT+3'))
                            c = await dm_guild.create_text_channel(name=a.id, category=dm_guild.categories[0], reason=f'Новое обращение от {a}.')
                            await c.send(f'Доброго времени суток.\n\nИзвините за вынужденное беспокойство. Дело в том, что ссылка на ваш **[проект]({i})** истекла. Это может быть связано с одной из следующих причин:\n1. Ссылка устарела и требует замены на новую, бесконечную.\n2. Проекта более не существует.\n\nМогу ли я узнать, какой из вышеперечисленных вариантов актуален для вашего проекта? Свой ответ вы можете дать прямо в данных личных сообщениях с ботом.\n\n**Спешим предупредить, что если информация касательно вашего сервера не будет нами получена в течение недели с момента нашего обращения, мы будем вынуждены разорвать с вами партнёрство.**\n\nС уважением,\nКоманда Каталога')
                            result += f'**[Ссылка]({i})** действительна. Сообщение отправлено в **[созданный диалог](https://discord.com/channels/822949304255119421/{c.id})**.\n'
                        except:
                            result += f'**[Ссылка]({i})** проигнорирована, так как у пользователя закрыты личные сообщения.\n'
                except:
                    result += f'**[Ссылка]({i})** проигнорирована ввиду возникновения ошибки.\n'
            await message.channel.send(embed=discord.Embed(colour=0x2f3136, title='Логи:', description=result))
        else:
            try:
                a = await client.fetch_user(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
                for i in dm_guild.channels:
                    if str(a.id) == i.name:
                        await message.channel.send(embed=discord.Embed(colour=0x2f3136, description=f'**[Диалог](https://discord.com/channels/822949304255119421/{i.id})** с пользователем {a} `[{a.id}]` уже существует.'))
                        break
                else:
                    c = await dm_guild.create_text_channel(name=a.id, category=dm_guild.categories[0], reason=f'Новое обращение от {a}.')
                    await message.channel.send(embed=discord.Embed(colour=0x2f3136, description=f'**[Диалог](https://discord.com/channels/822949304255119421/{c.id})** с пользователем {a} `[{a.id}]` успешно открыт.'))
            except:
                await message.channel.send(embed=discord.Embed(colour=0x2f3136, description='Указанного пользователя не существует.'))
  
@client.command()
async def ev(ctx, *, txt):
    if ctx.author.id == 414119169504575509 or ctx.author.id == 529044574660853761:
        if txt.startswith('```') and txt.endswith('```'):
            txt = '\n'.join(txt.split('\n')[1:][:-3])
    
        local_variables = {
            'discord': discord,
            'commands': commands,
            'bot': client,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            'datetime': datetime,
            'db': my_client
        }

        stdout = io.StringIO()

        try:
            with contextlib.redirect_stdout(stdout):
                exec(
                    f'async def func():\n{textwrap.indent(txt, "    ")}', local_variables
                )

                obj = await local_variables['func']()
                result = f'{stdout.getvalue()}\n-- {obj}\n'
        except Exception as e:
            result = ''.join(traceback.format_exception(e, e, e.__traceback__))

        await ctx.channel.send(embed=discord.Embed(description='```py\n' + result + '```', colour=0x000001, timestamp=datetime.datetime.utcnow()).set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url))
    
@client.command()
async def help(message):
    msg = await client.get_channel(690827050033872937).history(limit=20).flatten()
    msg = msg[0].content.replace("[","").replace("]","").replace("'","").split(', ')
    embed = discord.Embed(colour=discord.Colour(0x310000),title='Меню Каталог Серверов', description=f"**Страница 1. Команды для всех пользователей:**\n\n`K.help` — помощь.\n`K.avatar @user|ID` — аватар пользователя.\n`K.emoji emoji|ID` — информация об эмодзи (только нашего сервера).\n`K.bug <суть_бага>` — сообщить о баге разработчику.\n\n`K.notify` — настройки оповещений.\n\n`K.suggest текст` — предложить свою идею.\n`K.esuggest <номер> <новый_текст>` — отредактировать свою идею, если на неё не дан ответ.\n\n`K.problem` — задать вопрос поддержке сервера.\n`K.eproblem <номер_вопроса> <новый текст>` — отредактировать свой вопрос, если на него ещё не дан ответ.\n\n`K.info @user|ID` — информация о пользователе.\n`K.badges` — обозначение значков.\n`K.server` — информация о сервере.\n`K.stats` — статистика сервера.\n`K.team` — состав Команды сервера [@упоминаниями].\n`K.team -` — состав Команды сервера [текстом].\n\n[Случайный партнёр]({msg[random.randint(0,len(msg)-1)]})",timestamp=datetime.datetime.utcnow())
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    embed.set_thumbnail(url=message.guild.icon_url)
    
    embed2 = discord.Embed(colour=discord.Colour(0x310000),title='Меню Каталог Серверов', description=f"**Страница 2. Команды для состава:**\n\n`K.staff` — административные команды.\n`K.moder` — команды для модераторов.\n`K.support` — команды для Support Team.\n`K.op` — команды для главы отдела партнёрства.\n`K.pm` — команды для пиар-менеджера.\n`K.kk` — команды для всего персонала.\n\n[Случайный партнёр]({msg[random.randint(0,len(msg)-1)]})",timestamp=datetime.datetime.utcnow())
    embed2.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    embed2.set_thumbnail(url=message.guild.icon_url)
    
    embeds = [embed,embed2]
    msg = await message.channel.send(embed=embeds[0])
    page = Paginator(client, msg, footer=False, timeout=3600, use_exit=True, delete_message=False, reactions=['<:back:820233427411927071>', '<:go:820233452522569732>'], only=message.author, use_more=False, exit_reaction=['<:stop:820233391726133279>'], embeds=embeds)
    await page.start()

@client.command()
async def op(message):
  if message.channel.id != 642190411867226112 and not message.author.id in admins:
    await message.channel.send(embed=discord.Embed(colour=0x310000,description='<:kk:788850405157240833> Данная команда действует только в **[служебной](https://discord.com/channels/604636579545219072/642190411867226112)**.'))
  elif 686639786672652363 in [role.id for role in message.author.roles] or message.author.id in admins:
    embed=discord.Embed(colour=discord.Colour(0x310000),timestamp=datetime.datetime.utcnow(),description="<:kk:788850405157240833> **Команды для <@&686639786672652363>:**\n\n`K.modstats date1 date2` — показать статистику отдела партнёрства с date1 по date2.\n`K.apm @user|+/-` — выдать или забрать роли пиар-менеджера соответственно.\n`K.removebl <№случая>` — исключить сервер из чёрного списка по номеру случая.\n`K.rebuke @user|ID reason` — выдать выговор.\n`K.unrebuke №случая` — снять выговор.\n`K.rebukes @user|ID` — просмотреть выговоры.")
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    embed.set_thumbnail(url=message.guild.icon_url)
    await message.channel.send(embed=embed)
    
@client.command()
async def pm(message):
  if message.channel.id != 642190411867226112 and not message.author.id in admins:
    await message.channel.send(embed=discord.Embed(colour=0x310000,description='<:kk:788850405157240833> Данная команда действует только в **[служебной](https://discord.com/channels/604636579545219072/642190411867226112)**.'))
  elif 608600358570295307 in [role.id for role in message.author.roles] or message.author.id in admins:
    embed=discord.Embed(colour=discord.Colour(0x310000),timestamp=datetime.datetime.utcnow(),description="<:kk:788850405157240833> **Команды для <@&608600358570295307>:**\n\n`K.addbl <URL> <причина>` — добавить сервер в чёрный список. Вложение обязательно!\n`K.bl` — просмотреть чёрный список серверов каталога.\n`K.np +/- @user|ID` — выдать/снять пользователю роль партнёра первого уровня.\n`K.pms` — статистика работы пиар-менеджеров.")
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
                embed = discord.Embed(timestamp=datetime.datetime.utcnow(),colour=0x310000,description=f'Вы были забанены на сервере Каталог Серверов по причине `{reason}` модератором `{message.author.name}`. Если Вы считаете, что наказание было выдано необоснованно, у Вас есть возможность его обжаловать **[здесь](https://forms.gle/PSC8smGWMBZR7f6m8)**.')
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
  embed.add_field(name=f"```Главный Модератор:```",value=('Отсутствует.')) if a == '```md\n```' or a == '' else embed.add_field(name=f"```Главный Модератор:```",value=(a))
  a = '```md\nPandeMiaa```' if kl == '-' else '<@529044574660853761>'
  embed.add_field(name=f"```Глава Support Team:```",value=(a))

  a = '```md\n' + '\n'.join([i.name for i in message.guild.get_role(686621891230040077).members]).replace(message.author.name,f'#{message.author.name}') + '```' if kl == '-' else '\n'.join([i.mention for i in message.guild.get_role(686621891230040077).members])
  embed.add_field(name=f"```Отдел партнёрства: [0]```",value=('**[Правила и важное](https://discord.com/channels/604636579545219072/714909100214845541)**\nОтсутствует.')) if a == '```md\n```' or a == '' else embed.add_field(name=f"```Отдел партнёрства: [{len([i.name for i in message.guild.get_role(686621891230040077).members])}]```",value=(f'**[Правила и важное](https://discord.com/channels/604636579545219072/714909100214845541)**\n{a}'))
  c = '```md\n' + '\n'.join([i.name for i in message.guild.get_role(677397817966198788).members]).replace(message.author.name,f'#{message.author.name}') + '```' if kl == '-' else '\n'.join([i.mention for i in message.guild.get_role(677397817966198788).members])
  embed.add_field(name=f"```Модерация: [0]```",value=('**[Правила и наказания](https://discord.com/channels/604636579545219072/715130816480673872)**\nОтсутствует.')) if c == '```md\n```' or c == '' else embed.add_field(name=f"```Модерация: [{len([i.name for i in message.guild.get_role(677397817966198788).members])}]```",value=(f'**[Правила и наказания](https://discord.com/channels/604636579545219072/715130816480673872)**\n{c}'))
  a = '```md\n' + '\n'.join([i.name for i in message.guild.get_role(816386551222763561).members]).replace(message.author.name,f'#{message.author.name}') + '```' if kl == '-' else '\n'.join([i.mention for i in message.guild.get_role(816386551222763561).members])
  embed.add_field(name=f"```Support Team: [0]```",value=('**[Support info](https://discord.com/channels/604636579545219072/816805410379137024) | [Тикеты](https://discord.com/channels/604636579545219072/816385807958802522)**\nОтсутствует.\n\n**`Навигация для команды:`**\n**[Рекрутерам](https://discord.com/channels/604636579545219072/776484522329374761)**\n**[Новинки и анонсы](https://discord.com/channels/604636579545219072/818037038854176819)**\n**[Объявления и опросы](https://discord.com/channels/604636579545219072/619067194910703626)**\n**[Информация о ролях](https://discord.com/channels/604636579545219072/616656872703000587/802322890191274014)**\n**[Общие полномочия](https://discord.com/channels/604636579545219072/630432803942563840)**')) if a == '```md\n```' or a == '' else embed.add_field(name=f"```Support Team: [{len([i.name for i in message.guild.get_role(816386551222763561).members])}]```",value=(f'**[Support info](https://discord.com/channels/604636579545219072/816805410379137024) | [Тикеты](https://discord.com/channels/604636579545219072/816385807958802522)**\n{a}\n\n**`Навигация для команды:`**\n**[Рекрутерам](https://discord.com/channels/604636579545219072/776484522329374761)**\n**[Новинки и анонсы](https://discord.com/channels/604636579545219072/818037038854176819)**\n**[Объявления и опросы](https://discord.com/channels/604636579545219072/619067194910703626)**\n**[Информация о ролях](https://discord.com/channels/604636579545219072/616656872703000587/802322890191274014)**\n**[Общие полномочия](https://discord.com/channels/604636579545219072/630432803942563840)**'))
  a = '```md\n' + '\n'.join([i.name for i in message.guild.get_role(757890413838467133).members]).replace(message.author.name,f'#{message.author.name}') + '```' if kl == '-' else '\n'.join([i.mention for i in message.guild.get_role(757890413838467133).members])
  embed.add_field(name=f"```В отставке: [0]```",value=('Отсутствует.')) if a == '```md\n```' or a == '' else embed.add_field(name=f"```В отставке: [{len([i.name for i in message.guild.get_role(757890413838467133).members])}]```",value=(a))

  a = '```md\n' + '\n'.join([i.name for i in message.guild.get_role(686618397668147220).members]).replace(message.author.name,f'#{message.author.name}') + '```' if kl == '-' else '\n'.join([i.mention for i in message.guild.get_role(686618397668147220).members])
  embed.add_field(name=f"```Дизайнеры: [0]```",value=('**[Наброски](https://discord.com/channels/604636579545219072/686621337153699929)**\nОтсутствует.')) if a == '```md\n```' or a == '' else embed.add_field(name=f"```Дизайнеры: [{len([i.name for i in message.guild.get_role(686618397668147220).members])}]```",value=(f'**[Наброски](https://discord.com/channels/604636579545219072/686621337153699929)**\n{a}'))
  
  a = '```md\n' + '\n'.join([str(await client.fetch_user(i))[:-5] for i in admins]).replace(message.author.name,f'#{message.author.name}') + '```' if kl == '-' else '\n'.join([f'<@{i}>' for i in admins])
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
  page = Paginator(client, msg, timeout=3600, use_exit=True, delete_message=False, reactions=['<:back:820233427411927071>', '<:go:820233452522569732>'], only=message.author, use_more=False, exit_reaction=['<:stop:820233391726133279>'], embeds=embeds)
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
          aktiv = requests.get(f'https://api.catalogserverov.ml/v1/stats/pm/list?user={i}').text.split('||')
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
      embed=discord.Embed(timestamp=datetime.datetime.utcnow(),description="<:developer:785191301321719828> **Команды для <@&620955813850120192>:**\n\n`K.say #channel|ID текст` — отправить текст определённого содержания в предназначеный канал.\n`K.clear n` — удалить n сообщений в канале.\n`K.disable` — отключить основные каналы (применять только на случай рейда)\n`K.enable` — включить все основные каналы (применять только на случай рейда)\n`K.approve Номер (+/-) Текст` — принять/отклонить предложение\n`K.iban @user|ID Причина` — добавить в чс идей пользователя\n`K.iunban @user|ID` — убрать из чс идей пользователя\n`K.ibans` — посмотреть чс идей\n`K.answer номер|текст` — ответить на вопрос пользователя\n`K.rebuke @user|ID reason` — выдать выговор.\n`K.unrebuke №случая` — снять выговор.\n`K.rebukes @user|ID` — просмотреть выговоры.\n\n`K.cont url` — предоставить файл с контентом сообщения по ссылке на него.")
      embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
      embed.set_thumbnail(url=message.guild.icon_url)
      await message.channel.send(embed=embed)
        
@client.command()
async def moder(message):
    if message.channel.id != 642190411867226112 and not message.author.id in admins:
      await message.channel.send(embed=discord.Embed(colour=0x310000,description='<:moderator:827468511894700054> Данная команда действует только в **[служебной](https://discord.com/channels/604636579545219072/642190411867226112)**.'))
    elif 800474182474268734 in [role.id for role in message.author.roles] or 677397817966198788 in [role.id for role in message.author.roles] or message.author.id in admins:
      embed=discord.Embed(colour=discord.Colour(0x310000),timestamp=datetime.datetime.utcnow(),description="<:moderator:827468511894700054> **Команды для <@&677397817966198788>:**\n\n`K.ban @user|ID причина` — забанить пользователя.\n`K.unban @user|ID причина` — разбанить пользователя.\n\n`K.warn @user|ID причина` — выдать предупреждение пользователю.\n`K.warns @user|ID` — просмотреть предупреждения пользователя.\n`K.unwarn <Номер_случая>` — снять предупреждение по номеру случая.\n\n`K.mute @user|ID time причина` — замутить человека на time часов.\n`K.unmute @user|ID` — размутить человека.\n\n`K.rebuke @user|ID reason` — выдать выговор.\n`K.unrebuke №случая` — снять выговор.\n\n`K.active @user|ID <+/-> <причина>` — выдать/забрать роль активного участника соответственно.")
      embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
      embed.set_thumbnail(url=message.guild.icon_url)
      await message.channel.send(embed=embed)
      
@client.command()
async def kk(message):
  if message.channel.id != 642190411867226112 and not message.author.id in admins:
    await message.channel.send(embed=discord.Embed(colour=0x310000,description='<:kk:788850405157240833> Данная команда действует только в **[служебной](https://discord.com/channels/604636579545219072/642190411867226112)**.'))
  elif 608994688078184478 in [role.id for role in message.author.roles] or message.author.id in admins:
    embed=discord.Embed(colour=discord.Colour(0x310000),timestamp=datetime.datetime.utcnow(),description="<:kk:788850405157240833> **Команды для <@&608994688078184478>:**\n\n`K.rebukes` — посмотреть свои выговоры.\n\n`K.rate_stats` — статистика неоценённых идей и тех, что отправлены владельцу сервера.\n`Примечание:` проверяются последние 200 идей.\n`K.rate <номер_идеи> <оценка_[1..10]>` — дать свою оценку на оставленную идею (от 1 до 10)\n`K.approve <номер_идеи> <рецензия>` — оставить рецензию на идею.\n`Примечание:` 2 данных команды работают лишь в канале **[предложений](https://discord.com/channels/604636579545219072/678666229661171724)**.")
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    embed.set_thumbnail(url=message.guild.icon_url)
    await message.channel.send(embed=embed)

@client.command()
async def support(message):
    if message.channel.id != 642190411867226112 and not message.author.id in admins:
        await message.channel.send(embed=discord.Embed(colour=0x310000,description='<:Support:816800431249555498> Данная команда действует только в **[служебной](https://discord.com/channels/604636579545219072/642190411867226112)**.'))
    elif 816386551222763561 in [role.id for role in message.author.roles] or message.author.id in admins:
      embed=discord.Embed(colour=discord.Colour(0x310000),timestamp=datetime.datetime.utcnow(),description="<:Support:816800431249555498> **Команды для <@&816386551222763561>:**\n\n`K.active @user|ID <+/-> <причина>` — выдать/забрать роль активного участника соответственно.\n`K.answer <номер_вопроса> <ответ>` — дать ответ на вопрос пользователя.\n`K.ticket` — посмотреть список доступных аргументов.\n`K.ticket @user|ID <аргумент_вышестоящего> <мотив>` — создать тикет вышестоящему, где `@user|ID` - пользователь, который нуждается в помощи.")
      embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
      embed.set_thumbnail(url=message.guild.icon_url)
      await message.channel.send(embed=embed)
      
@client.command()
async def bug(message, *, txt=None):
    if txt is None:
        await message.channel.send(embed=discord.Embed(colour=0x2f3136, description='```yaml\nПожалуйста, опишите суть проблемы.```'))
    else:
        dm_date1 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[0].split('-')
        dm_date2 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[1].split('.')[0].split(':')
        await client.get_channel(829738150230360083).send(embed=discord.Embed(colour=0x2f3136, description=txt).set_author(name=f'{message.author.name} (Member)\n{dm_date1[2]} {cs.sokr_date[int(dm_date1[1])]} {dm_date2[0]}:{dm_date2[1]} GMT+3'))
        await message.channel.send(embed=discord.Embed(colour=0x2f3136, description='```yaml\nСпасибо, что помогаете делать бота лучше <3```'))
      
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
async def np(message, arg=None, id=None):
  b = [role.id for role in message.author.roles]
  if message.author.id in admins or 686621891230040077 in b:
    if arg is None:
      await message.channel.send('```css\nВы не указали аргумент.```')
    elif arg != '+' and arg != '-':
      await message.channel.send('```css\nАргументом может выступать только +/-.```')
    elif id is None:
      await message.channel.send('```css\nВы не указали id пользователя.```')
    else:
      try:
        member = client.get_guild(604636579545219072).get_member(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
        embed = discord.Embed(colour=0xb7bcd8, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
        if arg == '+':
          global d; global dk; global d_url
          sp = ['key', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
          if 688654966675603491 in [role.id for role in member.roles]:
            avr = '<@&688654966675603491>'
          elif 622501656591990784 in [role.id for role in member.roles]:
            avr = '<@&622501656591990784>'
          elif 622501691107049502 in [role.id for role in member.roles]:
            avr = '<@&622501691107049502>'
          elif 769916590686732319 in [role.id for role in member.roles]:
            avr = '<@&769916590686732319>'
          else:
            avr = False
          if not avr:
            await member.add_roles(message.guild.get_role(688654966675603491),reason=f'{message.author.name}: Новый партнёр.')
            embed.description = f'Пользователю {member} `[{member.id}]` успешна выдана роль <@&688654966675603491>.'
          else:
            embed.description = f'Роль партнёра первого уровня не была добавлена, т.к. пользователь {member} `[{member.id}]` уже имеет роль {avr}.'
          kolvo = dk.get(member.id) if dk.get(member.id) is not None else 0
          embed.description += f'\n\n**`Публикаций:` {kolvo}**'
          if d.get(member.id) is not None:
            datet = d.get(member.id).split('.')[0].split()[0].split('-')
            datet2 = d.get(member.id).split('.')[0].split()[1]
            embed.description += f'\n**[Последняя публикация]({d_url.get(member.id)})**: {datet[2]} {sp[int(datet[1])]} {datet[0]} года в {datet2}'
          else:
            embed.description += f'\n**[Последняя публикация]({d_url.get(member.id)})**: неизвестно.'
          await message.channel.send(embed=embed)
        else:
          global np_kd
          if np_kd.get(message.author.id) is None or time.time() - np_kd.get(message.author.id) >= 600:
            if 688654966675603491 in [role.id for role in member.roles]:
              await member.remove_roles(message.guild.get_role(688654966675603491),reason=f'{message.author.name}: Партнёрство разорвано.')
              embed.description = f'С пользователя {member} `[{member.id}]` успешна снята роль <@&688654966675603491>.'
              np_kd.update({message.author.id:time.time()})
            else:
              embed.description = f'Роль партнёра первого уровня не была снята, т.к. у пользователя {member} `[{member.id}]` она отсутствует.'
            await message.channel.send(embed=embed)
          else:
            otkat = f'Минут до отката команды: ~{int((600-(time.time()-np_kd.get(message.author.id)))//60)}' if (600-(time.time()-np_kd.get(message.author.id)))//60 != 0 else f'Секунд до отката команды: ~{int(600-(time.time()-np_kd.get(message.author.id)))}'
            await message.channel.send(embed=discord.Embed(colour=0x310000,description=f'```css\n[Данная команда имеет пользовательскую задержку в 10 минут.]```\n```md\n#{otkat}```'))
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
    for item in [i for i in my_warn.find({'id':member.id})]:
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
      page = Paginator(client, msg, timeout=3600, use_exit=True, delete_message=False, reactions=['<:back:820233427411927071>', '<:go:820233452522569732>'], only=message.author, use_more=False, exit_reaction=['<:stop:820233391726133279>'], embeds=embeds)
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
async def notify(message, *, txt=None):
    result = ''
    if [i for i in my_not.find({'id':message.author.id})] == []:
        my_not.insert_one({'id':message.author.id, 'p':True, 'i':True})
    if txt is None:
        result += '```md\n#Ваши персональные настройки уведомлений:```\n'
        a = my_not.find({'id':message.author.id})[0]
        if a['i']:
            result += '<:notify:829402470383353897> Вы будете получать уведомления в случае изменения статуса ваших идей.\n'
        else:
            result += '<:not_notify:829455038757339136> Вы не будете получать уведомления в случае изменения статуса ваших идей.\n'
        if a['p']:
            result += '<:notify:829402470383353897> Вы будете получать уведомления в случае изменения статуса ваших вопросов.\n'
        else:
            result += '<:not_notify:829455038757339136> Вы не будете получать уведомления в случае изменения статуса ваших вопросов.\n'
        result += '\n```yaml\nСписок доступных аргументов для данной команды:```\n`i+` — включить уведомления для идей.\n`i-` — выключить уведомления для идей.\n\n`p+` — включить уведомления для вопросов.\n`p-` — выключить уведомления для вопросов.'
    else:
        if not 'i+' in txt and not 'i-' in txt and not 'p+' in txt and not 'p-' in txt:
            result = 'Заданы несуществующие аргументы.\nСписок доступных аргументов для данной команды: `i+`, `i-`, `p+`, `p-`.'
        else:
            if 'i+' in txt and 'i-' in txt:
                result += 'Аргументы `i+` и `i-` противоречат друг другу.\n'
            elif 'i+' in txt:
                my_not.update_one({"id":message.author.id},{"$set":{"i":True}})
                result += '<:notify:829402470383353897> Вы будете получать уведомления в случае изменения статуса ваших идей.\n'
            elif 'i-' in txt:
                my_not.update_one({"id":message.author.id},{"$set":{"i":False}})
                result += '<:not_notify:829455038757339136> Вы не будете получать уведомления в случае изменения статуса ваших идей.\n'
            if 'p+' in txt and 'p-' in txt:
                result += 'Аргументы `p+` и `p-` противоречат друг другу.\n'
            elif 'p+' in txt:
                my_not.update_one({"id":message.author.id},{"$set":{"p":True}})
                result += '<:notify:829402470383353897> Вы будете получать уведомления в случае изменения статуса ваших вопросов.\n'
            elif 'p-' in txt:
                my_not.update_one({"id":message.author.id},{"$set":{"p":False}})
                result += '<:not_notify:829455038757339136> Вы не будете получать уведомления в случае изменения статуса ваших вопросов.\n'
    await message.channel.send(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x310000, description=f'**{result}**').set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url))
            
@client.command()
async def rate_stats(message):
    b = [role.id for role in message.author.roles]
    if 608994688078184478 in b or 816386551222763561 in b or 757890413838467133 in b or message.author.id in admins:
        mas, mas2, embeds = [], [], []
        his = await client.get_channel(cs.ideas_id).history(limit=200).flatten()
        for i in his[::-1]:
            try:
                if i.embeds[0].fields[-1].name == 'Оценки данной идеи:':
                    if not str(message.author.id) in i.embeds[0].fields[-1].value:
                        mas.append(f'**[Идея №{i.embeds[0].title.split("№")[-1]}]({i.jump_url})**')
                    if 'Идея передана' in i.embeds[0].fields[-1].value:
                        mas2.append(f'**[Идея №{i.embeds[0].title.split("№")[-1]}]({i.jump_url})**')
            except:
                pass
        embed = discord.Embed(colour=0x310000, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
        if mas == []:
            embed.description='```yaml\nВау, вы оценили все возможные предложения, спасибо <3```'
            embeds.append(embed)
        else:
            k = 0; ch = -1
            embed.description = f'**Оцените следующие идеи `[{len(mas)}]`:**'
            for i in range(len(mas)//9):
                ch += 1
                result = '\n'.join(mas[k:k+9])
                embed.add_field(name=cs.rim[ch], value=result)
                k += 9
                if ch == 2:
                    ch = -1
                    embeds.append(embed)
                    embed = discord.Embed(colour=0x310000, timestamp=datetime.datetime.utcnow())
                    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
            if len(mas) % 9 > 0:
                result = '\n'.join(mas[k:k+9])
                embed.add_field(name=cs.rim[ch+1], value=result)
                if ch == -1 and k == 0:
                    embeds.append(embed)
            if ch != -1:
                embeds.append(embed)

        embed = discord.Embed(colour=0x310000, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
        if mas2 == []:
            embed.description='```yaml\nВладельцем сервера были рассмотрены все отправленные идеи ^^```'
        else:
            k = 0; ch = -1
            embed.description = f'<:owner:784812161959854120> **Владельцу отправлены следующие идеи на рассмотрение `[{len(mas2)}]`:**'
            for i in range(len(mas2)//9):
                ch += 1
                result = '\n'.join(mas2[k:k+9])
                embed.add_field(name=cs.rim[ch], value=result)
                k += 9
            if len(mas2) % 9 > 0:
                result = '\n'.join(mas2[k:k+9])
                embed.add_field(name=cs.rim[ch+1], value=result)
        embeds.append(embed)
        msg = await message.channel.send(embed=embeds[0])
        page = Paginator(client, msg, timeout=3600, use_exit=True, delete_message=False, reactions=['<:back:820233427411927071>', '<:go:820233452522569732>'], only=message.author, use_more=False, exit_reaction=['<:stop:820233391726133279>'], embeds=embeds)
        await page.start()
                        
@client.command()
async def suggest(message, *, txt=None):
    await message.message.delete()
    if message.channel.id == cs.ideas_id:
        if not txt is None:
            if [i for i in my_not.find({'id':message.author.id})] == []:
                my_not.insert_one({'id':message.author.id, 'p':True, 'i':True})
            global ideas_key; ideas_key += 1
            embed = discord.Embed(title=f'Предложение №{ideas_key}', colour=0x2f3136, description=txt)
            embed.set_author(name=f'{message.author.name} | {message.author.id}', icon_url=message.author.avatar_url)
            embed.add_field(name='Оценки данной идеи:', value='Пока отсутствуют.', inline=False)
            dm_date1 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[0].split('-')
            dm_date2 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[1].split('.')[0].split(':')
            msg = await message.channel.send(embed=embed)
            if my_not.find({'id':message.author.id})[0]['i']:
                try:
                    await message.author.send(embed=discord.Embed(colour=0x310000, timestamp=datetime.datetime.utcnow(), description=f'Благодарим за вашу оставленную **[идею]({msg.jump_url})**!\nНаша администрация постарается как можно быстрее дать на неё свой ответ.\n\nНеправильно сформулировали идею? У вас есть возможность её отредактировать до первого оставленного ответа:\n`K.esuggest <номер_оставленной_идеи> <новый_текст>`.\nНапример: `K.esuggest {ideas_key} {txt} + печенек админам :).`\n\nНе желаете получать уведомления в личные сообщения об изменениях статуса идеи? Используйте `K.notify i-` для отключения оповещений.\n`Примечание:` все команды можно прописывать **[здесь](https://discord.com/channels/604636579545219072/712638398132650095)**.').set_footer(text='С уважением,\nКоманда Каталога', icon_url=message.guild.icon_url))
                    check = 'Доставлено.'
                except:
                    check = 'Не доставлено (лс закрыты).'
            else:
                check = 'Уведомления идей отключены.'
            await msg.edit(embed=msg.embeds[0].set_footer(text=f'{dm_date1[2]} {cs.sokr_date[int(dm_date1[1])]} {dm_date2[0]}:{dm_date2[1]} GMT+3 | {check}'))
            await client.get_channel(cs.i_and_p_logs).send(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x2f3136, description=f'Предложена новая **[идея №{ideas_key}]({msg.jump_url})**:\n`ЛС: {check}`\n```{txt}```').set_author(name=message.author, icon_url=message.author.avatar_url).set_footer(text=f'ID: {message.author.id}'))
    else:
        await message.channel.send(embed=discord.Embed(colour=0x310000, description=f'**[Канал для предложений](https://discord.com/channels/604636579545219072/{cs.ideas_id})**'))

@client.command()
async def esuggest(message, num=None, *, txt=None):
    await message.message.delete()
    if message.channel.id == cs.ideas_id and not num is None and not txt is None:
        for i in await client.get_channel(cs.ideas_id).history(limit=100).flatten():
            try:
                if i.embeds[0].title.split('№')[-1] == num and i.embeds[0].author.name.split('| ')[-1] == str(message.author.id) and len(i.embeds[0].fields) == 1 and 'Пока отсутствуют.' in i.embeds[0].fields[-1].value:
                    embed = i.embeds[0]
                    before_txt = embed.description if len(embed.description) <= 900 else f'{embed.description[:900]}...'
                    embed.description = txt
                    dm_date1 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[0].split('-')
                    dm_date2 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[1].split('.')[0].split(':')
                    embed.set_footer(text=f'{dm_date1[2]} {cs.sokr_date[int(dm_date1[1])]} {dm_date2[0]}:{dm_date2[1]} GMT+3 | Идея отредактирована автором.')
                    await i.edit(embed=embed)
                    txt = txt if len(txt) <= 900 else f'{txt[:900]}...'
                    await client.get_channel(cs.i_and_p_logs).send(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x4986e3, description=f'Отредактирована **[идея №{num}]({i.jump_url})**:\n\n**Старый текст:**\n```{before_txt}```**Новый текст:**\n```{txt}```').set_author(name=message.author, icon_url=message.author.avatar_url).set_footer(text=f'ID: {message.author.id}'))
                    break
            except:
                pass

@client.command()
async def approve(message, num=None, *, txt=None):
    await message.message.delete()
    b = [role.id for role in message.author.roles]
    if message.channel.id == cs.ideas_id and not num is None and not txt is None and (608994688078184478 in b or 816386551222763561 in b or 757890413838467133 in b or message.author.id in admins):
        for i in await client.get_channel(cs.ideas_id).history(limit=100).flatten():
            try:
                if i.embeds[0].title.split('№')[1] == num and not '<:owner:784812161959854120>' in i.embeds[0].fields[-1].name:
                    k = -1
                    for j in i.embeds[0].fields:
                        try:
                            k += 1
                            if j.name.split('| ')[-1] == str(message.author.id):
                                embed = i.embeds[0]
                                before_txt = i.embeds[0].fields[k].value
                                embed.set_field_at(index=k, name=j.name, value=txt, inline=False)
                                dm_date1 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[0].split('-')
                                dm_date2 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[1].split('.')[0].split(':')
                                embed.set_footer(text=f'{dm_date1[2]} {cs.sokr_date[int(dm_date1[1])]} {dm_date2[0]}:{dm_date2[1]} GMT+3 | Отредактирована рецензия от {message.author.name}')
                                await i.edit(embed=embed)
                                await client.get_channel(cs.i_and_p_logs).send(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x002137, description=f'Отредактирована рецензия **[предложению №{num}]({i.jump_url})**:\n\n**Старый текст:**\n```{before_txt}```**Новый текст:**\n```{txt}```').set_author(name=message.author, icon_url=message.author.avatar_url).set_footer(text=f'ID: {message.author.id}'))
                                break
                        except:
                            pass
                    else:
                        if len(i.embeds[0].fields) < 10:
                            zn = '<:developer:785191301321719828>' if message.author.id in admins else '<:moderator:827468511894700054>' if 677397817966198788 in b else '<:Support:816800431249555498>' if 816386551222763561 in b else '<:kk:788850405157240833>'
                            embed = i.embeds[0]
                            field_value = embed.fields[-1].value
                            embed.remove_field(-1)
                            embed.add_field(name=f'{zn} Рецензия от {message.author.name} | {message.author.id}', value=txt, inline=False)
                            embed.add_field(name='Оценки данной идеи:', value=field_value, inline=False)
                            dm_date1 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[0].split('-')
                            dm_date2 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[1].split('.')[0].split(':')
                            embed.set_footer(text=f'{dm_date1[2]} {cs.sokr_date[int(dm_date1[1])]} {dm_date2[0]}:{dm_date2[1]} GMT+3 | Оставлена рецензия от {message.author.name}')
                            await i.edit(embed=embed)
                            await client.get_channel(cs.i_and_p_logs).send(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x002137, description=f'Оставлена рецензия **[предложению №{num}]({i.jump_url})**:\n```{txt}```').set_author(name=message.author, icon_url=message.author.avatar_url).set_footer(text=f'ID: {message.author.id}'))
                            break
            except:
                pass

@client.command()
async def approve_h22(message, num=None, arg=None, *, txt=None):
    await message.message.delete()
    if message.author.id == 414119169504575509:
        color = 0xcc0605 if arg == '-' else 0x123524 if arg == '+' else 0x002137
        for i in await client.get_channel(cs.ideas_id).history(limit=100).flatten():
            try:
                if i.embeds[0].title.split('№')[-1] == num:
                    if [i for i in my_not.find({'id':int(i.embeds[0].author.name.split('| ')[-1])})] == []:
                        my_not.insert_one({'id':int(i.embeds[0].author.name.split('| ')[-1]), 'p':True, 'i':True})
                    embed = i.embeds[0]
                    embed.colour = color
                    dm_date1 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[0].split('-')
                    dm_date2 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[1].split('.')[0].split(':')
                    if '<:owner:784812161959854120>' in embed.fields[-1].name:
                        before_txt = embed.fields[-1].value
                        embed.remove_field(-1)
                        check2 = 'Отредактирован вердикт от владельца сервера.'
                        await client.get_channel(cs.i_and_p_logs).send(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x310000, description=f'Отредактирован вердикт на **[идею №{num}]({i.jump_url})**.\n\n**Старый текст:**\n```{before_txt}```**Новый текст:**\n```{txt}```').set_author(name=message.author, icon_url=message.author.avatar_url).set_footer(text=f'ID: {message.author.id}'))
                    else:
                        if my_not.find({'id':int(i.embeds[0].author.name.split('| ')[-1])})[0]['i']:
                            try:
                                mem = await client.fetch_user(i.embeds[0].author.name.split('| ')[-1])
                                await mem.send(embed=discord.Embed(colour=0x310000, timestamp=datetime.datetime.utcnow(), description=f'Вы получили ответ на **[оставленную идею]({i.jump_url})** от владельца сервера Helen22.\n\nНе желаете получать уведомления в личные сообщения об изменениях статуса идеи? Используйте `K.notify i-` для отключения оповещений.\n`Примечание:` все команды можно прописывать **[здесь](https://discord.com/channels/604636579545219072/712638398132650095)**.').set_footer(text='С уважением,\nКоманда Каталога', icon_url=message.guild.icon_url))
                                check2 = 'Доставлено.'
                            except:
                                check2 = 'Не доставлено (лс закрыты).'
                        else:
                            check2 = 'Уведомления идей отключены.'
                        await client.get_channel(cs.i_and_p_logs).send(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x310000, description=f'Оставлен вердикт на **[идею №{num}]({i.jump_url})**.\n`ЛС: {check2}`\n```{txt}```').set_author(name=message.author, icon_url=message.author.avatar_url).set_footer(text=f'ID: {message.author.id}'))

                    embed.add_field(name='<:owner:784812161959854120> Итоговое решение по предложению от владельца сервера Helen22:', value=txt, inline=False)
                    embed.set_footer(text=f'{dm_date1[2]} {cs.sokr_date[int(dm_date1[1])]} {dm_date2[0]}:{dm_date2[1]} GMT+3 | {check2}')
                    await i.edit(embed=embed)
                    break
            except:
                pass

@client.command()
async def rate(message, num=None, mark=None):
    await message.message.delete()
    b = [role.id for role in message.author.roles]
    if message.channel.id == cs.ideas_id and not num is None and not mark is None and (608994688078184478 in b or 816386551222763561 in b or 757890413838467133 in b or message.author.id in admins) and mark in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        for i in await client.get_channel(cs.ideas_id).history(limit=100).flatten():
            try:
                if i.embeds[0].title.split('№')[-1] == num and not '<:owner:784812161959854120>' in i.embeds[0].fields[-1].name:
                    zn = '<:developer:785191301321719828>' if message.author.id in admins else '<:moderator:827468511894700054>' if 677397817966198788 in b else '<:Support:816800431249555498>' if 816386551222763561 in b else '<:kk:788850405157240833>'
                    embed = i.embeds[0]
                    if str(message.author.id) in embed.fields[-1].value:
                        txt = embed.fields[-1].value.split('\n')
                        k = -1
                        for j in txt:
                            k += 1
                            if str(message.author.id) in j:
                                check = f'Оценка `{txt[k].split("— ")[-1]}` заменена на `{mark}` у **[предложения №{num}]({i.jump_url})**.'
                                txt[k] = f'{zn} <@{message.author.id}> — {mark}'
                                txt = '\n'.join(txt)
                                break
                    elif embed.fields[-1].value.count('\n') < 11:
                        if embed.fields[-1].value.count('\n') == 0:
                            txt = f'{zn} <@{message.author.id}> — {mark}'
                        else:
                            txt = f'{zn} <@{message.author.id}> — {mark}\n{embed.fields[-1].value}'
                        check = f'Поставлена оценка `{mark}` **[предложению №{num}]({i.jump_url})**.'
                    if txt.count('\n') < 6:
                        txt = txt.replace('\n**Среднее значение: `пока недоступно`.**\n❗ **Для подсчёта среднего значения необходимо минимум 5 оценок.**', '') + '\n**Среднее значение: `пока недоступно`.**\n❗ **Для подсчёта среднего значения необходимо минимум 5 оценок.**'
                    else:
                        avg = 0; k = 0; txt = '\n'.join(txt.split('\n')[:-2])
                        for j in txt.split('\n'):
                            avg += int(j.split(' ')[-1])
                            k += 1
                        avg /= k
                        if avg < 7.0:
                            txt += f'\n**Среднее значение: `{"%.2f" % avg}`**\n❗ **Для передачи идеи владельцу сервера необходимо минимум `7.0`.**'
                        else:
                            txt += f'\n**Среднее значение: `{"%.2f" % avg}`**\n<:Check_from_Helen22:760820919265656842> **Идея передана владельцу сервера на рассмотрение.**'
                    dm_date1 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[0].split('-')
                    dm_date2 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[1].split('.')[0].split(':')
                    embed.set_footer(text=f'{dm_date1[2]} {cs.sokr_date[int(dm_date1[1])]} {dm_date2[0]}:{dm_date2[1]} GMT+3 | Оценка от {message.author.name}')
                    embed.remove_field(-1)
                    embed.add_field(name='Оценки данной идеи:', value=txt, inline=False)
                    await i.edit(embed=embed)
                    await client.get_channel(cs.i_and_p_logs).send(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x002137, description=check).set_author(name=message.author, icon_url=message.author.avatar_url).set_footer(text=f'ID: {message.author.id}'))
                    break
            except:
                pass

@client.command()
async def problem(message, *, txt=None):
    await message.message.delete()
    if message.channel.id == cs.problems_id:
        if not txt is None:
            if [i for i in my_not.find({'id':message.author.id})] == []:
                my_not.insert_one({'id':message.author.id, 'p':True, 'i':True})
            global problems_key; problems_key += 1
            embed = discord.Embed(title=f'Вопрос №{problems_key}', colour=0x2f3136, description=txt)
            embed.set_author(name=f'{message.author} | {message.author.id}', icon_url=message.author.avatar_url)
            dm_date1 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[0].split('-')
            dm_date2 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[1].split('.')[0].split(':')
            msg = await message.channel.send(embed=embed)
            if my_not.find({'id':message.author.id})[0]['p']:
                try:
                    await message.author.send(embed=discord.Embed(colour=0x310000, timestamp=datetime.datetime.utcnow(), description=f'Благодарим за ваш **[вопрос]({msg.jump_url})**!\nНаш состав Support Team постарается как можно быстрее дать на него свой ответ.\n\nНеправильно сформулировали вопрос? У вас есть возможность его отредактировать до первого оставленного ответа:\n`K.eproblem <номер_оставленного_вопроса> <новый_текст_вопроса>`.\nНапример: `K.eproblem {problems_key} {txt} + печенек админам? :).`\n\nНе желаете получать уведомления в личные сообщения об изменениях статуса вопроса? Используйте `K.notify p-` для отключения оповещений.\n`Примечание:` все команды можно прописывать **[здесь](https://discord.com/channels/604636579545219072/712638398132650095)**.').set_footer(text='С уважением,\nКоманда Каталога', icon_url=message.guild.icon_url))
                    check = 'Доставлено.'
                except:
                    check = 'Не доставлено (лс закрыты).'
            else:
                check = 'Уведомления вопросов отключены.'
            await msg.edit(embed=msg.embeds[0].set_footer(text=f'{dm_date1[2]} {cs.sokr_date[int(dm_date1[1])]} {dm_date2[0]}:{dm_date2[1]} GMT+3 | {check}'))
            await client.get_channel(cs.i_and_p_logs).send(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x2f3136, description=f'Задан новый **[вопрос №{problems_key}]({msg.jump_url})**:\n`ЛС: {check}`\n```{txt}```').set_author(name=message.author, icon_url=message.author.avatar_url).set_footer(text=f'ID: {message.author.id}'))
    else:
        await message.channel.send(embed=discord.Embed(colour=0x310000, description=f'**[Канал для вопросов](https://discord.com/channels/604636579545219072/{cs.problems_id})**'))

@client.command()
async def eproblem(message, num=None, *, txt=None):
    await message.message.delete()
    if message.channel.id == cs.problems_id and not num is None and not txt is None:
        for i in await client.get_channel(cs.problems_id).history(limit=100).flatten():
            try:
                if i.embeds[0].title.split('№')[1] == num and i.embeds[0].author.name.split('| ')[-1] == str(message.author.id) and len(i.embeds[0].fields) == 0:
                    embed = i.embeds[0]
                    before_txt = embed.description if len(embed.description) <= 900 else f'{embed.description[:900]}...'
                    embed.description = txt
                    dm_date1 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[0].split('-')
                    dm_date2 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[1].split('.')[0].split(':')
                    embed.set_footer(text=f'{dm_date1[2]} {cs.sokr_date[int(dm_date1[1])]} {dm_date2[0]}:{dm_date2[1]} GMT+3 | Вопрос отредактирован автором.')
                    await i.edit(embed=embed)
                    txt = txt if len(txt) <= 900 else f'{txt[:900]}...'
                    await client.get_channel(cs.i_and_p_logs).send(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0x4986e3, description=f'Отредактирован **[вопрос №{num}]({i.jump_url})**:\n\n**Старый текст:**\n```{before_txt}```**Новый текст:**\n```{txt}```').set_author(name=message.author, icon_url=message.author.avatar_url).set_footer(text=f'ID: {message.author.id}'))
                    break
            except:
                pass

@client.command()
async def answer(message, num=None, *, txt=None):
    await message.message.delete()
    b = [role.id for role in message.author.roles]
    if message.channel.id == cs.problems_id and not num is None and not txt is None and (816386551222763561 in b or message.author.id in admins):
        for i in await client.get_channel(cs.problems_id).history(limit=100).flatten():
            if str(i.created_at).split()[0] == str(datetime.datetime.utcnow()).split()[0] or message.author.id in admins:
                try:
                    if i.embeds[0].title.split('№')[1] == num:
                        if [i for i in my_not.find({'id':int(i.embeds[0].author.name.split('| ')[-1])})] == []:
                            my_not.insert_one({'id':int(i.embeds[0].author.name.split('| ')[-1]), 'p':True, 'i':True})
                        k = -1
                        for j in i.embeds[0].fields:
                            try:
                                k += 1
                                if j.name.split('| ')[1] == str(message.author.id):
                                    embed = i.embeds[0]
                                    before_txt = i.embeds[0].fields[k].value
                                    embed.colour = discord.Colour.green()
                                    embed.set_field_at(index=k, name=j.name, value=txt, inline=False)
                                    dm_date1 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[0].split('-')
                                    dm_date2 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[1].split('.')[0].split(':')
                                    embed.set_footer(text=f'{dm_date1[2]} {cs.sokr_date[int(dm_date1[1])]} {dm_date2[0]}:{dm_date2[1]} GMT+3 | Отредактирован ответ от {message.author.name}')
                                    await i.edit(embed=embed)
                                    await client.get_channel(cs.i_and_p_logs).send(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=discord.Colour.green(), description=f'Отредактирован ответ на **[вопрос №{num}]({i.jump_url})**:\n\n**Старый текст:**\n```{before_txt}```**Новый текст:**\n```{txt}```').set_author(name=message.author, icon_url=message.author.avatar_url).set_footer(text=f'ID: {message.author.id}'))
                                    break
                            except:
                                pass
                        else:
                            if len(i.embeds[0].fields) < 3 or message.author.id in admins:
                                zn = '<:developer:785191301321719828>' if message.author.id in admins else '<:Support:816800431249555498>'
                                kto = 'администратора' if message.author.id in admins else 'Support Team'
                                kto2 = 'Ответ' if len(i.embeds[0].fields) == 0 else 'Дополнение'
                                embed = i.embeds[0]
                                embed.colour = discord.Colour.green()
                                embed.add_field(name=f'{zn} {kto2} от {kto} {message.author.name} | {message.author.id}', value=txt, inline=False)
                                dm_date1 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[0].split('-')
                                dm_date2 = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split(' ')[1].split('.')[0].split(':')
                                if my_not.find({'id':int(i.embeds[0].author.name.split('| ')[-1])})[0]['p']:
                                    try:
                                        mem = await client.fetch_user(i.embeds[0].author.name.split('| ')[-1])
                                        if kto2 == 'Ответ':
                                            await mem.send(embed=discord.Embed(colour=0x310000, timestamp=datetime.datetime.utcnow(), description=f'Вы получили ответ на свой **[вопрос]({i.jump_url})** от {kto} `{message.author.name}`.\n\nНе желаете получать уведомления в личные сообщения об изменениях статуса идеи? Используйте `K.notify p-` для отключения оповещений.\n`Примечание:` все команды можно прописывать **[здесь](https://discord.com/channels/604636579545219072/712638398132650095)**.').set_footer(text='С уважением,\nКоманда Каталога', icon_url=message.guild.icon_url))
                                            check = 'Ответ доставлен.'
                                        elif kto2 == 'Дополнение':
                                            await mem.send(embed=discord.Embed(colour=0x310000, timestamp=datetime.datetime.utcnow(), description=f'Вы получили дополнительный ответ на свой **[вопрос]({i.jump_url})** от {kto} `{message.author.name}`.\n\nНе желаете получать уведомления в личные сообщения об изменениях статуса идеи? Используйте `K.notify p-` для отключения оповещений.\n`Примечание:` все команды можно прописывать **[здесь](https://discord.com/channels/604636579545219072/712638398132650095)**.').set_footer(text='С уважением,\nКоманда Каталога', icon_url=message.guild.icon_url))
                                            check = 'Дополнение доставлено.'
                                    except:
                                        check = 'Ответ не доставлен (лс закрыты).' if kto2 == 'Ответ' else 'Дополнение не доставлено (лс закрыты).'
                                else:
                                    check = 'Уведомления вопросов отключены.'
                                embed.set_footer(text=f'{dm_date1[2]} {cs.sokr_date[int(dm_date1[1])]} {dm_date2[0]}:{dm_date2[1]} GMT+3 | {check}')
                                await i.edit(embed=embed)
                                if kto2 == 'Ответ':
                                    await client.get_channel(cs.i_and_p_logs).send(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=discord.Colour.green(), description=f'Оставлен ответ на **[вопрос №{num}]({i.jump_url})**:\n```{txt}```').set_author(name=message.author, icon_url=message.author.avatar_url).set_footer(text=f'ID: {message.author.id}'))
                                elif kto2 == 'Дополнение':
                                    await client.get_channel(cs.i_and_p_logs).send(embed=discord.Embed(timestamp=datetime.datetime.utcnow(), colour=discord.Colour.green(), description=f'Оставлено дополнение на **[вопрос №{num}]({i.jump_url})**:\n```{txt}```').set_author(name=message.author, icon_url=message.author.avatar_url).set_footer(text=f'ID: {message.author.id}'))
                                break
                except:
                    pass
                            
@client.command()
async def ticket(message, id=None, arg=None, *, txt=None):
  if message.author.id in admins or 816386551222763561 in [role.id for role in message.author.roles]:
    if id is None and arg is None and txt is None:
        embed = discord.Embed(colour=0x310000, timestamp=datetime.datetime.utcnow(), title='Список доступных аргументов:', description='`-gop` — отправить тикет главе отдела партнёрства.\n`-gm` — отправить тикет главному модератору.\n`-a` — отправить тикет администрации проекта.\n`-h22` — отправить тикет владельцу сервера.')
        embed.set_thumbnail(url=message.guild.icon_url)
        embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    elif id is None:
      await message.channel.send(embed=discord.Embed(colour=0, description='```css\n[Вы не указали пользователя, от которого подаётся запрос.]```'))
    elif arg is None:
      await message.channel.send(embed=discord.Embed(colour=0, description='```css\n[Вы не указали аргумент вышестоящего, к которому подаётся запрос.]```'))
    elif txt is None:
      await message.channel.send(embed=discord.Embed(colour=0, description='```css\n[Вы не указали мотив запроса.]```'))
    elif arg != '-gop' and arg != '-gm' and arg != '-a' and arg != '-h22':
      await message.channel.send(embed=discord.Embed(colour=0, description='```css\n[Введённого аргумента не существует.]```'))
    else:
      try:
        id = int(id.replace("!", "").replace("@","").replace("<","").replace(">",""))
        member = await client.fetch_user(id)
        arg = '<@&686639786672652363>' if arg == '-gop' else '<@&800474182474268734>' if arg == '-gm' else '<@&620955813850120192>' if arg == '-a' else '<@&620955813850120192> <@414119169504575509>'
        embed = discord.Embed(colour=0x70392f, description=f'```md\n#Мотив запроса:```{txt}')
        embed.add_field(name='```Статус тикета:```', value='❗ Не начинал рассматриваться.', inline=False)
        embed.set_author(name=f'Тикет от {message.author} | {message.author.id}', icon_url=message.author.avatar_url)
        global ticket_key; ticket_key += 1
        await client.get_channel(816385807958802522).send(content=f'{arg}|{ticket_key}\n**От пользователя:** {member.mention} | `{member.id}` | {member}', embed=embed)
        await message.channel.send(embed=discord.Embed(colour=0, description=f'Тикет успешно создан и передан на рассмотрение {arg}'))        
      except:
        await message.channel.send(embed=discord.Embed(colour=0, description='```css\n[Указанного пользователя не существует, либо запрос слишком велик.]```'))

@client.command()
async def tanswer(message, num=None, *, txt=None):
  await message.message.delete()
  b = [role.id for role in message.author.roles]
  if message.author.id in admins or 686639786672652363 in b or 800474182474268734 in b:
    if num is None:
      await message.channel.send(embed=discord.Embed(colour=0, description='```css\n[Вы не указали номер тикета.]```'))
    elif txt is None:
      await message.channel.send(embed=discord.Embed(colour=0, description='```css\n[Вы не указали ответ на тикет.]```'))
    else:
      for i in await client.get_channel(816385807958802522).history(limit=100).flatten():
        try:
          if int(i.content.split('\n')[0].split('|')[1]) == int(num) and (i.raw_role_mentions[0] in b or message.author.id in admins):
            if txt.split()[-1] == '-s':
              member = await client.fetch_user(int(i.content.split('`')[1]))
              try:
                msg = await member.send(embed=i.embeds[0])
                key_send_ticket = '<:Check_from_Helen22:760820919265656842>'
              except:
                key_send_ticket = ':x:'
            else:
              key_send_ticket = '—'
            e = i.embeds[0]
            e.clear_fields()
            if txt.split()[0] == '-ok':
              e.color = 0x234a36
              foot_text = '✔️ Тикет закрыт'
              e.add_field(name='```Статус тикета:```', value='\✔️ Рассмотрен.', inline=False)
            else:
              e.color = 0xffff01
              foot_text = '🕒 На рассмотрении от'
              e.add_field(name='```Статус тикета:```', value='\🕒 На рассмотрении.', inline=False)
            e.add_field(name=f'`Ответ от {message.author} | {message.author.id}:` {key_send_ticket}', value=txt.replace('-s', '').replace('-ok',''))
            sp = ['key', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
            a = str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split()[0].split('-')
            e.set_footer(text=f'{foot_text} {a[2]} {sp[int(a[1])]} {a[0]} года в {str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)).split()[1].split(".")[0]}', icon_url=message.author.avatar_url)
            await i.edit(embed=e)
            await msg.edit(embed=e)
            break
        except:
          pass

@client.command()
async def active(message, id=None, arg=None, *, reason=None):
    b = [role.id for role in message.author.roles]
    if message.author.id in admins or 816386551222763561 in b or 765212719380037663 in b or 677397817966198788 in b or 800474182474268734 in b:
        global active_kd
        if time.time()-active_kd >= 300:
            if id is None:
                await message.channel.send(embed=discord.Embed(description='```diff\n- Вы не указали пользователя.```'))
            elif arg is None:
                await message.channel.send(embed=discord.Embed(description='```diff\n- Вы не указали аргумент (+/-).```'))
            elif arg != '+' and arg != '-':
                await message.channel.send(embed=discord.Embed(description='```diff\n- Аргументом может выступать только + или -.```'))
            elif reason is None:
                await message.channel.send(embed=discord.Embed(description='```diff\n- Вы не указали причину.```'))
            else:
                try:
                    member = message.guild.get_member(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
                    if arg == '-' and not 619013112531517501 in [role.id for role in member.roles]:
                        await message.message.add_reaction('❌')
                    else:
                        if arg == '+':
                            await member.add_roles(message.guild.get_role(619013112531517501), reason=f'{message.author.name}: {reason}')
                        else:
                            await member.remove_roles(message.guild.get_role(619013112531517501), reason=f'{message.author.name}: {reason}')
                        await message.message.add_reaction('<:Check_from_Helen22:760820919265656842>')
                        active_kd = time.time()
                except:
                    await message.channel.send(embed=discord.Embed(description='```diff\n- Пользователя не существует.```'))
        else:
            otkat = f'Минут до отката команды: ~{int((300-(time.time()-active_kd))//60)}' if (300-(time.time()-active_kd))//60 != 0 else f'Секунд до отката команды: ~{int(300-(time.time()-active_kd))}'
            await message.channel.send(embed=discord.Embed(colour=0x310000,description=f'```css\n[Данная команда имеет общую задержку в 5 минут.]```\n```md\n#{otkat}```'))

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
async def Email(message, arg=None, komy=None):
  await message.message.delete()
  if message.author.id in admins or message.author.id == 735540766289690646:
    if arg is None:
      await message.channel.send('```css\n[Вы не указали аргумент отправки.]```')
    elif komy is None:
      await message.channel.send('```css\n[Вы не указали получателя.]```')
    elif arg == 'pms':        
      aktiv = requests.get(f'https://api.catalogserverov.ml/v1/stats/pm/all').text.split('{')[-1].split('}')[0].replace('"','').split(',')
      s, k = 'Доброго времени суток.<br><br>Актуальная информация касательно статистики отдела партнёрства находится ниже.<br><br>Статистика отдела партнёрства за последние 2 дня с момента отчёта:<br>', 1
      for i in aktiv:
        s += f"{k}. {await client.fetch_user(int(i.split(':')[0]))} [{i.split(':')[0]}] — {i.split(':')[1]}<br>"
        k += 1
      s += '<br>Примечание: в данном списке пропущены все пиар-менеджеры, количество партнёрств которых не превышает 0.<br><br>С уважением,<br>Support Team Каталог Серверов.'
      Theme = f'Partnership Department Statistics {str(datetime.datetime.utcnow()+datetime.timedelta(hours=3)).split()[1].split(".")[0]}'
    elif arg == 'unban':
      s = 'Доброго времени суток.<br><br>Мы получили запрос на обжалование Вашей блокировки на сервере Каталог Серверов.<br><br>Наша уполномоченная команда свяжется с Вами сразу же после того, как проверит всю предоставленную информацию и подтвердит факт выданной блокировки, если таковая присутствует.<br><br>Благодарим Вас за вынужденные ожидания.<br><br>С уважением,<br>Support Team Каталог Серверов.'
      Theme = f'Обжалование блокировки {str(datetime.datetime.utcnow()+datetime.timedelta(hours=3)).split()[1].split(".")[0]}'
    elif arg == 'design':
      s = 'Доброго времени суток.<br><br>Мы получили запрос на Ваше вступление в команду дизайнеров проекта Каталог Серверов.<br><br>Наша уполномоченная команда свяжется с Вами сразу же после того, как ознакомится с предоставленной информацией и проведёт оценку Ваших прикреплённых работ.<br><br>Благодарим Вас за вынужденные ожидания.<br><br>С уважением,<br>Support Team Каталог Серверов.'
      Theme = f'Заявка на дизайнера {str(datetime.datetime.utcnow()+datetime.timedelta(hours=3)).split()[1].split(".")[0]}'
    email_content = """
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
     <head> 
      <meta charset="UTF-8"> 
      <meta content="width=device-width, initial-scale=1" name="viewport"> 
      <meta name="x-apple-disable-message-reformatting"> 
      <meta http-equiv="X-UA-Compatible" content="IE=edge"> 
      <meta content="telephone=no" name="format-detection"> 
      <title>Новый шаблон</title> 
      <!--[if (mso 16)]>
        <style type="text/css">
        a {text-decoration: none;}
        </style>
        <![endif]--> 
      <!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]--> 
      <!--[if gte mso 9]>
    <xml>
        <o:OfficeDocumentSettings>
        <o:AllowPNG></o:AllowPNG>
        <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
    </xml>
    <![endif]--> 
      <style type="text/css">
    #outlook a {
      padding:0;
    }
    .es-button {
      mso-style-priority:100!important;
      text-decoration:none!important;
    }
    a[x-apple-data-detectors] {
      color:inherit!important;
      text-decoration:none!important;
      font-size:inherit!important;
      font-family:inherit!important;
      font-weight:inherit!important;
      line-height:inherit!important;
    }
    .es-desk-hidden {
      display:none;
      float:left;
      overflow:hidden;
      width:0;
      max-height:0;
      line-height:0;
      mso-hide:all;
    }
    @media only screen and (max-width:600px) {p, ul li, ol li, a { font-size:16px!important; line-height:150%!important } h1 { font-size:30px!important; text-align:center; line-height:120%!important } h2 { font-size:26px!important; text-align:center; line-height:120%!important } h3 { font-size:20px!important; text-align:center; line-height:120%!important } h1 a { font-size:30px!important } h2 a { font-size:26px!important } h3 a { font-size:20px!important } .es-menu td a { font-size:16px!important } .es-header-body p, .es-header-body ul li, .es-header-body ol li, .es-header-body a { font-size:16px!important } .es-footer-body p, .es-footer-body ul li, .es-footer-body ol li, .es-footer-body a { font-size:16px!important } .es-infoblock p, .es-infoblock ul li, .es-infoblock ol li, .es-infoblock a { font-size:12px!important } *[class="gmail-fix"] { display:none!important } .es-m-txt-c, .es-m-txt-c h1, .es-m-txt-c h2, .es-m-txt-c h3 { text-align:center!important } .es-m-txt-r, .es-m-txt-r h1, .es-m-txt-r h2, .es-m-txt-r h3 { text-align:right!important } .es-m-txt-l, .es-m-txt-l h1, .es-m-txt-l h2, .es-m-txt-l h3 { text-align:left!important } .es-m-txt-r img, .es-m-txt-c img, .es-m-txt-l img { display:inline!important } .es-button-border { display:block!important } .es-adaptive table, .es-left, .es-right { width:100%!important } .es-content table, .es-header table, .es-footer table, .es-content, .es-footer, .es-header { width:100%!important; max-width:600px!important } .es-adapt-td { display:block!important; width:100%!important } .adapt-img { width:100%!important; height:auto!important } .es-m-p0 { padding:0px!important } .es-m-p0r { padding-right:0px!important } .es-m-p0l { padding-left:0px!important } .es-m-p0t { padding-top:0px!important } .es-m-p0b { padding-bottom:0!important } .es-m-p20b { padding-bottom:20px!important } .es-mobile-hidden, .es-hidden { display:none!important } tr.es-desk-hidden, td.es-desk-hidden, table.es-desk-hidden { width:auto!important; overflow:visible!important; float:none!important; max-height:inherit!important; line-height:inherit!important } tr.es-desk-hidden { display:table-row!important } table.es-desk-hidden { display:table!important } td.es-desk-menu-hidden { display:table-cell!important } .es-menu td { width:1%!important } table.es-table-not-adapt, .esd-block-html table { width:auto!important } table.es-social { display:inline-block!important } table.es-social td { display:inline-block!important } a.es-button, button.es-button { font-size:20px!important; display:block!important; border-width:10px 0px 10px 0px!important } }
    </style> 
     </head> 
     <body style="width:100%;font-family:arial, 'helvetica neue', helvetica, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0"> 
      <div class="es-wrapper-color" style="background-color:#F6F6F6"> 
       <!--[if gte mso 9]>
          <v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
            <v:fill type="tile" color="#f6f6f6"></v:fill>
          </v:background>
        <![endif]--> 
       <table cellpadding="0" cellspacing="0" class="es-wrapper" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top"> 
         <tr> 
          <td valign="top" style="padding:0;Margin:0"> 
           <table cellpadding="0" cellspacing="0" class="es-content" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%"> 
             <tr> 
              <td align="center" style="padding:0;Margin:0"> 
               <table class="es-content-body" align="center" cellpadding="0" cellspacing="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;width:600px"> 
                 <tr> 
                  <td align="left" style="Margin:0;padding-top:20px;padding-bottom:20px;padding-left:20px;padding-right:20px"> 
                   <!--[if mso]><table style="width:560px" cellpadding="0" cellspacing="0"><tr><td style="width:356px" valign="top"><![endif]--> 
                   <table cellpadding="0" cellspacing="0" class="es-left" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left"> 
                     <tr> 
                      <td class="es-m-p0r es-m-p20b" valign="top" align="center" style="padding:0;Margin:0;width:356px"> 
                       <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                         <tr> 
                          <td align="center" style="padding:0;Margin:0;display:none"></td> 
                         </tr> 
                       </table></td> 
                     </tr> 
                   </table> 
                   <!--[if mso]></td><td style="width:20px"></td><td style="width:184px" valign="top"><![endif]--> 
                   <table cellpadding="0" cellspacing="0" align="right" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                     <tr> 
                      <td align="left" style="padding:0;Margin:0;width:184px"> 
                       <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                         <tr> 
                          <td align="center" style="padding:0;Margin:0;display:none"></td> 
                         </tr> 
                       </table></td> 
                     </tr> 
                   </table> 
                   <!--[if mso]></td></tr></table><![endif]--></td> 
                 </tr> 
               </table></td> 
             </tr> 
           </table> 
           <table cellpadding="0" cellspacing="0" class="es-content" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%"> 
             <tr> 
              <td align="center" style="padding:0;Margin:0"> 
               <table bgcolor="#ffffff" class="es-content-body" align="center" cellpadding="0" cellspacing="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;width:600px"> 
                 <tr> 
                  <td align="left" style="Margin:0;padding-top:20px;padding-bottom:20px;padding-left:20px;padding-right:20px"> 
                   <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                     <tr> 
                      <td align="center" valign="top" style="padding:0;Margin:0;width:560px"> 
                       <table cellpadding="0" cellspacing="0" width="100%" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                         <tr> 
                          <td align="center" style="padding:0;Margin:0;font-size:0px"><a href="https://discord.gg/nKPdC9V"><img class="adapt-img" src="https://media.discordapp.net/attachments/767656142285176843/817651448875057182/172_20210204223139.png" alt style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic" width="560"></td> 
                         </tr> 
                         <tr>
                          <td align="center" style="padding:0;Margin:0"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:14px;font-family:verdana, geneva, sans-serif;line-height:21px;color:#333333;text-align:left">"""+s+"""</p></td> 
                         </tr> 
                       </table></td> 
                     </tr> 
                   </table></td> 
                 </tr> 
               </table></td> 
             </tr> 
           </table> 
           <table cellpadding="0" cellspacing="0" class="es-footer" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;background-color:transparent;background-repeat:repeat;background-position:center top"> 
             <tr> 
              <td align="center" style="padding:0;Margin:0"> 
               <table class="es-footer-body" align="center" cellpadding="0" cellspacing="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;width:600px"> 
                 <tr> 
                  <td align="left" style="Margin:0;padding-top:20px;padding-bottom:20px;padding-left:20px;padding-right:20px"> 
                   <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                     <tr> 
                      <td align="center" valign="top" style="padding:0;Margin:0;width:560px"> 
                       <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                         <tr> 
                          <td align="center" style="padding:0;Margin:0;display:none"></td> 
                         </tr> 
                       </table></td> 
                     </tr> 
                   </table></td> 
                 </tr> 
               </table></td> 
             </tr> 
           </table> 
           <table cellpadding="0" cellspacing="0" class="es-content" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%"> 
             <tr> 
              <td align="center" style="padding:0;Margin:0"> 
               <table class="es-content-body" align="center" cellpadding="0" cellspacing="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;width:600px"> 
                 <tr> 
                  <td align="left" style="padding:0;Margin:0;padding-left:20px;padding-right:20px;padding-bottom:30px"> 
                   <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                     <tr> 
                      <td align="center" valign="top" style="padding:0;Margin:0;width:560px"> 
                       <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                         <tr> 
                          <td align="center" style="padding:0;Margin:0;display:none"></td> 
                         </tr> 
                       </table></td> 
                     </tr> 
                   </table></td> 
                 </tr> 
               </table></td> 
             </tr> 
           </table></td> 
         </tr> 
       </table> 
      </div>  
     </body>
    </html>
    """
    msg = email.message.Message()
    msg['Subject'] = Theme

    msg['From'] = 'catalogserverov@gmail.com'
    msg['To'] = komy
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)

    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    
    await message.channel.send(f'```md\n#Сообщение аргумента {arg} было отправлено на почтовый адрес {"*"*(len(komy)//4)}{komy[len(komy)//4-1::]}.```')

@client.command()
async def reload(message):
    if message.author.id in admins:
        #for cards_badges
        global msgbots; global bag; global medal22; global medal_chat_users; global souz; global help; global rm22; global ngl; global att; global ideas; global bang; global msgotz; global candys; global heart; global msgs; global feedback
        msgbots = await client.get_channel(764191031318937674).fetch_message(785189856988627004); msgbots = msgbots.content
        bag = await client.get_channel(764191031318937674).fetch_message(807351505455022160); bag = bag.content
        medal22 = await client.get_channel(764191031318937674).fetch_message(788848844980092989); medal22 = medal22.content
        medal_chat_users = await client.get_channel(764191031318937674).fetch_message(817427831460986891); medal_chat_users = medal_chat_users.content
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
        feedback = await client.get_channel(764191031318937674).fetch_message(827263853184286740); feedback = feedback.content
        await message.channel.send('Reload Complete.')
                               
@client.command()
async def badges(message):
    embeds = [discord.Embed(colour=0x310000,timestamp=datetime.datetime.utcnow(),title=':clipboard: Обозначение значков', description='**Значки Staff:**\n<:owner:784812161959854120> Владельцу сервера.\n<:developer:785191301321719828> Людям, принявшим участие в разработке/улучшении персонального бота.\n<:moderator:827468511894700054> Модераторам проекта.\n<:Support:816800431249555498> Представителям Support Team.\n<:rm:827468511956959232> Лучшему работнику на данный момент.').set_thumbnail(url=message.guild.icon_url)]
    embeds.append(discord.Embed(colour=0x310000,timestamp=datetime.datetime.utcnow(),title=':clipboard: Обозначение значков', description='**Пользовательские значки:**\n<:KC_bug_hunter:807347751641022486> Людям, нашедшим баги в боте <@656029229749764126> с последующим информированием разработчика через команду `K.bug`.\n`Примечание:` имея данный значок, открывается возможность быть приглашённым на закрытое BETA-тестирование нововведений бота. При замечании определённого бага несколькими пользователями, только первый получит значок.\n<:medal:814131867397783562> Людям, которые внесли огромный вклад в развитие сервера.\n<:medal_chat:817408266635444315> Людям, которые значительно повышают активность в голосовых и текстовых каналах посредством поднятия определённых тем, интереса положением дел других людей\n<:secret:827256596824195108> За заполнение **[формы обратной связи](https://forms.gle/9nQ9FSS733sYKWNi9)**.\n<:alliance:807310319852585051> Представителям союза каталога.\n<:glitch:822792011382784010> За нахождение глитч-карточки [Получить уже невозможно].\n<:Attentive:827475137518501888> Нашли определённые несостыковки в информационных сообщениях? Сообщите администрации проекта и получите значок за внимательность.\n`Примечание:` значок распространяется на пользователей, что нашли определённые несостыковки в конкретном случае первыми.\n<:ideas:824422636033409064> Предложившим большое количество дельных идей.\n<:complaints:827468511659556885> Подавшему большое количество жалоб.\n<:review:822792011391303680> Оставившему рецензию серверу на 3-х мониторингах.\n`Примечание:` **[здесь](https://server-discord.com/604636579545219072)**, **[здесь](https://disboard.org/ru/server/604636579545219072)** и **[здесь](https://discord-server.com/ru/604636579545219072)**.').set_thumbnail(url=message.guild.icon_url))
    embeds.append(discord.Embed(colour=0x310000,timestamp=datetime.datetime.utcnow(),title=':clipboard: Обозначение значков', description='**Значки-метки:**\n<:booster:797134090594680942> Бустерам сервера.\n<:p1:811016319607504936> Партнёру 1-го уровня.\n<:p2:811016319234605107> Партнёру 2-го уровня.\n<:p3:811016319716950046> Партнёру 3-го уровня.\n<:pmax:811016319238406175> Партнёру уровня MAX.').set_thumbnail(url=message.guild.icon_url))
    embeds.append(discord.Embed(colour=0x310000,timestamp=datetime.datetime.utcnow(),title=':clipboard: Обозначение значков', description='**Значки ивентов:**\n🍬 Выдаётся в новогоднюю ночь 2021 года за найденные пасхалки. Существует до 2022 года.\n❤️ Победителю ивента на день влюблённых. Существует до конца мая 2021 года.').set_thumbnail(url=message.guild.icon_url))
    embeds.append(discord.Embed(colour=0x310000,timestamp=datetime.datetime.utcnow(),title=':clipboard: Обозначение значков', description='**Примечания:**\n• Значков всего без учёта кастомных: `22`.\n• Кастомный значок возможен в случае больших заслуг перед Каталогом, а так же за 2 ваших буста.\n• Значки выдаются автоматизированной системой. Это значит, что нет необходимости выпрашивать их у администрации сервера.').set_thumbnail(url=message.guild.icon_url))
    msg = await message.channel.send(embed=embeds[0])
    page = Paginator(client, msg, timeout=3600, use_exit=True, delete_message=False, reactions=['<:back:820233427411927071>', '<:go:820233452522569732>'], only=message.author, use_more=False, exit_reaction=['<:stop:820233391726133279>'], embeds=embeds)
    await page.start()

@client.command()
async def info(message, id = None):
    if id is None or id == '-':
      id = str(message.author.id)
    sp = ['key', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    color = (255, 255, 255)
    try:
        async with message.typing():
          member = client.get_guild(604636579545219072).get_member(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
          mid = member.id

          avatar = requests.get(member.avatar_url, stream = True)
          avatar = Image.open(io.BytesIO(avatar.content))
          avatar = avatar.convert('RGBA')

          aktiv = requests.get(f'https://api.catalogserverov.ml/v1/stats?user={mid}').text

          b = [role.id for role in member.roles]
          if message.author.id == 394757049893912577 and 'png' in message.message.content:
            response = requests.get('https://media.discordapp.net/attachments/689800301468713106/820008119286759465/file.png', stream = True)
          else:
            if cards.get(mid):
              response = requests.get(cards.get(mid), stream = True)
            else:
              if 608994688078184478 in b:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/802581229613350942/test.png', stream = True)
              elif not member.premium_since is None:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/797145563191705630/booster.png', stream = True)
              elif 769916590686732319 in b:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/797134819993190430/partner_max.png', stream = True)
              elif 622501691107049502 in b:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/797134824123924546/partner3.png', stream = True)
              elif 622501656591990784 in b:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/817998355081723914/gold_redesign.png', stream = True)
              elif 688654966675603491 in b:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/797092901150392350/partner1.png', stream = True)
              else:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/819962677055979520/catalog_card1_test.png', stream = True)
          response = Image.open(io.BytesIO(response.content))
          idraw = ImageDraw.Draw(response)
          if 608994688078184478 in b and list(message.message.content)[-1] != '-':
            dol, otd = 'Не указана', 'Отдел не указан'
            if 608600358570295307 in b:
              dol = 'Пиар-менеджер'
              otd = 'Отдел партнерства'
            elif 800474182474268734 in b:
              dol = 'Главный Модератор'
              otd = 'Административный отдел'
            elif 686618397668147220 in b:
              dol = 'Дизайнер'
              otd = 'Отдел творчества'
            elif mid == 414119169504575509:
              dol = 'Developer'
              otd = 'Административный отдел'
            elif mid == 529044574660853761:
              dol = 'Технический Администратор'
              otd = 'Административный отдел'
            elif mid == 562561140786331650:
              dol = 'Руководящий Администратор'
              otd = 'Административный отдел'
            elif 686639786672652363 in b:
              dol = 'Глава отдела партнерства'
              otd = 'Отдел партнерства'
            idraw.text((365, 400), f'{otd}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
            idraw.text((365, 440), f'Должность: {dol}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))

            if str(mid) in msgs:
              for i in msgs.split('\n'):
                a = i.split('|')
                if a[0] == str(mid):
                  idraw.text((365, 480), f'В команде с {a[1]}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
                  break

            idraw.text((145 , 430), f'Выговоров: {len([i for i in my_warn_md.find({"id":mid})])}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))

          else:
            if 769916590686732319 in b or 622501691107049502 in b or 622501656591990784 in b or 688654966675603491 in b:
              if d.get(mid) is not None:
                datet = d.get(mid).split('.')[0].split()[0].split('-')
                datet2 = d.get(mid).split('.')[0].split()[1]
                idraw.text((55, 515), f'Последнее обновление: {datet[2]} {sp[int(datet[1])]} {datet[0]} года в {datet2}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
              else:
                idraw.text((55, 515), f'Последнее обновление: неизвестно', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
              kolvo = dk.get(mid) if dk.get(mid) is not None else 0
              idraw.text((135, 430), f'Публикаций: {kolvo}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
            try:
              idraw.text((365, 400), f'Активность сегодня: {aktiv.split("|")[0]}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
              idraw.text((365, 440), f'Voice сегодня: {aktiv.split("|")[1]}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
            except:
              idraw.text((365, 400), f'Активность сегодня: ?', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
              idraw.text((365, 440), f'Voice сегодня: ?', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))

          avatar = avatar.resize((212, 212), Image.ANTIALIAS)
          response.paste(avatar, (118, 169))
          idraw.text((400, 150), unicodedata.normalize('NFKD', str(member)).encode('utf-8', 'ignore').decode('utf-8'), color, font = ImageFont.truetype(r'./Gothic.ttf', size = 35))
          try:
            idraw.text((365, 260), f'{aktiv.split("|")[2]}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
          except:
            idraw.text((365, 260), 'В сети: ?', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
          a = str(member.created_at).split()[0].split('-')
          idraw.text((365 , 300), f'Дата создания: {a[2]} {sp[int(a[1])]} {a[0]} года', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
          a2 = str(member.joined_at).split()[0].split('-')
          idraw.text((365, 340), f'Дата вступления: {a2[2]} {sp[int(a2[1])]} {a2[0]} года', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
          idraw.text((165 , 400), f'Варнов: {len([i for i in my_warn.find({"id":mid})])}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))

          mst = str(member.status)
          if statuts.get(mst):
            st = Image.open(io.BytesIO(requests.get(statuts.get(mst), stream = True).content)).convert('RGBA')
            response.paste(st, (360, 155), st)
          else:
            st = Image.open(io.BytesIO(requests.get(statuts.get(member.is_on_mobile()).get(mst), stream = True).content)).convert('RGBA')
            response.paste(st, (360, statuts.get(member.is_on_mobile()).get('y')), st)

          #prioritetnostb
          zns, prioritet = [], -1
          ppz = [365, 405, 445, 485, 525, 565, 605, 645, 685, 725, 765, 805, 845, 885, 925, 965, 1005]
          if mid == message.guild.owner.id:
            zns.append(crown)
          if str(mid) in msgbots:
            zns.append(dev)
          if str(mid) in bag:
            zns.append(bag22)
          if str(mid) in medal22:
            zns.append(medal)
          if str(mid) in medal_chat_users:
            zns.append(medal_chat)
          if str(mid) in feedback:
            zns.append(feedback22)
          if str(mid) in souz:
            zns.append(allia)
          if 677397817966198788 in b:
            zns.append(moder22)
          if 816386551222763561 in b:
            zns.append(support)
          if str(mid) in rm22:
            zns.append(rm)
          if str(mid) in ngl:
            zns.append(ngl2)
          if str(mid) in att:
            zns.append(att22)
          if str(mid) in ideas:
            zns.append(id22)
          if str(mid) in bang:
            zns.append(bg22)
          if str(mid) in msgotz:
            zns.append(cotz)
          if 688654966675603491 in b or 622501656591990784 in b or 622501691107049502 in b or 769916590686732319 in b:
            if 688654966675603491 in b:
              znpart = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/811015500712509490/6.png', stream = True).content)).convert('RGBA')
            elif 622501656591990784 in b:
              znpart = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/811015502381187092/34.png', stream = True).content)).convert('RGBA')
            elif 622501691107049502 in b:
              znpart = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/811015503648784424/41.png', stream = True).content)).convert('RGBA')
            elif 769916590686732319 in b:
              znpart = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/811015504348708914/52.png', stream = True).content)).convert('RGBA')
            zns.append(znpart)
          if str(mid) in candys:
            zns.append(candy)
          if str(mid) in heart:
            zns.append(heart22)
          if zns == []:
            idraw.text((365 , 200), f'Значки отсутствуют ;(', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
          else:
            for i in zns:
              prioritet += 1
              response.paste(i, (ppz[prioritet], 205), i)

          if kastom_zn.get(mid):
            response.paste(kastom_zn.get(mid), (54, 100), kastom_zn.get(mid))
          elif not member.premium_since is None:
            boost = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/797122464026198066/rm.png', stream = True).content)).convert('RGBA')
            response.paste(boost, (54, 100), boost)
          if not member.premium_since is None or message.author.id == 602043590398705665:
            idraw.text((100 , 102), f'{member.top_role.name}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))

          response.save('user_card.png')
          await message.channel.send(file = discord.File(fp = 'user_card.png'))
    except:
        try:
            member = await client.fetch_user(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
            avatar = requests.get(member.avatar_url, stream = True)
            avatar = Image.open(io.BytesIO(avatar.content))
            avatar = avatar.convert('RGBA')
            response = requests.get('https://media.discordapp.net/attachments/689800301468713106/819962677055979520/catalog_card1_test.png', stream = True)
            response = Image.open(io.BytesIO(response.content))
            idraw = ImageDraw.Draw(response)
            avatar = avatar.resize((212, 212), Image.ANTIALIAS)
            response.paste(avatar, (119, 171, 331, 383))
            a = str(member.created_at).split()[0].split('-')
            idraw.text((365, 150), unicodedata.normalize('NFKD', str(member)).encode('utf-8', 'ignore').decode('utf-8'), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 35))
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

            response.save('user_card.png')
            await message.channel.send(file = discord.File(fp = 'user_card.png'))
        except:
            await message.channel.send('```css\nПользователя не существует.```')

client.run(tt)

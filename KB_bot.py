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

client = commands.Bot(command_prefix = "K.", intents = discord.Intents.all())
client.remove_command("help")

admins = [562561140786331650,414119169504575509,529044574660853761]

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.dnd,activity=discord.Game(f"K.help | #stayhome :3 | {len(client.get_guild(604636579545219072).members)}"))
  msg = await client.get_channel(742757799645413378).history(limit=200).flatten()
  b = []
  for i in msg:
      a = i.content.split('https://discord.gg')
      b.append('https://discord.gg' + a[-1])
  await client.get_channel(690827050033872937).purge(limit=10)
  await client.get_channel(690827050033872937).send('https://discord.gg/nKPdC9V')
  global d
  global dk
  a = client.get_guild(604636579545219072).categories
  idd = [747813531495301161, 642102626070036500, 747807222247063642, 642085815597400065, 642104779270782986]
  c, k, d, dk = [], [], {}, {}
  for i in a:
    if i.id in idd:
      for j in i.text_channels:
        if j.id != 764911620111204383:
          c = await j.history(limit=None).flatten()
          for kk in c:
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
  await client.get_channel(728932829026844672).send('Данные обновлены, бот перезапущен.')
    
@client.event
async def on_message(message):
  if message.channel.id == 740651083533254717:
    if "K.problem" != message.content.split()[0] and message.author.id != 656029229749764126 and not message.author.id in admins:
      await message.delete()
      embed = discord.Embed(timestamp=datetime.datetime.utcnow(),colour=discord.Colour(0x310000),description=f'Ваше сообщение в канале <#740651083533254717> следующего содержания: `{message.content}` было удалено по причине оффтопа.\nПросьба ознакомиться с **[закреплённым информационным сообщением](https://discord.com/channels/604636579545219072/740651083533254717/744485922258681896).**')
      embed.set_footer(text='С уважением, Команда Каталога!',icon_url=message.guild.icon_url)
      await message.author.send(embed=embed)
  if message.channel.id == 678666229661171724:
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
  idd = [747813531495301161, 642102626070036500, 747807222247063642, 642085815597400065, 642104779270782986]
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
    embed=discord.Embed(colour=discord.Colour(0x310000),title='Меню Каталог Серверов', description=f"**Страница 1. Команды для всех пользователей:**\n\n`K.help` — помощь.\n`K.avatar @user|ID` — аватар пользователя.\n`K.suggest текст` — предложить свою идею.\n`K.info @user|ID` — информация о пользователе.\n`K.server` — информация о сервере.\n`K.stats` — статистика сервера.\n`K.team` — состав Команды сервера.\n`K.problem` — задать вопрос администрации сервера.\n\n[Случайный партнёр]({msg[random.randint(0,len(msg)-1)]})",timestamp=datetime.datetime.utcnow())
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    embed.set_thumbnail(url=message.guild.icon_url)
    
    embed2=discord.Embed(colour=discord.Colour(0x310000),title='Меню Каталог Серверов', description=f"**Страница 2. Команды для состава:**\n\n`K.developer` — административные команды.\n`K.moder` — команды для модераторов.\n`K.op` — команды для главы отдела партнёрства.\n`K.pm` — команды для пиар-менеджера.\n\n[Случайный партнёр]({msg[random.randint(0,len(msg)-1)]})",timestamp=datetime.datetime.utcnow())
    embed2.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    embed2.set_thumbnail(url=message.guild.icon_url)
    
    embeds = [embed,embed2]
    msg = await message.channel.send(embed=embeds[0])
    page = Paginator(client, msg, only=message.author, use_more=False, embeds=embeds)
    await page.start()
    
@client.command()
async def op(message):
  if 686639786672652363 in [role.id for role in message.author.roles] or message.author.id in admins:
    embed=discord.Embed(colour=discord.Colour(0x310000),timestamp=datetime.datetime.utcnow(),description="**Команды для <@&686639786672652363>:**\n\n`K.modstats date1 date2` — показать статистику отдела партнёрства с date1 по date2.\n`K.apm @user|+/-` — выдать или забрать роли пиар-менеджера соответственно.\n`K.removebl <№случая>` — исключить сервер из чёрного списка по номеру случая.")
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    embed.set_thumbnail(url=message.guild.icon_url)
    await message.channel.send(embed=embed)
    
@client.command()
async def pm(message):
  if 608600358570295307 in [role.id for role in message.author.roles] or message.author.id in admins:
    embed=discord.Embed(colour=discord.Colour(0x310000),timestamp=datetime.datetime.utcnow(),description="**Команды для <@&608600358570295307>:**\n\n`K.addbl <URL> <причина>` — добавить сервер в чёрный список. Вложение обязательно!\n`K.bl` — просмотреть чёрный список серверов каталога.\n`K.np @user|ID` — выдать пользователю роль партнёра первого уровня.")
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    embed.set_thumbnail(url=message.guild.icon_url)
    await message.channel.send(embed=embed)
    
@client.command()
async def ban(message, id=None, *, reason=None):
    await message.message.delete()
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
    await message.message.delete()
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
    embed.add_field(name=len(gg.get_role(604645403664711680).members),value="<@&604645403664711680>")
    embed.add_field(name=len(gg.get_role(658154672237838347).members),value="<@&658154672237838347>")
    
    msg = await client.get_channel(690827050033872937).history(limit=20).flatten()
    msg = msg[0].content.replace("[","").replace("]","").replace("'","").split(', ')
    embed.add_field(name="Случайный партнёр",value="[Ссылка на сервер](" + msg[random.randint(0,len(msg)-1)]+")")

    await message.channel.send(embed=embed)
          
@client.command()
async def team(message):
    embed = discord.Embed(colour=discord.Colour(0x310000),title="Команда Каталога",description=f"Людей в команде: `{len([i.mention for i in message.guild.get_role(608994688078184478).members])}`",timestamp=datetime.datetime.utcnow())
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    d = [i.mention for i in message.guild.get_role(620955813850120192).members]
    embed.add_field(name=f"Администраторы: [{len(d)}]",value="<:crown:763415131622998046> <@414119169504575509>\n:crossed_swords: <@562561140786331650>\n<:PandeMiaa:775425060130652242> <@529044574660853761>")
    e = [i.mention for i in message.guild.get_role(686256550951649317).members]
    embed.add_field(name=f"Рекрутеры: [{len(e)}]",value=("\n".join(e)))
    f = [i.mention for i in message.guild.get_role(677397817966198788).members]
    embed.add_field(name=f"Модераторы: [{len(f)}]",value=("\n".join(f)))
    
    gp = [i.mention for i in message.guild.get_role(686639786672652363).members]
    gp = 'Отсутствует.' if gp==[] else ':crown: ' + "\n".join(gp)
    embed.add_field(name=f"Глава отдела партнерства:",value=gp)
    
    gt = [i.mention for i in message.guild.get_role(686639826308825089).members]
    gt = 'Отсутствует.' if gt==[] else '<a:black_fire:763424597369815042> ' + "\n".join(gt)
    embed.add_field(name=f"Глава отдела творчества:",value=gt)
    
    l = [i.mention for i in message.guild.get_role(765212719380037663).members]
    embed.add_field(name=f"Лента: [{len(l)}]",value=("\n".join(l)))
    a = [i.mention for i in message.guild.get_role(686621891230040077).members]
    embed.add_field(name=f"Отдел партнерства: [{len(a)}]",value=("\n".join(a)))
    c = [i.mention for i in message.guild.get_role(686618397668147220).members]
    embed.add_field(name=f"Отдел творчества: [{len(c)}]",value=("\n".join(c)))
    c = [i.mention for i in message.guild.get_role(757890413838467133).members]
    embed.add_field(name=f"В отставке: [{len(c)}]",value=("\n".join(c)))
    await message.channel.send(embed=embed)
    
@client.command()
async def developer(message):
    if message.author.id in admins:
        embed=discord.Embed(timestamp=datetime.datetime.utcnow(),description="**Команды для <@&620955813850120192>:**\n\n`K.say #channel|ID текст` — отправить текст определённого содержания в предназначеный канал.\n`K.clear n` — удалить n сообщений в канале.\n`K.disable` — отключить основные каналы (применять только на случай рейда)\n`K.enable` — включить все основные каналы (применять только на случай рейда)\n`K.approve Номер (+/-) Текст` — принять/отклонить предложение\n`K.iban @user|ID Причина` — добавить в чс идей пользователя\n`K.iunban @user|ID` — убрать из чс идей пользователя\n`K.ibans` — посмотреть чс идей\n`K.answer номер|текст` — ответить на вопрос пользователя")
        embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
        embed.set_thumbnail(url=message.guild.icon_url)
        await message.channel.send(embed=embed)
        
@client.command()
async def moder(message):
    b = [role.id for role in message.author.roles]
    if 620955813850120192 in b or 677397817966198788 in b or message.author.id in admins:
        embed=discord.Embed(colour=discord.Colour(0x310000),timestamp=datetime.datetime.utcnow(),description="**Команды для <@&677397817966198788>:**\n\n`K.ban @user|ID причина` — забанить пользователя.\n`K.unban @user|ID причина` — разбанить пользователя.\n\n`K.warn @user|ID причина` — выдать предупреждение пользователю.\n`K.warns @user|ID` — просмотреть предупреждения пользователя.\n`K.unwarn <Номер_случая>` — снять предупреждение по номеру случая.\n\n`K.mute @user|ID time причина` — замутить человека на time часов.\n`K.unmute @user|ID` — размутить человека.")
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
    
  idraw.text((365, 115), str(len(gg.emojis)), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 30))
  idraw.text((299, 167), str(len(gg.roles)), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 30))
  idraw.text((230, 243), str(gg.verification_level), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
  idraw.text((95, 345), str(gg.owner), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
  idraw.text((90, 425), '27 июля 2019 года', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
  idraw.text((540, 87), str(len(gg.voice_channels)), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 30))
  idraw.text((570, 142), str(len(gg.categories)), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 30))
  idraw.text((619, 215), str(len(gg.text_channels)), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 30))
  idraw.text((645, 290), str(gg.premium_subscription_count), (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 30))
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
async def modstats(message,data1=None,data2=None):
  b = [role.id for role in message.author.roles]
  if 686639786672652363 in b or 620955813850120192 in b:
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
        if i.id == 529044574660853761:
          d.update({i.id:4})
        else:
          d.update({i.id:0})
      for i in a:
        if i.id in idd:
          for j in i.text_channels:
            if j.id != 764911620111204383:
              b = await j.history(limit=200, after=datetime.datetime.strptime(data1, '%d.%m.%Y')-datetime.timedelta(hours=3),before=datetime.datetime.strptime(data2, '%d.%m.%Y')+datetime.timedelta(hours=24)).flatten()
              for k in b:
                d.update({k.author.id:d.setdefault(k.author.id, 0)+1})
      s = ''
      d1 = dict(sorted(d.items(), key = lambda x:x[1],reverse=True))
      key = 'neok'
      for i, j in d1.items():
        if j<8 and key == 'neok':
          s += '**-------Не выполнили установленную норму-------**\n'
          key = 'ok'
        s += f'<@{str(i)}> — {j}\n'
      s += f'\n**В период с `{data1}` по `{data2}`.**'
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
async def warn(message, id = None, *, reason=None):
  await message.message.delete()
  b = [role.id for role in message.author.roles]
  if 677397817966198788 in b or message.author.id in admins:
    if id is None:
      await message.channel.send('```\nВы не указали пользователя.```')
    elif reason is None:
      await message.channel.send('```\nВы не указали причину.```')
    else:
      try:
        member = message.guild.get_member(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
        flag = True
      except:
        await message.channel.send('```\nПользователя не существует.```')
        flag = False
      if flag:
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
        embed = discord.Embed(colour=discord.Colour(0x310000),description=f'Пользователь `{member}` получил предупреждение `№{count+1}` (случай `№{all}`) по причине: `{reason}`',timestamp=datetime.datetime.utcnow())
        embed.set_footer(text=f'Предупреждение от {message.author.name}',icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        my_warn_kol.update_one({"id":1},{"$set":{"all":all}})
        embed=discord.Embed(colour=discord.Colour.red(), description = f'Вы получили предупреждение `№{count+1}` по причине: `{reason}`',timestamp=datetime.datetime.utcnow())
        embed.set_footer(text=f'Предупреждение от {message.author.name}',icon_url=message.author.avatar_url)
        await member.send(embed=embed)
        
@client.command()
async def unwarn(message, number=None):
  await message.message.delete()
  b = [role.id for role in message.author.roles]
  if 677397817966198788 in b or message.author.id in admins:
    if number is None:
      await message.channel.send('```\nВы не указали номер случая.```')
    else:
      try:
        for item in my_warn.find():
          if item['all'] == int(number):
            a = await client.fetch_user(item['id'])
            embed = discord.Embed(colour=discord.Colour(0x310000),description=f'Случай `№{number}` благополучно был снят у пользователя `{a}`',timestamp=datetime.datetime.utcnow())
            embed.set_footer(text=f'Предупреждение снял(а) {message.author.name}',icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)
            my_warn.delete_one({'all':int(number)})
            break
        else:
          await message.channel.send('```Указанного случая нет в базе предупреждений.```')
      except:
        await message.channel.send('```Указанного случая нет в базе предупреждений.```')
        
@client.command()
async def warns(message, id=None):
  b = [role.id for role in message.author.roles]
  if 677397817966198788 in b or message.author.id in admins:
    if id is None:
      member = message.author
    else:
      member = message.guild.get_member(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
    embed = discord.Embed(colour=discord.Colour(0x310000),description=f'Предупреждения пользователя `{member}`:',timestamp=datetime.datetime.utcnow())
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    for item in my_warn.find():
      if item['id'] == member.id:
        namember = await client.fetch_user(item["mod_id"])
        embed.add_field(name=f'`Случай №{item["all"]}` {item["data"]} от `{namember}`',value=f'{item["reason"]}',inline=False)
    await message.channel.send(embed=embed)
  else:
    embed = discord.Embed(colour=discord.Colour(0x310000),description=f'Предупреждения пользователя `{message.author}`:',timestamp=datetime.datetime.utcnow())
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    for item in my_warn.find():
      if item['id'] == message.author.id:
        namember = await client.fetch_user(item["mod_id"])
        embed.add_field(name=f'`Случай №{item["all"]}` {item["data"]} от `{namember}`',value=f'{item["reason"]}',inline=False)
    await message.channel.send(embed=embed)
                        
@client.command()
async def mute(message, id=None, time=None, *, reason=None):
  await message.message.delete()
  b = [role.id for role in message.author.roles]
  if 677397817966198788 in b or message.author.id in admins:
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
  if 677397817966198788 in b or message.author.id in admins:
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
    if k % 6 != 0:
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

        if 608994688078184478 in b or member.id == 414119169504575509:
            response = requests.get('https://media.discordapp.net/attachments/734396452843028582/739819514589610064/b139e06844859b87.png?width=950&height=616', stream = True)
            dol, otd, flag, flag22 = 'Не указана', 'Отдел не указан', False, False
            if member.id == 414119169504575509:
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
            elif 677397817966198788 in b:
              dol = 'аперативник'
              otd = 'Отдел ОБТ "Модер"'
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
                  idraw.text((370, 500), f'В команде с {a[1]}', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
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
              if member.id == 529044574660853761:
                kol = 4
              else:
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
              idraw.text((457, 58), f'Партнёрств за 48 часов: {kol}', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
              part = requests.get('https://media.discordapp.net/attachments/689479689756344328/740856668698574858/unknown.png', stream = True)
              part = Image.open(io.BytesIO(part.content))
              part = part.convert('RGBA')
              part = part.resize((40, 25), Image.ANTIALIAS)
              response.paste(part, (410, 63, 450, 88))
              
            response.save('user_card.png')
            await message.channel.send(file = discord.File(fp = 'user_card.png'))
            
        else:
          if 769916590686732319 in b:
            response = requests.get('https://media.discordapp.net/attachments/767656142285176843/771005666999271445/full_mb.png', stream = True)
            color = (0, 0, 0)
          elif 622501691107049502 in b:
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
          
          if 769916590686732319 in b or 622501691107049502 in b or 622501656591990784 in b or 688654966675603491 in b:
            idraw.text((365, 400), f'Дата последнего обновления:', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
            if d.get(member.id) is not None:
              datet = d.get(member.id).split('.')[0].split()[0].split('-')
              datet2 = d.get(member.id).split('.')[0].split()[1]
              idraw.text((365, 440), f'{datet[2]} {sp[int(datet[1])]} {datet[0]} года в {datet2}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
            else:
              idraw.text((365, 440), f'Неизвестна', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
            kolvo = dk.get(member.id) if dk.get(member.id) is not None else 0
            idraw.text((365, 480), f'Всего публикаций с упоминанием: {kolvo}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
          warnow = 0
          for item in my_warn.find():
            if item['id'] == member.id:
              warnow += 1
          idraw.text((100 , 460), f'Предупреждений: {warnow}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 23))
          
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

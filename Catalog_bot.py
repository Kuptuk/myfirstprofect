import discord 
from discord.ext import commands
from discord.utils import get
import os
import pymongo
import inspect
import random
import datetime

tt = os.environ.get("TOKEN")
mm = os.environ.get("Mongo")

my_client = pymongo.MongoClient(mm)

my_database = my_client.Catalog
my_collection = my_database.Number

my_database2 = my_client.Catalog
my_collection2 = my_database.txtsug

my_db = my_client.Catalog
my_col = my_db.ibans

client = commands.Bot(command_prefix = "K.")
client.remove_command("help")
        
admins = [567025011408240667,704734583718936577,414119169504575509]

#Активность + перезапуск
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd,activity=discord.Game("K.help | #stayhome :3"))
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
async def info(message, id=None):
    if id is None:
        member = message.guild.get_member(int(message.author.id))
    else:
        try:
            member = message.guild.get_member(int(id))
        except:
            member = message.guild.get_member(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
    embed = discord.Embed(timestamp=datetime.datetime.utcnow())
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    embed.set_author(name=f'Информация о пользователе {member.name}',icon_url=message.guild.icon_url)
    if member.is_on_mobile():
        embed.add_field(name="Устройство",value="**Телефон**")
    else:
        if str(member.status) == "offline":
            embed.add_field(name="Устройство",value="**Оффлайн**")
        else:
            embed.add_field(name="Устройство",value="**ПК**")
    embed.add_field(name="Вступил", value="**"+str(member.joined_at).split(".")[0]+"**")
    embed.add_field(name="Высшая роль", value=member.top_role.mention)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Дата регистрации",value="**" + str(member.created_at).split(".")[0] + "**")
    if str(member.status) == "offline":
        embed.add_field(name="Статус",value="**:black_circle: Не в сети**")
    elif str(member.status) == "dnd":
        embed.add_field(name="Статус",value="**:red_circle: Не беспокоить**")
    elif str(member.status) == "idle":
        embed.add_field(name="Статус",value="**:yellow_circle: Не активен**")
    else:
        embed.add_field(name="Статус",value="**:green_circle: В сети**")

    msg = await client.get_channel(690827050033872937).history(limit=20).flatten()
    msg = msg[0].content.replace("[","").replace("]","").replace("'","").split(', ')
    embed.add_field(name="Случайный партнёр",value="[Ссылка на сервер](" + msg[random.randint(0,len(msg)-1)]+")")

    await message.channel.send(embed=embed)
    
@client.command()
async def help(message):
    embed=discord.Embed(timestamp=datetime.datetime.utcnow())
    msg = await client.get_channel(690827050033872937).history(limit=20).flatten()
    msg = msg[0].content.replace("[","").replace("]","").replace("'","").split(', ')
    embed.add_field(name='ᅠᅠᅠᅠᅠᅠᅠМеню **__Каталог__ Серверов **:',value="▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\nᅠᅠᅠᅠᅠᅠᅠᅠᅠ**Все __Команды__ **:\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n▻**K.help** — __Помощь __ по __Серверу__ !\n▻**K.avatar** __@user|ID__ — Аватар __Пользователя__ !\n▻**K.suggest** __Текст__ — Предложить свою __Идею__ !\n▻**K.info** __@user|ID__ — Информация о __Пользователе__ !\n▻**K.server** — Информация о __Сервере__ !\n▻**K.stat** — Статистика __Сервера__ !\n▻**K.team** — Состав __Команды Сервера__ !\n▻**K.upd** — __Обновления__ Бота !\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n▻**K.developer** — __Административные__ Команды !\n▻**K.bp** — Команды для __Бан Панелей__ !\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\nᅠᅠᅠᅠᅠᅠᅠᅠ**Случайный партнёр **:\nᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠ**[__Клик__](" + msg[random.randint(0,len(msg)-1)]+")**\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬",inline=False)
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    await message.channel.send(embed=embed)
    
@client.command()
async def ban(message, id=None, *, reason=None):
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
async def stat(message):
    k1,k2,k3,ka,km,ks,kh,kk,kb,nq,nw,ne,oo,ot,r,z,rr = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    a = message.guild.members
    for i in a:
        if 'Партнёр [Ур. 1]' in str(i.roles):
            k1 += 1
        if 'Партнёр [Ур. 2]' in str(i.roles):
            k2 += 1
        if 'Партнёр [Ур. 3]' in str(i.roles):
            k3 += 1
        if 'Активный' in str(i.roles):
            ka += 1
        if 'Отдел модерации' in str(i.roles):
            km += 1
        if 'Администратор' in str(i.roles):
            ks += 1
        if 'Боты' in str(i.roles):
            kh += 1
        if 'Бустер сервера' in str(i.roles):
            kb += 1
        if 'Команда каталога' in str(i.roles):
            kk += 1
        if 'Наставник' in str(i.roles):
            nq += 1
        if 'Бан панель' in str(i.roles):
            nw += 1
        if 'Медиа' in str(i.roles):
            ne += 1
        if 'Отдел контроля и оценки' in str(i.roles):
            oo += 1
        if 'Отдел творчества' in str(i.roles):
            ot += 1
        if 'Рекрутер' in str(i.roles):
            r += 1
        if 'Участник' in str(i.roles):
            z += 1
        if 'Новости' in str(i.roles):
            rr += 1
    embed = discord.Embed(title="Статистика",description=str(len(a))+" пользователей",timestamp=datetime.datetime.utcnow())
    embed.set_thumbnail(url=message.guild.icon_url)
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    embed.add_field(name="**"+str(k1)+"**",value="<@&688654966675603491>")
    embed.add_field(name="**"+str(k2)+"**",value="<@&622501656591990784>")
    embed.add_field(name="**"+str(k3)+"**",value="<@&622501691107049502>")
    embed.add_field(name="**"+str(kk)+"**",value="<@&608994688078184478>")
    embed.add_field(name="**"+str(ka)+"**",value="<@&619013112531517501>")
    embed.add_field(name="**"+str(kb)+"**",value="<@&657636549772705833>")
    embed.add_field(name="**"+str(km)+"**",value="<@&686621891230040077>")
    embed.add_field(name="**"+str(oo)+"**",value="<@&686621580620595296>")
    embed.add_field(name="**"+str(ot)+"**",value="<@&686618397668147220>")
    embed.add_field(name="**"+str(nq)+"**",value="<@&685079147017535493>")
    embed.add_field(name="**"+str(r)+"**",value="<@&686256550951649317>")
    embed.add_field(name="**"+str(nw)+"**",value="<@&677397817966198788>")
    embed.add_field(name="**"+str(ks)+"**",value="<@&620955813850120192>")
    embed.add_field(name="**"+str(ne)+"**",value="<@&658154672237838347>")
    embed.add_field(name="**"+str(kh)+"**",value="<@&604645403664711680>")
    embed.add_field(name="**"+str(z)+"**",value="<@&678657735218167818>")
    embed.add_field(name="**"+str(rr)+"**",value="<@&734089506713763861>")

    msg = await client.get_channel(690827050033872937).history(limit=20).flatten()
    msg = msg[0].content.replace("[","").replace("]","").replace("'","").split(', ')
    embed.add_field(name="Случайный партнёр",value="[Ссылка на сервер](" + msg[random.randint(0,len(msg)-1)]+")")

    await message.channel.send(embed=embed)
    
@client.command()
async def team(message):
    a = client.get_guild(604636579545219072).members
    s,sb,ns,q,w,e,r,t,y,u = "","","","","","",'','','',''
    oo = 0
    for i in a:
        if "Бан панель" in str(i.roles):
            sb += "<@" + str(i.id) + ">\n"
        if 'Отдел модерации' in str(i.roles):
            s += "<@" + str(i.id) + ">\n"
        if "Наставник" in str(i.roles):
            ns += "<@" + str(i.id) + ">\n"
        if "Команда каталога" in str(i.roles):
            oo += 1
        if "Рекрутер" in str(i.roles):
            q += "<@" + str(i.id) + ">\n"
        if "Отдел творчества" in str(i.roles):
            w += "<@" + str(i.id) + ">\n"
        if "Редактор" in str(i.roles):
            e += "<@" + str(i.id) + ">\n"
        if "Отдел контроля и оценки" in str(i.roles):
            r += "<@" + str(i.id) + ">\n"
        if "Глава отдела модерации" in str(i.roles):
            t += "<@" + str(i.id) + ">\n"
        if "Глава отдела оценки" in str(i.roles):
            y += "<@" + str(i.id) + ">\n"
        if "Глава отдела творчества" in str(i.roles):
            u += "<@" + str(i.id) + ">\n"
    if t == '':
        t = "Отсутствует."
    if y == '':
        y = "Отсутствует."
    if u == '':
        u = "Отсутствует."
    if s == '':
        s = "Отсутствует."
    if r == '':
        r = "Отсутствует."
    if w == '':
        w = "Отсутствует."
    if ns == '':
        ns = "Отсутствует."
    if q == '':
        q = "Отсутствует."
    if sb == '':
        sb = "Отсутствует."
    embed = discord.Embed(title="Команда Каталога",description=f"Людей в команде: `{str(oo)}`",timestamp=datetime.datetime.utcnow())
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    embed.add_field(name="Глава отдела модерации:",value=t)
    embed.add_field(name="Глава отдела оценки:",value=y)
    embed.add_field(name="Глава отдела творчества:",value=u)
    embed.add_field(name="Отдел модерации:",value=s)
    embed.add_field(name="Отдел контроля и оценки:",value=r)
    embed.add_field(name="Отдел творчества:",value=w)
    embed.add_field(name="Наставники:",value=ns)
    embed.add_field(name="Рекрутеры:",value=q)
    embed.add_field(name="Бан панель:",value=sb)
    await message.channel.send(embed=embed)
    
@client.command()
async def developer(message):
    if message.author.id in admins:
        embed=discord.Embed(timestamp=datetime.datetime.utcnow(),description="**Команды для <@&620955813850120192>:**\n\n`K.say #channel|ID текст` — отправить текст определённого содержания в предназначеный канал.\n`K.clear n` — удалить n сообщений в канале.\n`K.disable` — отключить основные каналы (применять только на случай рейда)\n`K.enable` — включить все основные каналы (применять только на случай рейда)\n`K.approve Номер Текст` — принять предложение\n`K.deny Номер Текст` — отклонить предложение\n`K.iban @user|ID Причина` — добавить в чс идей пользователя\n`K.iunban @user|ID` — убрать из чс идей пользователя\n`K.ibans` — посмотреть чс идей")
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
      
#server
@client.command()
async def server(message):
    embed=discord.Embed(timestamp=datetime.datetime.utcnow())
    embed.set_author(name=f'Информация о сервере {message.guild.name}')
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    embed.set_thumbnail(url=message.guild.icon_url)
    embed.add_field(name="Эмодзи",value="**:kissing_closed_eyes: " + str(len(message.guild.emojis)) + "**")
    embed.add_field(name="Регион",value="** :flag_ru: " + str(message.guild.region)[0].upper() + str(message.guild.region)[1::] + "**")
    embed.add_field(name="Владелец",value=message.guild.owner.mention)
    embed.add_field(name="Уровень верификации",value="** :smiling_imp: " + str(message.guild.verification_level) + "**")
    embed.add_field(name="Пользователей",value="**👤 " + str(len(message.guild.members)) + "**")
    embed.add_field(name="Ролей",value="**:jigsaw: " + str(len(message.guild.roles)) + "**")
    embed.add_field(name="Текстовых каналов",value="**:page_with_curl: " + str(len(message.guild.text_channels)) + "**")
    embed.add_field(name="Категорий",value="**:pencil: " + str(len(message.guild.categories)) + "**")
    embed.add_field(name="Голосовых каналов",value="**:microphone2: " + str(len(message.guild.voice_channels)) + "**")
    embed.add_field(name="Создан",value="**:clock1: " + str(str(message.guild.created_at).split(".")[0]) + "**")
    embed.add_field(name="Банов",value="**:bangbang: " + str(len(await message.guild.bans())) + "**")
    
    msg = await client.get_channel(690827050033872937).history(limit=20).flatten()
    msg = msg[0].content.replace("[","").replace("]","").replace("'","").split(', ')
    embed.add_field(name="Случайный партнёр",value="[Ссылка на сервер](" + msg[random.randint(0,len(msg)-1)]+")")

    await message.channel.send(embed=embed)
    
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
    if id is None:
        member = message.guild.get_member(int(message.author.id))
    else:
        member = message.guild.get_member(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
    embed=discord.Embed(timestamp=datetime.datetime.utcnow())
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
    embed.set_author(name=f'Аватар пользователя {member.name}',icon_url=message.guild.icon_url)
    await message.channel.send(embed=embed)
    
@client.command()
async def suggest(message):
    if message.channel.id != 678666229661171724:
        await message.channel.send("Канал для предложений => <#678666229661171724>")
    else:
        my_cursor = my_col.find()
        for item in my_cursor:
            if item['id'] == message.author.id:
                await message.channel.purge(limit=1)
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
        
client.run(tt)

import pymysql
import disnake
from settings import settings
from disnake.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None, intents=disnake.Intents.all())

db_user = settings['user']
password = settings['password']
host = settings['host']
database = settings['database']
TOKEN = settings['token']

bot = commands.Bot(command_prefix="!", help_command=None, intents=disnake.Intents.all())

@bot.event
async def on_ready():
    print('Зaпуск бота...')
    print('Бот запущен!')
    user = bot.get_user(1087354143821267017)
    await user.send(content = "Запуск бота успешен")

@bot.event
async def on_message(message):
    if message.guild is not None and message.guild.id == 1247471574387261462 and not message.author.bot:
        try:
            conn = pymysql.connect(user=db_user, password=password, host=host, database=database)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO `messages`(user_id, username, message, channel) VALUES (%s, %s, %s, %s)", (message.author.id, message.author.name, message.content, message.channel.name))
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
@bot.event
async def on_message_delete(message):
    if message.guild is not None and message.guild.id == 1247471574387261462 and not message.author.bot:
        try:
            conn = pymysql.connect(user=db_user, password=password, host=host, database=database)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO `delete_messages`(user_id, username, message, channel) VALUES (%s, %s, %s, %s)", (message.author.id, message.author.name, message.content, message.channel.name))
            cursor.execute("DELETE FROM `messages` WHERE `message` = %s AND `user_id` = %s", (message.content, message.author.id))
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)

@bot.event
async def on_voice_state_update(member, before, after):
    if member.guild.id == 1247471574387261462 and not member.bot:
        try:
            conn = pymysql.connect(user=db_user, password=password, host=host, database=database)
            cursor = conn.cursor()
            if before.channel is None and after.channel is not None:
                cursor.execute("INSERT INTO `voice_logs`(user_id, username, do, channel) VALUES (%s, %s, %s, %s)", 
                             (member.id, member.name, "Вход", after.channel.name))
            elif before.channel is not None and after.channel is None:
                cursor.execute("INSERT INTO `voice_logs`(user_id, username, do, channel) VALUES (%s, %s, %s, %s)", 
                             (member.id, member.name, "Выход", before.channel.name))
            elif before.channel != after.channel:
                cursor.execute("INSERT INTO `voice_logs`(user_id, username, do, channel) VALUES (%s, %s, %s, %s)", 
                             (member.id, member.name, "Перемещение", f"{before.channel.name} -> {after.channel.name}"))
            conn.commit()
        except Exception as e:
            print(e)

@bot.slash_command()
@commands.has_permissions(administrator=True)
async def ping(interaction):
    try:
        await interaction.response.defer(ephemeral=True)
        await interaction.edit_original_message(content="Бот работает!")
    except Exception as e:
        await interaction.edit_original_message(content = f'Произошла ошибка: {e}')

bot.run(TOKEN)
import pymysql
import disnake
from settings import settings
from disnake.ext import commands

db_user = settings['user']
password = settings['password']
host = settings['host']
database = settings['database']
TOKEN = settings['token']
conn = pymysql.connect(user=db_user, password=password, host=host, database=database)
cursor = conn.cursor()
bot = commands.Bot(command_prefix="!", help_command=None, intents=disnake.Intents.all())

if cursor.execute("SHOW TABLES LIKE 'a_users'"):
    print("Таблица пользователей уже существует")
else:
    print("Начинаю создание таблицы пользователей")
    cursor.execute("CREATE TABLE `a_users` (`id` INT AUTO_INCREMENT PRIMARY KEY, `username` TEXT, `password` TEXT)")
    password = hashlib.sha256('root'.encode('utf-8')).hexdigest()
    cursor.execute(f"INSERT INTO `a_users` (username, password) VALUES ('root', '{password}')")
    conn.commit()
    print("Таблица пользователей создана")

if cursor.execute("SHOW TABLES LIKE 'delete_messages'"):
    print("Таблица удаленных сообщений уже существует")
else:
    print("Начинаю создание таблицы удаленных сообщений")
    cursor.execute("CREATE TABLE `delete_messages` (`id` INT AUTO_INCREMENT PRIMARY KEY, `user_id` INT, `message` TEXT, `channel` TEXT, `time` timestamp DEFAULT CURRENT_TIMESTAMP)")
    conn.commit()
    print("Таблица удаленных сообщений создана")

if cursor.execute("SHOW TABLES LIKE 'messages'"):
    print("Таблица сообщений уже существует")
else:
    print("Начинаю создание таблицы сообщений")
    cursor.execute("CREATE TABLE `messages` (`id` INT AUTO_INCREMENT PRIMARY KEY, `user_id` INT, `message` TEXT, `channel` TEXT, `time` timestamp DEFAULT CURRENT_TIMESTAMP)")
    conn.commit()
    print("Таблица сообщений создана")

@bot.event
async def on_ready():
    print('Бот запущен!')

@bot.event
async def on_message(message):
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

bot.run(TOKEN)
from os import getenv


API_ID = int(getenv("API_ID", "25891183"))
API_HASH = getenv("API_HASH", "36709c81d7609a81f86de931cbc87f3a")
BOT_TOKEN = getenv("BOT_TOKEN", "7480167477:AAF7957itkjVj0VOoQApYh4DzLTTAaHJn0c")
OWNER_ID = int(getenv("OWNER_ID", "6750546542"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1001992164182").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://mohitag24082006:ge3z5sQOsr6NiTTt@cluster0.xxrppe5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002232922467"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002198271060"))



"""
    [DEFAULT]
    debug = False

    [WEB_SERVER]
    host = 127.0.0.1
    port = 80

    [DB_SERVER]
    host = 127.0.0.1
    port = 3306
"""
import configparser

# Write
config = configparser.ConfigParser()
config["DEFAULT"] = {
    "debug": True
}

config["WEB_SERVER"] = {
    "host": "127.0.0.1",
    "port": 80
}

config["DB_SERVER"] = {
    "host": "127.0.0.1",
    "port": 3306
}

with open("config.ini", "w") as config_fs:
    config.write(config_fs)

# Read
config = configparser.ConfigParser()
config.read("config.ini", "utf-8")
print(config["WEB_SERVER"]["host"])  # 127.0.0.1

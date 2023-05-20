"""
    pip install pyyaml
    web_server:
      host: 127.0.01
      port: 80
    
    db_server:
      host: 127.0.0.1
      port: 3306
"""

import yaml

# Write
with open("config.yml", "w") as yml_fs:
    yaml.dump({
        "web_server": {

            "host": "127.0.0.1",
            "port": 80
        },
        "db_server": {
            "host": "127.0.0.1",
            "post": "3306"
        }
    }, yml_fs, default_flow_style=False)

# Read
with open("config.yml", "r") as yml_fs:
    data = yaml.safe_load(yml_fs)
    print(data, type(data))

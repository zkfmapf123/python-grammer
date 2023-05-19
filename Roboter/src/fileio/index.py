import csv
import os


class RobertorIO(object):

    PATHS = {
        "user_file_path" : "{}/user.csv".format("public"),
        "menu_path" : "{}/menu.csv".format("public"),
        "select_menu" : "{}/select_menu.csv".format("public"),
    }

    def __init__(self) -> None:
        pass

    def __del__(self) -> None:
        pass

    def setting_user_info(self, profile : dict, keys :list[str]) -> bool:
        try:
            if not self._valid_username(profile["name"], keys):
                return False

            with open(self.PATHS["user_file_path"], "a") as fs:
                cd = csv.DictWriter(fs, keys)
                cd.writerow(profile)   
        except Exception as err:
            raise Exception(err)

        return True

    def _valid_username(self ,name: str, keys : list[str]) -> bool:
        try:
            with open(self.PATHS["user_file_path"], "r") as fs:
                lines = csv.DictReader(fs, keys)
                for row in lines:
                    if row["name"] == name:
                        return False
        except Exception as err:
            raise Exception(err)
        return True


    

from datetime import datetime


class CustomLogging:
    def set_log(self, message):
        today = datetime.now()
        with open('./logs.txt', 'a', encoding='utf8') as logs:
            logs.write(str(today) + ' : ' + message)

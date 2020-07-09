from mycroft import MycroftSkill, intent_file_handler


class Klima(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('klima.intent')
    def handle_klima(self, message):
        self.speak_dialog('klima')


def create_skill():
    return Klima()


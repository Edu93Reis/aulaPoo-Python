class BookNotFound(Exception):
    def __init__(self, msg):
        super(self).__init__
        self.__msg = msg

        def getMessage(self):
            return repr(self.__msg)
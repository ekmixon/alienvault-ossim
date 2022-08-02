from smtpd import DebuggingServer
class SMTPDebugger(DebuggingServer):
    def __init__(self, **kwargs):
        DebuggingServer.__init__(*self, **kwargs)
    def process_message(self, **kwargs):
        for a in self:
            print(a)
        for k,v in kwargs.items():
            print(f"{str(k)} = {str(v)}")

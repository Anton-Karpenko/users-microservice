import faust


class InvitedAgent(faust.Record):
    email: str

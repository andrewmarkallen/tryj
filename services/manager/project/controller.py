from collections import deque
from project.session import Session


class Controller:

    def __init__(self):
        self.active_sessions = deque()

    def session_exists(self, uuid):
        return uuid in [s.id for s in self.active_sessions]

    def add_new_session(self, uuid):
        print(f'{uuid=}')
        if self.session_exists(uuid):
            print('already exists')
            return False
        else:
            try:
                session = Session(uuid)
                self.active_sessions.append(session)
                print('adding')
                return True
            except Exception as e:
                print(e)
                return False

    def run_command(self, command, uuid):
        session = [s for s in self.active_sessions if s.id == uuid][0]
        return session.write(command)

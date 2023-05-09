from enum import Enum

class States(Enum):
    INIT = 0
    PLAY_LEVEL = 1
    RESULT_LEVEL = 2
    LOST_LIVES = 3
    END_GAME = 4
    WON = 5
    PAUSE = 6

class Actions(Enum):
    START = 0
    EXIT = 1
    FINISH_LEVEL = 2
    LOST_LIFE = 3
    CONTINUE = 4
    

class StateMachine:
    def __init__(self):
        self.state = States.INIT

    def transit(self, action):
        if self.state == States.INIT:
            if action == Actions.START:
                self.state = States.PLAY_LEVEL
        elif self.state == States.PLAY_LEVEL:
            if action == Actions.FINISH_LEVEL:
                self.state = States.RESULT_LEVEL
            if action == Actions.LOST_LIFE:
                self.state = States.LOST_LIVES
        elif self.state == States.RESULT_LEVEL:
            if action == Actions.START:
                self.state = States.PLAY_LEVEL
            if action == Actions.EXIT:
                self.state = States.END_GAME
from typing import Text, List
from rasa_core.actions import Action
from rasa_core.events import SlotSet


class GetMyLikes(Action):
    def name(self) -> Text:
        return "get_my_likes"

    def run(self, dispatcher: 'Dispatcher', tracker: 'DialogueStateTracker',
            domain: 'Domain') -> List['Event']:
        my_likes = tracker.get_slot("my_likes")
        '''
            TODO 여기부터 내가 하고 싶은 디테일한 로직을 생성한다고 한다.
            DB에서 가져오던지, API를 콜하던지 맘대로 해라
        '''
        return [SlotSet("my_likes", my_likes)]
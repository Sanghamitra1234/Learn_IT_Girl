from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


class ActionWeather(Action):
    def name(self):
        return 'action_weather'

    def run(self, dispatcher, tracker, domain):
        from apixu.client import ApixuClient
        api_key = 'c3e1096f0ccc478cb40101824192704'
        client = ApixuClient(api_key)

        loc = tracker.get_slot('location')
        current = client.current(q=loc)

        country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['condition']['text']
        temperature_c = current['current']['humidity']
        humidity = current['current']['humidity']

        response = """It is currently {} in {} at the moment.The temperature is {} degrees.""" .format(condition, city, temperature_c)

        dispatcher.utter_message(response)
        return [SlotSet('location', loc)]

import random
from Responses import responses

def respond(msg):
   text = msg.lower()
   if text in responses:
      bot_message = random.choice(responses[text])
   else:
          bot_message = random.choice(responses["default"])

   return bot_message

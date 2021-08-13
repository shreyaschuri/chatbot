
name = "Funny Bot 101"
weather = "rainy"
mood = "Happy"


responses = {

"what's your name?": [
   "They call me {0}".format(name),
   "I usually go by {0}".format(name),
   "My name is the {0}".format(name)
],

"what's today's weather?": [
    "The weather is {0}".format(weather),
    "It's {0} today".format(weather),
    "Let me check, it looks {0} today".format(weather)
],

"Are you a robot?": [
    "What do you think?",
    "Maybe yes, maybe no!",
    "Yes, I am a robot with human feelings.",
],

"how are you?": [
    "I am feeling {0}".format(mood),
    "{0}! How about you?".format(mood),
    "I am {0}! How about yourself?".format(mood),
],

"": [
    "Hey! Are you there?",
    "What do you mean by saying nothing?",
    "Sometimes saying nothing tells a lot :)",
],

"default": ["Sorry i didnt get you :("]

}

from furhat_remote_api import FurhatRemoteAPI
import random
import time

furhat = FurhatRemoteAPI("localhost")

# configs
expression_weights = {
    'smile': 36.3,
    'jawDrop': 32.9,
    'lipsPart': 30.1,
    'browRaise': 21.0,
    'eyesWide': 20.9,
    'browFrown': 17.1,
    'innerBrowRaise': 13.9,
}

# map expression names to Furhat's names
furhat_gesture_map = {
    'smile': 'Smile',
    'jawDrop': 'ExpressSurprise',
    'lipsPart': 'ExpressSurprise',
    'browRaise': 'BrowRaise',
    'eyesWide':'ExpressFear',
    'browFrown': 'BrowFrown',
    'innerBrowRaise':'BrowInnerUp',
}

story = [
    "The blue whale is the largest animal on Earth. It can grow up to 30 meters like creatures called krill. A blue whale can consume 4 tons of krill per day. They can live up to long and weigh 200 tons. Its heart sounds alone is the size of a small car. Blue whales communicate using low-frequency that travel thousands of kilometers underwater. Despite their size, they eat tiny shrimp-fewer than 25,000 left. They are protected under international law since 1966."
]

#random expression based on speaker proportions.
def pick_expression(weights):
    total = sum(weights.values())
    r = random.uniform(0, total)
    cumulative = 0
    for expr, weight in weights.items():
        cumulative += weight
        if r <= cumulative:
            return expr

# run the story
print("Starting story...")
furhat.set_voice(name='Matthew-Neural')

for i, sentence in enumerate(story):
    expr_key     = pick_expression(expression_weights)
    gesture_name = furhat_gesture_map[expr_key]

    print(f"Sentence {i+1}: '{gesture_name}' → {sentence[:40]}...")

    # Show expression
    furhat.gesture(name=gesture_name)
    time.sleep(0.3)

    # Speak
    furhat.say(text=sentence, blocking=True)

    # Reset face between sentences
    furhat.gesture(name='Reset')
    time.sleep(0.4)

print("Story complete!")
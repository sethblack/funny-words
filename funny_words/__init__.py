#
# funny-words
# copyright 2016 Seth Black
# 11/09/2016
#

import argparse
import random

# taken from http://marshmallow_666.tripod.com/cgi-bin/
funny_words = [
    u'aardvark', u'abacus', u'abundance', u'ache', u'acupuncture',
    u'airbrush', u'alien', u'anagram', u'angle', u'amazing', u'ankle',
    u'alphabet', u'antenna', u'aqua', u'asphalt', u'bacon', u'banana',
    u'bangles', u'banjo', u'bankrupt', u'bar', u'barracuda', u'basket',
    u'beluga', u'binder', u'birthday', u'bisect', u'blizzard', u'blunderbuss',
    u'boa', u'bog', u'bounce', u'broomstick', u'brought', u'bubble',
    u'budgie', u'bug', u'bug-a-boo', u'bugger', u'buff', u'burst', u'butter',
    u'buzz', u'cabana', u'cake', u'calculator', u'camera', u'candle',
    u'carnival', u'carpet', u'casino', u'cashew', u'catfish', u'ceiling',
    u'celery', u'chalet', u'chalk', u'chart', u'cheddar', u'chesterfield',
    u'chicken', u'chinchill', u'chit-chat', u'chocolate', u'chowder', u'coal',
    u'compass', u'compress', u'computer', u'conduct', u'contents', u'cookie',
    u'copper', u'corduroy', u'cow', u'cracker', u'crackle', u'croissant',
    u'cube', u'cupcake', u'curly', u'curtain', u'cushion', u'cuticle',
    u'daffodil', u'delicious', u'dictionary', u'dimple', u'ding-a-ling',
    u'disk', u'disco duck', u'dodo', u'dolphin', u'dong', u'donuts', u'dork',
    u'dracula', u'duct tape', u'effigy', u'egad', u'elastic', u'elephant',
    u'encasement', u'erosion', u'eyelash', u'fabulous', u'fantastic',
    u'feather', u'felafel', u'fetish', u'financial', u'finger', u'finite',
    u'fish', u'fizzle', u'fizzy', u'flame', u'flash', u'flavour', u'flick',
    u'flock', u'flour', u'flower', u'foamy', u'foot', u'fork', u'fritter',
    u'fudge', u'fungus', u'funny', u'fuse', u'fusion', u'fuzzy', u'garlic',
    u'gelatin', u'gelato', u'ghetto', u'glebe', u'glitter', u'glossy',
    u'groceries', u'goulashes', u'guacamole', u'gumdrop', u'haberdashery',
    u'hamster', u'happy', u'highlight', u'hippopotamus', u'hobbit', u'hold',
    u'hooligan', u'hydrant', u'icicles', u'idiot', u'implode', u'implosion',
    u'indeed', u'issue', u'itchy', u'jell-o', u'jewel', u'jump', u'kabob',
    u'kasai', u'kite', u'kiwi', u'ketchup', u'knob', u'laces', u'lacy',
    u'laughter', u'laundry', u'leaflet', u'legacy', u'leprechaun', u'lollypop',
    u'lumberjack', u'macadamia', u'magenta', u'magic', u'magnanimous',
    u'mango', u'margarine', u'massimo', u'mechanical', u'medicine', u'meh',
    u'melon', u'meow', u'mesh', u'metric', u'microphone', u'minnow', u'mitten',
    u'mozzarella', u'muck', u'mumble', u'mushy', u'mustache', u'nanimo',
    u'noodle', u'nostril', u'nuggets', u'oatmeal', u'oboe', u'o\'clock',
    u'octopus', u'odour', u'ointment', u'olive', u'optic', u'overhead', u'ox',
    u'oxen', u'pajamas', u'pancake', u'pansy', u'paper', u'paprika',
    u'parmesan', u'pasta', u'pattern', u'pecan', u'peek-a-boo', u'pen',
    u'pepper', u'pepperoni', u'peppermint', u'perfume', u'periwinkle',
    u'photograph', u'pie', u'pierce', u'pillow', u'pimple', u'pineapple',
    u'pistachio', u'plush', u'polish', u'pompom', u'poodle', u'pop',
    u'popsicle', u'prism', u'prospector', u'prosper', u'pudding', u'puppet',
    u'puzzle', u'queer', u'query', u'radish', u'rainbow', u'ribbon', u'rotate',
    u'salami', u'sandwich', u'saturday', u'saturn', u'saxophone', u'scissors',
    u'scooter', u'scrabbleship', u'scrunchie', u'scuffle', u'shadow',
    u'sickish', u'silicone', u'slippery', u'smash', u'smooch', u'snap',
    u'snooker', u'socks', u'soya', u'spaghett', u'sparkle', u'spatula',
    u'spiral', u'splurge', u'spoon', u'sprinkle', u'square', u'squiggle',
    u'squirrel', u'statistics', u'stuffing', u'sticky', u'sugar',
    u'sunshine', u'super', u'swirl', u'taffy', u'tangy', u'tape', u'tat',
    u'teepee', u'telephone', u'television', u'thinkable', u'tip', u'tofu',
    u'toga', u'trestle', u'tulip', u'turnip', u'turtle', u'tusks',
    u'ultimate', u'unicycle', u'unique', u'uranus', u'vegetable', u'waddle',
    u'waffle', u'wallet', u'walnut', u'wagon', u'window', u'whatever',
    u'whimsical', u'wobbly', u'yellow', u'zap', u'zebra', u'zigzag', u'zip',
    ]


def pick_funny_word(but_not=u''):
    funny_word = random.choice(funny_words)

    while funny_word == but_not:
        funny_word = random.choice(funny_words)

    return funny_word


def build_n_gram(words=2, join_with=u' '):
    # Special thanks to /u/finlay_mcwalter for thinking through this problem
    # way too much!
    # https://www.reddit.com/r/Python/comments/5cexrm/just_released_the_tool_we_use_at_atlas_wearables/d9w1123/
    return join_with.join(random.sample(funny_words, words))


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument(
            u'-w',
            u'--words',
            help=u'how many funny words to generate per line',
            type=int,
            default=2)
    parser.add_argument(
            u'-n',
            u'--number',
            help=u'how many lines of funny words to generate',
            type=int,
            default=1)
    parser.add_argument(
            u'-d',
            u'--delimiter',
            help=u'what to put between the funny words',
            type=str,
            default=u' ')
    args = parser.parse_args()

    for n in xrange(args.number):
        print build_n_gram(args.words, args.delimiter)

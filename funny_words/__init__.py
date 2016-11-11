#
# funny-words
# copyright 2016 Seth Black
# 11/09/2016
#

import argparse
import random

# taken from http://marshmallow_666.tripod.com/cgi-bin/
funny_words = [
    'aardvark','abacus','abundance','ache','acupuncture','airbrush','alien','anagram','angle','amazing','ankle','alphabet','antenna','aqua','asphalt',
    'bacon','banana','bangles','banjo','bankrupt','bar','barracuda','basket','beluga','binder','birthday','bisect','blizzard','blunderbuss','boa','bog',
    'bounce','broomstick','brought','bubble','budgie','bug','bug-a-boo','bugger','buff','burst','butter','buzz','cabana','cake','calculator','camera',
    'candle','carnival','carpet','casino','cashew','catfish','ceiling','celery','chalet','chalk','chart','cheddar','chesterfield','chicken','chinchill',
    'chit-chat','chocolate','chowder','coal','compass','compress','computer','conduct','contents','cookie','copper','corduroy','cow','cracker','crackle',
    'croissant','cube','cupcake','curly','curtain','cushion','cuticle','daffodil','delicious','dictionary','dimple','ding-a-ling','disk',
    'disco duck','dodo','dolphin','dong','donuts','dork','dracula','duct tape','effigy','egad','elastic','elephant','encasement','erosion','eyelash','fabulous',
    'fantastic','feather','felafel','fetish','financial','finger','finite','fish','fizzle','fizzy','flame','flash','flavour','flick','flock','flour','flower',
    'foamy','foot','fork','fritter','fudge','fungus','funny','fuse','fusion','fuzzy','garlic','gelatin','gelato','ghetto','glebe','glitter','glossy','groceries',
    'goulashes','guacamole','gumdrop','haberdashery','hamster','happy','highlight','hippopotamus','hobbit','hold','hooligan','hydrant','icicles','idiot',
    'implode','implosion','indeed','issue','itchy','jell-o','jewel','jump','kabob','kasai','kite','kiwi','ketchup','knob','laces','lacy','laughter','laundry',
    'leaflet','legacy','leprechaun','lollypop','lumberjack','macadamia','magenta','magic','magnanimous','mango','margarine','massimo','mechanical','medicine',
    'meh','melon','meow','mesh','metric','microphone','minnow','mitten','mozzarella','muck','mumble','mushy','mustache','nanimo','noodle','nostril','nuggets',
    'oatmeal','oboe','o\'clock','octopus','odour','ointment','olive','optic','overhead','ox','oxen','pajamas','pancake','pansy','paper','paprika','parmesan',
    'pasta','pattern','pecan','peek-a-boo','pen','pepper','pepperoni','peppermint','perfume','periwinkle','photograph','pie','pierce','pillow','pimple',
    'pineapple','pistachio','plush','polish','pompom','poodle','pop','popsicle','prism','prospector','prosper','pudding','puppet','puzzle','queer','query',
    'radish','rainbow','ribbon','rotate','salami','sandwich','saturday','saturn','saxophone','scissors','scooter','scrabbleship','scrunchie','scuffle','shadow',
    'sickish','silicone','slippery','smash','smooch','smut','snap','snooker','socks','soya','spaghett','sparkle','spatula','spiral','splurge','spoon','sprinkle',
    'square','squiggle','squirrel','statistics','stuffing','sticky','sugar','sunshine','super','swirl','taffy','tangy','tape','tat','teepee','telephone','television',
    'thinkable','tip','tofu','toga','trestle','tulip','turnip','turtle','tusks','ultimate','unicycle','unique','uranus','vegetable','waddle','waffle','wallet',
    'walnut','wagon','window','whatever','whimsical','wobbly','yellow','zap','zebra','zigzag','zip',]

def pick_not_word(word=''):
    funny_word = random.choice(funny_words)

    while funny_word == word:
        funny_word = random.choice(funny_words)

    return funny_word

def pick_n_gram(words=2, join=' '):
    previous_words = ''
    local_funny_words = []

    for i in xrange(words):
        new_funny_word = pick_not_word()

        while new_funny_word in previous_words:
            new_funny_word = pick_not_word()

        local_funny_words.append(new_funny_word)

    return join.join(local_funny_words)

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', help='how many lines of funny words to generate', type=int, default='1')
    parser.add_argument('-w', '--words', help='how many funny words to generate per line', type=int, default='2')
    parser.add_argument('-d', '--delimiter', help='what to put between the funny words', type=str, default=' ')
    args = parser.parse_args()

    for n in xrange(args.number):
        print pick_n_gram(args.words, args.delimiter)
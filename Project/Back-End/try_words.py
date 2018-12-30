import json, time

def show_on_screen(word):
    time.sleep(0.01)
    data = {}
    data['state'] = [" ############################# " + word + " ############################# "]
    data['answer'] = [""]
    with open('static/state.json', 'w') as write_file:
        json.dump(data, write_file)
    print("#############################", word, "#############################" )
    return

"""
def remove_others(i, word_list, desired_word):
    for word in word_list[:]:
        if word[i] != desired_word[i]:
            word_list.remove(word)
    time.sleep(0.01)
    data = {}
    data['state'] = ["other words are removed from the list"]
    data['answer'] = [""]
    with open('static/state.json', 'w') as write_file:
        json.dump(data, write_file)
    print("... ... other words are removed from the list")
    return

def test(cur_word, word_list, desired_word):
    for i in range(len(desired_word)):
        if desired_word[i] == cur_word[i]:
            time.sleep(0.01)
            data = {}
            data['state'] = [str(i) + "th index is the same: " + desired_word[i]]
            data['answer'] = [""]
            with open('static/state.json', 'w') as write_file:
                json.dump(data, write_file)
            print(i, "th index is the same: ", desired_word[i])
            remove_others(i, word_list, desired_word)
"""

def try_words(word_list, desired_word):
    for cur_word in word_list:
        if cur_word != desired_word:
            show_on_screen(cur_word)
            #test(cur_word, word_list, desired_word)
        else:
            show_on_screen(cur_word)
            time.sleep(0.01)
            data = {}
            data['state'] = ["I find the word: " + cur_word]
            data['answer'] = [cur_word]
            with open('static/state.json', 'w') as write_file:
                json.dump(data, write_file)
            print("*********** I find the word ***********")
            return data['answer']

    if desired_word in word_list:
        for cur_word in word_list:
            if cur_word != desired_word:
                show_on_screen(cur_word)
            else:
                show_on_screen(cur_word)
                time.sleep(0.01)
                data = {}
                data['state'] = ["I find the word: " + cur_word]
                data['answer'] = [cur_word]
                with open('static/state.json', 'w') as write_file:
                    json.dump(data, write_file)
                print("*********** I find the word ***********")
                return data['answer']
    else:
        time.sleep(0.01)
        data = {}
        data['state'] = ["NOT FOUND!"]
        data['answer'] = [""]
        with open('static/state.json', 'w') as write_file:
            json.dump(data, write_file)
        print("*********** the word is not in the list ***********")
        return [""]
"""
word_list = ["safer", "safes", "sagas", "sager", "sages", "saggy", "sagos", "sahib", "saids", "sails", "saint", "saith", "sakes", "sakis", "salad", "salem", "sales", "sally", "salon", "salsa", "salts", "salty", "salve", "salvo", "samba", "sambo", "samoa", "sands", "sandy", "saned", "saner", "sanes", "sanga", "sangh", "sanka", "santa", "sapid", "sapor", "sappy", "sarah", "saran", "saree", "sarge", "saris", "sarod", "sassy", "satan", "sated", "sates", "satin", "satyr", "sauce", "saucy", "saudi", "sauls", "sault", "sauna", "saute", "saved", "saver", "saves", "savor", "savoy", "savvy", "sawed", "sawer", "saxes", "saxon", "sayee", "sayer", "sayst", "scabs", "scads", "scags", "scald", "scale", "scalp", "scaly", "scamp", "scams", "scans", "scant", "scape", "scare", "scarf", "scarp", "scars", "scary", "scats", "scene", "scent", "schmo", "schul", "schwa", "scion", "scoff", "scold", "scone", "scoop", "scoot", "scope", "score", "scorn", "scots", "scott", "scour", "scout", "scowl", "scows", "scrag", "scram", "scrap", "scree", "screw", "scrim", "scrip", "scrod", "scrub", "scuba", "scuds", "scuff", "sculk", "scull", "sculp", "scums", "scups", "scurf", "scuta", "scute", "scuts", "seals", "seams", "seamy", "sears", "seats", "sects", "sedan", "seder", "sedge", "sedgy", "sedum", "seeds", "seedy", "seeks", "seels", "seems", "seeps", "seepy", "seers", "segno", "segos", "segue", "seige", "seine", "seism", "seize", "selfs", "sells", "semen", "semis", "sends", "senna", "senor", "sense", "sensu", "senti", "seoul", "sepal", "sepia", "sepoy", "septa", "septs", "seral", "sered", "serer", "seres", "serfs", "serge", "serif", "serin", "serow", "serum", "serve", "servo", "setae", "setal", "seton", "setup", "seven", "sever", "sewed", "sewer", "sexed", "sexes", "sexto", "sexts", "shack", "shade", "shads", "shady", "shaft", "shags", "shahs", "shake", "shako", "shaky", "shale", "shall", "shalt", "shaly", "shame", "shams", "shank", "shape", "shard", "share", "shark", "sharp", "shave", "shawl", "shawm", "shawn", "shaws", "shays", "sheaf", "shear", "sheds", "sheen", "sheep", "sheer", "sheet", "sheik", "shelf", "shell", "sheol", "sherd", "shewn", "shews", "shied", "shier", "shies", "shift", "shill", "shily", "shims", "shine", "shins", "shiny", "ships", "shipt", "shire", "shirk", "shirr", "shirt", "shish", "shist", "shits", "shiva", "shive", "shivs", "shlep", "shoal", "shoat", "shock", "shoed", "shoer", "shoes", "shoji", "shone", "shook", "shoos", "shoot", "shope", "shops", "shore", "shorn", "short", "shote", "shots", "shout", "shove", "shown", "shows", "showy", "shred", "shrew", "shrub", "shrug", "shuck", "shuls", "shuns", "shunt", "shush", "shute", "shuts", "shyer", "shyly", "sibyl", "sicks", "sided", "sides", "sidle", "siege", "sieur", "sieve", "sifts", "sighs", "sight", "sigil", "sigma", "signs", "sikhs", "silex", "silks", "silky", "sills", "silly", "silos", "silts", "silty", "silva", "simon", "simps", "since", "sines", "sinew", "singe", "sings", "sinhs", "sinks", "sinus", "sioux", "sippy", "sired", "siree", "siren", "sires", "sirup", "sisal", "sissy", "sitar", "sited", "sites", "situp", "situs", "sixes", "sixte", "sixth", "sixty", "sized", "sizer", "sizes", "skags", "skald", "skate", "skean", "skeet", "skein", "skews", "skids", "skied", "skier", "skies", "skiey", "skiff", "skiis", "skill", "skimp", "skims", "skink", "skins", "skips", "skirl", "skirt", "skits", "skoal", "skuas", "skulk", "skull", "skunk", "skyed", "skyey", "slabs", "slack", "slags", "slain", "slake", "slams", "slang", "slant", "slaps", "slash", "slate", "slats", "slaty", "slave", "slavs", "slaws", "slays", "sleds", "sleek", "sleep", "sleet", "slept", "slews", "slice", "slick", "slide", "slier", "slily", "slime", "slims", "slimy", "sling", "slink", "slips", "slipt", "slits", "slobs", "sloes", "slogs", "sloop", "slope", "slops", "slosh", "sloth", "slots", "slows", "slubs", "slued", "slues", "slugs", "slump", "slums", "slung", "slunk", "slurp", "slurs", "slush", "sluts", "slyer", "slyly", "smack", "small", "smart", "smash", "smear", "smell", "smelt", "smile", "smirk", "smite", "smith", "smock", "smoke", "smoky", "smote", "smuts", "snack", "snafu", "snags", "snail", "snake", "snaky", "snaps", "snare", "snark", "snarl", "sneak", "sneer", "snick", "snide", "sniff", "snipe", "snips", "snits", "snobs", "snood", "snoop", "snoot", "snore", "snort", "snots", "snout", "snows", "snowy", "snubs", "snuck", "snuff", "snugs", "soaks", "soaps", "soapy", "soars", "soave", "sober", "socks", "sodas", "soddy", "sodom", "sofar", "sofas", "sofia", "softs", "softy", "soggy", "soils", "solar", "soled", "soles", "solid", "solos", "solve", "somas", "sonar", "sonde", "sones", "songs", "sonic", "sonny", "sooey", "sooth", "soots", "sooty", "sophs", "sophy", "sopor", "soppy", "sorel", "sorer", "sores", "sorry", "sorts", "sough", "souls", "sound", "soups", "soupy", "sours", "souse", "south", "sowed", "sower", "soyas", "space", "spade", "spain", "spake", "spale", "spank", "spans", "spare", "spark", "spars", "spasm", "spate", "spats", "spawn", "spays", "speak", "spear", "speck", "specs", "speed", "spell", "spelt", "spend", "spent", "sperm", "spews", "spica", "spice", "spick", "spics", "spicy", "spied", "spiel", "spier", "spies", "spiff", "spike", "spiky", "spill", "spilt", "spine", "spins", "spiny", "spire", "spiry", "spite", "spits", "spitz", "splat", "splay", "split", "spoil", "spoke", "spoof", "spook", "spool", "spoon", "spoor", "spore", "sport", "spots", "spout", "sprat", "spray", "spree", "sprig", "sprit", "spuds", "spued", "spues", "spume", "spumy", "spunk", "spurn", "spurs", "spurt", "sputa", "squab", "squad", "squat", "squaw", "squib", "squid", "stabs", "stack", "staff", "stage", "stags", "stagy", "staid", "stain", "stair", "stake", "stale", "stalk", "stall", "stamp", "stand", "stank", "staph", "stare", "stark", "stars", "start", "stash", "state", "stats", "stave", "stays", "stead", "steak", "steal", "steam", "steed", "steel", "steep", "steer", "stein", "stele", "stems", "steno", "steps", "stere", "stern"]
desired_word  = "smart"
try_words(word_list, desired_word)
"""

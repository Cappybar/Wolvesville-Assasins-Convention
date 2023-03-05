

roles = ('doctor','bodyguard','vigilante','jailer','warden','priest','seer','detective','sheriff','medium','mayor','witch','loudmouth','cupid',
         'cursed','fool','headhunter','arsonist','corruptor','bandit','butcher','flagger','gunner','marksman','analyst','gambler','mortician',
         'violinist','ritualist','conjuror','baker','preacher','astronomer','forger','avenger','trapper','bell-ringer','pacifist','instigator',
         'wolffluencer','sorcerer','bomber','cannibal','illusionist','zombie','alchemist','villager','president')

double_roles = ('red lady','aura seer','beast hunter','flower child','junior werewolf','nightmare werewolf','wolf shaman','shadow wolf','guardian wolf','alpha werewolf',
                'wolf seer','serial killer','night watchman','tough guy','ghost lady','spirit seer','seer apprentice','grumpy grandma','werewolf fan','grave robber',
                'voodoo werewolf','kitten wolf','wolf pacifist','jelly wolf','werewolf berserk','wolf summoner','stubborn werewolf','storm wolf','split wolf',
                'wolf trickster','sect leader','regular werewolf','pumpkin king','easter bunny','fortune teller')


while 1:
    chars = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
             'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, '-':0 ,' ':0}
    roles_result = []
    def count_char(role):
        for i in role:
            chars[i] += 1


    char_length = input("\nchar length: \n")
    if char_length[0] == 'f':
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        for i in range(len(double_roles)):
            halfrole = double_roles[i].split()
            #print(halfrole)
            if len(halfrole[0]) == int(char_length[1]):
                print(f"{double_roles[i]}")
                count_char(double_roles[i])
                roles_result.append(double_roles[i])
        print("\n")
        sorted_chars = sorted(chars.items(), key=lambda x: x[1])[::-1]
        new_sorted_chars = []
        for i in sorted_chars:
            if i[1] > 0:
                new_sorted_chars.append(i)
        new_sorted_chars_no_value = list(dict(new_sorted_chars).keys())

        top5 = 0
        for letter in new_sorted_chars_no_value:
            if top5 == 5:
                print("\n")
            count = 0
            for role in roles_result:
                if letter in role:
                    count += 1
            print(f"{letter} probability is {int((count / len(roles_result)) * 100)}%")
            top5 += 1
    elif char_length[0] == 'l':
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        for i in range(len(double_roles)):
            halfrole = double_roles[i].split()
            #print(halfrole)
            if len(halfrole[1]) == int(char_length[1]):
                print(f"{double_roles[i]}")
                count_char(double_roles[i])
                roles_result.append(double_roles[i])
        print("\n")
        sorted_chars = sorted(chars.items(), key=lambda x: x[1])[::-1]
        new_sorted_chars = []
        for i in sorted_chars:
            if i[1] > 0:
                new_sorted_chars.append(i)
        new_sorted_chars_no_value = list(dict(new_sorted_chars).keys())

        top5 = 0
        for letter in new_sorted_chars_no_value:
            if top5 == 5:
                print("\n")
            count = 0
            for role in roles_result:
                if letter in role:
                    count += 1
            print(f"{letter} probability is {int((count / len(roles_result)) * 100)}%")
            top5 += 1
    else:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        for i in range(len(roles)):
            if len(roles[i]) == int(char_length):
                print(f"{roles[i]}")
                count_char(roles[i])
                roles_result.append(roles[i])
        print("\n")
        sorted_chars = sorted(chars.items(), key=lambda x: x[1])[::-1]
        new_sorted_chars = []
        for i in sorted_chars:
            if i[1] > 0:
                new_sorted_chars.append(i)
        new_sorted_chars_no_value = list(dict(new_sorted_chars).keys())

        top5 = 0
        for letter in new_sorted_chars_no_value:
            if top5 == 5:
                print("\n")
            count = 0
            for role in roles_result:
                if letter in role:
                    count += 1
            print(f"{letter} probability is {int((count / len(roles_result)) * 100)}%")
            top5 += 1

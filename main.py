from dict import enchmnts, recipients

def sep_words(name: str, sep: str, lower: bool = False, upper: bool = False, capitalise: bool = False,) -> str:
    '''
    A general use version of mc_id(name) with no default word-seperator and extra formatting options
    '''

def mc_id(name: str,mc=False) -> str:
    '''
    Turns string to lowercase,
    Splits words in string into a list,
    Join words with underscores
    '''
    if mc:
        return "minecraft:" + "_".join(name.lower().split())
    return "_".join(name.lower().split())

def give_item():
    enchantments = set()

    print("Input Item: ",end="") 
    item = f"minecraft:{mc_id(input())}"

    print()

    print("[Y/N] Custom Name: ",end="")
    isCustomName:str = input().upper()
    isCustomName:bool = True if isCustomName == "Y" else False if isCustomName == "N" else None
    
    print()

    print("[Y/N] Custom Lore: ",end="")
    isCustomLore:str = input().upper()
    isCustomLore:bool = True if isCustomLore == "Y" else False if isCustomName == "N" else None

    if isCustomName:
        print()
        print("Custom Name: ",end="")
        custom_name:str = input()

    if isCustomLore:
        print()
        print("Custom Lore: ",end="")
        custom_lore:str = input()
        print()

    print("Input Quantity: ",end="")
    quantity:str = input()

    print()

    print("[1] Nearest Player")
    print("[2] Random Player")
    print("[3] All Players")
    print("[4] All Entites")
    print("Input Recipient: ",end="")
    player:int = int(input())

    print()

    print("[Y/N] Enchantments: ",end="")
    isEnchantments:str = input().upper()
    isEnchantments:bool = True if isEnchantments == "Y" else False if isEnchantments == "N" else None

    if isEnchantments:
        print("""
    Enchantments:
        [1]  Aqua Affinity
        [2]  Bane of Arthropods
        [3]  Blast Protection
        [4]  Channeling
        [5]  Curse of Binding
        [6]  Curse of Vanishing
        [7]  Depth Strider
        [8]  Efficiency
        [9]  Feather Falling
        [10] Fire Aspect
        [11] Fire Protection
        [12] Flame
        [13] Fortune
        [14] Frost Walker
        [15] Impaling
        [16] Infinity
        [17] Knockback
        [18] Looting
        [19] Loyalty
        [20] Luck of the Sea
        [21] Lure
        [22] Mending
        [23] Multishot
        [24] Piercing
        [25] Power
        [26] Projectile Protection
        [27] Protection
        [28] Punch
        [29] Quick Charge
        [30] Respiration
        [31] Riptide
        [32] Sharpness
        [33] Silk Touch
        [34] Smite
        [35] Soul Speed
        [36] Sweeping Edge
        [37] Thorns
        [38] Unbreaking
    [100] to Exit
    """)

        ench_names = []

        while True:
            e = []
            print("Enchantment Number: ",end="")        
            enchmnt = int(input())
            
            if enchmnt != 100: e.append(mc_id(enchmnts[enchmnt],mc=True))
            else: break

            print("\nEnchantment Level: ",end="")
            e.append(input())

            if enchmnt not in ench_names:
                enchantments.add(tuple(e))
                ench_names.append(enchmnt)

            print()

    # Command Concentration

    command = f"/give {recipients[player]} {item}"

    enchantments = list(enchantments)

    if isEnchantments:
        command += "{Enchantments:["

        for enchantment in enchantments:
            e = f"id:\"{enchantment[0]}\",lvl:{enchantment[1]}"


            command += "{"
            command += e
            command += "}"

            if enchantment != tuple(enchantments[-1]):
                command += ", "
            else:
                command += "]"

    if isCustomName:
        if isCustomLore:
            n = f"Name:\"{custom_name}\",Lore:\"{custom_lore}\""
        else:
            n = f"Name:\"{custom_name}\""

        if isEnchantments:
            command += ", "
        else:
            command += "{"
        command += "display:{Name:"
        command += "\""
        command += custom_name
        command += "\""
        command += "}"

    command += "}"
    command += " "
    command += quantity

    print()
    print(command)
    print()
    
give_item()

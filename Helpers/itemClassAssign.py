def item_class_assign(item):
    item_type = 7
    item_sub_type = 11
    if item["class"] == 0:
        item_type = "consumable"
        if item["subclass"] == 0:
            item_sub_type = "generic"
        elif item["subclass"] == 1:
            item_sub_type = "potion"
        elif item["subclass"] == 2:
            item_sub_type = "elixir"
        elif item["subclass"] == 3:
            item_sub_type = "scroll"
        elif item["subclass"] == 4:
            item_sub_type = "food and drink"
        elif item["subclass"] == 5:
            item_sub_type = "item enhancement"
        elif item["subclass"] == 6:
            item_sub_type = "bandage"
    elif item["class"] == 1:
        item_type = "container"
        if item["subclass"] == 0:
            item_sub_type = "bag"
        elif item["subclass"] == 1:
            item_sub_type = "soul bag"
        elif item["subclass"] == 2:
            item_sub_type = "herb bag"
        elif item["subclass"] == 3:
            item_sub_type = "enchanting bag"
        elif item["subclass"] == 4:
            item_sub_type = "engineering bag"
        elif item["subclass"] == 5:
            item_sub_type = "gem bag"
        elif item["subclass"] == 6:
            item_sub_type = "mining bag"
        elif item["subclass"] == 7:
            item_sub_type = "leatherworking bag"
        elif item["subclass"] == 8:
            item_sub_type = "inscription bag"
        elif item["subclass"] == 9:
            item_sub_type = "tackle box"
        elif item["subclass"] == 10:
            item_sub_type = "cooking bag"
    elif item["class"] == 2:
        item_type = "weapon"
        if item["subclass"] == 0:
            item_sub_type = "one-handed axes"
        elif item["subclass"] == 1:
            item_sub_type = "two-handed axes"
        elif item["subclass"] == 2:
            item_sub_type = "bows"
        elif item["subclass"] == 3:
            item_sub_type = "guns"
        elif item["subclass"] == 4:
            item_sub_type = "one-handed maces"
        elif item["subclass"] == 5:
            item_sub_type = "two-handed maces"
        elif item["subclass"] == 6:
            item_sub_type = "polearms"
        elif item["subclass"] == 7:
            item_sub_type = "one-handed sword"
        elif item["subclass"] == 8:
            item_sub_type = "two-handed sword"
        elif item["subclass"] == 9:
            item_sub_type = "warglaives"
        elif item["subclass"] == 10:
            item_sub_type = "staves"
        elif item["subclass"] == 11:
            item_sub_type = "bear claws"
        elif item["subclass"] == 12:
            item_sub_type = "cat claws"
        elif item["subclass"] == 13:
            item_sub_type = "fist weapons"
        elif item["subclass"] == 14:
            item_sub_type = "miscellaneous"
        elif item["subclass"] == 15:
            item_sub_type = "daggers"
        elif item["subclass"] == 16:
            item_sub_type = "thrown"
        elif item["subclass"] == 17:
            item_sub_type = "spears"
        elif item["subclass"] == 18:
            item_sub_type = "crossbows"
        elif item["subclass"] == 19:
            item_sub_type = "wands"
        elif item["subclass"] == 20:
            item_sub_type = "fishing poles"
    elif item["class"] == 4:
        item_type = "armor"
        if item["subclass"] == 0:
            item_sub_type = "jewlrey"  # Miscellaneous Includes Spellstones, Firestones, Trinkets, Rings and Necks
        elif item["subclass"] == 1:
            item_sub_type = "cloth"
        elif item["subclass"] == 2:
            item_sub_type = "leather"
        elif item["subclass"] == 3:
            item_sub_type = "mail"
        elif item["subclass"] == 4:
            item_sub_type = "plate"
        elif item["subclass"] == 5:
            item_sub_type = "cosmetic"
        elif item["subclass"] == 6:
            item_sub_type = "shields"
    elif item["class"] == 5:
        item_type = "reagent"
    elif item["class"] == 6:
        item_type = "projectile"
        if item["subclass"] == 2:
            item_sub_type = "arrow"
        elif item["subclass"] == 3:
            item_sub_type = "bullet"
    elif item["class"] == 7:
        item_type = "trade goods"
        if item["subclass"] == 0:
            item_sub_type = "herbs"
        if item["subclass"] == 1:
            item_sub_type = "parts"
        elif item["subclass"] == 2:
            item_sub_type = "explosives"
        elif item["subclass"] == 3:
            item_sub_type = "devices"
        elif item["subclass"] == 4:
            item_sub_type = "jewelry"
        elif item["subclass"] == 5:
            item_sub_type = "cloth"
        elif item["subclass"] == 6:
            item_sub_type = "leather"
        elif item["subclass"] == 7:
            item_sub_type = "metal and stone"
        elif item["subclass"] == 8:
            item_sub_type = "cooking"
        elif item["subclass"] == 9:
            item_sub_type = "herbs"
        elif item["subclass"] == 10:
            item_sub_type = "elemental"
        elif item["subclass"] == 11:
            item_sub_type = "other"
        elif item["subclass"] == 12:
            item_sub_type = "enchanting"
    elif item["class"] == 8:
        item_type = "item enhancement"
    elif item["class"] == 9:
        item_type = "recipe"
        if item["subclass"] == 0:
            item_sub_type = "book"
        elif item["subclass"] == 1:
            item_sub_type = "leatherworking recipe"
        elif item["subclass"] == 2:
            item_sub_type = "tailoring recipe"
        elif item["subclass"] == 3:
            item_sub_type = "engineering recipe"
        elif item["subclass"] == 4:
            item_sub_type = "blacksmithing recipe"
        elif item["subclass"] == 5:
            item_sub_type = "cooking recipe"
        elif item["subclass"] == 6:
            item_sub_type = "alchemy recipe"
        elif item["subclass"] == 7:
            item_sub_type = "first Aid"
        elif item["subclass"] == 8:
            item_sub_type = "enchanting recipe"
        elif item["subclass"] == 9:
            item_sub_type = "fishing"
    elif item["class"] == 11:
        item_type = "quiver"
        if item["subclass"] == 2:
            item_sub_type = "quiver"
        elif item["subclass"] == 3:
            item_sub_type = "ammo"
    elif item["class"] == 12:
        item_type = "quest item"
        item_sub_type = "quest"
    elif item["class"] == 13:
        item_type = "key"
        if item["subclass"] == 0:
            item_sub_type = "key"
        elif item["subclass"] == 1:
            item_sub_type = "lockpick"
    elif item["class"] == 15:
        item_type = "miscellaneous"
        if item["subclass"] == 0:
            item_sub_type = "junk"
        elif item["subclass"] == 1:
            item_sub_type = "reagent"
        elif item["subclass"] == 2:
            item_sub_type = "companion pet"
        elif item["subclass"] == 3:
            item_sub_type = "holiday"
        elif item["subclass"] == 4:
            item_sub_type = "other"
        elif item["subclass"] == 5:
            item_sub_type = "mount"
        elif item["subclass"] == 6:
            item_sub_type = "mount equipment"

    return {"item_type": item_type, "item_sub_type": item_sub_type}

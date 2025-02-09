def item_class_assign(item):
    item_type = 7
    item_sub_type = 11
    print(item)
    if item["class"] == 0:
        item_type = "consumable"
        if item["subclass"] == 0:
            item_sub_type = "generic"
        elif item["subclass"] == 1:
            item_sub_type = "Potion"
        elif item["subclass"] == 2:
            item_sub_type = "Elixir"
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
            item_sub_type = "Bag"
        elif item["subclass"] == 1:
            item_sub_type = "Soul bag"
        elif item["subclass"] == 2:
            item_sub_type = "Herb bag"
        elif item["subclass"] == 3:
            item_sub_type = "Enchanting bag"
        elif item["subclass"] == 4:
            item_sub_type = "Engineering bag"
        elif item["subclass"] == 5:
            item_sub_type = "Gem bag"
        elif item["subclass"] == 6:
            item_sub_type = "Mining bag"
        elif item["subclass"] == 7:
            item_sub_type = "Leatherworking bag"
        elif item["subclass"] == 8:
            item_sub_type = "Inscription Bag"
        elif item["subclass"] == 9:
            item_sub_type = "Tackle Box"
        elif item["subclass"] == 10:
            item_sub_type = "Cooking Bag"
    elif item["class"] == 2:
        item_type = "weapon"
        if item["subclass"] == 0:
            item_sub_type = "One-handed axes"
        elif item["subclass"] == 1:
            item_sub_type = "Two-handed axes"
        elif item["subclass"] == 2:
            item_sub_type = "Bows"
        elif item["subclass"] == 3:
            item_sub_type = "Guns"
        elif item["subclass"] == 4:
            item_sub_type = "One-handed maces"
        elif item["subclass"] == 5:
            item_sub_type = "Two-handed maces"
        elif item["subclass"] == 6:
            item_sub_type = "Polearms"
        elif item["subclass"] == 7:
            item_sub_type = "One-handed sword"
        elif item["subclass"] == 8:
            item_sub_type = "Two-handed sword"
        elif item["subclass"] == 9:
            item_sub_type = "Warglaives"
        elif item["subclass"] == 10:
            item_sub_type = "Staves"
        elif item["subclass"] == 11:
            item_sub_type = "Bear Claws"
        elif item["subclass"] == 12:
            item_sub_type = "Cat Claws"
        elif item["subclass"] == 13:
            item_sub_type = "Fist Weapons"
        elif item["subclass"] == 14:
            item_sub_type = "Miscellaneous"
        elif item["subclass"] == 15:
            item_sub_type = "Daggers"
        elif item["subclass"] == 16:
            item_sub_type = "Thrown"
        elif item["subclass"] == 17:
            item_sub_type = "Spears"
        elif item["subclass"] == 18:
            item_sub_type = "Crossbows"
        elif item["subclass"] == 19:
            item_sub_type = "Wands"
        elif item["subclass"] == 20:
            item_sub_type = "Fishing Poles"
    elif item["class"] == 4:
        item_type = "armor"
        if item["subclass"] == 0:
            item_sub_type = "Jewlrey"  # Miscellaneous Includes Spellstones, Firestones, Trinkets, Rings and Necks
        elif item["subclass"] == 1:
            item_sub_type = "Cloth"
        elif item["subclass"] == 2:
            item_sub_type = "Leather"
        elif item["subclass"] == 3:
            item_sub_type = "Mail"
        elif item["subclass"] == 4:
            item_sub_type = "Plate"
        elif item["subclass"] == 5:
            item_sub_type = "Cosmetic"
        elif item["subclass"] == 6:
            item_sub_type = "Shields"
    elif item["class"] == 5:
        item_type = "reagent"
    elif item["class"] == 6:
        item_type = "projectile"
        if item["subclass"] == 2:
            item_sub_type = "Arrow"
        elif item["subclass"] == 3:
            item_sub_type = "Bullet"
    elif item["class"] == 7:
        item_type = "trade goods"
        if item["subclass"] == 1:
            item_sub_type = "Parts"
        elif item["subclass"] == 2:
            item_sub_type = "Explosives"
        elif item["subclass"] == 3:
            item_sub_type = "Devices"
        elif item["subclass"] == 4:
            item_sub_type = "Jewelry"
        elif item["subclass"] == 5:
            item_sub_type = "Cloth"
        elif item["subclass"] == 6:
            item_sub_type = "Leather"
        elif item["subclass"] == 7:
            item_sub_type = "Metal and Stone"
        elif item["subclass"] == 8:
            item_sub_type = "Cooking"
        elif item["subclass"] == 9:
            item_sub_type = "Herbs"
        elif item["subclass"] == 10:
            item_sub_type = "Elemental"
        elif item["subclass"] == 11:
            item_sub_type = "Other"
        elif item["subclass"] == 12:
            item_sub_type = "Enchanting"
    elif item["class"] == 8:
        item_type = "Item Enhancement"
    elif item["class"] == 9:
        item_type = "Recipe"
        if item["subclass"] == 0:
            item_sub_type = "Book"
        elif item["subclass"] == 1:
            item_sub_type = "Leatherworking Recipe"
        elif item["subclass"] == 2:
            item_sub_type = "Tailoring Recipe"
        elif item["subclass"] == 3:
            item_sub_type = "Engineering Recipe"
        elif item["subclass"] == 4:
            item_sub_type = "Blacksmithing Recipe"
        elif item["subclass"] == 5:
            item_sub_type = "Cooking Recipe"
        elif item["subclass"] == 6:
            item_sub_type = "Alchemy Recipe"
        elif item["subclass"] == 7:
            item_sub_type = "First Aid"
        elif item["subclass"] == 8:
            item_sub_type = "Enchanting Recipe"
        elif item["subclass"] == 9:
            item_sub_type = "Fishing"
    elif item["class"] == 11:
        item_type = "Quiver"
        if item["subclass"] == 2:
            item_sub_type = "Quiver"
        elif item["subclass"] == 3:
            item_sub_type = "Ammo"
    elif item["class"] == 12:
        item_type = "Quest Item"
        item_sub_type = "Quest"
    elif item["class"] == 13:
        item_type = "key"
        if item["subclass"] == 0:
            item_sub_type = "Key"
        elif item["subclass"] == 1:
            item_sub_type = "Lockpick"
    elif item["class"] == 15:
        item_type = "Miscellaneous"
        if item["subclass"] == 0:
            item_sub_type = "Junk"
        elif item["subclass"] == 1:
            item_sub_type = "Reagent"
        elif item["subclass"] == 2:
            item_sub_type = "Companion Pet"
        elif item["subclass"] == 3:
            item_sub_type = "Holiday"
        elif item["subclass"] == 4:
            item_sub_type = "Other"
        elif item["subclass"] == 5:
            item_sub_type = "Mount"
        elif item["subclass"] == 6:
            item_sub_type = "Mount Equipment"

    return {"item_type": item_type, "item_sub_type": item_sub_type}

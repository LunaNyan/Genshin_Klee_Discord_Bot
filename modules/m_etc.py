import sys

if __name__=="__main__":
    print("FATAL   : Run this bot from right way.")
    sys.exit(1)

def reset_stats(db, message):
    gm = int(db.get(str(message.author.id), "gacha_mode"))
    db.set(str(message.author.id), "stack_5star_pull_" + str(gm), "0")
    db.set(str(message.author.id), "stack_4star_pull_" + str(gm), "0")
    if gm != 3:
        db.set(str(message.author.id), "stack_5star_nothope_" + str(gm), "0")
        db.set(str(message.author.id), "stack_4star_nothope_" + str(gm), "0")
        db.set(str(message.author.id), "total_nothope_" + str(gm), "0")
    db.set(str(message.author.id), "total_pull_" + str(gm), "0")
    db.set(str(message.author.id), "total_5star_" + str(gm), "0")
    db.set(str(message.author.id), "total_4star_" + str(gm), "0")
    db.set(str(message.author.id), "total_3star_" + str(gm), "0")
    db.set(str(message.author.id), "total_character_" + str(gm), "0")
    db.set(str(message.author.id), "total_item_" + str(gm), "0")


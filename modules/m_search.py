import sys, discord

#if __name__=="__main__":
#    print("FATAL   : Run this bot from right way.")
#    sys.exit(1)

import m_gacha_pull

def search(db, message, m):
    dba = m_gacha_pull.get_gacha_mode(db, message)
    sl = []
    for i in dba[1]:
        sl.append(i)
    for i in dba[2]:
        sl.append(i)
    for i1 in sl:
        for i2 in i1:
            if m in i2:
                return True
            else:
                pass
    return False
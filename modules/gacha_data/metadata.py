import C0100A_venti, C0100B_klee, \
        C0101A_childe, C0101B_zhongli, \
        C0102A_albedo, C0102B_ganyu, \
        C0103A_xiao, C0103B_keqing, C0103C_hutao, \
        C0104A_venti, C0104B_childe, \
        C0105A_zhongli, C0105B_eula, \
        C0106A_klee, C0106B_kazuha, \
        C0200A_ayaka, C0200B_yoimiya, \
        C0201A_raiden, C0201B_kokomi, \
        C0202A_childe, C0202B_hutao, \
        C0203AA_albedo, C0203AB_eula, C0203B_itto, \
        C0204AA_shenhe, C0204AB_xiao, \
        C0204BA_zhongli, C0204BB_ganyu, \
        C0205AA_yaemiko, \
        C0205BA_raiden, C0205BB_kokomi, \
        C0206AA_ayato, C0206AB_venti, \
        C0206B_ayaka, \
        W0100A, W0100B, \
        W0101A, W0101B, \
        W0102A, W0102B, \
        W0103A, W0103B, \
        W0104A, W0104B, \
        W0105A, W0105B, \
        W0106A, W0106B, \
        W0200A, W0200B, \
        W0201A, W0201B, \
        W0202A, W0202B, \
        W0203A, W0203B, \
        W0204A, W0204B, \
        W0205A, W0205B, \
        W0206A, \
        S0100_standard, \
        C0000Z_3stars

current_standard = "S0100"

# 이중 픽업 진행 시 대응 방법
# current_char_sub에 첫번째 픽업, current_char에 두번째 픽업을 넣고 update하시면 됩니다.
# 단일 픽업일 경우 current_char_sub은 None으로 두시면 됩니다.

current_char_sub = "C0205BA"
current_char = "C0205BB"

current_weapon = "W0205B0"

def get_gacha_data(id):
    if id == "C0100A":
        return ["C0100A", [C0100A_venti.data_name, C0100A_venti.data_ver, C0100A_venti.run_date], C0100A_venti.wishlists, C0100A_venti.meta_prob, C0100A_venti.stack_group]
    elif id == "C0100B":
        return ["C0100B", [C0100B_klee.data_name, C0100B_klee.data_ver, C0100B_klee.run_date], C0100B_klee.wishlists, C0100B_klee.meta_prob, C0100B_klee.stack_group]
    elif id == "C0101A":
        return ["C0101A", [C0101A_childe.data_name, C0101A_childe.data_ver, C0101A_childe.run_date], C0101A_childe.wishlists, C0101A_childe.meta_prob, C0101A_childe.stack_group]
    elif id == "C0101B":
        return ["C0101B", [C0101B_zhongli.data_name, C0101B_zhongli.data_ver, C0101B_zhongli.run_date], C0101B_zhongli.wishlists, C0101B_zhongli.meta_prob, C0101B_zhongli.stack_group]
    elif id == "C0102A":
        return ["C0102A", [C0102A_albedo.data_name, C0102A_albedo.data_ver, C0102A_albedo.run_date], C0102A_albedo.wishlists, C0102A_albedo.meta_prob, C0102A_albedo.stack_group]
    elif id == "C0102B":
        return ["C0102B", [C0102B_ganyu.data_name, C0102B_ganyu.data_ver, C0102B_ganyu.run_date], C0102B_ganyu.wishlists, C0102B_ganyu.meta_prob, C0102B_ganyu.stack_group]
    elif id == "C0103A":
        return ["C0103A", [C0103A_xiao.data_name, C0103A_xiao.data_ver, C0103A_xiao.run_date], C0103A_xiao.wishlists, C0103A_xiao.meta_prob, C0103A_xiao.stack_group]
    elif id == "C0103B":
        return ["C0103B", [C0103B_keqing.data_name, C0103B_keqing.data_ver, C0103B_keqing.run_date], C0103B_keqing.wishlists, C0103B_keqing.meta_prob, C0103B_keqing.stack_group]
    elif id == "C0103C":
        return ["C0103C", [C0103C_hutao.data_name, C0103C_hutao.data_ver, C0103C_hutao.run_date], C0103C_hutao.wishlists, C0103C_hutao.meta_prob, C0103C_hutao.stack_group]
    elif id == "C0104A":
        return ["C0104A", [C0104A_venti.data_name, C0104A_venti.data_ver, C0104A_venti.run_date], C0104A_venti.wishlists, C0104A_venti.meta_prob, C0104A_venti.stack_group]
    elif id == "C0104B":
        return ["C0104B", [C0104B_childe.data_name, C0104B_childe.data_ver, C0104B_childe.run_date], C0104B_childe.wishlists, C0104B_childe.meta_prob, C0104B_childe.stack_group]
    elif id == "C0105A":
        return ["C0105A", [C0105A_zhongli.data_name, C0105A_zhongli.data_ver, C0105A_zhongli.run_date], C0105A_zhongli.wishlists, C0105A_zhongli.meta_prob, C0105A_zhongli.stack_group]
    elif id == "C0105B":
        return ["C0105B", [C0105B_eula.data_name, C0105B_eula.data_ver, C0105B_eula.run_date], C0105B_eula.wishlists, C0105B_eula.meta_prob, C0105B_eula.stack_group]
    elif id == "C0106A":
        return ["C0106A", [C0106A_klee.data_name, C0106A_klee.data_ver, C0106A_klee.run_date], C0106A_klee.wishlists, C0106A_klee.meta_prob, C0106A_klee.stack_group]
    elif id == "C0106B":
        return ["C0106B", [C0106B_kazuha.data_name, C0106B_kazuha.data_ver, C0106B_kazuha.run_date], C0106B_kazuha.wishlists, C0106B_kazuha.meta_prob, C0106B_kazuha.stack_group]
    elif id == "C0200A":
        return ["C0200A", [C0200A_ayaka.data_name, C0200A_ayaka.data_ver, C0200A_ayaka.run_date], C0200A_ayaka.wishlists, C0200A_ayaka.meta_prob, C0200A_ayaka.stack_group]
    elif id == "C0200B":
        return ["C0200B", [C0200B_yoimiya.data_name, C0200B_yoimiya.data_ver, C0200B_yoimiya.run_date], C0200B_yoimiya.wishlists, C0200B_yoimiya.meta_prob, C0200B_yoimiya.stack_group]
    elif id == "C0201A":
        return ["C0201A", [C0201A_raiden.data_name, C0201A_raiden.data_ver, C0201A_raiden.run_date], C0201A_raiden.wishlists, C0201A_raiden.meta_prob, C0201A_raiden.stack_group]
    elif id == "C0201B":
        return ["C0201B", [C0201B_kokomi.data_name, C0201B_kokomi.data_ver, C0201B_kokomi.run_date], C0201B_kokomi.wishlists, C0201B_kokomi.meta_prob, C0201B_kokomi.stack_group]
    elif id == "C0202A":
        return ["C0202A", [C0202A_childe.data_name, C0202A_childe.data_ver, C0202A_childe.run_date], C0202A_childe.wishlists, C0202A_childe.meta_prob, C0202A_childe.stack_group]
    elif id == "C0202B":
        return ["C0202b", [C0202B_hutao.data_name, C0202B_hutao.data_ver, C0202B_hutao.run_date], C0202B_hutao.wishlists, C0202B_hutao.meta_prob, C0202B_hutao.stack_group]
    elif id == "C0203AA":
        return ["C0203AA", [C0203AA_albedo.data_name, C0203AA_albedo.data_ver, C0203AA_albedo.run_date], C0203AA_albedo.wishlists, C0203AA_albedo.meta_prob, C0203AA_albedo.stack_group]
    elif id == "C0203AB":
        return ["C0203AB", [C0203AB_eula.data_name, C0203AB_eula.data_ver, C0203AB_eula.run_date], C0203AB_eula.wishlists, C0203AB_eula.meta_prob, C0203AB_eula.stack_group]
    elif id == "C0203B":
        return ["C0203B", [C0203B_itto.data_name, C0203B_itto.data_ver, C0203B_itto.run_date], C0203B_itto.wishlists, C0203B_itto.meta_prob, C0203B_itto.stack_group]
    elif id == "C0204AA":
        return ["C0204AA", [C0204AA_shenhe.data_name, C0204AA_shenhe.data_ver, C0204AA_shenhe.run_date], C0204AA_shenhe.wishlists, C0204AA_shenhe.meta_prob, C0204AA_shenhe.stack_group]
    elif id == "C0204AB":
        return ["C0204AB", [C0204AB_xiao.data_name, C0204AB_xiao.data_ver, C0204AB_xiao.run_date], C0204AB_xiao.wishlists, C0204AB_xiao.meta_prob, C0204AB_xiao.stack_group]
    elif id == "C0204BA":
        return ["C0204BA", [C0204BA_zhongli.data_name, C0204BA_zhongli.data_ver, C0204BA_zhongli.run_date], C0204BA_zhongli.wishlists, C0204BA_zhongli.meta_prob, C0204BA_zhongli.stack_group]
    elif id == "C0204BB":
        return ["C0204BB", [C0204BB_ganyu.data_name, C0204BB_ganyu.data_ver, C0204BB_ganyu.run_date], C0204BB_ganyu.wishlists, C0204BB_ganyu.meta_prob, C0204BB_ganyu.stack_group]
    elif id == "C0205AA":
        return ["C0205AA", [C0205AA_yaemiko.data_name, C0205AA_yaemiko.data_ver, C0205AA_yaemiko.run_date], C0205AA_yaemiko.wishlists, C0205AA_yaemiko.meta_prob, C0205AA_yaemiko.stack_group]
    elif id == "C0205BA":
        return ["C0205BA", [C0205BA_raiden.data_name, C0205BA_raiden.data_ver, C0205BA_raiden.run_date], C0205BA_raiden.wishlists, C0205BA_raiden.meta_prob, C0205BA_raiden.stack_group]
    elif id == "C0205BB":
        return ["C0205BB", [C0205BB_kokomi.data_name, C0205BB_kokomi.data_ver, C0205BB_kokomi.run_date], C0205BB_kokomi.wishlists, C0205BB_kokomi.meta_prob, C0205BB_kokomi.stack_group]
    elif id == "C0206AA":
        return ["C0206AA", [C0206AA_ayato.data_name, C0206AA_ayato.data_ver, C0206AA_ayato.run_date], C0206AA_ayato.wishlists, C0206AA_ayato.meta_prob, C0206AA_ayato.stack_group]
    elif id == "C0206AB":
        return ["C0206AB", [C0206AB_venti.data_name, C0206AB_venti.data_ver, C0206AB_venti.run_date], C0206AB_venti.wishlists, C0206AB_venti.meta_prob, C0206AB_venti.stack_group]
    elif id == "C0206B":
        return ["C0206B", [C0206B_ayaka.data_name, C0206B_ayaka.data_ver, C0206B_ayaka.run_date], C0206B_ayaka.wishlists, C0206B_ayaka.meta_prob, C0206B_ayaka.stack_group]
    elif id == "W0100A0":
        return ["W0100A0", [W0100A.data_name, W0100A.data_ver, W0100A.run_date], W0100A.wishlists, W0100A.meta_prob, W0100A.stack_group]
    elif id == "W0100B0":
        return ["W0100B0", [W0100B.data_name, W0100B.data_ver, W0100B.run_date], W0100B.wishlists, W0100B.meta_prob, W0100B.stack_group]
    elif id == "W0101A0":
        return ["W0101A0", [W0101A.data_name, W0101A.data_ver, W0101A.run_date], W0101A.wishlists, W0101A.meta_prob, W0101A.stack_group]
    elif id == "W0101B0":
        return ["W0101B0", [W0101B.data_name, W0101B.data_ver, W0101B.run_date], W0101B.wishlists, W0101B.meta_prob, W0101B.stack_group]
    elif id == "W0102A0":
        return ["W0102A0", [W0102A.data_name, W0102A.data_ver, W0102A.run_date], W0102A.wishlists, W0102A.meta_prob, W0102A.stack_group]
    elif id == "W0102B0":
        return ["W0102B0", [W0102B.data_name, W0102B.data_ver, W0102B.run_date], W0102B.wishlists, W0102B.meta_prob, W0102B.stack_group]
    elif id == "W0103A0":
        return ["W0103A0", [W0103A.data_name, W0103A.data_ver, W0103A.run_date], W0103A.wishlists, W0103A.meta_prob, W0103A.stack_group]
    elif id == "W0103B0":
        return ["W0103B0", [W0103B.data_name, W0103B.data_ver, W0103B.run_date], W0103B.wishlists, W0103B.meta_prob, W0103B.stack_group]
    elif id == "W0104A0":
        return ["W0104A0", [W0104A.data_name, W0104A.data_ver, W0104A.run_date], W0104A.wishlists, W0104A.meta_prob, W0104A.stack_group]
    elif id == "W0104B0":
        return ["W0104B0", [W0104B.data_name, W0104B.data_ver, W0104B.run_date], W0104B.wishlists, W0104B.meta_prob, W0104B.stack_group]
    elif id == "W0105A0":
        return ["W0105A0", [W0105A.data_name, W0105A.data_ver, W0105A.run_date], W0105A.wishlists, W0105A.meta_prob, W0105A.stack_group]
    elif id == "W0105B0":
        return ["W0105B0", [W0105B.data_name, W0105B.data_ver, W0105B.run_date], W0105B.wishlists, W0105B.meta_prob, W0105B.stack_group]
    elif id == "W0106A0":
        return ["W0106A0", [W0106A.data_name, W0106A.data_ver, W0106A.run_date], W0106A.wishlists, W0106A.meta_prob, W0106A.stack_group]
    elif id == "W0106B0":
        return ["W0106B0", [W0106B.data_name, W0106B.data_ver, W0106B.run_date], W0106B.wishlists, W0106B.meta_prob, W0106B.stack_group]
    elif id == "W0200A0":
        return ["W0200A0", [W0200A.data_name, W0200A.data_ver, W0200A.run_date], W0200A.wishlists, W0200A.meta_prob, W0200A.stack_group]
    elif id == "W0200B0":
        return ["W0200B0", [W0200B.data_name, W0200B.data_ver, W0200B.run_date], W0200B.wishlists, W0200B.meta_prob, W0200B.stack_group]
    elif id == "W0201A0":
        return ["W0201A0", [W0201A.data_name, W0201A.data_ver, W0201A.run_date], W0201A.wishlists, W0201A.meta_prob, W0201A.stack_group]
    elif id == "W0201B0":
        return ["W0201B0", [W0201B.data_name, W0201B.data_ver, W0201B.run_date], W0201B.wishlists, W0201B.meta_prob, W0201B.stack_group]
    elif id == "W0202A0":
        return ["W0202A0", [W0202A.data_name, W0202A.data_ver, W0202A.run_date], W0202A.wishlists, W0202A.meta_prob, W0202A.stack_group]
    elif id == "W0202B0":
        return ["W0202B0", [W0202B.data_name, W0202B.data_ver, W0202B.run_date], W0202B.wishlists, W0202B.meta_prob, W0202B.stack_group]
    elif id == "W0203A0":
        return ["W0203A0", [W0203A.data_name, W0203A.data_ver, W0203A.run_date], W0203A.wishlists, W0203A.meta_prob, W0203A.stack_group]
    elif id == "W0203B0":
        return ["W0203B0", [W0203B.data_name, W0203B.data_ver, W0203B.run_date], W0203B.wishlists, W0203B.meta_prob, W0203B.stack_group]
    elif id == "W0204A0":
        return ["W0204A0", [W0204A.data_name, W0204A.data_ver, W0204A.run_date], W0204A.wishlists, W0204A.meta_prob, W0204A.stack_group]
    elif id == "W0204B0":
        return ["W0204B0", [W0204B.data_name, W0204B.data_ver, W0204B.run_date], W0204B.wishlists, W0204B.meta_prob, W0204B.stack_group]
    elif id == "W0205A0":
        return ["W0205A0", [W0205A.data_name, W0205A.data_ver, W0205A.run_date], W0205A.wishlists, W0205A.meta_prob, W0205A.stack_group]
    elif id == "W0205B0":
        return ["W0205B0", [W0205B.data_name, W0205B.data_ver, W0205B.run_date], W0205B.wishlists, W0205B.meta_prob, W0205B.stack_group]
    elif id == "W0206A0":
        return ["W0206A0", [W0206A.data_name, W0206A.data_ver, W0206A.run_date], W0206A.wishlists, W0206A.meta_prob, W0206A.stack_group]
    elif id == "S0100":
        return ["S0100", [S0100_standard.data_name, S0100_standard.data_ver, S0100_standard.run_date], S0100_standard.wishlists, S0100_standard.meta_prob, S0100_standard.stack_group]
    else:
        raise ValueError

def get_gachas():
    return [
        ["C0100A", [C0100A_venti.data_name, C0100A_venti.data_ver, C0100A_venti.run_date]],
        ["C0100B", [C0100B_klee.data_name, C0100B_klee.data_ver, C0100B_klee.run_date]],
        ["C0101A", [C0101A_childe.data_name, C0101A_childe.data_ver, C0101A_childe.run_date]],
        ["C0101B", [C0101B_zhongli.data_name, C0101B_zhongli.data_ver, C0101B_zhongli.run_date]],
        ["C0102A", [C0102A_albedo.data_name, C0102A_albedo.data_ver, C0102A_albedo.run_date]],
        ["C0102B", [C0102B_ganyu.data_name, C0102B_ganyu.data_ver, C0102B_ganyu.run_date]],
        ["C0103A", [C0103A_xiao.data_name, C0103A_xiao.data_ver, C0103A_xiao.run_date]],
        ["C0103B", [C0103B_keqing.data_name, C0103B_keqing.data_ver, C0103B_keqing.run_date]],
        ["C0103C", [C0103C_hutao.data_name, C0103C_hutao.data_ver, C0103C_hutao.run_date]],
        ["C0104A", [C0104A_venti.data_name, C0104A_venti.data_ver, C0104A_venti.run_date]],
        ["C0104B", [C0104B_childe.data_name, C0104B_childe.data_ver, C0104B_childe.run_date]],
        ["C0105A", [C0105A_zhongli.data_name, C0105A_zhongli.data_ver, C0105A_zhongli.run_date]],
        ["C0105B", [C0105B_eula.data_name, C0105B_eula.data_ver, C0105B_eula.run_date]],
        ["C0106A", [C0106A_klee.data_name, C0106A_klee.data_ver, C0106A_klee.run_date]],
        ["C0106B", [C0106B_kazuha.data_name, C0106B_kazuha.data_ver, C0106B_kazuha.run_date]],
        ["C0200A", [C0200A_ayaka.data_name, C0200A_ayaka.data_ver, C0200A_ayaka.run_date]],
        ["C0200B", [C0200B_yoimiya.data_name, C0200B_yoimiya.data_ver, C0200B_yoimiya.run_date]],
        ["C0201A", [C0201A_raiden.data_name, C0201A_raiden.data_ver, C0201A_raiden.run_date]],
        ["C0201B", [C0201B_kokomi.data_name, C0201B_kokomi.data_ver, C0201B_kokomi.run_date]],
        ["C0202A", [C0202A_childe.data_name, C0202A_childe.data_ver, C0202A_childe.run_date]],
        ["C0202B", [C0202B_hutao.data_name, C0202B_hutao.data_ver, C0202B_hutao.run_date]],
        ["C0203AA", [C0203AA_albedo.data_name, C0203AA_albedo.data_ver, C0203AA_albedo.run_date]],
        ["C0203AB", [C0203AB_eula.data_name, C0203AB_eula.data_ver, C0203AB_eula.run_date]],
        ["C0203B", [C0203B_itto.data_name, C0203B_itto.data_ver, C0203B_itto.run_date]],
        ["C0204AA", [C0204AA_shenhe.data_name, C0204AA_shenhe.data_ver, C0204AA_shenhe.run_date]],
        ["C0204AB", [C0204AB_xiao.data_name, C0204AB_xiao.data_ver, C0204AB_xiao.run_date]],
        ["C0204BA", [C0204BA_zhongli.data_name, C0204BA_zhongli.data_ver, C0204BA_zhongli.run_date]],
        ["C0204BB", [C0204BB_ganyu.data_name, C0204BB_ganyu.data_ver, C0204BB_ganyu.run_date]],
        ["C0205AA", [C0205AA_yaemiko.data_name, C0205AA_yaemiko.data_ver, C0205AA_yaemiko.run_date]],
        ["C0205BA", [C0205BA_raiden.data_name, C0205BA_raiden.data_ver, C0205BA_raiden.run_date]],
        ["C0205BB", [C0205BB_kokomi.data_name, C0205BB_kokomi.data_ver, C0205BB_kokomi.run_date]],
        ["C0206AA", [C0206AA_ayato.data_name, C0206AA_ayato.data_ver, C0206AA_ayato.run_date]],
        ["C0206AB", [C0206AB_venti.data_name, C0206AB_venti.data_ver, C0206AB_venti.run_date]],
        ["C0206B", [C0206B_ayaka.data_name, C0206B_ayaka.data_ver, C0206B_ayaka.run_date]],
        ["W0100A0", [W0100A.data_name, W0100A.data_ver, W0100A.run_date]],
        ["W0100B0", [W0100B.data_name, W0100B.data_ver, W0100B.run_date]],
        ["W0101A0", [W0101A.data_name, W0101A.data_ver, W0101A.run_date]],
        ["W0101B0", [W0101B.data_name, W0101B.data_ver, W0101B.run_date]],
        ["W0102A0", [W0102A.data_name, W0102A.data_ver, W0102A.run_date]],
        ["W0102B0", [W0102B.data_name, W0102B.data_ver, W0102B.run_date]],
        ["W0103A0", [W0103A.data_name, W0103A.data_ver, W0103A.run_date]],
        ["W0103B0", [W0103B.data_name, W0103B.data_ver, W0103B.run_date]],
        ["W0104A0", [W0104A.data_name, W0104A.data_ver, W0104A.run_date]],
        ["W0104B0", [W0104B.data_name, W0104B.data_ver, W0104B.run_date]],
        ["W0105A0", [W0105A.data_name, W0105A.data_ver, W0105A.run_date]],
        ["W0105B0", [W0105B.data_name, W0105B.data_ver, W0105B.run_date]],
        ["W0106A0", [W0106A.data_name, W0106A.data_ver, W0106A.run_date]],
        ["W0106B0", [W0106B.data_name, W0106B.data_ver, W0106B.run_date]],
        ["W0200A0", [W0200A.data_name, W0200A.data_ver, W0200A.run_date]],
        ["W0200B0", [W0200B.data_name, W0200B.data_ver, W0200B.run_date]],
        ["W0201A0", [W0201A.data_name, W0201A.data_ver, W0201A.run_date]],
        ["W0201B0", [W0201B.data_name, W0201B.data_ver, W0201B.run_date]],
        ["W0202A0", [W0202A.data_name, W0202A.data_ver, W0202A.run_date]],
        ["W0202B0", [W0202B.data_name, W0202B.data_ver, W0202B.run_date]],
        ["W0203A0", [W0203A.data_name, W0203A.data_ver, W0203A.run_date]],
        ["W0203B0", [W0203B.data_name, W0203B.data_ver, W0203B.run_date]],
        ["W0204A0", [W0204A.data_name, W0204A.data_ver, W0204A.run_date]],
        ["W0204B0", [W0204B.data_name, W0204B.data_ver, W0204B.run_date]],
        ["W0205A0", [W0205A.data_name, W0205A.data_ver, W0205A.run_date]],
        ["W0205B0", [W0205B.data_name, W0205B.data_ver, W0205B.run_date]],
        ["W0206A0", [W0206A.data_name, W0206A.data_ver, W0206A.run_date]],
        ["S0100", [S0100_standard.data_name, S0100_standard.data_ver, S0100_standard.run_date]]
    ]

def get_gacha_name(id):
    li = get_gachas()
    for l in li:
        if l[0] == id:
            return l[1][0]

def get_3stars():
    return C0000Z_3stars.l_3star

def get_pickup_name(m):
    # data
    dt = [
        ["벤티", "C0104A"],
        ["클레", "C0106A"],
        ["타르탈리아", "C0202A"],
        ["종려", "C0204BA"],
        ["알베도", "C0203AA"],
        ["감우", "C0204BB"],
        ["소", "C0204AB"],
        ["호두", "C0202B"],
        ["유라", "C0203AB"],
        ["카즈하", "C0106B"],
        ["아야카", "C0200A"],
        ["요이미야", "C0200B"],
        ["라이덴", "C0201A"],
        ["코코미", "C0201B"],
        ["이토", "C0203B"],
        ["야에 미코", "C0205AA"],
        ["아야토", "C0206AA"],
        ["디오나", "S0100"], # 4성 리다이렉트
        ["신염", "S0100"],
        ["로자리아", "S0100"],
        ["연비", "S0100"],
        ["사유", "S0100"],
        ["쿠죠 사라", "S0100"],
        ["토마", "S0100"],
        ["고로", "C0203B"],
        ["운근", "C0204AA"],
        ["엠버", "S0100"], # 기본제공 4성 캐릭터의 돌파는 상시에서 가능
        ["케이아", "S0100"],
        ["리사", "S0100"],
        ["카에데하라 카즈하", "C0106B"], # 풀네임 있는 캐릭터
        ["카미사토 아야카", "C0200A"],
        ["라이덴 쇼군", "C0201A"],
        ["사라", "S0100"],
        ["산고노미야 코코미", "C0201B"],
        ["카미사토 아야토", "C0206AA"]
    ]
    for i in dt:
        if m == i[0]:
            return i[1]
    raise NameError

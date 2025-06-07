#Enemy Images
#Red Fang
image fang_adam_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/en/fang/fang_adam.png",
    "persistent.PC98_mode == True", "images/PC98/en/fang/fang_adam.png")
image fang_adam_damage:
    "fang_adam_base"
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.0))
image fang_adam_damage_mp:
    "fang_adam_base"
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.0))
image fang_adam_healing:
    "fang_adam_base"
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.0))
image fang_adam_prezoom = ConditionSwitch(
    "en1_dmg != 0", "fang_adam_damage",
    "en1_dmg_mp != 0", "fang_adam_damage_mp",
    "en1_hlx != 0", "fang_adam_healing",
    None, "fang_adam_base")
image fang_adam:
    "fang_adam_prezoom"
    zoom 0.3

image fang_blade_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/en/fang/fang_blade.png",
    "persistent.PC98_mode == True", "images/PC98/en/fang/fang_blade.png")
image fang_blade_damage:
    "fang_blade_base"
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.0))
image fang_blade_damage_mp:
    "fang_blade_base"
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.0))
image fang_blade_healing:
    "fang_blade_base"
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.0))
image fang_blade_prezoom = ConditionSwitch(
    "en1_dmg != 0", "fang_blade_damage",
    "en1_dmg_mp != 0", "fang_blade_damage_mp",
    "en1_hlx != 0", "fang_blade_healing",
    None, "fang_blade_base")
image fang_blade:
    "fang_blade_prezoom"
    zoom 0.3
image fang_blade_2:
    "fang_blade_prezoom"

image fang_gun_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/en/fang/fang_gun.png",
    "persistent.PC98_mode == True", "images/PC98/en/fang/fang_gun.png")
image fang_gun_damage:
    "fang_gun_base"
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.0))
image fang_gun_damage_mp:
    "fang_gun_base"
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.0))
image fang_gun_healing:
    "fang_gun_base"
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.0))
image fang_gun_prezoom = ConditionSwitch(
    "en1_dmg != 0", "fang_gun_damage",
    "en1_dmg_mp != 0", "fang_gun_damage_mp",
    "en1_hlx != 0", "fang_gun_healing",
    None, "fang_gun_base")
image fang_gun:
    "fang_gun_prezoom"
    zoom 0.3
image fang_gun_2:
    "fang_gun_prezoom"

image fang_scourge_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/en/fang/fang_scourge.png",
    "persistent.PC98_mode == True", "images/PC98/en/fang/fang_scourge.png")
image fang_scourge_damage:
    "fang_scourge_base"
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.0))
image fang_scourge_damage_mp:
    "fang_scourge_base"
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.0))
image fang_scourge_healing:
    "fang_scourge_base"
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.0))
image fang_scourge_prezoom = ConditionSwitch(
    "en1_dmg != 0", "fang_scourge_damage",
    "en1_dmg_mp != 0", "fang_scourge_damage_mp",
    "en1_hlx != 0", "fang_scourge_healing",
    None, "fang_scourge_base")
image scourge_face = ConditionSwitch(
    "persistent.PC98_mode == False", "images/en/fang/scourge_face.png",
    "persistent.PC98_mode == True", "images/PC98/en/fang/scourge_face.png")
image fang_scourge:
    "fang_scourge_prezoom"
    zoom 0.3

image grimm_kataglyph_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/en/grimm/grimm_kataglyph.png",
    "persistent.PC98_mode == True", "images/PC98/en/grimm/grimm_kataglyph.png")
image grimm_kataglyph_damage:
    "grimm_kataglyph_base"
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.0))
image grimm_kataglyph_damage_mp:
    "grimm_kataglyph_base"
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.0))
image grimm_kataglyph_healing:
    "grimm_kataglyph_base"
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.0))
image grimm_kataglyph_prezoom = ConditionSwitch(
    "en1_dmg != 0", "grimm_kataglyph_damage",
    "en1_dmg_mp != 0", "grimm_kataglyph_damage_mp",
    "en1_hlx != 0", "grimm_kataglyph_healing",
    None, "grimm_kataglyph_base")
image grimm_kataglyph:
    "grimm_kataglyph_prezoom"
    zoom 0.45

image grimm_kataglyph_worker_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/en/grimm/grimm_kataglyph_worker.png",
    "persistent.PC98_mode == True", "images/PC98/en/grimm/grimm_kataglyph_worker.png")
image grimm_kataglyph_worker_damage:
    "grimm_kataglyph_worker_base"
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.0))
image grimm_kataglyph_worker_damage_mp:
    "grimm_kataglyph_worker_base"
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.0))
image grimm_kataglyph_worker_healing:
    "grimm_kataglyph_worker_base"
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.0))
image grimm_kataglyph_worker_prezoom = ConditionSwitch(
    "en1_dmg != 0", "grimm_kataglyph_worker_damage",
    "en1_dmg_mp != 0", "grimm_kataglyph_worker_damage_mp",
    "en1_hlx != 0", "grimm_kataglyph_worker_healing",
    None, "grimm_kataglyph_worker_base")
image grimm_kataglyph_worker:
    "grimm_kataglyph_worker_prezoom"
    zoom 0.45

image grimm_kulimshan_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/en/grimm/grimm_kulimshan.png",
    "persistent.PC98_mode == True", "images/PC98/en/grimm/grimm_kulimshan.png")
image grimm_kulimshan_damage:
    "grimm_kulimshan_base"
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.0))
image grimm_kulimshan_damage_mp:
    "grimm_kulimshan_base"
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.0))
image grimm_kulimshan_healing:
    "grimm_kulimshan_base"
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.0))
image grimm_kulimshan_prezoom = ConditionSwitch(
    "en1_dmg != 0", "grimm_kulimshan_damage",
    "en1_dmg_mp != 0", "grimm_kulimshan_damage_mp",
    "en1_hlx != 0", "grimm_kulimshan_healing",
    None, "grimm_kulimshan_base")
image grimm_kulimshan:
    "grimm_kulimshan_prezoom"
    zoom 0.3

image grimm_oppel_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/en/grimm/grimm_oppel.png",
    "persistent.PC98_mode == True", "images/PC98/en/grimm/grimm_oppel.png")
image grimm_oppel_damage:
    "grimm_oppel_base"
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.0))
image grimm_oppel_damage_mp:
    "grimm_oppel_base"
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.0))
image grimm_oppel_healing:
    "grimm_oppel_base"
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.0))
image grimm_oppel_prezoom = ConditionSwitch(
    "en1_dmg != 0", "grimm_oppel_damage",
    "en1_dmg_mp != 0", "grimm_oppel_damage_mp",
    "en1_hlx != 0", "grimm_oppel_healing",
    None, "grimm_oppel_base")
image grimm_oppel:
    "grimm_oppel_prezoom"
    zoom 0.3

image grimm_moorgula_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/en/grimm/grimm_moorgula.png",
    "persistent.PC98_mode == True", "images/PC98/en/grimm/grimm_moorgula.png")
image grimm_moorgula_damage:
    "grimm_moorgula_base"
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.0))
image grimm_moorgula_damage_mp:
    "grimm_moorgula_base"
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.0))
image grimm_moorgula_healing:
    "grimm_moorgula_base"
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.0))
image grimm_moorgula_prezoom = ConditionSwitch(
    "en1_dmg != 0", "grimm_moorgula_damage",
    "en1_dmg_mp != 0", "grimm_moorgula_damage_mp",
    "en1_hlx != 0", "grimm_moorgula_healing",
    None, "grimm_moorgula_base")
image grimm_moorgula:
    "grimm_moorgula_prezoom"
    zoom 0.4

image grimm_gangurru_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/en/grimm/grimm_gangurru.png",
    "persistent.PC98_mode == True", "images/PC98/en/grimm/grimm_gangurru.png")
image grimm_gangurru_damage:
    "grimm_gangurru_base"
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.0))
image grimm_gangurru_damage_mp:
    "grimm_gangurru_base"
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.0))
image grimm_gangurru_healing:
    "grimm_gangurru_base"
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.0))
image grimm_gangurru_prezoom = ConditionSwitch(
    "en1_dmg != 0", "grimm_gangurru_damage",
    "en1_dmg_mp != 0", "grimm_gangurru_damage_mp",
    "en1_hlx != 0", "grimm_gangurru_healing",
    None, "grimm_gangurru_base")
image grimm_gangurru:
    "grimm_gangurru_prezoom"
    zoom 0.5

image grimm_thylacine_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/en/grimm/grimm_thylacine.png",
    "persistent.PC98_mode == True", "images/PC98/en/grimm/grimm_thylacine.png")
image grimm_thylacine_damage:
    "grimm_thylacine_base"
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.0))
image grimm_thylacine_damage_mp:
    "grimm_thylacine_base"
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.0))
image grimm_thylacine_healing:
    "grimm_thylacine_base"
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.0))
image grimm_thylacine_prezoom = ConditionSwitch(
    "en1_dmg != 0", "grimm_thylacine_damage",
    "en1_dmg_mp != 0", "grimm_thylacine_damage_mp",
    "en1_hlx != 0", "grimm_thylacine_healing",
    None, "grimm_thylacine_base")
image grimm_thylacine:
    "grimm_thylacine_prezoom"
    zoom 0.5
image grimm_thylacine2:
    "grimm_thylacine_prezoom"
image grimm_thylacine3:
    "grimm_thylacine_prezoom"

image grimm_naracoorte_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/en/grimm/grimm_naracoorte.png",
    "persistent.PC98_mode == True", "images/PC98/en/grimm/grimm_naracoorte.png")
image grimm_naracoorte_damage:
    "grimm_naracoorte_base"
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.0))
image grimm_naracoorte_damage_mp:
    "grimm_naracoorte_base"
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.0))
image grimm_naracoorte_healing:
    "grimm_naracoorte_base"
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.0))
image grimm_naracoorte_prezoom = ConditionSwitch(
    "en1_dmg != 0", "grimm_naracoorte_damage",
    "en1_dmg_mp != 0", "grimm_naracoorte_damage_mp",
    "en1_hlx != 0", "grimm_naracoorte_healing",
    None, "grimm_naracoorte_base")
image grimm_naracoorte:
    "grimm_naracoorte_prezoom"
    zoom 0.4

image grimm_atrax_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/en/grimm/grimm_atrax.png",
    "persistent.PC98_mode == True", "images/PC98/en/grimm/grimm_atrax.png")
image grimm_atrax_damage:
    "grimm_atrax_base"
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#ad1a00", alpha=0.0))
image grimm_atrax_damage_mp:
    "grimm_atrax_base"
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#47008e", alpha=0.0))
image grimm_atrax_healing:
    "grimm_atrax_base"
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.66))
    pause 0.05
    linear 0.1 matrixcolor TintMatrix(Color("#0bf4aa", alpha=0.0))
image grimm_atrax_prezoom = ConditionSwitch(
    "en1_dmg != 0", "grimm_atrax_damage",
    "en1_dmg_mp != 0", "grimm_atrax_damage_mp",
    "en1_hlx != 0", "grimm_atrax_healing",
    None, "grimm_atrax_base")
image grimm_atrax:
    "grimm_atrax_prezoom"
    zoom 0.3
image boss_empty_atrax = "images/en/grimm/boss_empty_atrax.png"
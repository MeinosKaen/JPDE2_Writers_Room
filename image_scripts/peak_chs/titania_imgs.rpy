
image titania_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/titania/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/titania/body_base.png"
)
image titania_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/titania/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/titania/clothes_full.png"
)
image titania_acc_apron = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/titania/acc_apron.png",
    "persistent.PC98_mode == True", "images/PC98/ch/titania/acc_apron.png"
)
image titania_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/titania/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/titania/exp_neutral.png"
)
image titania_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/titania/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/titania/exp_smile.png"
)
image titania_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/titania/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/titania/exp_amused.png"
)
image titania_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/titania/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/titania/exp_laugh.png"
)
image titania_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/titania/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/titania/exp_surprise.png"
)
image titania_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/titania/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/titania/exp_shock.png"
)
image titania_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/titania/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/titania/exp_angry.png"
)
image titania_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/titania/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/titania/exp_frown.png"
)
image titania_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/titania/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/titania/exp_sad.png"
)
image titania_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/titania/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/titania/exp_pain.png"
)
image titania_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/titania/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/titania/acc_sweat.png"
)
image titania_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/titania/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/titania/acc_blush.png"
)
image titania_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/titania/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/titania/acc_sweatdrop.png"
)
layeredimage Titania:
    group body:
        attribute base default:
            "titania_body_base"
    group clothes:
        attribute c_full default:
            "titania_clothes_full"
    group accessories_2:
        attribute blush:
            "titania_acc_blush"
    group face:
        attribute neutral default:
            "titania_exp_neutral"#
        attribute amused:
            "titania_exp_amused"#
        attribute laugh:
            "titania_exp_laugh"#
        attribute smile:
            "titania_exp_smile"#
        attribute surprise:
            "titania_exp_surprise"#
        attribute shock:
            "titania_exp_shock"#
        attribute angry:
            "titania_exp_angry"#
        attribute frown:
            "titania_exp_frown"#
        attribute sad:
            "titania_exp_sad"#
        attribute pain:
            "titania_exp_pain"#
    group accessories:
        attribute sweat:
            "titania_acc_sweat"
        attribute sweatdrop:
            "titania_acc_sweatdrop"
        attribute apron:
            "titania_acc_apron"
    at character_sprites_titania
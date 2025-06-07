image bunny_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/bunny/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/bunny/body_base.png"
)
image bunny_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/bunny/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/bunny/clothes_full.png"
)
image bunny_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/bunny/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/bunny/exp_neutral.png"
)
image bunny_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/bunny/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/bunny/exp_smile.png"
)
image bunny_exp_emba = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/bunny/exp_emba.png",
    "persistent.PC98_mode == True", "images/PC98/ch/bunny/exp_emba.png"
)
image bunny_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/bunny/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/bunny/exp_amused.png"
)
image bunny_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/bunny/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/bunny/exp_laugh.png"
)
image bunny_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/bunny/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/bunny/exp_surprise.png"
)
image bunny_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/bunny/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/bunny/exp_shock.png"
)
image bunny_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/bunny/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/bunny/exp_angry.png"
)
image bunny_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/bunny/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/bunny/exp_frown.png"
)
image bunny_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/bunny/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/bunny/exp_sad.png"
)
image bunny_exp_sadder = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/bunny/exp_sadder.png",
    "persistent.PC98_mode == True", "images/PC98/ch/bunny/exp_sadder.png"
)
image bunny_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/bunny/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/bunny/exp_pain.png"
)
image bunny_exp_cry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/bunny/exp_cry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/bunny/exp_cry.png"
)
image bunny_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/bunny/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/bunny/acc_sweat.png"
)
image bunny_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/bunny/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/bunny/acc_blush.png"
)
image bunny_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/bunny/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/bunny/acc_sweatdrop.png"
)
image bunny_acc_pin = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/bunny/acc_pin.png",
    "persistent.PC98_mode == True", "images/PC98/ch/bunny/acc_pin.png"
)
layeredimage Bunny:
    group body:
        attribute base default:
            "bunny_body_base"
    group clothes:
        attribute c_full default:
            "bunny_clothes_full"
    group accessories_2:
        attribute blush:
            "bunny_acc_blush"
    group face:
        attribute neutral default:
            "bunny_exp_neutral"#
        attribute amused:
            "bunny_exp_amused"#
        attribute laugh:
            "bunny_exp_laugh"#
        attribute smile:
            "bunny_exp_smile"#
        attribute emba:
            "bunny_exp_emba"#
        attribute surprise:
            "bunny_exp_surprise"#
        attribute shock:
            "bunny_exp_shock"#
        attribute angry:
            "bunny_exp_angry"#
        attribute frown:
            "bunny_exp_frown"#
        attribute sad:
            "bunny_exp_sad"#
        attribute cry:
            "bunny_exp_cry"#
        attribute pain:
            "bunny_exp_pain"#
        attribute sadder:
            "bunny_exp_sadder"#
    group accessories:
        attribute sweat:
            "bunny_acc_sweat"
        attribute sweatdrop:
            "bunny_acc_sweatdrop"
    group accessories_3:
        attribute pin:
            "bunny_acc_pin"
    at character_sprites_bunny
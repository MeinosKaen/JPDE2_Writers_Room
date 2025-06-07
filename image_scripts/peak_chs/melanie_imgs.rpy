image melanie_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/melanie/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/melanie/body_base.png"
)
image melanie_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/melanie/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/melanie/clothes_full.png"
)
image melanie_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/melanie/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/melanie/exp_neutral.png"
)
image melanie_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/melanie/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/melanie/exp_smile.png"
)
image melanie_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/melanie/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/melanie/exp_amused.png"
)
image melanie_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/melanie/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/melanie/exp_laugh.png"
)
image melanie_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/melanie/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/melanie/exp_surprise.png"
)
image melanie_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/melanie/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/melanie/exp_shock.png"
)
image melanie_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/melanie/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/melanie/exp_angry.png"
)
image melanie_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/melanie/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/melanie/exp_frown.png"
)
image melanie_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/melanie/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/melanie/exp_sad.png"
)
image melanie_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/melanie/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/melanie/exp_pain.png"
)
image melanie_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/melanie/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/melanie/acc_sweat.png"
)
image melanie_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/melanie/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/melanie/acc_blush.png"
)
image melanie_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/melanie/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/melanie/acc_sweatdrop.png"
)
layeredimage Melanie:
    group body:
        attribute base default:
            "melanie_body_base"
    group clothes:
        attribute c_full default:
            "melanie_clothes_full"
    group accessories_2:
        attribute blush:
            "melanie_acc_blush"
    group face:
        attribute neutral default:
            "melanie_exp_neutral"#
        attribute amused:
            "melanie_exp_amused"#
        attribute laugh:
            "melanie_exp_laugh"#
        attribute smile:
            "melanie_exp_smile"#
        attribute surprise:
            "melanie_exp_surprise"#
        attribute shock:
            "melanie_exp_shock"#
        attribute angry:
            "melanie_exp_angry"#
        attribute frown:
            "melanie_exp_frown"#
        attribute sad:
            "melanie_exp_sad"#
        attribute pain:
            "melanie_exp_pain"#
    group accessories:
        attribute sweat:
            "melanie_acc_sweat"
        attribute sweatdrop:
            "melanie_acc_sweatdrop"
    at character_sprites_melanie

image morgan_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/morgan/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/morgan/body_base.png"
)
image morgan_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/morgan/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/morgan/clothes_full.png"
)
image morgan_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/morgan/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/morgan/exp_neutral.png"
)
image morgan_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/morgan/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/morgan/exp_smile.png"
)
image morgan_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/morgan/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/morgan/exp_amused.png"
)
image morgan_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/morgan/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/morgan/exp_laugh.png"
)
image morgan_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/morgan/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/morgan/exp_surprise.png"
)
image morgan_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/morgan/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/morgan/exp_shock.png"
)
image morgan_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/morgan/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/morgan/exp_angry.png"
)
image morgan_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/morgan/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/morgan/exp_frown.png"
)
image morgan_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/morgan/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/morgan/exp_sad.png"
)
image morgan_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/morgan/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/morgan/exp_pain.png"
)
image morgan_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/morgan/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/morgan/acc_sweat.png"
)
image morgan_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/morgan/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/morgan/acc_blush.png"
)
image morgan_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/morgan/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/morgan/acc_sweatdrop.png"
)
layeredimage Morgan:
    group body:
        attribute base default:
            "morgan_body_base"
    group clothes:
        attribute c_full default:
            "morgan_clothes_full"
    group accessories_2:
        attribute blush:
            "morgan_acc_blush"
    group face:
        attribute neutral default:
            "morgan_exp_neutral"#
        attribute amused:
            "morgan_exp_amused"#
        attribute laugh:
            "morgan_exp_laugh"#
        attribute smile:
            "morgan_exp_smile"#
        attribute surprise:
            "morgan_exp_surprise"#
        attribute shock:
            "morgan_exp_shock"#
        attribute angry:
            "morgan_exp_angry"#
        attribute frown:
            "morgan_exp_frown"#
        attribute sad:
            "morgan_exp_sad"#
        attribute pain:
            "morgan_exp_pain"#
    group accessories:
        attribute sweat:
            "morgan_acc_sweat"
        attribute sweatdrop:
            "morgan_acc_sweatdrop"
    at character_sprites_morgan
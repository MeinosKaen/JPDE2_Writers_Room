image miltia_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/miltia/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/miltia/body_base.png"
)
image miltia_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/miltia/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/miltia/clothes_full.png"
)
image miltia_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/miltia/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/miltia/exp_neutral.png"
)
image miltia_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/miltia/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/miltia/exp_smile.png"
)
image miltia_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/miltia/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/miltia/exp_amused.png"
)
image miltia_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/miltia/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/miltia/exp_laugh.png"
)
image miltia_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/miltia/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/miltia/exp_surprise.png"
)
image miltia_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/miltia/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/miltia/exp_shock.png"
)
image miltia_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/miltia/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/miltia/exp_angry.png"
)
image miltia_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/miltia/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/miltia/exp_frown.png"
)
image miltia_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/miltia/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/miltia/exp_sad.png"
)
image miltia_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/miltia/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/miltia/exp_pain.png"
)
image miltia_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/miltia/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/miltia/acc_sweat.png"
)
image miltia_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/miltia/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/miltia/acc_blush.png"
)
image miltia_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/miltia/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/miltia/acc_sweatdrop.png"
)
layeredimage Miltia:
    group body:
        attribute base default:
            "miltia_body_base"
    group clothes:
        attribute c_full default:
            "miltia_clothes_full"
    group accessories_2:
        attribute blush:
            "miltia_acc_blush"
    group face:
        attribute neutral default:
            "miltia_exp_neutral"#
        attribute amused:
            "miltia_exp_amused"#
        attribute laugh:
            "miltia_exp_laugh"#
        attribute smile:
            "miltia_exp_smile"#
        attribute surprise:
            "miltia_exp_surprise"#
        attribute shock:
            "miltia_exp_shock"#
        attribute angry:
            "miltia_exp_angry"#
        attribute frown:
            "miltia_exp_frown"#
        attribute sad:
            "miltia_exp_sad"#
        attribute pain:
            "miltia_exp_pain"#
    group accessories:
        attribute sweat:
            "miltia_acc_sweat"
        attribute sweatdrop:
            "miltia_acc_sweatdrop"
    at character_sprites_miltia
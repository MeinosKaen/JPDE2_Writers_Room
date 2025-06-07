
image howard_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/howard/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/howard/body_base.png"
)
image howard_clothes_half = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/howard/clothes_half.png",
    "persistent.PC98_mode == True", "images/PC98/ch/howard/clothes_half.png"
)
image howard_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/howard/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/howard/clothes_full.png"
)
image howard_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/howard/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/howard/exp_neutral.png"
)
image howard_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/howard/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/howard/exp_smile.png"
)
image howard_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/howard/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/howard/exp_amused.png"
)
image howard_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/howard/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/howard/exp_laugh.png"
)
image howard_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/howard/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/howard/exp_surprise.png"
)
image howard_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/howard/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/howard/exp_shock.png"
)
image howard_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/howard/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/howard/exp_angry.png"
)
image howard_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/howard/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/howard/exp_frown.png"
)
image howard_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/howard/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/howard/exp_sad.png"
)
image howard_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/howard/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/howard/exp_pain.png"
)
image howard_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/howard/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/howard/acc_sweat.png"
)
image howard_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/howard/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/howard/acc_blush.png"
)
image howard_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/howard/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/howard/acc_sweatdrop.png"
)
layeredimage Howard:
    group body:
        attribute base default:
            "howard_body_base"
    group clothes:
        attribute c_half default:
            "howard_clothes_half"
    group accessories_2:
        attribute blush:
            "howard_acc_blush"
    group face:
        attribute neutral default:
            "howard_exp_neutral"#
        attribute amused:
            "howard_exp_amused"#
        attribute laugh:
            "howard_exp_laugh"#
        attribute smile:
            "howard_exp_smile"#
        attribute surprise:
            "howard_exp_surprise"#
        attribute shock:
            "howard_exp_shock"#
        attribute angry:
            "howard_exp_angry"#
        attribute frown:
            "howard_exp_frown"#
        attribute sad:
            "howard_exp_sad"#
        attribute pain:
            "howard_exp_pain"#
    group accessories:
        attribute sweat:
            "howard_acc_sweat"
        attribute sweatdrop:
            "howard_acc_sweatdrop"
    group accessories_3:
        attribute jacket default:
            "howard_clothes_full"
    at character_sprites_howard
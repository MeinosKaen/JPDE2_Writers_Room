
image james_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/james/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/james/body_base.png"
)
image james_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/james/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/james/clothes_full.png"
)
image james_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/james/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/james/exp_neutral.png"
)
image james_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/james/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/james/exp_smile.png"
)
image james_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/james/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/james/exp_amused.png"
)
image james_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/james/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/james/exp_laugh.png"
)
image james_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/james/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/james/exp_surprise.png"
)
image james_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/james/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/james/exp_shock.png"
)
image james_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/james/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/james/exp_angry.png"
)
image james_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/james/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/james/exp_frown.png"
)
image james_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/james/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/james/exp_sad.png"
)
image james_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/james/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/james/exp_pain.png"
)
image james_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/james/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/james/acc_sweat.png"
)
image james_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/james/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/james/acc_blush.png"
)
image james_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/james/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/james/acc_sweatdrop.png"
)
layeredimage James:
    group body:
        attribute base default:
            "james_body_base"
    group clothes:
        attribute c_full default:
            "james_clothes_full"
    group accessories_2:
        attribute blush:
            "james_acc_blush"
    group face:
        attribute neutral default:
            "james_exp_neutral"#
        attribute amused:
            "james_exp_amused"#
        attribute laugh:
            "james_exp_laugh"#
        attribute smile:
            "james_exp_smile"#
        attribute surprise:
            "james_exp_surprise"#
        attribute shock:
            "james_exp_shock"#
        attribute angry:
            "james_exp_angry"#
        attribute frown:
            "james_exp_frown"#
        attribute sad:
            "james_exp_sad"#
        attribute pain:
            "james_exp_pain"#
    group accessories:
        attribute sweat:
            "james_acc_sweat"
        attribute sweatdrop:
            "james_acc_sweatdrop"
    at character_sprites_james
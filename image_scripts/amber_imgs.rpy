
image amber_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/amber/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/amber/body_base.png"
)
image amber_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/amber/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/amber/clothes_full.png"
)
image amber_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/amber/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/amber/exp_neutral.png"
)
image amber_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/amber/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/amber/exp_smile.png"
)
image amber_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/amber/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/amber/exp_amused.png"
)
image amber_exp_cry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/amber/exp_cry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/amber/exp_cry.png"
)
image amber_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/amber/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/amber/exp_laugh.png"
)
image amber_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/amber/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/amber/exp_surprise.png"
)
image amber_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/amber/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/amber/exp_shock.png"
)
image amber_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/amber/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/amber/exp_angry.png"
)
image amber_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/amber/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/amber/exp_frown.png"
)
image amber_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/amber/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/amber/exp_sad.png"
)
image amber_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/amber/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/amber/exp_pain.png"
)
image amber_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/amber/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/amber/acc_sweat.png"
)
image amber_acc_coat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/amber/acc_coat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/amber/acc_coat.png"
)
image amber_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/amber/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/amber/acc_blush.png"
)
image amber_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/amber/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/amber/acc_sweatdrop.png"
)
layeredimage Amber:
    group body:
        attribute base default:
            "amber_body_base"
    group clothes:
        attribute c_full default:
            "amber_clothes_full"
    group accessories_2:
        attribute blush:
            "amber_acc_blush"
    group face:
        attribute neutral default:
            "amber_exp_neutral"#
        attribute amused:
            "amber_exp_amused"#
        attribute cry:
            "amber_exp_cry"#
        attribute laugh:
            "amber_exp_laugh"#
        attribute smile:
            "amber_exp_smile"#
        attribute surprise:
            "amber_exp_surprise"#
        attribute shock:
            "amber_exp_shock"#
        attribute angry:
            "amber_exp_angry"#
        attribute frown:
            "amber_exp_frown"#
        attribute sad:
            "amber_exp_sad"#
        attribute pain:
            "amber_exp_pain"#
    group accessories:
        attribute coat:
            "amber_acc_coat"
        attribute sweat:
            "amber_acc_sweat"
        attribute sweatdrop:
            "amber_acc_sweatdrop"
    at character_sprites_amber
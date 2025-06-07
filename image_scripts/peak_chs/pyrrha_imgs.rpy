
image pyrrha_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/pyrrha/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/pyrrha/body_base.png"
)
image pyrrha_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/pyrrha/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/pyrrha/clothes_full.png"
)
image pyrrha_acc_glasses = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/pyrrha/acc_glasses.png",
    "persistent.PC98_mode == True", "images/PC98/ch/pyrrha/acc_glasses.png"
)
image pyrrha_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/pyrrha/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/pyrrha/exp_neutral.png"
)
image pyrrha_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/pyrrha/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/pyrrha/exp_smile.png"
)
image pyrrha_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/pyrrha/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/pyrrha/exp_amused.png"
)
image pyrrha_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/pyrrha/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/pyrrha/exp_laugh.png"
)
image pyrrha_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/pyrrha/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/pyrrha/exp_surprise.png"
)
image pyrrha_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/pyrrha/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/pyrrha/exp_shock.png"
)
image pyrrha_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/pyrrha/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/pyrrha/exp_angry.png"
)
image pyrrha_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/pyrrha/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/pyrrha/exp_frown.png"
)
image pyrrha_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/pyrrha/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/pyrrha/exp_sad.png"
)
image pyrrha_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/pyrrha/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/pyrrha/exp_pain.png"
)
image pyrrha_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/pyrrha/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/pyrrha/acc_sweat.png"
)
image pyrrha_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/pyrrha/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/pyrrha/acc_blush.png"
)
image pyrrha_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/pyrrha/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/pyrrha/acc_sweatdrop.png"
)
layeredimage Pyrrha:
    group body:
        attribute base default:
            "pyrrha_body_base"
    group clothes:
        attribute c_full default:
            "pyrrha_clothes_full"
    group accessories_2:
        attribute blush:
            "pyrrha_acc_blush"
    group face:
        attribute neutral default:
            "pyrrha_exp_neutral"#
        attribute amused:
            "pyrrha_exp_amused"#
        attribute laugh:
            "pyrrha_exp_laugh"#
        attribute smile:
            "pyrrha_exp_smile"#
        attribute surprise:
            "pyrrha_exp_surprise"#
        attribute shock:
            "pyrrha_exp_shock"#
        attribute angry:
            "pyrrha_exp_angry"#
        attribute frown:
            "pyrrha_exp_frown"#
        attribute sad:
            "pyrrha_exp_sad"#
        attribute pain:
            "pyrrha_exp_pain"#
    group accessories_3:
        attribute glasses default:
            "pyrrha_acc_glasses"
    group accessories:
        attribute sweat:
            "pyrrha_acc_sweat"
        attribute sweatdrop:
            "pyrrha_acc_sweatdrop"
    at character_sprites_pyrrha
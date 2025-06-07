
image enrico_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/enrico/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/enrico/body_base.png"
)
image enrico_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/enrico/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/enrico/clothes_full.png"
)
image enrico_acc_hat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/enrico/acc_hat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/enrico/acc_hat.png"
)
image enrico_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/enrico/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/enrico/exp_neutral.png"
)
image enrico_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/enrico/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/enrico/exp_smile.png"
)
image enrico_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/enrico/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/enrico/exp_amused.png"
)
image enrico_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/enrico/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/enrico/exp_laugh.png"
)
image enrico_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/enrico/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/enrico/exp_surprise.png"
)
image enrico_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/enrico/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/enrico/exp_shock.png"
)
image enrico_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/enrico/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/enrico/exp_angry.png"
)
image enrico_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/enrico/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/enrico/exp_frown.png"
)
image enrico_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/enrico/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/enrico/exp_sad.png"
)
image enrico_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/enrico/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/enrico/exp_pain.png"
)
image enrico_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/enrico/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/enrico/acc_sweat.png"
)
image enrico_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/enrico/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/enrico/acc_blush.png"
)
image enrico_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/enrico/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/enrico/acc_sweatdrop.png"
)
layeredimage Enrico:
    group body:
        attribute base default:
            "enrico_body_base"
    group clothes:
        attribute c_full default:
            "enrico_clothes_full"
    group accessories_2:
        attribute blush:
            "enrico_acc_blush"
    group face:
        attribute neutral default:
            "enrico_exp_neutral"#
        attribute amused:
            "enrico_exp_amused"#
        attribute laugh:
            "enrico_exp_laugh"#
        attribute smile:
            "enrico_exp_smile"#
        attribute surprise:
            "enrico_exp_surprise"#
        attribute shock:
            "enrico_exp_shock"#
        attribute angry:
            "enrico_exp_angry"#
        attribute frown:
            "enrico_exp_frown"#
        attribute sad:
            "enrico_exp_sad"#
        attribute pain:
            "enrico_exp_pain"#
    group accessories:
        attribute sweat:
            "enrico_acc_sweat"
        attribute sweatdrop:
            "enrico_acc_sweatdrop"
        attribute hat:
            "enrico_acc_hat"
    at character_sprites_enrico
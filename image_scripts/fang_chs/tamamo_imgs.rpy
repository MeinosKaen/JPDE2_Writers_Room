
image tamamo_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tamamo/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tamamo/body_base.png"
)
image tamamo_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tamamo/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tamamo/clothes_full.png"
)
image tamamo_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tamamo/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tamamo/exp_neutral.png"
)
image tamamo_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tamamo/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tamamo/exp_smile.png"
)
image tamamo_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tamamo/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tamamo/exp_amused.png"
)
image tamamo_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tamamo/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tamamo/exp_laugh.png"
)
image tamamo_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tamamo/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tamamo/exp_surprise.png"
)
image tamamo_exp_cold = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tamamo/exp_cold.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tamamo/exp_cold.png"
)
image tamamo_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tamamo/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tamamo/exp_shock.png"
)
image tamamo_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tamamo/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tamamo/exp_angry.png"
)
image tamamo_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tamamo/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tamamo/exp_frown.png"
)
image tamamo_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tamamo/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tamamo/exp_sad.png"
)
image tamamo_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tamamo/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tamamo/exp_pain.png"
)
image tamamo_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tamamo/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tamamo/acc_sweat.png"
)
image tamamo_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tamamo/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tamamo/acc_blush.png"
)
image tamamo_acc_up = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tamamo/acc_up.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tamamo/acc_up.png"
)
image tamamo_acc_down = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tamamo/acc_down.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tamamo/acc_down.png"
)
image tamamo_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tamamo/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tamamo/acc_sweatdrop.png"
)
layeredimage Tamamo:
    group body:
        attribute base default:
            "tamamo_body_base"
    group accessories_2:
        attribute blush:
            "tamamo_acc_blush"
    group ears:
        attribute down:
            "tamamo_acc_down"
        attribute up default:
            "tamamo_acc_up"
    group face:
        attribute neutral default:
            "tamamo_exp_neutral"#
        attribute amused:
            "tamamo_exp_amused"#
        attribute laugh:
            "tamamo_exp_laugh"#
        attribute smile:
            "tamamo_exp_smile"#
        attribute cold:
            "tamamo_exp_cold"#
        attribute surprise:
            "tamamo_exp_surprise"#
        attribute shock:
            "tamamo_exp_shock"#
        attribute angry:
            "tamamo_exp_angry"#
        attribute frown:
            "tamamo_exp_frown"#
        attribute sad:
            "tamamo_exp_sad"#
        attribute pain:
            "tamamo_exp_pain"#
    group clothes:
        attribute c_full default:
            "tamamo_clothes_full"
    group accessories:
        attribute sweat:
            "tamamo_acc_sweat"
        attribute sweatdrop:
            "tamamo_acc_sweatdrop"
    at character_sprites_tamamo
image evelyn_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/evelyn/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/evelyn/body_base.png"
)
image evelyn_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/evelyn/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/evelyn/clothes_full.png"
)
image evelyn_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/evelyn/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/evelyn/exp_neutral.png"
)
image evelyn_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/evelyn/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/evelyn/exp_smile.png"
)
image evelyn_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/evelyn/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/evelyn/exp_amused.png"
)
image evelyn_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/evelyn/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/evelyn/exp_laugh.png"
)
image evelyn_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/evelyn/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/evelyn/exp_surprise.png"
)
image evelyn_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/evelyn/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/evelyn/exp_shock.png"
)
image evelyn_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/evelyn/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/evelyn/exp_angry.png"
)
image evelyn_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/evelyn/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/evelyn/exp_frown.png"
)
image evelyn_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/evelyn/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/evelyn/exp_sad.png"
)
image evelyn_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/evelyn/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/evelyn/exp_pain.png"
)
image evelyn_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/evelyn/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/evelyn/acc_sweat.png"
)
image evelyn_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/evelyn/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/evelyn/acc_blush.png"
)
image evelyn_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/evelyn/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/evelyn/acc_sweatdrop.png"
)
layeredimage Evelyn:
    group body:
        attribute base default:
            "evelyn_body_base"
    group clothes:
        attribute c_full default:
            "evelyn_clothes_full"
    group accessories_2:
        attribute blush:
            "evelyn_acc_blush"
    group face:
        attribute neutral default:
            "evelyn_exp_neutral"#
        attribute amused:
            "evelyn_exp_amused"#
        attribute laugh:
            "evelyn_exp_laugh"#
        attribute smile:
            "evelyn_exp_smile"#
        attribute surprise:
            "evelyn_exp_surprise"#
        attribute shock:
            "evelyn_exp_shock"#
        attribute angry:
            "evelyn_exp_angry"#
        attribute frown:
            "evelyn_exp_frown"#
        attribute sad:
            "evelyn_exp_sad"#
        attribute pain:
            "evelyn_exp_pain"#
    group accessories:
        attribute sweat:
            "evelyn_acc_sweat"
        attribute sweatdrop:
            "evelyn_acc_sweatdrop"
    at character_sprites_evelyn

image Evelyn_bub = LayeredImageProxy("Evelyn", Transform(crop=(140, 0, 244, 260), zoom=0.9, xpos=1748, ypos=750, anchor=((0.5,0))))#Bottom Right
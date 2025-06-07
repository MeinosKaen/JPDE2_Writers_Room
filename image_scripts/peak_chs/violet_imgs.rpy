image violet_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/violet/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/violet/body_base.png"
)
image violet_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/violet/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/violet/clothes_full.png"
)
image violet_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/violet/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/violet/exp_neutral.png"
)
image violet_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/violet/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/violet/exp_smile.png"
)
image violet_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/violet/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/violet/exp_amused.png"
)
image violet_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/violet/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/violet/exp_laugh.png"
)
image violet_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/violet/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/violet/exp_surprise.png"
)
image violet_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/violet/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/violet/exp_shock.png"
)
image violet_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/violet/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/violet/exp_angry.png"
)
image violet_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/violet/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/violet/exp_frown.png"
)
image violet_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/violet/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/violet/exp_sad.png"
)
image violet_exp_mad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/violet/exp_mad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/violet/exp_mad.png"
)
image violet_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/violet/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/violet/exp_pain.png"
)
image violet_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/violet/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/violet/acc_sweat.png"
)
image violet_acc_sparkle = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/violet/acc_sparkle.png",
    "persistent.PC98_mode == True", "images/PC98/ch/violet/acc_sparkle.png"
)
image violet_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/violet/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/violet/acc_blush.png"
)
image violet_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/violet/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/violet/acc_sweatdrop.png"
)
layeredimage Violet:
    group body:
        attribute base default:
            "violet_body_base"
    group clothes:
        attribute c_full default:
            "violet_clothes_full"
    group accessories_2:
        attribute blush:
            "violet_acc_blush"
    group face:
        attribute neutral default:
            "violet_exp_neutral"#
        attribute amused:
            "violet_exp_amused"#
        attribute laugh:
            "violet_exp_laugh"#
        attribute smile:
            "violet_exp_smile"#
        attribute surprise:
            "violet_exp_surprise"#
        attribute shock:
            "violet_exp_shock"#
        attribute angry:
            "violet_exp_angry"#
        attribute frown:
            "violet_exp_frown"#
        attribute sad:
            "violet_exp_sad"#
        attribute pain:
            "violet_exp_pain"#
        attribute mad:
            "violet_exp_mad"#
    group accessories:
        attribute sweat:
            "violet_acc_sweat"
        attribute sweatdrop:
            "violet_acc_sweatdrop"
        attribute sparkle:
            "violet_acc_sparkle"
    at character_sprites_violet
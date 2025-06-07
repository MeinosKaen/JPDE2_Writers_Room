image glynda_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/glynda/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/glynda/body_base.png"
)
image glynda_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/glynda/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/glynda/clothes_full.png"
)
image glynda_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/glynda/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/glynda/exp_neutral.png"
)
image glynda_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/glynda/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/glynda/exp_smile.png"
)
image glynda_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/glynda/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/glynda/exp_amused.png"
)
image glynda_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/glynda/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/glynda/exp_laugh.png"
)
image glynda_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/glynda/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/glynda/exp_surprise.png"
)
image glynda_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/glynda/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/glynda/exp_shock.png"
)
image glynda_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/glynda/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/glynda/exp_angry.png"
)
image glynda_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/glynda/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/glynda/exp_frown.png"
)
image glynda_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/glynda/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/glynda/exp_sad.png"
)
image glynda_exp_mad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/glynda/exp_mad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/glynda/exp_mad.png"
)
image glynda_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/glynda/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/glynda/exp_pain.png"
)
image glynda_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/glynda/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/glynda/acc_sweat.png"
)
image glynda_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/glynda/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/glynda/acc_blush.png"
)
image glynda_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/glynda/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/glynda/acc_sweatdrop.png"
)
image glynda_acc_glasses = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/glynda/acc_glasses.png",
    "persistent.PC98_mode == True", "images/PC98/ch/glynda/acc_glasses.png"
)
layeredimage Glynda:
    group body:
        attribute base default:
            "glynda_body_base"
    group clothes:
        attribute c_full default:
            "glynda_clothes_full"
    group accessories_2:
        attribute blush:
            "glynda_acc_blush"
    group face:
        attribute neutral default:
            "glynda_exp_neutral"#
        attribute amused:
            "glynda_exp_amused"#
        attribute laugh:
            "glynda_exp_laugh"#
        attribute smile:
            "glynda_exp_smile"#
        attribute surprise:
            "glynda_exp_surprise"#
        attribute shock:
            "glynda_exp_shock"#
        attribute angry:
            "glynda_exp_angry"#
        attribute frown:
            "glynda_exp_frown"#
        attribute sad:
            "glynda_exp_sad"#
        attribute pain:
            "glynda_exp_pain"#
        attribute mad:
            "glynda_exp_mad"#
    group accessories:
        attribute sweat:
            "glynda_acc_sweat"
        attribute sweatdrop:
            "glynda_acc_sweatdrop"
    group accessories_3:
        attribute glasses:
            "glynda_acc_glasses"
    at character_sprites_glynda
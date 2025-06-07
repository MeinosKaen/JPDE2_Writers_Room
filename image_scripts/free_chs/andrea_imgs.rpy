
image andrea_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/andrea/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/andrea/body_base.png"
)
image andrea_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/andrea/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/andrea/clothes_full.png"
)
image andrea_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/andrea/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/andrea/exp_neutral.png"
)
image andrea_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/andrea/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/andrea/exp_smile.png"
)
image andrea_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/andrea/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/andrea/exp_amused.png"
)
image andrea_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/andrea/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/andrea/exp_laugh.png"
)
image andrea_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/andrea/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/andrea/exp_surprise.png"
)
image andrea_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/andrea/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/andrea/exp_shock.png"
)
image andrea_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/andrea/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/andrea/exp_angry.png"
)
image andrea_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/andrea/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/andrea/exp_frown.png"
)
image andrea_exp_dist = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/andrea/exp_dist.png",
    "persistent.PC98_mode == True", "images/PC98/ch/andrea/exp_dist.png"
)
image andrea_exp_desp = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/andrea/exp_desp.png",
    "persistent.PC98_mode == True", "images/PC98/ch/andrea/exp_desp.png"
)
image andrea_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/andrea/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/andrea/exp_sad.png"
)
image andrea_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/andrea/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/andrea/exp_pain.png"
)
image andrea_exp_sigh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/andrea/exp_sigh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/andrea/exp_sigh.png"
)
image andrea_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/andrea/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/andrea/acc_sweat.png"
)
image andrea_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/andrea/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/andrea/acc_blush.png"
)
image andrea_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/andrea/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/andrea/acc_sweatdrop.png"
)
layeredimage Andrea:
    group body:
        attribute base default:
            "andrea_body_base"
    group clothes:
        attribute c_full default:
            "andrea_clothes_full"
    group accessories_2:
        attribute blush:
            "andrea_acc_blush"
    group face:
        attribute neutral default:
            "andrea_exp_neutral"#
        attribute amused:
            "andrea_exp_amused"#
        attribute laugh:
            "andrea_exp_laugh"#
        attribute smile:
            "andrea_exp_smile"#
        attribute surprise:
            "andrea_exp_surprise"#
        attribute shock:
            "andrea_exp_shock"#
        attribute angry:
            "andrea_exp_angry"#
        attribute frown:
            "andrea_exp_frown"#
        attribute desp:
            "andrea_exp_desp"#
        attribute dist:
            "andrea_exp_dist"#
        attribute sad:
            "andrea_exp_sad"#
        attribute pain:
            "andrea_exp_pain"#
        attribute sigh:
            "andrea_exp_sigh"#
    group accessories:
        attribute sweat:
            "andrea_acc_sweat"
        attribute sweatdrop:
            "andrea_acc_sweatdrop"
    at character_sprites_andrea
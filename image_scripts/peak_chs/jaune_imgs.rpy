
image jaune_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jaune/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jaune/body_base.png"
)
image jaune_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jaune/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jaune/clothes_full.png"
)
image jaune_clothes_half = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jaune/clothes_half.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jaune/clothes_half.png"
)
image jaune_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jaune/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jaune/exp_neutral.png"
)
image jaune_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jaune/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jaune/exp_smile.png"
)
image jaune_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jaune/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jaune/exp_amused.png"
)
image jaune_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jaune/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jaune/exp_laugh.png"
)
image jaune_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jaune/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jaune/exp_surprise.png"
)
image jaune_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jaune/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jaune/exp_shock.png"
)
image jaune_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jaune/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jaune/exp_angry.png"
)
image jaune_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jaune/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jaune/exp_frown.png"
)
image jaune_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jaune/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jaune/exp_sad.png"
)
image jaune_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jaune/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jaune/exp_pain.png"
)
image jaune_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jaune/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jaune/acc_sweat.png"
)
image jaune_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jaune/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jaune/acc_blush.png"
)
image jaune_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jaune/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jaune/acc_sweatdrop.png"
)
layeredimage Jaune:
    group body:
        attribute base default:
            "jaune_body_base"
    group clothes:
        attribute c_full default:
            "jaune_clothes_full"
        attribute c_half:
            "jaune_clothes_half"
    group accessories_2:
        attribute blush:
            "jaune_acc_blush"
    group face:
        attribute neutral default:
            "jaune_exp_neutral"#
        attribute amused:
            "jaune_exp_amused"#
        attribute laugh:
            "jaune_exp_laugh"#
        attribute smile:
            "jaune_exp_smile"#
        attribute surprise:
            "jaune_exp_surprise"#
        attribute shock:
            "jaune_exp_shock"#
        attribute angry:
            "jaune_exp_angry"#
        attribute frown:
            "jaune_exp_frown"#
        attribute sad:
            "jaune_exp_sad"#
        attribute pain:
            "jaune_exp_pain"#
    group accessories:
        attribute sweat:
            "jaune_acc_sweat"
        attribute sweatdrop:
            "jaune_acc_sweatdrop"
    at character_sprites_jaune
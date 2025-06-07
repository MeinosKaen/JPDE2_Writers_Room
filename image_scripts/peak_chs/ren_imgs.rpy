#Character Layered Images
#Conditional Ren Images
image ren_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ren/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ren/body_base.png"
)
image ren_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ren/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ren/clothes_full.png"
)
image ren_clothes_half = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ren/clothes_half.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ren/clothes_half.png"
)
image ren_acc_sparkle = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ren/acc_sparkle.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ren/acc_sparkle.png"
)
image ren_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ren/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ren/exp_neutral.png"
)
image ren_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ren/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ren/exp_smile.png"
)
image ren_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ren/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ren/exp_amused.png"
)
image ren_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ren/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ren/exp_laugh.png"
)
image ren_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ren/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ren/exp_surprise.png"
)
image ren_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ren/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ren/exp_shock.png"
)
image ren_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ren/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ren/exp_angry.png"
)
image ren_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ren/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ren/exp_frown.png"
)
image ren_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ren/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ren/exp_sad.png"
)
image ren_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ren/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ren/exp_pain.png"
)
image ren_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ren/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ren/acc_sweat.png"
)
image ren_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ren/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ren/acc_blush.png"
)
image ren_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ren/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ren/acc_sweatdrop.png"
)
layeredimage Ren:
    group body:
        attribute base default:
            "ren_body_base"
    group clothes:
        attribute c_full default:
            "ren_clothes_full"
        attribute c_half:
            "ren_clothes_half"
    group accessories_2:
        attribute sparkle:
            "ren_acc_sparkle"
    group accessories_3:
        attribute blush:
            "ren_acc_blush"
    group face:
        attribute neutral default:
            "ren_exp_neutral"#
        attribute amused:
            "ren_exp_amused"#
        attribute laugh:
            "ren_exp_laugh"#
        attribute smile:
            "ren_exp_smile"#
        attribute surprise:
            "ren_exp_surprise"#
        attribute shock:
            "ren_exp_shock"#
        attribute angry:
            "ren_exp_angry"#
        attribute frown:
            "ren_exp_frown"#
        attribute sad:
            "ren_exp_sad"#
        attribute pain:
            "ren_exp_pain"#
        attribute fury:
            "ren_exp_fury"#
    group accessories:
        attribute sweat:
            "ren_acc_sweat"
        attribute sweatdrop:
            "ren_acc_sweatdrop"
    at character_sprites_ren
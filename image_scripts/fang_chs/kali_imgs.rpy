
image kali_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/kali/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/kali/body_base.png"
)
image kali_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/kali/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/kali/clothes_full.png"
)
image kali_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/kali/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/kali/exp_neutral.png"
)
image kali_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/kali/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/kali/exp_smile.png"
)
image kali_exp_csmile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/kali/exp_csmile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/kali/exp_csmile.png"
)
image kali_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/kali/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/kali/exp_amused.png"
)
image kali_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/kali/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/kali/exp_laugh.png"
)
image kali_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/kali/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/kali/exp_surprise.png"
)
image kali_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/kali/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/kali/exp_shock.png"
)
image kali_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/kali/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/kali/exp_angry.png"
)
image kali_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/kali/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/kali/exp_frown.png"
)
image kali_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/kali/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/kali/exp_sad.png"
)
image kali_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/kali/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/kali/exp_pain.png"
)
image kali_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/kali/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/kali/acc_sweat.png"
)
image kali_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/kali/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/kali/acc_blush.png"
)
image kali_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/kali/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/kali/acc_sweatdrop.png"
)
layeredimage Kali:
    group body:
        attribute base default:
            "kali_body_base"
    group clothes:
        attribute c_full default:
            "kali_clothes_full"
    group accessories_2:
        attribute blush:
            "kali_acc_blush"
    group face:
        attribute neutral default:
            "kali_exp_neutral"#
        attribute amused:
            "kali_exp_amused"#
        attribute laugh:
            "kali_exp_laugh"#
        attribute smile:
            "kali_exp_smile"#
        attribute csmile:
            "kali_exp_csmile"#
        attribute surprise:
            "kali_exp_surprise"#
        attribute shock:
            "kali_exp_shock"#
        attribute angry:
            "kali_exp_angry"#
        attribute frown:
            "kali_exp_frown"#
        attribute sad:
            "kali_exp_sad"#
        attribute pain:
            "kali_exp_pain"#
    group accessories:
        attribute sweat:
            "kali_acc_sweat"
        attribute sweatdrop:
            "kali_acc_sweatdrop"
    at character_sprites_kali
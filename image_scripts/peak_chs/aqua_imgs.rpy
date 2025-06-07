image aqua_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/aqua/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/aqua/body_base.png"
)
image aqua_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/aqua/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/aqua/clothes_full.png"
)
image aqua_clothes_half = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/aqua/clothes_half.png",
    "persistent.PC98_mode == True", "images/PC98/ch/aqua/clothes_half.png"
)
image aqua_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/aqua/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/aqua/exp_neutral.png"
)
image aqua_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/aqua/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/aqua/exp_smile.png"
)
image aqua_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/aqua/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/aqua/exp_amused.png"
)
image aqua_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/aqua/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/aqua/exp_laugh.png"
)
image aqua_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/aqua/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/aqua/exp_surprise.png"
)
image aqua_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/aqua/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/aqua/exp_shock.png"
)
image aqua_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/aqua/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/aqua/exp_angry.png"
)
image aqua_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/aqua/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/aqua/exp_frown.png"
)
image aqua_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/aqua/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/aqua/exp_sad.png"
)
image aqua_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/aqua/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/aqua/exp_pain.png"
)
image aqua_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/aqua/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/aqua/acc_sweat.png"
)
image aqua_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/aqua/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/aqua/acc_blush.png"
)
image aqua_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/aqua/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/aqua/acc_sweatdrop.png"
)
image aqua_acc_scarf = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/aqua/acc_scarf.png",
    "persistent.PC98_mode == True", "images/PC98/ch/aqua/acc_scarf.png"
)
image aqua_acc_eye_up = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/aqua/acc_eye_up.png",
    "persistent.PC98_mode == True", "images/PC98/ch/aqua/acc_eye_up.png"
)
image aqua_acc_eye_down = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/aqua/acc_eye_down.png",
    "persistent.PC98_mode == True", "images/PC98/ch/aqua/acc_eye_down.png"
)
layeredimage Aqua:
    group body:
        attribute base default:
            "aqua_body_base"
    group clothes:
        attribute c_full default:
            "aqua_clothes_full"
        attribute c_half:
            "aqua_clothes_half"
    group accessories_2:
        attribute blush:
            "aqua_acc_blush"
        attribute scarf:
            "aqua_acc_scarf"
    group face:
        attribute neutral default:
            "aqua_exp_neutral"#
        attribute amused:
            "aqua_exp_amused"#
        attribute laugh:
            "aqua_exp_laugh"#
        attribute smile:
            "aqua_exp_smile"#
        attribute surprise:
            "aqua_exp_surprise"#
        attribute shock:
            "aqua_exp_shock"#
        attribute angry:
            "aqua_exp_angry"#
        attribute frown:
            "aqua_exp_frown"#
        attribute sad:
            "aqua_exp_sad"#
        attribute pain:
            "aqua_exp_pain"#
    group accessories:
        attribute sweat:
            "aqua_acc_sweat"
        attribute sweatdrop:
            "aqua_acc_sweatdrop"
    group accessories_3:
        attribute eye_up:
            "aqua_acc_eye_up"
        attribute eye_down default:
            "aqua_acc_eye_down"
    at character_sprites_aqua
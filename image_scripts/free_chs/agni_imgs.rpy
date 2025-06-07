
image agni_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/agni/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/agni/body_base.png"
)
image agni_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/agni/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/agni/clothes_full.png"
)
image agni_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/agni/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/agni/exp_neutral.png"
)
image agni_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/agni/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/agni/exp_smile.png"
)
image agni_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/agni/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/agni/exp_amused.png"
)
image agni_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/agni/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/agni/exp_laugh.png"
)
image agni_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/agni/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/agni/exp_laugh.png"
)
image agni_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/agni/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/agni/exp_surprise.png"
)
image agni_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/agni/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/agni/exp_shock.png"
)
image agni_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/agni/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/agni/exp_angry.png"
)
image agni_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/agni/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/agni/exp_frown.png"
)
image agni_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/agni/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/agni/exp_sad.png"
)
image agni_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/agni/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/agni/exp_pain.png"
)
image agni_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/agni/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/agni/acc_sweat.png"
)
image agni_acc_fire = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/agni/acc_fire.png",
    "persistent.PC98_mode == True", "images/PC98/ch/agni/acc_fire.png"
)
image agni_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/agni/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/agni/acc_blush.png"
)
image agni_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/agni/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/agni/acc_sweatdrop.png"
)
layeredimage Agni:
    group body:
        attribute base default:
            "agni_body_base"
    group clothes:
        attribute c_full default:
            "agni_clothes_full"
    group accessories_2:
        attribute blush:
            "agni_acc_blush"
    group face:
        attribute neutral default:
            "agni_exp_neutral"#
        attribute amused:
            "agni_exp_amused"#
        attribute laugh:
            "agni_exp_laugh"#
            
        attribute smile:
            "agni_exp_smile"#
        attribute surprise:
            "agni_exp_surprise"#
        attribute shock:
            "agni_exp_shock"#
        attribute angry:
            "agni_exp_angry"#
        attribute frown:
            "agni_exp_frown"#
        attribute sad:
            "agni_exp_sad"#
        attribute pain:
            "agni_exp_pain"#
    group accessories:
        attribute sweat:
            "agni_acc_sweat"
        attribute sweatdrop:
            "agni_acc_sweatdrop"
    group accessories_3:
        attribute fire:
            "agni_acc_fire"
    at character_sprites_agni
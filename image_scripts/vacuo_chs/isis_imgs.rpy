
image isis_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/isis/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/isis/body_base.png"
)
image isis_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/isis/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/isis/clothes_full.png"
)
image isis_clothes_half = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/isis/clothes_half.png",
    "persistent.PC98_mode == True", "images/PC98/ch/isis/clothes_half.png"
)
image isis_acc_hat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/isis/acc_hat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/isis/acc_hat.png"
)
image isis_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/isis/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/isis/exp_neutral.png"
)
image isis_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/isis/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/isis/exp_smile.png"
)
image isis_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/isis/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/isis/exp_amused.png"
)
image isis_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/isis/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/isis/exp_laugh.png"
)
image isis_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/isis/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/isis/exp_surprise.png"
)
image isis_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/isis/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/isis/exp_shock.png"
)
image isis_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/isis/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/isis/exp_angry.png"
)
image isis_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/isis/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/isis/exp_frown.png"
)
image isis_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/isis/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/isis/exp_sad.png"
)
image isis_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/isis/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/isis/exp_pain.png"
)
image isis_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/isis/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/isis/acc_sweat.png"
)
image isis_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/isis/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/isis/acc_blush.png"
)
image isis_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/isis/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/isis/acc_sweatdrop.png"
)
layeredimage Isis:
    group body:
        attribute base default:
            "isis_body_base"
    group clothes:
        attribute c_half:
            "isis_clothes_half"
        attribute c_full default:
            "isis_clothes_full"
    group accessories_2:
        attribute blush:
            "isis_acc_blush"
    group face:
        attribute neutral default:
            "isis_exp_neutral"#
        attribute amused:
            "isis_exp_amused"#
        attribute laugh:
            "isis_exp_laugh"#
        attribute smile:
            "isis_exp_smile"#
        attribute surprise:
            "isis_exp_surprise"#
        attribute shock:
            "isis_exp_shock"#
        attribute angry:
            "isis_exp_angry"#
        attribute frown:
            "isis_exp_frown"#
        attribute sad:
            "isis_exp_sad"#
        attribute pain:
            "isis_exp_pain"#
    group accessories:
        attribute sweat:
            "isis_acc_sweat"
        attribute sweatdrop:
            "isis_acc_sweatdrop"
    group accessories_3:
        attribute hat default:
            "isis_acc_hat"
    at character_sprites_isis
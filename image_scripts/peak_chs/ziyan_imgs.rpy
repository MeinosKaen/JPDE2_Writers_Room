image ziyan_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ziyan/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ziyan/body_base.png"
)
image ziyan_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ziyan/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ziyan/clothes_full.png"
)
image ziyan_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ziyan/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ziyan/exp_neutral.png"
)
image ziyan_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ziyan/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ziyan/exp_smile.png"
)
image ziyan_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ziyan/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ziyan/exp_amused.png"
)
image ziyan_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ziyan/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ziyan/exp_laugh.png"
)
image ziyan_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ziyan/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ziyan/exp_surprise.png"
)
image ziyan_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ziyan/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ziyan/exp_shock.png"
)
image ziyan_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ziyan/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ziyan/exp_angry.png"
)
image ziyan_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ziyan/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ziyan/exp_frown.png"
)
image ziyan_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ziyan/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ziyan/exp_sad.png"
)
image ziyan_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ziyan/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ziyan/exp_pain.png"
)
image ziyan_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ziyan/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ziyan/acc_sweat.png"
)
image ziyan_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ziyan/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ziyan/acc_blush.png"
)
image ziyan_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ziyan/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ziyan/acc_sweatdrop.png"
)
layeredimage Ziyan:
    group body:
        attribute base default:
            "ziyan_body_base"
    group clothes:
        attribute c_full default:
            "ziyan_clothes_full"
    group accessories_2:
        attribute blush:
            "ziyan_acc_blush"
    group face:
        attribute neutral default:
            "ziyan_exp_neutral"#
        attribute amused:
            "ziyan_exp_amused"#
        attribute laugh:
            "ziyan_exp_laugh"#
        attribute smile:
            "ziyan_exp_smile"#
        attribute surprise:
            "ziyan_exp_surprise"#
        attribute shock:
            "ziyan_exp_shock"#
        attribute angry:
            "ziyan_exp_angry"#
        attribute frown:
            "ziyan_exp_frown"#
        attribute sad:
            "ziyan_exp_sad"#
        attribute pain:
            "ziyan_exp_pain"#
    group accessories:
        attribute sweat:
            "ziyan_acc_sweat"
        attribute sweatdrop:
            "ziyan_acc_sweatdrop"
    at character_sprites_ziyan
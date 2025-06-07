image torchwick_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/torchwick/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/torchwick/body_base.png"
)
image torchwick_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/torchwick/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/torchwick/clothes_full.png"
)
image torchwick_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/torchwick/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/torchwick/exp_neutral.png"
)
image torchwick_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/torchwick/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/torchwick/exp_smile.png"
)
image torchwick_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/torchwick/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/torchwick/exp_amused.png"
)
image torchwick_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/torchwick/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/torchwick/exp_surprise.png"
)
image torchwick_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/torchwick/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/torchwick/exp_shock.png"
)
image torchwick_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/torchwick/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/torchwick/exp_angry.png"
)
image torchwick_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/torchwick/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/torchwick/exp_frown.png"
)
image torchwick_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/torchwick/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/torchwick/exp_sad.png"
)
image torchwick_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/torchwick/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/torchwick/exp_pain.png"
)
image torchwick_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/torchwick/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/torchwick/acc_sweat.png"
)
image torchwick_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/torchwick/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/torchwick/acc_blush.png"
)
image torchwick_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/torchwick/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/torchwick/acc_sweatdrop.png"
)
layeredimage Torchwick:
    group body:
        attribute base default:
            "torchwick_body_base"
    group clothes:
        attribute c_full default:
            "torchwick_clothes_full"
    group accessories_2:
        attribute blush:
            "torchwick_acc_blush"
    group face:
        attribute neutral default:
            "torchwick_exp_neutral"#
        attribute amused:
            "torchwick_exp_amused"#
        attribute smile:
            "torchwick_exp_smile"#
        attribute surprise:
            "torchwick_exp_surprise"#
        attribute shock:
            "torchwick_exp_shock"#
        attribute angry:
            "torchwick_exp_angry"#
        attribute frown:
            "torchwick_exp_frown"#
        attribute sad:
            "torchwick_exp_sad"#
        attribute pain:
            "torchwick_exp_pain"#
    group accessories:
        attribute sweat:
            "torchwick_acc_sweat"
        attribute sweatdrop:
            "torchwick_acc_sweatdrop"
    at character_sprites

image sierra_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sierra/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sierra/body_base.png"
)
image sierra_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sierra/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sierra/clothes_full.png"
)
image sierra_clothes_half = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sierra/clothes_half.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sierra/clothes_half.png"
)
image sierra_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sierra/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sierra/exp_neutral.png"
)
image sierra_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sierra/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sierra/exp_smile.png"
)
image sierra_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sierra/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sierra/exp_amused.png"
)
image sierra_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sierra/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sierra/exp_laugh.png"
)
image sierra_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sierra/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sierra/exp_surprise.png"
)
image sierra_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sierra/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sierra/exp_shock.png"
)
image sierra_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sierra/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sierra/exp_angry.png"
)
image sierra_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sierra/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sierra/exp_frown.png"
)
image sierra_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sierra/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sierra/exp_sad.png"
)
image sierra_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sierra/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sierra/exp_pain.png"
)
image sierra_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sierra/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sierra/acc_sweat.png"
)
image sierra_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sierra/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sierra/acc_blush.png"
)
image sierra_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sierra/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sierra/acc_sweatdrop.png"
)
image sierra_acc_bag = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sierra/acc_bag.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sierra/acc_bag.png"
)
layeredimage Sierra:
    group body:
        attribute base default:
            "sierra_body_base"
    group clothes:
        attribute c_full default:
            "sierra_clothes_full"
        attribute c_half:
            "sierra_clothes_half"
    group accessories_2:
        attribute blush:
            "sierra_acc_blush"
    group face:
        attribute neutral default:
            "sierra_exp_neutral"#
        attribute amused:
            "sierra_exp_amused"#
        attribute laugh:
            "sierra_exp_laugh"#
        attribute smile:
            "sierra_exp_smile"#
        attribute surprise:
            "sierra_exp_surprise"#
        attribute shock:
            "sierra_exp_shock"#
        attribute angry:
            "sierra_exp_angry"#
        attribute frown:
            "sierra_exp_frown"#
        attribute sad:
            "sierra_exp_sad"#
        attribute pain:
            "sierra_exp_pain"#
    group accessories:
        attribute sweat:
            "sierra_acc_sweat"
        attribute sweatdrop:
            "sierra_acc_sweatdrop"
    group accessories_3:
        attribute bag:
            "sierra_acc_bag"
    at character_sprites_sierra
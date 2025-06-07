
image weser_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/weser/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/weser/body_base.png"
)
image weser_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/weser/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/weser/clothes_full.png"
)
image weser_acc_jacket = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/weser/acc_jacket.png",
    "persistent.PC98_mode == True", "images/PC98/ch/weser/acc_jacket.png"
)
image weser_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/weser/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/weser/exp_neutral.png"
)
image weser_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/weser/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/weser/exp_smile.png"
)
image weser_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/weser/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/weser/exp_amused.png"
)
image weser_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/weser/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/weser/exp_laugh.png"
)
image weser_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/weser/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/weser/exp_surprise.png"
)
image weser_exp_mad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/weser/exp_mad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/weser/exp_mad.png"
)
image weser_exp_crazy = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/weser/exp_crazy.png",
    "persistent.PC98_mode == True", "images/PC98/ch/weser/exp_crazy.png"
)
image weser_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/weser/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/weser/exp_shock.png"
)
image weser_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/weser/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/weser/exp_angry.png"
)
image weser_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/weser/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/weser/exp_frown.png"
)
image weser_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/weser/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/weser/exp_pain.png"
)
image weser_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/weser/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/weser/acc_sweat.png"
)
image weser_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/weser/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/weser/acc_blush.png"
)
image weser_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/weser/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/weser/acc_sweatdrop.png"
)
layeredimage Weser:
    group body:
        attribute base default:
            "weser_body_base"
    group clothes:
        attribute c_full default:
            "weser_clothes_full"
    group accessories_2:
        attribute blush:
            "weser_acc_blush"
    group face:
        attribute neutral default:
            "weser_exp_neutral"#
        attribute amused:
            "weser_exp_amused"#
        attribute laugh:
            "weser_exp_laugh"#
        attribute smile:
            "weser_exp_smile"#
        attribute surprise:
            "weser_exp_surprise"#
        attribute crazy:
            "weser_exp_crazy"#
        attribute mad:
            "weser_exp_mad"#
        attribute shock:
            "weser_exp_shock"#
        attribute angry:
            "weser_exp_angry"#
        attribute frown:
            "weser_exp_frown"#
        attribute pain:
            "weser_exp_pain"#
    group accessories:
        attribute sweat:
            "weser_acc_sweat"
        attribute sweatdrop:
            "weser_acc_sweatdrop"
    group accessories_3:
        attribute jacket:
            "weser_acc_jacket"
    at character_sprites_weser
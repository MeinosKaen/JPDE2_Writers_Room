image tip_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/body_base.png"
)
image tip_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/clothes_full.png"
)
image tip_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/exp_neutral.png"
)
image tip_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/exp_smile.png"
)
image tip_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/exp_amused.png"
)
image tip_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/exp_laugh.png"
)
image tip_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/exp_surprise.png"
)
image tip_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/exp_shock.png"
)
image tip_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/exp_angry.png"
)
image tip_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/exp_frown.png"
)
image tip_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/exp_sad.png"
)
image tip_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/exp_pain.png"
)
image tip_exp_cringe = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/exp_cringe.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/exp_cringe.png"
)
image tip_exp_w_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/wizard/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/wizard/exp_neutral.png"
)
image tip_exp_w_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/wizard/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/wizard/exp_smile.png"
)
image tip_exp_w_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/wizard/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/wizard/exp_amused.png"
)
image tip_exp_w_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/wizard/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/wizard/exp_laugh.png"
)
image tip_exp_w_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/wizard/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/wizard/exp_surprise.png"
)
image tip_exp_w_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/wizard/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/wizard/exp_shock.png"
)
image tip_exp_w_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/wizard/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/wizard/exp_angry.png"
)
image tip_exp_w_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/wizard/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/wizard/exp_frown.png"
)
image tip_exp_w_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/wizard/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/wizard/exp_sad.png"
)
image tip_exp_w_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/wizard/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/wizard/exp_pain.png"
)
image tip_exp_w_cringe = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/wizard/exp_cringe.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/wizard/exp_cringe.png"
)
image tip_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/acc_sweat.png"
)
image tip_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/acc_blush.png"
)
image tip_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/tip/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/tip/acc_sweatdrop.png"
)
layeredimage Tip:
    group body:
        attribute base default:
            "tip_body_base"
    group clothes:
        attribute c_full default:
            "tip_clothes_full"
    group accessories_2:
        attribute blush:
            "tip_acc_blush"
    group face:
        attribute neutral default:
            "tip_exp_neutral"#
        attribute amused:
            "tip_exp_amused"#
        attribute laugh:
            "tip_exp_laugh"#
        attribute smile:
            "tip_exp_smile"#
        attribute surprise:
            "tip_exp_surprise"#
        attribute shock:
            "tip_exp_shock"#
        attribute angry:
            "tip_exp_angry"#
        attribute frown:
            "tip_exp_frown"#
        attribute sad:
            "tip_exp_sad"#
        attribute pain:
            "tip_exp_pain"#
        attribute cringe:
            "tip_exp_cringe"#
        attribute w_neutral:
            "tip_exp_w_neutral"#
        attribute w_amused:
            "tip_exp_w_amused"#
        attribute w_laugh:
            "tip_exp_w_laugh"#
        attribute w_smile:
            "tip_exp_w_smile"#
        attribute w_surprise:
            "tip_exp_w_surprise"#
        attribute w_shock:
            "tip_exp_w_shock"#
        attribute w_angry:
            "tip_exp_w_angry"#
        attribute w_frown:
            "tip_exp_w_frown"#
        attribute w_sad:
            "tip_exp_w_sad"#
        attribute w_pain:
            "tip_exp_w_pain"#
        attribute w_cringe:
            "tip_exp_w_cringe"#
    group accessories:
        attribute sweat:
            "tip_acc_sweat"
        attribute sweatdrop:
            "tip_acc_sweatdrop"
    at character_sprites_tip
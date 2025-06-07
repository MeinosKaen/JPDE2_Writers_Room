
image janara_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/body_base.png"
)
image janara_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/clothes_full.png"
)
image janara_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/exp_neutral.png"
)
image janara_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/exp_smile.png"
)
image janara_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/exp_amused.png"
)
image janara_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/exp_laugh.png"
)
image janara_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/exp_surprise.png"
)
image janara_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/exp_shock.png"
)
image janara_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/exp_angry.png"
)
image janara_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/exp_frown.png"
)
image janara_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/exp_sad.png"
)
image janara_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/exp_pain.png"
)
image janara_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/acc_sweat.png"
)
image janara_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/acc_blush.png"
)
image janara_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/acc_sweatdrop.png"
)
image janara_exp_w_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/witch/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/witch/exp_neutral.png"
)
image janara_exp_w_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/witch/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/witch/exp_smile.png"
)
image janara_exp_w_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/witch/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/witch/exp_amused.png"
)
image janara_exp_w_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/witch/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/witch/exp_laugh.png"
)
image janara_exp_w_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/witch/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/witch/exp_surprise.png"
)
image janara_exp_w_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/witch/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/witch/exp_shock.png"
)
image janara_exp_w_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/witch/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/witch/exp_angry.png"
)
image janara_exp_w_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/witch/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/witch/exp_frown.png"
)
image janara_exp_w_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/witch/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/witch/exp_sad.png"
)
image janara_exp_w_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/janara/witch/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/janara/witch/exp_pain.png"
)
layeredimage Janara:
    group body:
        attribute base default:
            "janara_body_base"
    group clothes:
        attribute c_full default:
            "janara_clothes_full"
    group accessories_2:
        attribute blush:
            "janara_acc_blush"
    group face:
        attribute neutral default:
            "janara_exp_neutral"#
        attribute amused:
            "janara_exp_amused"#
        attribute laugh:
            "janara_exp_laugh"#
        attribute smile:
            "janara_exp_smile"#
        attribute surprise:
            "janara_exp_surprise"#
        attribute shock:
            "janara_exp_shock"#
        attribute angry:
            "janara_exp_angry"#
        attribute frown:
            "janara_exp_frown"#
        attribute sad:
            "janara_exp_sad"#
        attribute pain:
            "janara_exp_pain"#
        attribute w_neutral:
            "janara_exp_w_neutral"#
        attribute w_amused:
            "janara_exp_w_amused"#
        attribute w_laugh:
            "janara_exp_w_laugh"#
        attribute w_smile:
            "janara_exp_w_smile"#
        attribute w_surprise:
            "janara_exp_w_surprise"#
        attribute w_shock:
            "janara_exp_w_shock"#
        attribute w_angry:
            "janara_exp_w_angry"#
        attribute w_frown:
            "janara_exp_w_frown"#
        attribute w_sad:
            "janara_exp_w_sad"#
        attribute w_pain:
            "janara_exp_w_pain"#
    group accessories:
        attribute sweat:
            "janara_acc_sweat"
        attribute sweatdrop:
            "janara_acc_sweatdrop"
    at character_sprites_janara
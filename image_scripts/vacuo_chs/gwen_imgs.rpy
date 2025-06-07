
image gwen_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gwen/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gwen/body_base.png"
)
image gwen_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gwen/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gwen/clothes_full.png"
)
image gwen_acc_ribbon = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gwen/acc_ribbon.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gwen/acc_ribbon.png"
)
image gwen_acc_lilribbons = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gwen/acc_lilribbons.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gwen/acc_lilribbons.png"
)
image gwen_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gwen/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gwen/exp_neutral.png"
)
image gwen_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gwen/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gwen/exp_smile.png"
)
image gwen_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gwen/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gwen/exp_amused.png"
)
image gwen_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gwen/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gwen/exp_laugh.png"
)
image gwen_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gwen/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gwen/exp_surprise.png"
)
image gwen_exp_cold = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gwen/exp_cold.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gwen/exp_cold.png"
)
image gwen_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gwen/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gwen/exp_shock.png"
)
image gwen_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gwen/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gwen/exp_angry.png"
)
image gwen_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gwen/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gwen/exp_frown.png"
)
image gwen_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gwen/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gwen/exp_sad.png"
)
image gwen_exp_mock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gwen/exp_mock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gwen/exp_mock.png"
)
image gwen_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gwen/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gwen/exp_pain.png"
)
image gwen_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gwen/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gwen/acc_sweat.png"
)
image gwen_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gwen/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gwen/acc_blush.png"
)
image gwen_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gwen/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gwen/acc_sweatdrop.png"
)
layeredimage Gwen:
    group accessories_3:
        attribute ribbon:
            "gwen_acc_ribbon"
    group body:
        attribute base default:
            "gwen_body_base"
    group clothes:
        attribute c_full default:
            "gwen_clothes_full"
    group accessories_4:
        attribute lilribbons default if_any "ribbon":
            "gwen_acc_lilribbons"
    group accessories_2:
        attribute blush:
            "gwen_acc_blush"
    group face:
        attribute neutral default:
            "gwen_exp_neutral"#
        attribute amused:
            "gwen_exp_amused"#
        attribute laugh:
            "gwen_exp_laugh"#
        attribute smile:
            "gwen_exp_smile"#
        attribute cold:
            "gwen_exp_cold"#
        attribute surprise:
            "gwen_exp_surprise"#
        attribute shock:
            "gwen_exp_shock"#
        attribute angry:
            "gwen_exp_angry"#
        attribute frown:
            "gwen_exp_frown"#
        attribute mock:
            "gwen_exp_mock"#
        attribute sad:
            "gwen_exp_sad"#
        attribute pain:
            "gwen_exp_pain"#
    group accessories:
        attribute sweat:
            "gwen_acc_sweat"
        attribute sweatdrop:
            "gwen_acc_sweatdrop"
    at character_sprites_gwen
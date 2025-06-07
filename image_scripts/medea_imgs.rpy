
image medea_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/medea/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/medea/body_base.png"
)
image medea_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/medea/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/medea/clothes_full.png"
)
image medea_acc_hat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/medea/acc_hat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/medea/acc_hat.png"
)
image medea_acc_jwls = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/medea/acc_jwls.png",
    "persistent.PC98_mode == True", "images/PC98/ch/medea/acc_jwls.png"
)
image medea_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/medea/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/medea/exp_neutral.png"
)
image medea_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/medea/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/medea/exp_smile.png"
)
image medea_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/medea/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/medea/exp_amused.png"
)
image medea_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/medea/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/medea/exp_laugh.png"
)
image medea_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/medea/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/medea/exp_surprise.png"
)
image medea_exp_cold = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/medea/exp_cold.png",
    "persistent.PC98_mode == True", "images/PC98/ch/medea/exp_cold.png"
)
image medea_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/medea/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/medea/exp_shock.png"
)
image medea_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/medea/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/medea/exp_angry.png"
)
image medea_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/medea/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/medea/exp_frown.png"
)
image medea_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/medea/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/medea/exp_sad.png"
)
image medea_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/medea/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/medea/exp_pain.png"
)
image medea_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/medea/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/medea/acc_sweat.png"
)
image medea_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/medea/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/medea/acc_blush.png"
)
image medea_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/medea/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/medea/acc_sweatdrop.png"
)
layeredimage Medea:
    group body:
        attribute base default:
            "medea_body_base"
    group accessories_2:
        attribute blush:
            "medea_acc_blush"
    group face:
        attribute neutral default:
            "medea_exp_neutral"#
        attribute amused:
            "medea_exp_amused"#
        attribute laugh:
            "medea_exp_laugh"#
        attribute smile:
            "medea_exp_smile"#
        attribute cold:
            "medea_exp_cold"#
        attribute surprise:
            "medea_exp_surprise"#
        attribute shock:
            "medea_exp_shock"#
        attribute angry:
            "medea_exp_angry"#
        attribute frown:
            "medea_exp_frown"#
        attribute sad:
            "medea_exp_sad"#
        attribute pain:
            "medea_exp_pain"#
    group clothes:
        attribute c_full default:
            "medea_clothes_full"
    group accessories:
        attribute sweat:
            "medea_acc_sweat"
        attribute sweatdrop:
            "medea_acc_sweatdrop"
    group accessories_4:
        attribute jwls:
            "medea_acc_jwls"
    group accessories_3:
        attribute hat:
            "medea_acc_hat"
    at character_sprites_medea
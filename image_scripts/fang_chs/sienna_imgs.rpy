#Character Layered Images
#Conditional Sienna Images
image sienna_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sienna/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sienna/body_base.png"
)
image sienna_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sienna/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sienna/exp_neutral.png"
)
image sienna_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sienna/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sienna/exp_smile.png"
)
image sienna_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sienna/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sienna/exp_amused.png"
)
image sienna_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sienna/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sienna/exp_surprise.png"
)
image sienna_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sienna/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sienna/exp_shock.png"
)
image sienna_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sienna/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sienna/exp_angry.png"
)
image sienna_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sienna/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sienna/exp_frown.png"
)
image sienna_exp_fury = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sienna/exp_fury.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sienna/exp_fury.png"
)
image sienna_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sienna/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sienna/exp_sad.png"
)
image sienna_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sienna/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sienna/exp_pain.png"
)
image sienna_exp_tsk = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sienna/exp_tsk.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sienna/exp_tsk.png"
)
image sienna_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sienna/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sienna/acc_sweat.png"
)
image sienna_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sienna/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sienna/acc_blush.png"
)
image sienna_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/sienna/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/sienna/acc_sweatdrop.png"
)

layeredimage Sienna:
    group body:
        attribute base default:
            "sienna_body_base"
    group accessories_2:
        attribute blush:
            "sienna_acc_blush"
    group face:
        attribute neutral default:
            "sienna_exp_neutral"#
        attribute amused:
            "sienna_exp_amused"#
        attribute smile:
            "sienna_exp_smile"#
        attribute surprise:
            "sienna_exp_surprise"#
        attribute shock:
            "sienna_exp_shock"#
        attribute angry:
            "sienna_exp_angry"#
        attribute frown:
            "sienna_exp_frown"#
        attribute fury:
            "sienna_exp_fury"#
        attribute sad:
            "sienna_exp_sad"#
        attribute pain:
            "sienna_exp_pain"#
        attribute tsk:
            "sienna_exp_tsk"#
    group accessories:
        attribute sweat:
            "sienna_acc_sweat"
        attribute sweatdrop:
            "sienna_acc_sweatdrop"
    at character_sprites_sienna

image Sienna_bub = LayeredImageProxy("Sienna", Transform(crop=(60, 0, 225, 238), zoom=0.9, xpos=1727, ypos=760, anchor=((0.5,0))))#LOWER RIGHT
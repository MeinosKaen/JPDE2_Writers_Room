#Character Layered Images
#Conditional Nora Images
image nora_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/nora/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/nora/body_base.png"
)
image nora_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/nora/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/nora/clothes_full.png"
)
image nora_clothes_half = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/nora/clothes_half.png",
    "persistent.PC98_mode == True", "images/PC98/ch/nora/clothes_half.png"
)
image nora_clothes_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/nora/clothes_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/nora/clothes_sweat.png"
)
image nora_acc_dark = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/nora/acc_dark.png",
    "persistent.PC98_mode == True", "images/PC98/ch/nora/acc_dark.png"
)
image nora_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/nora/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/nora/exp_neutral.png"
)
image nora_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/nora/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/nora/exp_smile.png"
)
image nora_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/nora/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/nora/exp_amused.png"
)
image nora_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/nora/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/nora/exp_laugh.png"
)
image nora_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/nora/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/nora/exp_surprise.png"
)
image nora_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/nora/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/nora/exp_shock.png"
)
image nora_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/nora/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/nora/exp_angry.png"
)
image nora_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/nora/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/nora/exp_frown.png"
)
image nora_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/nora/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/nora/exp_sad.png"
)
image nora_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/nora/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/nora/exp_pain.png"
)
image nora_exp_fury = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/nora/exp_fury.png",
    "persistent.PC98_mode == True", "images/PC98/ch/nora/exp_fury.png"
)
image nora_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/nora/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/nora/acc_sweat.png"
)
image nora_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/nora/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/nora/acc_blush.png"
)
image nora_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/nora/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/nora/acc_sweatdrop.png"
)
layeredimage Nora:
    group body:
        attribute base default:
            "nora_body_base"
    group clothes:
        attribute c_full default:
            "nora_clothes_full"
        attribute c_half:
            "nora_clothes_half"
        attribute c_sweat:
            "nora_clothes_sweat"
    group accessories_2:
        attribute dark:
            "nora_acc_dark"
    group accessories_3:
        attribute blush:
            "nora_acc_blush"
    group face:
        attribute neutral default:
            "nora_exp_neutral"#
        attribute amused:
            "nora_exp_amused"#
        attribute laugh:
            "nora_exp_laugh"#
        attribute smile:
            "nora_exp_smile"#
        attribute surprise:
            "nora_exp_surprise"#
        attribute shock:
            "nora_exp_shock"#
        attribute angry:
            "nora_exp_angry"#
        attribute frown:
            "nora_exp_frown"#
        attribute sad:
            "nora_exp_sad"#
        attribute pain:
            "nora_exp_pain"#
        attribute fury:
            "nora_exp_fury"#
    group accessories:
        attribute sweat:
            "nora_acc_sweat"
        attribute sweatdrop:
            "nora_acc_sweatdrop"
    at character_sprites_nora
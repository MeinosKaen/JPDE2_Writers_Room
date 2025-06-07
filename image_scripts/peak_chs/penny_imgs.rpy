image penny_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/penny/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/penny/body_base.png"
)
image penny_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/penny/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/penny/clothes_full.png"
)
image penny_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/penny/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/penny/exp_neutral.png"
)
image penny_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/penny/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/penny/exp_smile.png"
)
image penny_exp_emba = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/penny/exp_emba.png",
    "persistent.PC98_mode == True", "images/PC98/ch/penny/exp_emba.png"
)
image penny_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/penny/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/penny/exp_amused.png"
)
image penny_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/penny/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/penny/exp_laugh.png"
)
image penny_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/penny/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/penny/exp_surprise.png"
)
image penny_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/penny/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/penny/exp_shock.png"
)
image penny_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/penny/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/penny/exp_angry.png"
)
image penny_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/penny/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/penny/exp_frown.png"
)
image penny_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/penny/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/penny/exp_sad.png"
)
image penny_exp_sadder = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/penny/exp_sadder.png",
    "persistent.PC98_mode == True", "images/PC98/ch/penny/exp_sadder.png"
)
image penny_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/penny/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/penny/exp_pain.png"
)
image penny_exp_off = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/penny/exp_off.png",
    "persistent.PC98_mode == True", "images/PC98/ch/penny/exp_off.png"
)
image penny_exp_grit = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/penny/exp_grit.png",
    "persistent.PC98_mode == True", "images/PC98/ch/penny/exp_grit.png"
)
image penny_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/penny/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/penny/acc_sweat.png"
)
image penny_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/penny/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/penny/acc_blush.png"
)
image penny_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/penny/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/penny/acc_sweatdrop.png"
)
layeredimage Penny:
    group body:
        attribute base default:
            "penny_body_base"
    group clothes:
        attribute c_full default:
            "penny_clothes_full"
    group accessories_2:
        attribute blush:
            "penny_acc_blush"
    group face:
        attribute neutral default:
            "penny_exp_neutral"#
        attribute amused:
            "penny_exp_amused"#
        attribute laugh:
            "penny_exp_laugh"#
        attribute smile:
            "penny_exp_smile"#
        attribute emba:
            "penny_exp_emba"#
        attribute surprise:
            "penny_exp_surprise"#
        attribute shock:
            "penny_exp_shock"#
        attribute angry:
            "penny_exp_angry"#
        attribute frown:
            "penny_exp_frown"#
        attribute sad:
            "penny_exp_sad"#
        attribute grit:
            "penny_exp_grit"#
        attribute off:
            "penny_exp_off"#
        attribute pain:
            "penny_exp_pain"#
        attribute sadder:
            "penny_exp_sadder"#
    group accessories:
        attribute sweat:
            "penny_acc_sweat"
        attribute sweatdrop:
            "penny_acc_sweatdrop"
    at character_sprites_penny

image Penny_bub = LayeredImageProxy("Penny", Transform(crop=(50, 0, 210, 238), zoom=0.9, xpos=180, ypos=750, anchor=((0.5,0))))#LOWER LEFT
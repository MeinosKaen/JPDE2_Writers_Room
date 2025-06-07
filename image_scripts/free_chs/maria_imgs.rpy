image maria_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/maria/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/maria/body_base.png"
)
image maria_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/maria/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/maria/clothes_full.png"
)
image maria_clothes_half = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/maria/clothes_half.png",
    "persistent.PC98_mode == True", "images/PC98/ch/maria/clothes_half.png"
)
image maria_acc_mask = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/maria/acc_mask.png",
    "persistent.PC98_mode == True", "images/PC98/ch/maria/acc_mask.png"
)
image maria_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/maria/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/maria/exp_neutral.png"
)
image maria_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/maria/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/maria/exp_smile.png"
)
image maria_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/maria/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/maria/exp_amused.png"
)
image maria_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/maria/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/maria/exp_laugh.png"
)
image maria_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/maria/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/maria/exp_surprise.png"
)
image maria_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/maria/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/maria/exp_shock.png"
)
image maria_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/maria/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/maria/exp_angry.png"
)
image maria_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/maria/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/maria/exp_frown.png"
)
image maria_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/maria/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/maria/exp_sad.png"
)
image maria_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/maria/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/maria/exp_pain.png"
)
image maria_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/maria/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/maria/acc_sweat.png"
)
image maria_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/maria/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/maria/acc_sweatdrop.png"
)
layeredimage Maria:
    group body:
        attribute base default:
            "maria_body_base"
    group clothes:
        attribute c_full default:
            "maria_clothes_full"
        attribute c_half:
            "maria_clothes_half"
    group face:
        attribute neutral default:
            "maria_exp_neutral"#
        attribute amused:
            "maria_exp_amused"#
        attribute laugh:
            "maria_exp_laugh"#
        attribute smile:
            "maria_exp_smile"#
        attribute surprise:
            "maria_exp_surprise"#
        attribute shock:
            "maria_exp_shock"#
        attribute angry:
            "maria_exp_angry"#
        attribute frown:
            "maria_exp_frown"#
        attribute sad:
            "maria_exp_sad"#
        attribute pain:
            "maria_exp_pain"#
    group accessories_2:
        attribute mask:
            "maria_acc_mask"
    group accessories:
        attribute sweat:
            "maria_acc_sweat"
        attribute sweatdrop:
            "maria_acc_sweatdrop"
    at character_sprites_maria

image Maria_bub = LayeredImageProxy("Maria", Transform(crop=(90, 0, 244, 238), zoom=0.9, xpos=188, ypos=85, anchor=((0.5,0))))#BOTTOM RIGHT
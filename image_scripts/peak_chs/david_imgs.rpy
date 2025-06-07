#Character Layered Images
#Conditional David Images
image david_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/body_base.png"
)
image david_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/clothes_full.png"
)
image david_clothes_half = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/clothes_half.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/clothes_half.png"
)
image david_clothes_pants = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/clothes_pants.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/clothes_pants.png"
)
image david_clothes_jacket = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/clothes_jacket.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/clothes_jacket.png"
)
image david_acc_dark = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/acc_dark.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/acc_dark.png"
)
image david_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/exp_neutral.png"
)
image david_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/exp_smile.png"
)
image david_exp_sasmile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/exp_sasmile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/exp_sasmile.png"
)
image david_exp_susmile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/exp_susmile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/exp_susmile.png"
)
image david_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/exp_amused.png"
)
image david_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/exp_laugh.png"
)
image david_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/exp_surprise.png"
)
image david_exp_ansurprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/exp_ansurprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/exp_ansurprise.png"
)
image david_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/exp_shock.png"
)
image david_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/exp_angry.png"
)
image david_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/exp_frown.png"
)
image david_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/exp_sad.png"
)
image david_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/exp_pain.png"
)
image david_exp_fury = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/exp_fury.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/exp_fury.png"
)
image david_exp_suffer = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/exp_suffer.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/exp_suffer.png"
)
image david_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/acc_sweat.png"
)
image david_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/acc_blush.png"
)
image david_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/david/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/david/acc_sweatdrop.png"
)
layeredimage David:
    group body:
        attribute base default:
            "david_body_base"
    group clothes:
        attribute c_full default:
            "david_clothes_full"
        attribute c_half:
            "david_clothes_half"
        attribute c_pants:
            "david_clothes_pants"
        attribute jacket:
            "david_clothes_jacket"
    group accessories_2:
        attribute dark:
            "david_acc_dark"
        attribute blush:
            "david_acc_blush"
    group face:
        attribute neutral default:
            "david_exp_neutral"#
        attribute amused:
            "david_exp_amused"#
        attribute laugh:
            "david_exp_laugh"#
        attribute smile:
            "david_exp_smile"#
        attribute sasmile:
            "david_exp_sasmile"#
        attribute ansurprise:
            "david_exp_ansurprise"#
        attribute surprise:
            "david_exp_surprise"#
        attribute shock:
            "david_exp_shock"#
        attribute angry:
            "david_exp_angry"#
        attribute frown:
            "david_exp_frown"#
        attribute sad:
            "david_exp_sad"#
        attribute pain:
            "david_exp_pain"#
        attribute suffer:
            "david_exp_suffer"#
        attribute fury:
            "david_exp_fury"#
        attribute susmile:
            "david_exp_susmile"#
    group accessories:
        attribute sweat:
            "david_acc_sweat"
        attribute sweatdrop:
            "david_acc_sweatdrop"
    at character_sprites_david

image David_bub = LayeredImageProxy("David", Transform(crop=(90, 0, 244, 238), zoom=0.9, xpos=188, ypos=85, anchor=((0.5,0))))#TOP LEFT

default david_direction = "right"

image david_walking_left:
    "images/ch/david/walk/left_02.png"
    pause 0.5
    "images/ch/david/walk/left_03.png"
    pause 0.5
    "images/ch/david/walk/left_02.png"
    pause 0.5
    "images/ch/david/walk/left_01.png"
    pause 0.5
    repeat

image david_walking_right:
    "images/ch/david/walk/right_02.png"
    pause 0.5
    "images/ch/david/walk/right_03.png"
    pause 0.5
    "images/ch/david/walk/right_02.png"
    pause 0.5
    "images/ch/david/walk/right_01.png"
    pause 0.5
    repeat

image david_walking_up:
    "images/ch/david/walk/up_02.png"
    pause 0.5
    "images/ch/david/walk/up_03.png"
    pause 0.5
    "images/ch/david/walk/up_02.png"
    pause 0.5
    "images/ch/david/walk/up_01.png"
    pause 0.5
    repeat

image david_walking_down:
    "images/ch/david/walk/down_02.png"
    pause 0.5
    "images/ch/david/walk/down_03.png"
    pause 0.5
    "images/ch/david/walk/down_02.png"
    pause 0.5
    "images/ch/david/walk/down_01.png"
    pause 0.5
    repeat

image david_walking_sprite = ConditionSwitch(
    "david_direction == 'down'", "david_walking_down",
    "david_direction == 'left'", "david_walking_left",
    "david_direction == 'up'", "david_walking_up",
    "david_direction == 'right'", "david_walking_right"
)
image david_hover_sprite = ConditionSwitch(
    "david_direction == 'down'", "images/ch/david/walk/down_02.png",
    "david_direction == 'left'", "images/ch/david/walk/left_02.png",
    "david_direction == 'up'", "images/ch/david/walk/up_02.png",
    "david_direction == 'right'", "images/ch/david/walk/right_02.png",
)
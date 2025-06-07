default ruby_new_groove = False
default ruby_align = 0.5

image ruby_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/body_base.png"
)
image ruby_body_braid = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/body_braid.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/body_braid.png"
)
image ruby_body_base_calc = ConditionSwitch(
    "ruby_new_groove == False", "ruby_body_base",
    "ruby_new_groove == True", "ruby_body_braid"
)
image ruby_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/clothes_full.png"
)
image ruby_clothes_half = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/clothes_half.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/clothes_half.png"
)
image ruby_clothes_full_n = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/clothes_full_n.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/clothes_full_n.png"
)
image ruby_clothes_half_n = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/clothes_half_n.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/clothes_half_n.png"
)
image ruby_clothes_full_calc = ConditionSwitch(
    "ruby_new_groove == False", "ruby_clothes_full",
    "ruby_new_groove == True", "ruby_clothes_full_n"
)
image ruby_clothes_half_calc = ConditionSwitch(
    "ruby_new_groove == False", "ruby_clothes_half",
    "ruby_new_groove == True", "ruby_clothes_half_n"
)
image ruby_acc_goggles_up = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/acc_goggles_up.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/acc_goggles_up.png"
)
image ruby_acc_goggles_down = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/acc_goggles_down.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/acc_goggles_down.png"
)
image ruby_acc_goggles_up_n = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/acc_goggles_up_n.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/acc_goggles_up_n.png"
)
image ruby_acc_goggles_up_calc = ConditionSwitch(
    "ruby_new_groove == False", "ruby_acc_goggles_up",
    "ruby_new_groove == True", "ruby_acc_goggles_up_n"
)
image ruby_acc_goggles_down_calc = ConditionSwitch(
    "ruby_new_groove == False", "ruby_acc_goggles_down",
    "ruby_new_groove == True", "ruby_none"
)
image ruby_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/exp_neutral.png"
)
image ruby_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/exp_smile.png"
)
image ruby_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/exp_amused.png"
)
image ruby_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/exp_laugh.png"
)
image ruby_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/exp_surprise.png"
)
image ruby_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/exp_shock.png"
)
image ruby_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/exp_angry.png"
)
image ruby_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/exp_frown.png"
)
image ruby_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/exp_sad.png"
)
image ruby_exp_cry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/exp_cry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/exp_cry.png"
)
image ruby_exp_sniffles = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/exp_sniffles.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/exp_sniffles.png"
)
image ruby_exp_psniffles = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/exp_psniffles.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/exp_psniffles.png"
)
image ruby_exp_hsniffles = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/exp_hsniffles.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/exp_hsniffles.png"
)
image ruby_exp_hcry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/exp_hcry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/exp_hcry.png"
)
image ruby_exp_acry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/exp_acry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/exp_acry.png"
)
image ruby_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/exp_pain.png"
)
image ruby_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/acc_sweat.png"
)
image ruby_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/acc_blush.png"
)
image ruby_acc_blush_2 = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/acc_blush_2.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/acc_blush_2.png"
)
image ruby_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/acc_sweatdrop.png"
)
image ruby_acc_b_cloak = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ruby/acc_b_cloak.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ruby/acc_b_cloak.png"
)
image ruby_none = "images/ch/none.png"
image ruby_acc_b_cloak_calc = ConditionSwitch(
    "ruby_new_groove == True", "ruby_acc_b_cloak",
    "ruby_new_groove == False", "ruby_none"
)
layeredimage Ruby:
    attribute b_cloak default if_all "c_full":
        "ruby_acc_b_cloak_calc"
    group body:
        attribute base default:
            "ruby_body_base_calc"
    group clothes:
        attribute c_full default:
            "ruby_clothes_full_calc"
        attribute c_half:
            "ruby_clothes_half_calc"
    group accessories_2:
        attribute blush:
            "ruby_acc_blush"
        attribute blush_2:
            "ruby_acc_blush_2"
    group face:
        attribute neutral default:
            "ruby_exp_neutral"#
        attribute amused:
            "ruby_exp_amused"#
        attribute laugh:
            "ruby_exp_laugh"#
        attribute smile:
            "ruby_exp_smile"#
        attribute surprise:
            "ruby_exp_surprise"#
        attribute shock:
            "ruby_exp_shock"#
        attribute angry:
            "ruby_exp_angry"#
        attribute frown:
            "ruby_exp_frown"#
        attribute sad:
            "ruby_exp_sad"#
        attribute cry:
            "ruby_exp_cry"#
        attribute sniffles:
            "ruby_exp_sniffles"#
        attribute hsniffles:
            "ruby_exp_hsniffles"#
        attribute psniffles:
            "ruby_exp_psniffles"#
        attribute hcry:
            "ruby_exp_hcry"#
        attribute acry:
            "ruby_exp_acry"#
        attribute pain:
            "ruby_exp_pain"#
    group accessories:
        attribute sweat:
            "ruby_acc_sweat"
        attribute sweatdrop:
            "ruby_acc_sweatdrop"
    group accessories_3:
        attribute g_up:
            "ruby_acc_goggles_up_calc"
        attribute g_down:
            "ruby_acc_goggles_down_calc"
    at character_sprites_ruby

image Ruby_bub = LayeredImageProxy("Ruby", Transform(crop=(90, 0, 244, 238), zoom=0.9, xpos=1748, ypos=85, anchor=((0.5,0))))#TOP RIGHT
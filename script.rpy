image main_menu_bg = "gui/screen_backgrounds/main_menu.png"

image ctc:
    subpixel True
    "gui/ctc.png"
    xalign 0.5 ypos 975
    linear 0.8 yoffset 10
    linear 0.8 yoffset 0
    repeat

#Character Definitions
define na = Character(_("Narrator"), voice_tag="narrator", who_color="#9F65E7", what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", what_text_align=0.5, what_xalign=0.5, callback=male_beep)
define vopa = Character(_("Voice from the Past"), voice_tag="vopa", who_color="#e6b65e", what_color="#e6b65e", what_prefix='{i}\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", what_text_align=0.5, what_xalign=0.5)

define all_else = Character(_("Everyone Else"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed")

define d = Character(_("[p_n] di Kabegis"), what_prefix='\"', what_suffix='\"', image="david", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define bub_d = Character(None, image="David_bub", kind=bubble, callback=male_beep)
define d_i = Character(_("[p_n] di Kabegis"), what_prefix='{i}', image="david", ctc="ctc" , ctc_position="fixed")
define d_st = Character(_("[p_n] di Kabegis"), what_prefix='{u}\"', what_suffix='\"', image="david", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define d_x = Character(_("?????"), what_prefix='{u}\"', what_suffix='\"', image="david", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define d_n = Character(_("[p_n] di Kabegis"), what_suffix='\"', image="david", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define dntip = Character(_("[p_n]&Tip"), what_prefix='\"', what_suffix='\"', image="david", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define dnp = Character(_("[p_n]&Penny"), what_prefix='\"', what_suffix='\"', image="david", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define jpde = Character(_("Team JPDE"), what_prefix='\"', what_suffix='\"', image="david", ctc="ctc" , ctc_position="fixed", callback=male_beep)
image side david = LayeredImageProxy("David", Transform(crop=(15, 0, 385, 440), zoom=0.8))
image side david nulla = Null()
image side david darko = LayeredImageProxy("David", Transform(crop=(15, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side david sera = LayeredImageProxy("David", Transform(crop=(15, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))
image side david sneak = LayeredImageProxy("David", Transform(crop=(15, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.33))))
image side david sun = LayeredImageProxy("David", Transform(crop=(35, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#ffa652", alpha=0.33))))
image side david torch = LayeredImageProxy("David", Transform(crop=(35, 0, 385, 440), zoom=0.8, matrixcolor=(TintMatrix(Color("#e3563d", alpha=0.33))*BrightnessMatrix(-0.05))))

define p = Character(_("Penny Polendina"), what_prefix='\"', what_suffix='\"', image="penny", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define bub_p = Character(None, image="Penny_bub", kind=bubble, callback=female_beep)
define p_i = Character(_("Penny Polendina"), what_prefix='{i}', image="penny", ctc="ctc" , ctc_position="fixed")
define p_st = Character(_("Penny Polendina"), what_prefix='{u}\"', what_suffix='\"', image="penny", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define p_no = Character(_("Penny Polendina"), what_suffix='\"', image="penny", ctc="ctc" , ctc_position="fixed", callback=female_beep)

define j = Character(_("Jack B. Ivory"), what_prefix='\"', what_suffix='\"', image="jack", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define bub_j = Character(None, image="Jack_bub", kind=bubble, callback=female_beep)
define j_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="jack", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define j_i = Character(_("Jack B. Ivory"), what_prefix='{i}', image="jack", ctc="ctc" , ctc_position="fixed")
define j_st = Character(_("Jack B. Ivory"), what_prefix='{u}\"', what_suffix='\"', image="jack", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define j_n = Character(_("Jack B. Ivory"), what_suffix='\"', image="jack", ctc="ctc" , ctc_position="fixed", callback=female_beep)
image side jack = LayeredImageProxy("Jack", Transform(crop=(75, 0, 445, 440), zoom=0.8))
image side jack nulla = Null()
image side jack darko = LayeredImageProxy("Jack", Transform(crop=(75, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side jack sera = LayeredImageProxy("Jack", Transform(crop=(75, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))

define ge_st = Character(_("Gerda Ivory"), what_prefix='{u}\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=female_beep)

define e = Character(_("Evelyn Damerot"), what_prefix='\"', what_suffix='\"', image="evelyn", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define bub_e = Character(None, image="Evelyn_bub", kind=bubble, callback=female_beep)
define e_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="evelyn", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define e_i = Character(_("Evelyn Damerot"), what_prefix='{i}', image="evelyn", ctc="ctc" , ctc_position="fixed")
define e_st = Character(_("Evelyn Damerot"), what_prefix='{u}\"', what_suffix='\"', image="evelyn", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define e_n = Character(_("Evelyn Damerot"), what_suffix='\"', image="evelyn", ctc="ctc" , ctc_position="fixed", callback=female_beep)

define g_x = Character(_("?????"), what_prefix='{u}\"', what_suffix='\"', image="gemma", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define g_xx = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="gemma", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define g = Character(_("Gemma Polendina"), what_prefix='\"', what_suffix='\"', image="gemma", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define g_i = Character(_("Gemma Polendina"), what_prefix='{i}', image="gemma", ctc="ctc" , ctc_position="fixed")
define g_st = Character(_("Gemma Polendina"), what_prefix='{u}\"', what_suffix='\"', image="gemma", ctc="ctc" , ctc_position="fixed", callback=female_beep)

define sk = Character(_("Sienna Khan"), what_prefix='\"', what_suffix='\"', image="sienna", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define bub_sk = Character(None, image="Sienna_bub", kind=bubble, callback=female_beep)
define sk_i = Character(_("Sienna Khan"), what_prefix='{i}', image="sienna", ctc="ctc" , ctc_position="fixed")
define sk_st = Character(_("Sienna Khan"), what_prefix='{u}\"', what_suffix='\"', image="sienna", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define sk_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="sienna", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define sk_xc = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="sienna", ctc="ctc" , ctc_position="fixed", callback=female_beep)
image side sienna = LayeredImageProxy("Sienna", Transform(crop=(25, 0, 385, 440), zoom=0.8))
image side sienna nulla = Null()
image side sienna darko = LayeredImageProxy("Sienna", Transform(crop=(25, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side sienna sera = LayeredImageProxy("Sienna", Transform(crop=(25, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))
image side sienna sun = LayeredImageProxy("Sienna", Transform(crop=(25, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#ffa652", alpha=0.33))))
image side sienna torch = LayeredImageProxy("Sienna", Transform(crop=(25, 0, 385, 440), zoom=0.8, matrixcolor=(TintMatrix(Color("#e3563d", alpha=0.33))*BrightnessMatrix(-0.05))))

define n = Character(_("Neopolitan Torchwick"), what_prefix='\"', what_suffix='\"', image="neopolitan", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define n_i = Character(_("Neopolitan Torchwick"), what_prefix='{i}', image="neopolitan", ctc="ctc" , ctc_position="fixed")
define n_st = Character(_("Neopolitan Torchwick"), what_prefix='{u}\"', what_suffix='\"', image="neopolitan", ctc="ctc" , ctc_position="fixed", callback=female_beep)

define tc = Character(_("Commander Torchwick"), what_prefix='\"', what_suffix='\"', image="torchwick", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define tc_x = Character(_("The Commander"), what_prefix='\"', what_suffix='\"', image="torchwick", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define tc_i = Character(_("Commander Torchwick"), what_prefix='{i}', image="torchwick", ctc="ctc" , ctc_position="fixed")

define gl_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="glynda", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define gl = Character(_("Glynda Goodwitch I"), what_prefix='\"', what_suffix='\"', image="glynda", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define gl_i = Character(_("Glynda Goodwitch I"), what_prefix='{i}', image="glynda", ctc="ctc" , ctc_position="fixed")
define gl_st = Character(_("Glynda Goodwitch I"), what_prefix='{u}\"', what_suffix='\"', image="glynda", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define gl_n = Character(_("Glynda Goodwitch I"), what_suffix='\"', image="glynda", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define v_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="violet", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define v = Character(_("Violet Peach"), what_prefix='\"', what_suffix='\"', image="violet", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define v_i = Character(_("Violet Peach"), what_prefix='{i}', image="violet", ctc="ctc" , ctc_position="fixed")
define v_st = Character(_("Violet Peach"), what_prefix='{u}\"', what_suffix='\"', image="violet", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define v_n = Character(_("Violet Peach"), what_suffix='\"', image="violet", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define en_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="enrico", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define en = Character(_("Enrico Polendina"), what_prefix='\"', what_suffix='\"', image="enrico", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define en_i = Character(_("Enrico Polendina"), what_prefix='{i}', image="enrico", ctc="ctc" , ctc_position="fixed")
define en_st = Character(_("Enrico Polendina"), what_prefix='{u}\"', what_suffix='\"', image="enrico", ctc="ctc" , ctc_position="fixed", callback=male_beep)

define aq_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="aqua", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define aq_xn = Character(_("?????"), what_suffix='\"', image="aqua", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define aq = Character(_("Aqua Skyver"), what_prefix='\"', what_suffix='\"', image="aqua", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define aq_n = Character(_("Aqua Skyver"), what_suffix='\"', image="aqua", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define aq_i = Character(_("Aqua Skyver"), what_prefix='{i}', image="aqua", ctc="ctc" , ctc_position="fixed")
define aq_st = Character(_("Aqua Skyver"), what_prefix='{u}\"', what_suffix='\"', image="aqua", ctc="ctc" , ctc_position="fixed", callback=female_beep)

define py_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="pyrrha", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define py = Character(_("Pyrrha Nikos"), what_prefix='\"', what_suffix='\"', image="pyrrha", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define py_i = Character(_("Pyrrha Nikos"), what_prefix='{i}', image="pyrrha", ctc="ctc" , ctc_position="fixed")
define pyt_i = Character(_("Pythia Nikos"), what_prefix='{i}', image="pythia", ctc="ctc" , ctc_position="fixed")
define py_st = Character(_("Pyrrha Nikos"), what_prefix='{u}\"', what_suffix='\"', image="pyrrha", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define py_no = Character(_("Pyrrha Nikos"), what_suffix='\"', image="pyrrha", ctc="ctc" , ctc_position="fixed", callback=female_beep)
image side pyrrha = LayeredImageProxy("Pyrrha", Transform(crop=(108, 0, 385, 440), zoom=0.8))
image side pyrrha nulla = Null()
image side pyrrha darko = LayeredImageProxy("Pyrrha", Transform(crop=(108, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side pyrrha sera = LayeredImageProxy("Pyrrha", Transform(crop=(108, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))
image side pythia = LayeredImageProxy("Pyrrha", Transform(crop=(108, 0, 385, 440), zoom=0.8, shader="MakeVisualNovels.VHS", u_color=(1.0, 1.0, 1.0, 1.0)))

define m = Character(_("Maria Calavera"), what_prefix='\"', what_suffix='\"', image="maria", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define bub_m = Character(None, image="Maria_bub", kind=bubble, callback=female_beep)
define m_n = Character(_("Maria Calavera"), what_suffix='\"', image="maria", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define m_i = Character(_("Maria Calavera"), what_prefix='{i}', image="maria", ctc="ctc" , ctc_position="fixed")
define m_st = Character(_("Maria Calavera"), what_prefix='{u}\"', what_suffix='\"', image="maria", ctc="ctc" , ctc_position="fixed", callback=female_beep)

define ru = Character(_("Ruby Rose"), what_prefix='\"', what_suffix='\"', image="ruby", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define bub_ru = Character(None, image="Ruby_bub", kind=bubble, callback=female_beep)
define ru_n = Character(_("Ruby Rose"), what_suffix='\"', image="ruby", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define ru_i = Character(_("Ruby Rose"), what_prefix='{i}', image="ruby", ctc="ctc" , ctc_position="fixed")
define ru_st = Character(_("Ruby Rose"), what_prefix='{u}\"', what_suffix='\"', image="ruby", ctc="ctc" , ctc_position="fixed", callback=female_beep)

#TEAM ARSN
define jn = Character(_("Jaune Arc"), what_prefix='\"', what_suffix='\"', image="jaune", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define jn_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="jaune", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define jn_n = Character(_("Jaune Arc"), what_suffix='\"', image="jaune", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define jn_i = Character(_("Jaune Arc"), what_prefix='{i}', image="jaune", ctc="ctc" , ctc_position="fixed")
define jn_st = Character(_("Jaune Arc"), what_prefix='{u}\"', what_suffix='\"', image="jaune", ctc="ctc" , ctc_position="fixed", callback=male_beep)
image side jaune = LayeredImageProxy("Jaune", Transform(crop=(125, 0, 385, 440), zoom=0.8))
image side jaune nulla = Null()
image side jaune darko = LayeredImageProxy("Jaune", Transform(crop=(125, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side jaune sera = LayeredImageProxy("Jaune", Transform(crop=(125, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))
image side jaune sun = LayeredImageProxy("Jaune", Transform(crop=(125, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#ffa652", alpha=0.33))))

define si = Character(_("Sierra Taipan"), what_prefix='\"', what_suffix='\"', image="sierra", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define si_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="sierra", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define si_n = Character(_("Sierra Taipan"), what_suffix='\"', image="sierra", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define si_i = Character(_("Sierra Taipan"), what_prefix='{i}', image="sierra", ctc="ctc" , ctc_position="fixed")
define si_st = Character(_("Sierra Taipan"), what_prefix='{u}\"', what_suffix='\"', image="sierra", ctc="ctc" , ctc_position="fixed", callback=female_beep)
image side sierra = LayeredImageProxy("Sierra", Transform(crop=(-5, 0, 385, 440), zoom=0.8))
image side sierra nulla = Null()
image side sierra darko = LayeredImageProxy("Sierra", Transform(crop=(-5, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side sierra sera = LayeredImageProxy("Sierra", Transform(crop=(-5, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))
image side sierra sun = LayeredImageProxy("Sierra", Transform(crop=(-5, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#ffa652", alpha=0.33))))

define no = Character(_("Nora Valkyrie"), what_prefix='\"', what_suffix='\"', image="nora", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define no_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="nora", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define no_n = Character(_("Nora Valkyrie"), what_suffix='\"', image="nora", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define no_i = Character(_("Nora Valkyrie"), what_prefix='{i}', image="nora", ctc="ctc" , ctc_position="fixed")
define no_st = Character(_("Nora Valkyrie"), what_prefix='{u}\"', what_suffix='\"', image="nora", ctc="ctc" , ctc_position="fixed", callback=female_beep)
image side nora = LayeredImageProxy("Nora", Transform(crop=(55, 0, 385, 440), zoom=0.8))
image side nora nulla = Null()
image side nora darko = LayeredImageProxy("Nora", Transform(crop=(55, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side nora sera = LayeredImageProxy("Nora", Transform(crop=(55, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))
image side nora sun = LayeredImageProxy("Nora", Transform(crop=(55, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#ffa652", alpha=0.33))))

define re = Character(_("Lie Ren"), what_prefix='\"', what_suffix='\"', image="ren", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define re_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="ren", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define re_n = Character(_("Lie Ren"), what_suffix='\"', image="ren", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define re_i = Character(_("Lie Ren"), what_prefix='{i}', image="ren", ctc="ctc" , ctc_position="fixed")
define re_st = Character(_("Lie Ren"), what_prefix='{u}\"', what_suffix='\"', image="ren", ctc="ctc" , ctc_position="fixed", callback=male_beep)
image side ren = LayeredImageProxy("Ren", Transform(crop=(125, 0, 385, 440), zoom=0.8))
image side ren nulla = Null()
image side ren darko = LayeredImageProxy("Ren", Transform(crop=(125, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side ren sera = LayeredImageProxy("Ren", Transform(crop=(125, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))
image side ren sun = LayeredImageProxy("Ren", Transform(crop=(125, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#ffa652", alpha=0.33))))

#Allies

define ja_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="janara", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define ja = Character(_("Janara Peach"), what_prefix='\"', what_suffix='\"', image="janara", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define ja_n = Character(_("Janara Peach"), what_suffix='\"', image="janara", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define ja_i = Character(_("Janara Peach"), what_prefix='{i}', image="janara", ctc="ctc" , ctc_position="fixed")
define ja_st = Character(_("Janara Peach"), what_prefix='{u}\"', what_suffix='\"', image="janara", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define ja_w = Character(_("Janara Peach"), what_prefix='\"', what_suffix='\"', image="janara", ctc="ctc" , ctc_position="fixed", what_font="fonts/HauntAOE.ttf", what_size=37, what_line_spacing=5, what_kerning=3)
define ja_w_n = Character(_("Janara Peach"), what_suffix='\"', image="janara", ctc="ctc" , ctc_position="fixed", what_font="fonts/HauntAOE.ttf", what_size=37, what_line_spacing=5, what_kerning=3)
define ja_w_i = Character(_("Janara Peach"), what_prefix='{i}', image="janara", ctc="ctc" , ctc_position="fixed", what_font="fonts/HauntAOE.ttf", what_size=37, what_line_spacing=5, what_kerning=3)
define ja_w_st = Character(_("Janara Peach"), what_prefix='{u}\"', what_suffix='\"', image="janara", ctc="ctc", ctc_position="fixed", what_font="fonts/HauntAOE.ttf", what_size=37, what_line_spacing=5, what_kerning=3)
image side janara = LayeredImageProxy("Janara", Transform(crop=(80, -50, 385, 440), zoom=0.9))
image side janara nulla = Null()
image side janara darko = LayeredImageProxy("Janara", Transform(crop=(80, -50, 385, 440), zoom=0.9, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side janara sun = LayeredImageProxy("Janara", Transform(crop=(80, -50, 385, 440), zoom=0.9, matrixcolor=TintMatrix(Color("#ffa652", alpha=0.33))))
image side janara sera = LayeredImageProxy("Janara", Transform(crop=(80, -50, 385, 440), zoom=0.9, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))

define am_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="amber", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define am = Character(_("Amber Talia Valesianis"), what_prefix='\"', what_suffix='\"', image="amber", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define am_n = Character(_("Amber Talia Valesianis"), what_suffix='\"', image="amber", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define am_i = Character(_("Amber Talia Valesianis"), what_prefix='{i}', image="amber", ctc="ctc" , ctc_position="fixed")

define tip_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="tip", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define tip = Character(_("Tip Pines"), what_prefix='\"', what_suffix='\"', image="tip", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define tip_n = Character(_("Tip Pines"), what_suffix='\"', image="tip", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define tip_i = Character(_("Tip Pines"), what_prefix='{i}', image="tip", ctc="ctc" , ctc_position="fixed")
define tip_st = Character(_("Tip Pines"), what_prefix='{u}\"', what_suffix='\"', image="tip", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define tip_w = Character(_("Tip Pines"), what_prefix='\"', what_suffix='\"', image="janara", ctc="ctc" , ctc_position="fixed", what_font="fonts/HauntAOE.ttf", what_size=37, what_line_spacing=5, what_kerning=3, callback=male_beep)
define tip_w_n = Character(_("Tip Pines"), what_suffix='\"', image="janara", ctc="ctc" , ctc_position="fixed", what_font="fonts/HauntAOE.ttf", what_size=37, what_line_spacing=5, what_kerning=3, callback=male_beep)
define tip_w_i = Character(_("Tip Pines"), what_prefix='{i}', image="janara", ctc="ctc" , ctc_position="fixed", what_font="fonts/HauntAOE.ttf", what_size=37, what_line_spacing=5, what_kerning=3, callback=male_beep)
define tip_w_st = Character(_("Tip Pines"), what_prefix='{u}\"', what_suffix='\"', image="janara", ctc="ctc", ctc_position="fixed", what_font="fonts/HauntAOE.ttf", what_size=37, what_line_spacing=5, what_kerning=3, callback=male_beep)
image side tip = LayeredImageProxy("Tip", Transform(crop=(10, -70, 385, 440), zoom=0.9))
image side tip nulla = Null()
image side tip darko = LayeredImageProxy("Tip", Transform(crop=(10, -70, 385, 440), zoom=0.9, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side tip sun = LayeredImageProxy("Tip", Transform(crop=(10, -70, 385, 440), zoom=0.9, matrixcolor=TintMatrix(Color("#ffa652", alpha=0.33))))
image side tip sera = LayeredImageProxy("Tip", Transform(crop=(10, -70, 385, 440), zoom=0.9, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))

define ml = Character(_("Melanie Malachite"), what_prefix='\"', what_suffix='\"', image="melanie", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define ml_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="melanie", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define ml_n = Character(_("Melanie Malachite"), what_suffix='\"', image="melanie", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define ml_i = Character(_("Melanie Malachite"), what_prefix='{i}', image="melanie", ctc="ctc" , ctc_position="fixed")
define ml_st = Character(_("Melanie Malachite"), what_prefix='{u}\"', what_suffix='\"', image="melanie", ctc="ctc" , ctc_position="fixed", callback=female_beep)
image side melanie = LayeredImageProxy("Melanie", Transform(crop=(15, 0, 385, 440), zoom=0.8))
image side melanie nulla = Null()
image side melanie darko = LayeredImageProxy("Melanie", Transform(crop=(15, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side melanie sera = LayeredImageProxy("Melanie", Transform(crop=(15, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))
image side melanie sun = LayeredImageProxy("Melanie", Transform(crop=(15, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#ffa652", alpha=0.33))))

define mi = Character(_("Miltia Malachite"), what_prefix='\"', what_suffix='\"', image="miltia", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define mi_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="miltia", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define mi_n = Character(_("Miltia Malachite"), what_suffix='\"', image="miltia", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define mi_i = Character(_("Miltia Malachite"), what_prefix='{i}', image="miltia", ctc="ctc" , ctc_position="fixed")
define mi_st = Character(_("Miltia Malachite"), what_prefix='{u}\"', what_suffix='\"', image="miltia", ctc="ctc" , ctc_position="fixed", callback=female_beep)
image side miltia = LayeredImageProxy("Miltia", Transform(crop=(15, 0, 385, 440), zoom=0.8))
image side miltia nulla = Null()
image side miltia darko = LayeredImageProxy("Miltia", Transform(crop=(15, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side miltia sera = LayeredImageProxy("Miltia", Transform(crop=(15, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))
image side miltia sun = LayeredImageProxy("Miltia", Transform(crop=(15, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#ffa652", alpha=0.33))))

define ti_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="titania", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define ti = Character(_("Titania Peach"), what_prefix='\"', what_suffix='\"', image="titania", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define ti_i = Character(_("Titania Peach"), what_prefix='{i}', image="titania", ctc="ctc" , ctc_position="fixed")
define ti_st = Character(_("Titania Peach"), what_prefix='{u}\"', what_suffix='\"', image="titania", ctc="ctc" , ctc_position="fixed", callback=female_beep)

define ph_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="philo", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define ph = Character(_("Philo Tiogonia"), what_prefix='\"', what_suffix='\"', image="philo", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define ph_i = Character(_("Philo Tiogonia"), what_prefix='{i}', image="philo", ctc="ctc" , ctc_position="fixed")
define ph_n = Character(_("Philo Tiogonia"), image="philo", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define ph_st = Character(_("Philo Tiogonia"), what_prefix='{u}\"', what_suffix='\"', image="philo", ctc="ctc" , ctc_position="fixed", callback=female_beep)

define z_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="ziyan", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define z = Character(_("Zi-Yan Chan"), what_prefix='\"', what_suffix='\"', image="ziyan", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define z_i = Character(_("Zi-Yan Chan"), what_prefix='{i}', image="ziyan", ctc="ctc" , ctc_position="fixed")
define z_st = Character(_("Zi-Yan Chan"), what_prefix='{u}\"', what_suffix='\"', image="ziyan", ctc="ctc" , ctc_position="fixed", callback=female_beep)

define ma_ma = Character(_("Royal Marine - Magenta"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)
define ma_mi = Character(_("Royal Marine - Mint"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=female_beep)
define ma_1 = Character(_("Royal Marine - A"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=female_beep)
define ma_2 = Character(_("Royal Marine - B"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)
define ma_3 = Character(_("Royal Marine - C"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)
define ma_st = Character(_("Royal Marine"), what_prefix='\"{u}', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=female_beep)
define cus = Character(_("Royal Customs Officer"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=female_beep)
define stu_f = Character(_("Female Student"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=female_beep)
define stu_m = Character(_("Male Student"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)
define stu_f_i = Character(_("Female Student"), what_prefix='{i}', ctc="ctc" , ctc_position="fixed", callback=female_beep)
define stu_m_i = Character(_("Male Student"), what_prefix='{i}', ctc="ctc" , ctc_position="fixed", callback=female_beep)

define ntc = Character(_("Intercom"), what_prefix='{u}\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=female_beep)

define dr_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=female_beep)
define dr_m = Character(_("Doctor Momo"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)
define tae = Character(_("Madame Tae"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=female_beep)
define group = Character(_("Group"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=female_beep)
define pro = Character(_("Promoter"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=female_beep)
define dj = Character(_("Disk Jockey"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)


##Fang and Menagerie Characters
define adt = Character(_("Adam Taurus"), what_prefix='\"', what_suffix='\"', image="adam", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define adt_i = Character(_("Adam Taurus"), what_prefix='{i}', image="adam", ctc="ctc" , ctc_position="fixed")
define adt_st = Character(_("Adam Taurus"), what_prefix='{u}\"', what_suffix='\"', image="adam", ctc="ctc" , ctc_position="fixed", callback=male_beep)
image side adam = LayeredImageProxy("Adam", Transform(crop=(45, 0, 360, 440), zoom=0.8))
image side adam nulla = Null()
image side adam nito = LayeredImageProxy("Adam", Transform(crop=(45, 0, 360, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000D56", alpha=0.45))))
image side adam sun = LayeredImageProxy("Adam", Transform(crop=(45, 0, 360, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#ffa652", alpha=0.33))))

define tm = Character(_("Tamamo Kyuso"), what_prefix='\"', what_suffix='\"', image="tamamo", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define tm_x = Character(_("????"), what_prefix='\"', what_suffix='\"', image="tamamo", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define tm_i = Character(_("Tamamo Kyuso"), what_prefix='{i}', image="tamamo", ctc="ctc" , ctc_position="fixed")
define tm_st = Character(_("Tamamo Kyuso"), what_prefix='{u}\"', what_suffix='\"', image="tamamo", ctc="ctc" , ctc_position="fixed", callback=female_beep)
image side tamamo = LayeredImageProxy("Tamamo", Transform(crop=(45, 0, 365, 440), zoom=0.8))
image side tamamo nulla = Null()
image side tamamo darko = LayeredImageProxy("Tamamo", Transform(crop=(45, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side tamamo nito = LayeredImageProxy("Tamamo", Transform(crop=(45, 0, 365, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000D56", alpha=0.45))))
image side tamamo sun = LayeredImageProxy("Tamamo", Transform(crop=(45, 0, 365, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#ffa652", alpha=0.33))))

define sco = Character(_("Lieutenant Scourge"), what_prefix='\"', what_suffix='\"', image="scourge", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define sco_x = Character(_("????"), what_prefix='\"', what_suffix='\"', image="scourge", ctc="ctc" , ctc_position="fixed", callback=male_beep)

define rf_1 = Character(_("Fang"), what_prefix='\"', what_suffix='\"', image="wf_blade", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define rf_2 = Character(_("Fang"), what_prefix='\"', what_suffix='\"', image="wf_gun", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define rf_3 = Character(_("Fang"), what_prefix='\"', what_suffix='\"', image="wf_blade", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define rf_4 = Character(_("Fang"), what_prefix='\"', what_suffix='\"', image="wf_gun", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define rf_4_i = Character(_("Fang"), what_prefix='{i}', image="wf_gun", ctc="ctc" , ctc_position="fixed", callback=male_beep)

define ka_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="kali", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define ka = Character(_("Kali Belladonna"), what_prefix='\"', what_suffix='\"', image="kali", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define ka_i = Character(_("Kali Belladonna"), what_prefix='{i}', image="kali", ctc="ctc" , ctc_position="fixed")
define ka_st = Character(_("Kali Belladonna"), what_prefix='{u}\"', what_suffix='\"', image="kali", ctc="ctc" , ctc_position="fixed", callback=female_beep)
image side kali = LayeredImageProxy("Kali", Transform(crop=(0, 0, 445, 440), zoom=0.8))
image side kali nulla = Null()
image side kali darko = LayeredImageProxy("Kali", Transform(crop=(0, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side kali sera = LayeredImageProxy("Kali", Transform(crop=(0, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))
image side kali sneak = LayeredImageProxy("Kali", Transform(crop=(0, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.33))))

define gh_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="ghira", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define gh = Character(_("Ghira Belladonna"), what_prefix='\"', what_suffix='\"', image="ghira", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define gh_i = Character(_("Ghira Belladonna"), what_prefix='{i}', image="ghira", ctc="ctc" , ctc_position="fixed")
define gh_st = Character(_("Ghira Belladonna"), what_prefix='{u}\"', what_suffix='\"', image="ghira", ctc="ctc" , ctc_position="fixed", callback=male_beep)

define me_aide = Character(_("Menagerian Aide"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)
define me_sta = Character(_("Menagerian Stall Cook"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=female_beep)
define me_bla = Character(_("Menagerian Blacksmith"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)
define me_dus = Character(_("Menagerian Dustmonger"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=female_beep)
define me_dri = Character(_("Menagerian Driver"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)

##Vale Characters
define sai_c = Character(_("Captain"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)
define sai_e = Character(_("Chief Engineer"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)
define sai_n = Character(_("Navigator"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)

##Atlas Characters
define jm_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="james", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define jm = Character(_("James Ironwood"), what_prefix='\"', what_suffix='\"', image="james", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define jm_i = Character(_("James Ironwood"), what_prefix='{i}', image="james", ctc="ctc" , ctc_position="fixed")
define jm_st = Character(_("James Ironwood"), what_prefix='{u}\"', what_suffix='\"', image="james", ctc="ctc" , ctc_position="fixed", callback=male_beep)
image side james = LayeredImageProxy("James", Transform(crop=(15, 0, 445, 440), zoom=0.8))
image side james nulla = Null()
image side james darko = LayeredImageProxy("James", Transform(crop=(15, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side james sera = LayeredImageProxy("James", Transform(crop=(15, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))

define bu_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="bunny", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define bu = Character(_("Bunny Soleil"), what_prefix='\"', what_suffix='\"', image="bunny", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define bu_i = Character(_("Bunny Soleil"), what_prefix='{i}', image="bunny", ctc="ctc" , ctc_position="fixed")
define bu_st = Character(_("Bunny Soleil"), what_prefix='{u}\"', what_suffix='\"', image="bunny", ctc="ctc" , ctc_position="fixed", callback=female_beep)
image side bunny = LayeredImageProxy("Bunny", Transform(crop=(15, 0, 445, 440), zoom=0.85))
image side bunny nulla = Null()
image side bunny darko = LayeredImageProxy("Bunny", Transform(crop=(15, 0, 445, 440), zoom=0.85, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side bunny sera = LayeredImageProxy("Bunny", Transform(crop=(15, 0, 445, 440), zoom=0.85, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))

define at_of = Character(_("Security Officer"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)
define in_of = Character(_("Intelligence Officer"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=female_beep)

##Vacuo Characters
define isi_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="isis", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define isi = Character(_("Isis Ozma"), what_prefix='\"', what_suffix='\"', image="isis", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define isi_i = Character(_("Isis Ozma"), what_prefix='{i}', image="isis", ctc="ctc" , ctc_position="fixed")
define isi_st = Character(_("Isis Ozma"), what_prefix='{u}\"', what_suffix='\"', image="isis", ctc="ctc" , ctc_position="fixed", callback=female_beep)
image side isis = LayeredImageProxy("Isis", Transform(crop=(75, 0, 375, 440), zoom=0.8))
image side isis nulla = Null()
image side isis darko = LayeredImageProxy("Isis", Transform(crop=(75, 0, 375, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side isis sera = LayeredImageProxy("Isis", Transform(crop=(75, 0, 375, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))

define may_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="may", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define may = Character(_("May Zedong"), what_prefix='\"', what_suffix='\"', image="may", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define may_i = Character(_("May Zedong"), what_prefix='{i}', image="may", ctc="ctc" , ctc_position="fixed")
define may_st = Character(_("May Zedong"), what_prefix='{u}\"', what_suffix='\"', image="may", ctc="ctc" , ctc_position="fixed", callback=female_beep)
image side may = LayeredImageProxy("May", Transform(crop=(25, 0, 445, 440), zoom=0.8))
image side may nulla = Null()
image side may darko = LayeredImageProxy("May", Transform(crop=(25, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side may sera = LayeredImageProxy("May", Transform(crop=(25, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))

define gw_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="gwen", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define gw = Character(_("Gwen Darcy"), what_prefix='\"', what_suffix='\"', image="gwen", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define gw_i = Character(_("Gwen Darcy"), what_prefix='{i}', image="gwen", ctc="ctc" , ctc_position="fixed")
define gw_st = Character(_("Gwen Darcy"), what_prefix='{u}\"', what_suffix='\"', image="gwen", ctc="ctc" , ctc_position="fixed", callback=female_beep)
image side gwen = LayeredImageProxy("Gwen", Transform(crop=(50, 0, 445, 440), zoom=0.8))
image side gwen nulla = Null()
image side gwen darko = LayeredImageProxy("Gwen", Transform(crop=(50, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side gwen sera = LayeredImageProxy("Gwen", Transform(crop=(50, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))

define serv = Character(_("Server"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)
define vaide = Character(_("Federal Aide"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=female_beep)
define vaide_i = Character(_("Federal Aide"), what_prefix='{i}', ctc="ctc" , ctc_position="fixed")

define f_found = Character(_("Female Foundation Worker"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=female_beep)
define m_found = Character(_("Male Foundation Worker"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_posiion="fixed", callback=male_beep)

##Agni Side Characters
define ho_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="howard", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define ho = Character(_("Howard Tarangi"), what_prefix='\"', what_suffix='\"', image="howard", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define ho_i = Character(_("Howard Tarangi"), what_prefix='{i}', image="howard", ctc="ctc" , ctc_position="fixed")
define ho_st = Character(_("Howard Tarangi"), what_prefix='{u}\"', what_suffix='\"', image="howard", ctc="ctc" , ctc_position="fixed", callback=male_beep)
image side howard = LayeredImageProxy("Howard", Transform(crop=(15, 0, 445, 440), zoom=0.8))
image side howard nulla = Null()
image side howard darko = LayeredImageProxy("Howard", Transform(crop=(15, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side howard sera = LayeredImageProxy("Howard", Transform(crop=(15, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))

define an_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="andrea", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define an = Character(_("Andrea Damerot"), what_prefix='\"', what_suffix='\"', image="andrea", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define an_n = Character(_("Andrea Damerot"), what_suffix='\"', image="andrea", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define an_i = Character(_("Andrea Damerot"), what_prefix='{i}', image="andrea", ctc="ctc" , ctc_position="fixed")
define an_st = Character(_("Andrea Damerot"), what_prefix='{u}\"', what_suffix='\"', image="andrea", ctc="ctc" , ctc_position="fixed", callback=male_beep)
image side andrea = LayeredImageProxy("Andrea", Transform(crop=(15, 0, 445, 440), zoom=0.8))
image side andrea nulla = Null()
image side andrea darko = LayeredImageProxy("Andrea", Transform(crop=(15, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side andrea sepia = LayeredImageProxy("Andrea", Transform(crop=(15, 0, 445, 440), zoom=0.8, matrixcolor=SepiaMatrix()))
image side andrea sera = LayeredImageProxy("Andrea", Transform(crop=(15, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))
define anho = Character(_("Andrea&Howard"), what_prefix='\"', what_suffix='\"', image="andrea", ctc="ctc" , ctc_position="fixed")

define we_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="weser", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define we = Character(_("Weser van Goethe"), what_prefix='\"', what_suffix='\"', image="weser", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define we_i = Character(_("Weser van Goethe"), what_prefix='{i}', image="weser", ctc="ctc" , ctc_position="fixed")
define we_st = Character(_("Weser van Goethe"), what_prefix='{u}\"', what_suffix='\"', image="weser", ctc="ctc" , ctc_position="fixed", callback=male_beep)
image side weser = LayeredImageProxy("Weser", Transform(crop=(15, 0, 445, 440), zoom=0.8))
image side weser nulla = Null()
image side weser darko = LayeredImageProxy("Weser", Transform(crop=(15, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side weser sera = LayeredImageProxy("Weser", Transform(crop=(15, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))

define ag_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="agni", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define ag = Character(_("Agni"), what_prefix='\"', what_suffix='\"', image="agni", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define ag_n = Character(_("Agni"), what_suffix='\"', image="agni", ctc="ctc" , ctc_position="fixed", callback=male_beep)
define ag_i = Character(_("Agni"), what_prefix='{i}', image="agni", ctc="ctc" , ctc_position="fixed")
define ag_st = Character(_("Agni"), what_prefix='{u}\"', what_suffix='\"', image="agni", ctc="ctc" , ctc_position="fixed", callback=male_beep)
image side agni = LayeredImageProxy("Agni", Transform(crop=(110, -30, 445, 440), zoom=0.85))
image side agni nulla = Null()
image side agni darko = LayeredImageProxy("Agni", Transform(crop=(110, -30, 445, 440), zoom=0.85, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side agni sera = LayeredImageProxy("Agni", Transform(crop=(110, -30, 445, 440), zoom=0.85, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))

define pop = Character(_("Pop Pop"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)
define gran = Character(_("Gran Gran"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=female_beep)
define fis = Character(_("Fishmonger"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)
define fruit = Character(_("Fruitmonger"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=female_beep)
define carp = Character(_("Carpenter"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)
define mer = Character(_("Merchant"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)
define reg = Character(_("Benbow Regular"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)
define reg2 = Character(_("Benbow Female Regular"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=female_beep)
define regs = Character(_("Regulars"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)

##Salem Side Characters
define ci_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="cinder", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define ci = Character(_("Cinder Fall"), what_prefix='\"', what_suffix='\"', image="cinder", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define ci_i = Character(_("Cinder Fall"), what_prefix='{i}', image="cinder", ctc="ctc" , ctc_position="fixed")
define ci_st = Character(_("Cinder Fall"), what_prefix='{u}\"', what_suffix='\"', image="cinder", ctc="ctc" , ctc_position="fixed", callback=female_beep)
image side cinder = LayeredImageProxy("Cinder", Transform(crop=(45, 0, 445, 440), zoom=0.8))
image side cinder nulla = Null()
image side cinder darko = LayeredImageProxy("Cinder", Transform(crop=(45, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side cinder sera = LayeredImageProxy("Cinder", Transform(crop=(45, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))

define me_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="medea", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define me = Character(_("Medea Kallas"), what_prefix='\"', what_suffix='\"', image="medea", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define me_i = Character(_("Medea Kallas"), what_prefix='{i}', image="medea", ctc="ctc" , ctc_position="fixed")
define me_st = Character(_("Medea Kallas"), what_prefix='{u}\"', what_suffix='\"', image="medea", ctc="ctc" , ctc_position="fixed", callback=female_beep)
image side medea = LayeredImageProxy("Medea", Transform(crop=(75, 0, 380, 440), zoom=0.8))
image side medea nulla = Null()
image side medea darko = LayeredImageProxy("Medea", Transform(crop=(75, 0, 380, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side medea sera = LayeredImageProxy("Medea", Transform(crop=(75, 0, 380, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))

define mo_x = Character(_("?????"), what_prefix='\"', what_suffix='\"', image="morgan", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define mo = Character(_("Morgan Braeburn"), what_prefix='\"', what_suffix='\"', image="morgan", ctc="ctc" , ctc_position="fixed", callback=female_beep)
define mo_i = Character(_("Morgan Braeburn"), what_prefix='{i}', image="morgan", ctc="ctc" , ctc_position="fixed")
define mo_st = Character(_("Morgan Braeburn"), what_prefix='{u}\"', what_suffix='\"', image="morgan", ctc="ctc" , ctc_position="fixed", callback=female_beep)
image side morgan = LayeredImageProxy("Morgan", Transform(crop=(15, 0, 445, 440), zoom=0.8))
image side morgan nulla = Null()
image side morgan darko = LayeredImageProxy("Morgan", Transform(crop=(15, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side morgan sera = LayeredImageProxy("Morgan", Transform(crop=(15, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))

#Portraits

image side penny = LayeredImageProxy("Penny", Transform(crop=(15, 0, 385, 440), zoom=0.8))
image side penny nulla = Null()
image side penny darko = LayeredImageProxy("Penny", Transform(crop=(15, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side penny sera = LayeredImageProxy("Penny", Transform(crop=(15, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))

image side evelyn = LayeredImageProxy("Evelyn", Transform(crop=(55, 0, 445, 440), zoom=0.8))
image side evelyn nulla = Null()
image side evelyn darko = LayeredImageProxy("Evelyn", Transform(crop=(55, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side evelyn sera = LayeredImageProxy("Evelyn", Transform(crop=(55, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))

image side gemma = LayeredImageProxy("Gemma", Transform(crop=(15, 0, 385, 440), zoom=0.8))
image side gemma nulla = Null()
image side gemma darko = LayeredImageProxy("Gemma", Transform(crop=(15, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side gemma sera = LayeredImageProxy("Gemma", Transform(crop=(15, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))
image side neopolitan = LayeredImageProxy("Neopolitan", Transform(crop=(15, 0, 385, 440), zoom=0.8))
image side neopolitan nulla = Null()
image side neopolitan darko = LayeredImageProxy("Neopolitan", Transform(crop=(15, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side neopolitan sera = LayeredImageProxy("Neopolitan", Transform(crop=(15, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))

image side torchwick = LayeredImageProxy("Torchwick", Transform(crop=(85, 0, 425, 440), zoom=0.8))
image side torchwick nulla = Null()
image side glynda = LayeredImageProxy("Glynda", Transform(crop=(65, 0, 425, 440), zoom=0.8))
image side glynda nulla = Null()
image side glynda darko = LayeredImageProxy("Glynda", Transform(crop=(65, 0, 425, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side glynda sera = LayeredImageProxy("Glynda", Transform(crop=(65, 0, 425, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))
image side violet = LayeredImageProxy("Violet", Transform(crop=(15, 0, 385, 440), zoom=0.8))
image side violet nulla = Null()
image side violet darko = LayeredImageProxy("Violet", Transform(crop=(15, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side violet sera = LayeredImageProxy("Violet", Transform(crop=(15, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))
image side aqua = LayeredImageProxy("Aqua", Transform(crop=(55, 0, 445, 440), zoom=0.8))
image side aqua nulla = Null()
image side aqua darko = LayeredImageProxy("Aqua", Transform(crop=(55, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side aqua sera = LayeredImageProxy("Aqua", Transform(crop=(55, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))

image side maria = LayeredImageProxy("Maria", Transform(crop=(55, 0, 445, 440), zoom=0.8))
image side maria nulla = Null()
image side maria darko = LayeredImageProxy("Maria", Transform(crop=(55, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side maria sera = LayeredImageProxy("Maria", Transform(crop=(55, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))
image side maria sun = LayeredImageProxy("Maria", Transform(crop=(35, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#ffa652", alpha=0.33))))

image side ruby = LayeredImageProxy("Ruby", Transform(crop=(55, 0, 445, 440), zoom=0.8))
image side ruby nulla = Null()
image side ruby darko = LayeredImageProxy("Ruby", Transform(crop=(55, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side ruby sera = LayeredImageProxy("Ruby", Transform(crop=(55, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))
image side ruby sun = LayeredImageProxy("Ruby", Transform(crop=(35, 0, 385, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#ffa652", alpha=0.33))))

image side titania = LayeredImageProxy("Titania", Transform(crop=(25, 0, 445, 440), zoom=0.8))
image side titania nulla = Null()
image side titania darko = LayeredImageProxy("Titania", Transform(crop=(25, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side titania sera = LayeredImageProxy("Titania", Transform(crop=(25, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))
image side ziyan = LayeredImageProxy("Ziyan", Transform(crop=(15, 0, 445, 440), zoom=0.8))
image side ziyan nulla = Null()
image side ziyan darko = LayeredImageProxy("Ziyan", Transform(crop=(15, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side ziyan sera = LayeredImageProxy("Ziyan", Transform(crop=(15, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))
image side philo = LayeredImageProxy("Philo", Transform(crop=(15, 0, 445, 440), zoom=0.8))
image side philo nulla = Null()
image side philo darko = LayeredImageProxy("Philo", Transform(crop=(15, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side philo sera = LayeredImageProxy("Philo", Transform(crop=(15, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))
image side enrico = LayeredImageProxy("Enrico", Transform(crop=(15, 0, 445, 440), zoom=0.8))
image side enrico nulla = Null()
image side enrico darko = LayeredImageProxy("Enrico", Transform(crop=(15, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side enrico sera = LayeredImageProxy("Enrico", Transform(crop=(15, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))

image side ghira = LayeredImageProxy("Ghira", Transform(crop=(145, 0, 500, 440), zoom=0.8))
image side ghira nulla = Null()
image side ghira darko = LayeredImageProxy("Ghira", Transform(crop=(145, 0, 500, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side ghira sera = LayeredImageProxy("Ghira", Transform(crop=(145, 0, 500, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))

image side amber = LayeredImageProxy("Amber", Transform(crop=(5, 0, 445, 440), zoom=0.8))
image side amber nulla = Null()
image side amber darko = LayeredImageProxy("Amber", Transform(crop=(5, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000", alpha=0.95))))
image side amber sera = LayeredImageProxy("Amber", Transform(crop=(5, 0, 445, 440), zoom=0.8, matrixcolor=TintMatrix(Color("#000632", alpha=0.15))))

image side scourge:
    Crop((-20, 0, 545, 740), "scourge_face")
    zoom 0.55
image side scourge nulla = Null()

image side wf_blade neutral:
    Crop((285, 100, 545, 740), "fang_blade_prezoom")
    zoom 0.5
image side wf_blade sun:
    Crop((285, 100, 545, 740), "fang_blade_prezoom")
    matrixcolor TintMatrix(Color("#ffa652",alpha=0.33))
    zoom 0.5
image side wf_blade nito:
    Crop((285, 100, 545, 740), "fang_blade_prezoom")
    matrixcolor TintMatrix(Color("#000D56",alpha=0.45))
    zoom 0.5
image side wf_blade torch:
    Crop((285, 100, 545, 740), "fang_blade_prezoom")
    matrixcolor TintMatrix(Color("#e3563d", alpha=0.33)) * BrightnessMatrix(-0.05)
    zoom 0.5
image side wf_gun neutral:
    Crop((120, 0, 545, 740), "fang_gun_prezoom")
    zoom 0.5
image side wf_gun sun:
    Crop((120, 0, 545, 740), "fang_gun_prezoom")
    matrixcolor TintMatrix(Color("#ffa652",alpha=0.33))
    zoom 0.5
image side wf_gun torch:
    Crop((120, 0, 545, 740), "fang_gun_prezoom")
    matrixcolor TintMatrix(Color("#e3563d", alpha=0.33)) * BrightnessMatrix(-0.05)
    zoom 0.5

image intro_vid_base = Movie(play="gui/intro/main_menu.webm")
image intro_vid:
    "intro_vid_base"
    matrixcolor TintMatrix(Color("#470800",alpha=0.6)) * SaturationMatrix(0.6)

#DEFINING TRANSITIONS
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define flashu = Fade(0.1, 0.0, 0.2, color="#fff")
define stun = Fade(0.1, 0.0, 0.5, color="#DAA520")
define flashO = Fade(0.1, 5.0, 0.5, color="#fff")
define flashi = Fade(0.1, 1.0, 0.5, color="#fff")
define golsho = Fade(0.1, 0.0, 0.5, color="#FFDF00")
define ozsho = Fade(0.1, 0.0, 0.5, color="#50c878")
define DustO = Fade(0.1, 1.0, 0.5, color="#994d00")
define fire = Fade(0.1, 0.0, 0.5, color="#E05F5F")
define poison = Fade(0.1, 0.0, 0.5, color="#88CC00")
define Vision = Fade(0.1, 0.0, 0.5, color="#B4045F")
define firo = Fade(0.1, 1.5, 0.5, color="#E05F5F")
define inferno = Fade(0.1, 0.5, 0.5, color="#ff6600")
define thunder = Fade(0.1, 0.0, 0.5, color="#FF56AF")
define ice = Fade(0.1, 0.0, 0.5, color="#5E99B5")
define aur = Fade(0.1, 0.0, 0.5, color="#76ff7a")
define windt = Fade(0.1, 0.0, 0.5, color="#00e673")
define windto = Fade(0.1, 3.0, 0.5, color="#00e673")
define cream = Fade(0.1, 0.0, 0.5, color="#ffecbf")
define attarn = Fade(0.1, 0.0, 0.5, color="#DCE3E0")
define blood = Fade(0.1, 0.0, 0.1, color="#8A0707")
define bloodo = Fade(0.1, 3.0, 3.0, color="#8A0707")
define silver = Fade(0.1, 0.0, 0.1, color="#999999")
define kiss = Fade(0.1, 5.0, 1.5, color="#FF56AF")
define kisso = Fade(0.1, 2.5, 1.5, color="#FF56AF")
define epup = Fade(0.1, 0.0, 0.1, color="#B7250E")
define pelaser = Fade(0.1, 0.0, 0.1, color="#088A68")
define pebarrier = Fade(0.5, 1.0, 0.5, color="#088A68")
define KO = Fade(0.1, 0.5, 0.5, color="#8A0707")
define healing = Fade(0.1, 0.0, 0.1, color="#088A68")
define lures = Fade(0.1, 0.0, 0.1, color="#006d03")
define mines = Fade(0.1, 0.0, 0.1, color="#00BFFF")
define walls = Fade(0.1, 0.0, 0.1, color="#7e1c1c")
define aurac = Fade(0.1, 0.0, 0.5, color="#ffcc33")
define death = Fade(0.5, 3.0, 0.5, color="#cc0000")
define NRed = Fade(0.1, 0.0, 0.5, color="#ff0101")
define NOrange = Fade(0.1, 0.0, 0.5, color="#FD5F00")
define NYellow = Fade(0.1, 0.0, 0.5, color="#F3F315")
define NGreen = Fade(0.1, 0.0, 0.5, color="#39ff14")
define NBlue = Fade(0.1, 0.0, 0.5, color="#0000ff")
define flash_indigo = Fade(0.1, 0.0, 0.5, color="#6F00FF")
define NViolet = Fade(0.1, 0.0, 0.5, color="#8F00FF")

define Reveal = Dissolve(2.0, alpha=False, time_warp=None)
define Reveal2 = Dissolve(5.0, alpha=False, time_warp=None)
define quick_dissolve = Dissolve(0.20, alpha=False, time_warp=None)

define drone_hit = ImageDissolve("gui/transitions/011.jpg", 0.35, 8)
define hyperspace = ImageDissolve("gui/transitions/019.jpg", 0.5, 16)
define explosive = ImageDissolve("gui/transitions/036.jpg", 0.5, 32)
define load_down = ImageDissolve("gui/transitions/038.jpg", 0.6, 128)
define load_up = ImageDissolve("gui/transitions/038.jpg", 0.6, 128, reverse=True)
define space_explosion = ComposeTransition(explosive, before=hpunch, after=fire)
define eyeopen_slow = ImageDissolve("gui/transitions/transition_eye.png", 3.0, ramplen=128)

define pixel_load = ImageDissolve("gui/transitions/036_pixel.jpg", 0.35, 128)
define pixel_unload = ImageDissolve("gui/transitions/036_pixel.jpg", 0.35, 128, reverse=True)

define maze_load = ImageDissolve("gui/transitions/maze.png", 0.35, 128)
define shatter = ImageDissolve("gui/transitions/shatter.png", 1.0, 8)
define shatter_quick = ImageDissolve("gui/transitions/shatter.png", 0.15, 8)
define comet_load = ImageDissolve("gui/transitions/comet.jpg", 0.66, 64)
define wet = ImageDissolve("gui/transitions/wet.jpg", 1.5, 128, reverse=True)
define smoke = ImageDissolve("gui/transitions/020.jpg", 1.0, 8)

#DEFINING MUSIC CHANNELS
init python:
    renpy.music.register_channel("LoNoise", "bgs",)
    renpy.music.register_channel("LoNoise2", "bgs",)
    renpy.music.register_channel("LoNoise3", "bgs",)
    renpy.music.register_channel("music_room", "music", loop=True, stop_on_mute=True, buffer_queue=True)
    renpy.music.register_channel("sound2", "sfx", loop=False) #Pan Left Channel
    renpy.music.register_channel("sound3", "sfx", loop=False) #Pan Right Channel
    renpy.music.register_channel("sound4", "sfx", loop=False)
    renpy.music.register_channel("sound5", "sfx", loop=False)
    renpy.music.register_channel("sound6", "sfx", loop=False)
    renpy.music.register_channel("sound7", "sfx", loop=False)
    renpy.music.register_channel("beeps", "beeps", loop=False)

#Variables
init:
    default persistent.PC98_mode = False
    default persistent.xtras_mode = False
    default persistent.scroll_music = False
    default func_PC98_mode = False
    default persistent.episodic_mode = False
    default persistent.first_play = False
    default time_screen = False
    default scroll_button = False
    default jewel_owned = False
    default jewel_menus = False
    default dust_suit_menu = False
    default money_available = False
    ## Map related - "one square" for easier resizing
    define osq = 48
    define tooltip_textual = "None"
    define tooltip_display = False
    default map_progress = 0
    default map_name = "None"
    default map_location = "None"
    default progress_hint = False
    default progress_hint_text = "None"
    default story_progress = 0
    default tutorials_showing = True
    default tooltip_explore = "None"
    default relevant_choice = "None"
    default persistent.what_a_guy = False

#EP_00
init:
    default redcliff_target_locked = False

label splashscreen:
    scene black
    pause 1.5
    scene intro_00 with dissolve
    pause 5.0
    play music "audio/bgm/the_day.ogg"
    pause 1.5
    scene intro_01 with dissolve
    pause 2.5
    scene intro_02 with dissolve
    pause 2.5
    scene black with dissolve
    pause 0.5
    scene intro_bg with Reveal
    pause 3.0
    return

label start:
    stop LoNoise fadeout 0.2
    #call bubble_heads_positioning
    call battle_setup_prologue from _call_battle_setup_prologue#battle_screen_test
    $ quick_menu = False
    jump s00_last_time_on_jpde

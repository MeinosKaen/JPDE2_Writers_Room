#Rough Draft of a side quest in Vacuo by 3044Smike
#Quest giver is Haman Navet, first mate for the Vismunger, a fishing vessel in Vacuo that trawls almost exclusively for Moonfish and Pearls.
#He is a dolphin faunus with a penchant for fine liqours, spicy foods, and a good fantasy adventure book.
#My intention is that he has a bit of a South African accent, I don't know if I've accomplished that here though, feel free to normalize his speech if not.

define side_quest3044a_SailorsDelight = SideQuest("Sailor's Delight", "img name", "Haman Navet - Firstmate of the Vismunger", "State of Silver Scales", "75 Hunter Merits", "side_quest3044a_desc", 2)
define ham_x = Character(_("Bald Sailor"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)
define ham = Character(_("Haman Navet"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)
define abrew = Character(_("Amarula Brewer"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=female_beep)
define abark = Character(_("Barkeeper"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)
define amerc = Character(_("Amarula Merchant"), what_prefix='\"', what_suffix='\"', ctc="ctc" , ctc_position="fixed", callback=male_beep)

default side_quest3044a_accepted = False
default side_quest3044a_amarula = False
default side_quest3044a_berbere = False
default side_quest3044a_completed = False
default side_quest3044a_a2 = False
default side_quest3044a_a3 = False
default side_quest3044a_a4 = False

screen side_quest3044a_desc():
    text """A well known fishing vessel's first mate, Haman Navet, has requested additional supplies.""" justify True
    if side_quest3044a_accepted:
        text """The requested supplies are booze and spices not commonly found in the civilized regions of Vacuo.""" justify True
    if side_quest3044a_amarula:
        text """The liquor has been aquired, now to find the spices...""" justify True
    if side_quest3044a_berbere:
        text """The requested supplies have been procured, all that remains is to return to the port.""" justify True
    if side_quest3044a_completed:
        text """The requested supplies have been handed off. Haman has also provided an additional reward in the form of some small mishapen pearls the crew had failed to sell.""" justify True
#
#Quest Start
#
label side_quest3044a_start:
    d surprise "Wow, that ship is nearly the size of the Ambrosia; and you say it's a fishing vessel?"
    ham_x neutral "Indeed she es, the Vismunger beh the most profitable ship en the port too. Meh name es Haman Navet, yeh must beh the Hunteh I requested."
    d neutral "O-oh... right. Yes, I saw it on the network. My team and I have some down time so I figured I could run a quick errand or two for the locals."
    ham neutral "Eh quick errand heh? Yeh must beh ratheh accomplished. E'm lookin foh some additional provisions ef eh specific nature."
    d neutral "Yeah, you mentioned on the post. What exactly am I looking for in the desert that'd count as provisions?"
    ham smile "Well, truth tell, yeh lookin' foh sem uncommen booze en spices. Weh 'bout teh ship off en two dehs foh eh month eh so, need em afoh then."
    ham smile "The booze eh called Amarula. 'S not exactleh semthin' yeh'd find en the more civilized regions of Vacuo. Yeh'll hafteh find eh vendeh in eh village eh semthin."
    ham neutral "The spices eh called Berbere, ehn theh... theh'll beh eh bit trickeh."
    d neutral "How so?"
    ham neutral "'S eh bush root. Noh exactleh common, but commen ehnuff. Feh sem reason tho, Gliphids like teh nest neah them."
    d frown "Hence why you need a team of Hunters."
    d frown "...hmm..."
    ham neutral "Yeh think yeh can do et?"
    d neutral "Probably. My team and I'll give it a shot if nothing else. Just a bit concerned about the time limit."
    ham surprise "Eh take et yeh've handled eh Glyphid nest behfoh then. Most eh the locals hesitate et the word nest."
    d smile "Oh yeah, not too long ago up near the Red Cliffs. They're annoyingly numerous, but quite manageable so long as you kill them fast enough to keep them from surrounding you."
    ham surprise "Ratheh accomplished indeed."
    ham neutral "Eh'll beh here et the port till weh ship off. Wheneveh yeh get the goods."
    d neutral "Understood, see you in two days then."
    if side_quest3044a_accepted == False:
        $ side_quest3044a_accepted = True
#
#Aquiring the Amarula at an outskirts village.
#
label side_quest3044a_booze1:
    d neutral "All right, this village certainly seems remote. Jack, Penny, are you sure we'll find a brewery out here?"
    p smile "This is the village the nice merchant lady mentioned."
    j neutral "I don't remember a brewery, but I know dad got it from around here. I also remember him getting yelled at by my mother for enjoying a bit too much at some festival of some sort."
    e smile "Also you're making alot of assumptions about how this stuff is made. It's probably made in the home of a local."
    j smile "If memory serves, Amarula's basically the equivilant of moonshine. Just less potent and... spicier? Also legal to produce, probably because it's less potent."
    d neutral "I see... Guess we'll have to ask around then. Shall we pair off? Each pair take one side of the main street, the town's pretty small. Shouldn't take long that way."
    j neutral "Sure, let's work with our partners this time. Reconvene here in an hour?"
    d smile "Sounds like a plan."
    p smile "Timer set."
    e smile "Let's find those booze!"
#Transition from open desert to sparse desert town, an investigation space.
label side_quest3044a_booze2:
    d neutral "A saloon seems like a good place to check, don't you think."
    j neutral "Seems logical enough, let me do the talking. I'm kind of a local."
    d neutral "Fine by me."
    j smile "Hey boss, don't suppose you've got any local stuff in stock?"
    abark neutral "Nope."
    j surprise "O-oh... you don't?"
    abark neutral "Merchants just purchased the last of my stock in exchange for this... swill..."
    j pain "A-ah, I see..."
    abark frown "Yeah..."
    abark frown "Ya might be able to find one of 'em lurking around town still. If you're lucky they might still have some in stock. Sold at a premium I'm sure."
    if side_quest3044a_a3 == False:
        d neutral "Thanks, we'll do that then. Here, for the info."
        #Pay barkeep 10 LiYen
        if side_quest3044a_a3 == True:
            d neutral "No dice there actually, they said they'd already sent it all to Oasis."
            abark neutral "Huh, guess they're on a time limit or something, that was quick. Other place you might check is the old lady down the road."
            abark neutral "She actually used to get some big time clients back in the day for her special blend. It's unlikely but probably your best shot."
            j neutral "Thanks, we'll do that then. Here, for the info."
            #Pay barkeep 10 LiYen
    if side_quest3044a_a2 == False:
        $ side_quest3044a_a2 = True
label side_quest3044a_booze3:
    d neutral "Oh, a merchant."
    if side_quest3044a_a2 == False:
        j neutral "Doesn't look local, probably from Oasis. Still worth a try though."
        d smile "Pardon me sir, you wouldn't happen to have any Amarula in stock would you?"
        amerc neutral "Ah, no sorry, just sent it all to Oasis this morning. There's a festival on the horizon after all."
        d neutral "Oh... don't suppose you'd know where to find more."
        amerc neutral "No, but I did get my stock from the saloon up the road. You could ask him if he's got any more. If not I know he at least has some stuff from Oasis thats... not exactly high quality. It'll get you hammered though."
        j smile "Oh, that's... We'll ask him. Thank you sir."
        if side_quest3044a_a2 == True:
            j neutral "Must be the one the barkeep mentioned."
            d smile "Pardon me sir, you wouldn't happen to have any Amarula in stock would you?"
            amerc neutral "Ah, no sorry, just sent it all to Oasis this morning. There's a festival on the horizon after all."
            d neutral "Oh... don't suppose you'd know where to find more."
            amerc neutral "Not particularly. Sorry."
            j surprise "Oh yeah! Hey [p_n] I just remembered, my dad used to get some of that stuff from this lady down the road, lets check there."
            d surprise "Oh? Ok, sure, if you think it's worth a shot."
    if side_quest3044a_a3 == False:
        $ side_quest3044a_a3 = True
label side_quest3044a_booze4:
    if side_quest3044a_a2 == False:
        if side_quest3044a_a3 == False:
            d_i neutral "(An elderly lady is sweeping her porch. She's giving me the stink eye... we are outsiders after all, better leave her be.)"
    if side_quest3044a_a2 == False:
        if side_quest3044a_a3 == True:
            d_i neutral "(An elderly lady is sweeping her porch absently... I think she's swept the same spot 4 times now... we should probably avoid her.)"
    if side_quest3044a_a2 == True:
        if side_quest3044a_a3 == False:
            d_i frown "(An elderly lady is sitting on her porch watching us intensely... I have the feeling we should steer clear.)"
    if side_quest3044a_a2 == True:
        if side_quest3044a_a3 == True:
        j neutral "Pardon me ma'am."
        abrew frown "Yes? How can I help you young lady?"
        j smile "My friends and I have been asking around and it seems you're the only one in town who might have any Amarula in stock. Would you be willing to part with a few jars?"
        abrew neutral "Why of course dear, for a... nominal... fee of course."
        j smile "Of course ma'am, what's your price?"
        abrew smile "650 per jar. And you can't have the last one, it's for personal use."
        j surprise "That's..."
        d surprise "That's a bit steep."
        abrew frown "... Consider it the price of tourism."
        d frown "Not a great buisness model."
        j smile "Wait! What if I were a local. I'm just looking to show my friends a taste of my home."
        abrew frown "Waddya mean a local, you don't-"
        abrew surprise "Wait... ... are you that-"
        j smile "The name's Jaquline B. Ivory."
        abrew smile "Well I'll be... Ivory family's best thing that happened to Vacuo short of Lady Ozma taking Sovereignship."
        abrew neutral "Tell you what, you and your friends are Hunters yeah? I can tell by the gear. 800 and I'll give you all 20 jars."
        j surprise "W-Why thank you very much, but that seems like {b}far{/b} too much of a discount."
        abrew neutral "Nonsense girl. To this day your family's been helping the people of Vacuo one way or another. Regardless of how things may have happened in the past. Think of it as a long overdue and well deserved thanks."
        abrew smile "And if you happen to have some left over after sharing with your friends, why don't you pour out a jar for your old man. He used to buy this stuff from me all the time back in the day."
        j smile "I-I think I will, umm... thank you."
        abrew smile "You're quite welcome young miss. Run along now."
        if side_quest3044a_a4 == False:
            $ side_quest3044a_a4 = True
#Transition from sparse desert town back to open desert
label side_quest3044a_booze5:
    e frown "No dice"
    p frown "It looks like everyone on our half of the town is out of stock."
    d neutral "That's all right, Jack used her wiles on a kind older lady and we got some."
    j frown "Don't say it like that. And I didn't use any wiles."
    e neutral "Oh yeah... sometimes I forget the Ivory name goes far here in Vacuo. Penny, we should've tried that."
    p neutral "Probably for the best we didn't, otherwise we would've had to drag Jack around from home to home."
    d smile "Ha. That would have been a sight for sure."
    j neutral "Uh huh, would you all like to get in a quick sparring session."
    e pain "Let's not."
    d pain "No thanks."
    p pain "Maybe later."
    j neutral "That's what I thought."
    j neutral "Now then, Penny I believe you had mentioned there were Gliphid sightings near this village a couple weeks back."
    p smile "Indeed, no attacks mind you, just sightings. Which means-"
    e neutral "Which means there may be a nest close by."
    d neutral "A nest who's queen is smart enough to know attacks would bring Hunters."
    j frown "Well, that'll be fun."
    e frown "Why's it gotta be the bug-like ones..."
    if side_quest3044a_amarula == False:
        $ side_quest3044a_amarula = True
#
#Tracking down a Gliphid nest and aquiring the Berbere.
#
label side_quest3044a_spices:
    e frown "Penny..."
    e frown "Penny..."
    e frown "Penny..."
    p neutral "Evelyn..."
    e frown "Are we there yet."
    p neutral "Nearly."
    j frown "Carrots, shut up."
    d frown "Byun, why do you do these things."
    e frown "Boredom."
    p frown "We've arrived."
    e surprise "Oh, you weren't kidding about nearly."
    j neutral "Right, someone will have to wait with the Waste Strider."
    d smile "Can I just say again that I love this thing by the way. It's like a train or a shuttle but so much more convenient."
    p smile "I agree, unfortunately not much use outside the open spaces of Vacuo or Menagerie. We'll have to ask Ruby to try and make a more compact version. Maybe something like Yang's motorbike."
    e smile "Ooh, I'd love a version that could be used like the cars back in Vale."
    j smile "Right, right, focus up everyone. While we're technically just here for the Berbere root, it'd probably be handy to take out a few Glyphids since we're already here."
    j neutral "I'm not saying we go looking for a fight, but there's no need to sneak around. Be prepared. Now then, like I was saying before, who'll stay with the Waste Strider? Any volunteers?"
    e neutral "Well, if no one else is going to. I'll stay, I don't like how Glyphid legs wriggle."
    j neutral "Fair enough, no objections I presume."
    d neutral "Nope."
    p neutral "Negative."
    j neutral "All right then, let's get going. I'm pretty sure those bushes there atop the next dune are the type we're looking for."
    #Transition from open desert to open desert with a handfull of bushes
    p neutral "You were right Jack, these are the correct bushes. If you two keep a look out, I shall extract enough roots for the request."
    d neutral "Rodger."
    j frown "No need for a look out."
    j frown "Here comes a welcoming party."
    #Simple combat encounter starts against a large group of Glyphids with David and Jack as the team members.
    d neutral "I think that's it for now. How's the progress Penny?"
    p smile "All set here. Let's head back before any more show up."
    j smile "Excellent. Let's head back then, I'm sure Carrots is probably starting to lose her mind by now."
    if side_quest3044a_berbere == False:
        $ side_quest3044a_berbere = True
        $ side_quest3044a_amarula = False
#
#Returning to Haman to exchange the supplies for the rewards.
#
label side_quest3044a_turnIn:
    e surprise "Wow, it is a large ship."
    d smile "That's what I said. Why'd you come with me again?"
    e smile "Well if you're gonna need help with carrying this stuff any way, I figure the port will be more entertaining than helping Penny clean her joints of sand."
    d smile "Had enough of sitting around for the day huh?"
    ham smile "Ah, the Hunteh lad. Ehn eh cute lass ehs well."
    d neutral "Oh! Hello again Haman. This is Evelyn, one of my teammates and my girlfriend. We've brought the supplies you requested."
    ham smile "Perfect timehn. Weh've just finished accountehn feh the crew ehn eh plannehn teh head eff en eh hour."
    ham neutral "Eh'll mark et eff ehs complete ehn the netwehk."
    ham surprise "Brothehs thehts good. Heh eh little extreh the lads couldehn't sell."
    d confused "Great, thanks... What are these?"
    ham neutral "Mishappehn pearls. Eh beht too small feh the local markehts, but eh figure eh Hunteh who travels ehround eh bunch 'll find sehmone teh buy ehm."
    e smile "I could also use them to make some simple accessories for Janara. They'd match well with her skin tone."
    d smile "Oh, I see. Well thanks again then. And fair seas to you Mr. Haman."
    ham smile "Ehn teh you lad."
    if side_quest3044a_completed == False:
        $ side_quest3044a_completed = True
        $ side_quest3044a_berbere = False
#Quest reward is 75 Hunter merits and a set of mishapen pearls that can be sold for 1000 LiYen in Peak or given as a gift to Janara on her birthday later on in the form of a hair accessory.
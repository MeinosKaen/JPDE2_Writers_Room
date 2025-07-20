#Investigative Side Quest made by comradedawgo.
#This is literally my first time messing with coding, so sorry for inaccuracies.
#This quest starts in Peak, but has the team travel about 5-10 miles east of Peak to enter the Sirius Region.


define side_quest007_grimm_prognosis = SideQuest("Grimm Prognosis", "image_placeholder", "Dr. Althea Quill", "Sirius Region", "20 Hunter Merits", "side_quest007_desc", 1)

default side_quest007_step1 = False
default side_quest007_step2 = False
default side_quest007_step3 = False

screen side_quest007_desc():
    text """Dr. Althea Quill, a physican from Vale's Sirius Region, asks our help to retrieve a momento that she was given from her late father.""" justify True
    if side_quest007_step1:
        text """Arriving at the Grimm infested town, [p_n] and his team make it to the abandoned clinic to find the lost item.""" justify True
    if side_quest007_step2:
        text """After dealing with some resistance, the group recovers the stethoscope that Quill asked for. Now, to return home.""" justify True
    if side_quest007_step3:
        text """[p_n] gives the item back to Quill, who in returns, offers her many thanks and a reward.""" justify True
#
#Beginning
#
label side_quest007_start:
    David Neutral: "You look down."
    Althea: "I do? Well, suppose someone was bound to notice."
    David Neutral: "May I ask why?"
    Althea: "A bit of a long story, but have you heard of Sirius region?"
    David Neutral: "That area of Vale that the leadership barely messed with? Heard a bit about it. Why?"
    Althea: "Well, before I came to Peak, I used to live in a town about...5 miles-ish from here? I worked in a clinic there, atleast until the Grimm overran it. Wasn't a lot of Grimm, so I doubt it'll be an issue to Peak. We just didn't have any Huntsmen with us."
    Althea: "During the evacutation we barely scrambled to make, I had to leave behind the only thing I had left of my dad. He...died a few years ago and gave me a stethoscope as a gift."
    David Sad: "I'm sorry to hear that. I understand how it feels to lose something you care about."
    Althea: "Thanks. I've been trying to find someone who could try to get it back for me, but no luck."
    David Smile: "Well, me and my Team happen to have some freetime. Maybe we could get it for you?"
    Althea: "You would do that? Oh thank you! It would mean the world to me, and I promise to reward you generously!"
    Althea: "I believe I left the stethoscope in my office. It should have a fire pattern on the metal."
    David Smile: "We'll see what we can do. We promise."

#When Team JPDE arrives at the town
label side_quest007_arrival:
    Evelyn Surprise: "Woah, they weren't kidding when they said it was overrun!"
    Penny Sad: "It's ashame they had no huntsmen to protect them. If they did, maybe this town would still be thriving."
    Jack Frown: "There's not much we can do now, unfortunately. Let's get what we came here for, before more Grimm get here."
    David Neutral: "Althea said it should be in her office inside that clinic up ahead."
    Jack Neutral: "I'd say we cut through and try to only fight the Grimm we need to."
    David Smile; "Seems like a plan, partner. Let's go."

#Transition to the interior of the clinic, an investigation area.
label side_quest007_event01:
    Evelyn Neutral: "Huh, most of the stuff here still looks...okay."
    Jack Neutral: "You think we can bring some of this back to Peak?"
    Penny Smile: "I'm sure Goodwitch wouldn't mind us bringing more supplies back!"
    David Smile: "Then let's start searching and see what we can get, as a bonus."

label side_quest007_event02:
    David (thought) Neutral: "(A first aid cabinet. Maybe there's something we can use in there?)"
    David Surprise: "Neat. Bandages. We can use these."
    #Give Player 2-3 Bandages, an HP Item restoring a minimal amount of HP.

label side_quest007_event03:
    Jack Neutral: "So this is her office? Looks like a cozy space."
    Evelyn Frown: "If you ignore the shattered windows and holes in the walls."
    Penny Neutral: "If what David said is true, the Stethoscope should be somewhere in here."

label side_quest007_event04:
If desk drawer has not been inspected:
    David Neutral: "You guys reckon this drawer has what we're looking for?"
    Evelyn Smile: "Wouldn't hurt to check, hehe."
    David Frown: "If it wasn't locked, that is..."
    If office cabinet has been inspected:
      David Smile: "Thankfully, we found this key."
      David Smile: "This should be what Althea wanted. Fire pattern on the metal, just like she said."
      Jack Smile: "Guess we can head home now, hmm?"
    If office cabinet has not been inspected:
      Evelyn Frown: "Welp, wouldn't be fun if it was that easy, huh?"
      David Neutral: "Let's keep searching then."
If desk drawer has been inspected:
  David (thought) Frown: "(Not gonna open itself, David...)"

#After the Group leaves the building with the quest item
label side_quest007_event05:
    Evelyn Neutral: "You know, for a place full of Grimm, I'm surprised none of them bothered us yet."
    Jack Frown: "And just for saying that, you most definitely jinxed us."
    Evelyn Smile: "Pfft, no I didn't!"
    Jack Frown: "Way to go, carrots..."
#After a fight against a large amount of Beowolves, with Team JPDE being the current party.
    Penny Neutral: "I think that's all of them. We should hurry before more arrive."
    David Surprised: "Yeah, come on."

#After returning to Peak and speaking with Althea
label side_quest007_event06
   David Smile: "We brought back what you wanted."
   Althea: "Oh. Oh, brother gods, you really did! You cannot begin to understand just how happy I am to see this again! A million thanks to you!"
   David Smile: "It was no trouble, really. We're just glad to help."
   Althea: "It was a selfish request of me, but you still did it. You're a great Huntsman!"
   Althea: "Ah right, your reward! Uhm...please, accept these!"
   David Surprised: "Huh, what's this?"
   Althea: "It's a copy of a research paper of how we can use Dust better, especially for medicine. I thought, maybe as a Huntsman, it might come in handy. Oh, and the firstaid tips."
   David Surprised: "Well, thanks I guess?"
   #Player recieves 500-1500 Lien, whichever is fairer

#My suggestions for what the Research Paper could do was have a extremely remote boost to healing items, or just as a gift for Professor/Headmistress Peach. 



    

    


 
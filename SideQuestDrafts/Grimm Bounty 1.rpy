#Ryebread Sidequest entry #1, Grimm Bounty 1 Rought Draft
#How did I do? I'm totally willing to refine this quest after I get feedback about how it can be improved. Espicially in regards to my "coding".

#This is a very basic quest, not that interesting, I know. I plan for two sequal quests with greater challenges and greater rewards. 
#The second and third quests are going to be just like this one, basic dungeon crawler, but the hunted grimm get larger and thus more dangerous. 
#Grimm Bounty 2 would have the objective of fighting LIZARD and Death Stalker Grimm from Vacuo. While Grimm Bounty 3 would feature Ursa from Vale. 

#I have better idea's, I just wanted to get one quest done, one that I was confident I could get done, one I knew would be possible to code.

#I introduce a new character in this quest, I'm not sure what steps I need to take to code that in.
#I've made a dungeon map rought draft, just the basic shape. Its a rough draft because I'm not sure exactly how to make a dungeon map that you can use.

#I will be counting my quests in prime numbers added to 100. Of course you can change that to whatever you'd like if you decide to implement the quest.

#Quest Basics

define side_quest102_grimm_bounty_1 = Sidequest("Grimm Bounty", "image", "Velma Baker", "State of Oasis", "15 Hunter Merits", "side_quest002_desc", 1)

default side_quest102_step1 = False

Screen side_quest102_desc():
    Text """Velma Garner, a leader of Golden Stream Labs, a lab within the Semer cast of Vacuo, requests captured living grimm. Particularly eight Kataglyphs from the Vacuo Wastes. The grimm would be used for scientific experimentation, furthering the understanding of humanity’s oldest enemy. They have provided the cages to hold the small grimm. Golden Stream Labs will be providing transportation for the Hunters who accept the job, since they need to transport the cages back to Vacuo anyway.""" justify True
    If side_quest102_step1:
        text """After a grueling day of hunting Grimm, Team JADE has developed skills in the wrangling of Kataglyphs. The Golden Stream Lab’s airship crew remarked that the wounds Team JADE suffered, are a sign of a respectable job well done. Additionally, they hope to meet JADE again in the future. The Golden Stream Labs crew dropped Team JADE off at Peak, and returned to Vacuo with their newly captured grimm.""" Justify True


#Quest Events

#Triggered at the beginning of the mission
Label grimm_bounty_102_event01:
    *The team disembarks from the Golden Stream Labs airship into the desert. They’re each carrying two small cages.*

    Airship captain: “We’ll wait here until you’ve completed your mission. Then we’ll fly you back to Peak.”

    Jack smile: “Got it, we shouldn’t be long. Thanks for the lift.”

    *The captain retreats back into the airship and closes the door. Leaving Team JADE alone in the Grimm infested desert.*

    Jack Neutral: “Alright, team. Our goal is the capture of Kataglyphs. Capturing them will take finesse and time, it's probably best to only capture Grimm that are alone. So if we found a group, kill all but one. Evelyn, Penny, any intel for me?”

    Evelyn Smile: “There’s definitely Grimm in the area. I can hear a few groups.”

    Penny neutral: “I spotted a pack to the north while we were landing, including Kataglyphs.”

    Jack smile: “Great work. [p_n], take point. Everyone be careful, if you can’t cage a Kataglyph safely, kill it. We’ll just find more.”

#These events are meant to happen in order, as its a continued conversation. Is that possible?

Label grimm_bounty_102_event02:
    David frown: “This is tougher than I expected.”

    Evelyn frown: “Yes it is. Capturing them alive while they’re hellbent on killing you is a daunting task.

    Penny neutral: "That's likely because the task is new to us. We received extensive education on how to kill Grimm, yet next to nothing about capturing them alive.”

    Evelyn frown: “I wonder if capturing Grimm is taught at Shade.”

    Jack frown: “Considering the size of the Semer caste, I bet it is.”

    David surprised: “If that's true, then why aren’t Vacuo Hunters handling this?”

    Evelyn alert: "There's another group of Grimm nearby.”

    Jack surprised: “We’ll figure it out later, get ready for combat.”



Label grimm_bounty_102_event03:
    *Team JADE has captured several Kataglyphs and completed their objective. Now they head back towards the Golden Stream Labs airship.*

    David neutral: “Maybe Vacuo doesn’t have enough Hunters for these types of missions.”

    Penny neutral: “Vacuo has always had a large amount of Hunters though. If there aren’t enough available that either tells us that their numbers have diminished, or they have a higher demand for Hunters.”

    Jack neutral: “It could be a political matter instead of manpower. Maybe Golden Stream Labs supports Peak and wants to give us the work over Hunters from Vacuo.”

    David smile: “That could be. The crew on the airship were nice to us.”

    Eveyln frown: “Or hiring us is cheaper than hiring Vacuo Hunters.”

    David frown: “...And if something goes wrong on this dangerous mission and we’re hurt, only Peak is harmed, instead of Vacuo. They could have hired us because we are expendable.”

    Penny sad: “Should we ask the airship crew?”

    Jack frown: “I will, once we’re almost at Peak. That way if we get an answer we don’t like we won’t have to spend much time in a bad atmosphere. But we might not get an answer at all. That crew is acting as a taxi service, they aren’t the ones who made the job offer.” 

#This event is meant to be triggered at the end of the mission
#In this event I wrote people's expressions even though they don't have dialogue, I'm imagining this being a standard visual novel scene, with everyone being present on the screen. If thats possible.
Label grimm_bounty_102_event04:
*Team JADE completed their mission and are now being ferried back to Peak aboard Golden Stream Lab’s airship.*

    Jack smile: 
    David smile:
    Penny smile:
    Evelyn smile:

    Airship Captain: “Good work today Hunters, a job well done.”

    Jack smile: “Thank you Captain, we’re happy to help.”

    Jack frown: “We do have a question for you, if you don’t mind.”

    Airship Captain: “Well sure, ask away.”

    Jack neutral: “Do you know why we were hired for the job, over Hunters in Vacuo?”
    David frown:
    Penny neutral:
    Evelyn frown:

    Airship captain: “Sorry las, I don’t know why the top dogs do anything. Though I can tell you why I’m here. The role to provide transport for this mission was left up to volunteers. My crew and I volunteered, because we wanted to work with Peak Hunters. At least to see how you operate, at most to build friendships.”

    David surprised:
    Evelyn surprised:
    Penny smile:
    Jack smile: “Well then, what do you think of our performance?”

    Airship Captain: “Efficient and professional. Just like how Hunters should be. We’re coming up on Peak, better get to the cockpit. But it was a pleasure meeting you Team JADE. I hope we can work with you again.”

    Jack smile: “The same to you, Captain.”

#Quest end

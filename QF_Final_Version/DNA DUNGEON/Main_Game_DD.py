import pygame
from Bio.Seq import Seq
import button
import random
import subprocess
from subprocess import Popen
import sys

shell = True

def open_snake_file():
    #Popen(["python3", "Snake_Minigame.py"])
    snake = subprocess.Popen([sys.executable,"Snake_Minigame.py"])
    snake.communicate()
    
def open_matching_file():
    #Popen(["python3", "match_minigame.py"])
    matching = subprocess.Popen([sys.executable,"match_minigame.py"])
    matching.communicate()

def open_dots_file():
    #Popen(["python3", "dots_minigame.py"])
    dots = subprocess.Popen([sys.executable,"dots_minigame.py"])
    dots.communicate()


pygame.init() #initializing <3 never forget it 
pygame.mixer.init(frequency = 44100, size = -16, channels = 1, buffer = 2**12)

#screen
screen = pygame.display.set_mode((800,500)) #width and height
pygame.display.set_caption(' DNA DUNGEON')
clock =  pygame.time.Clock() #controls our lovley frame rate 
pygame.mouse.set_cursor(*pygame.cursors.tri_left) #Cursor, we can change






#fonts and typing below
title_font= pygame.font.Font(r'fonts\\MorrisRoman-Black.ttf', 60) #font type, font size
normal_font = pygame.font.Font('fonts\\dumbledor.TTF', 34)
DNA_font = pygame.font.Font('fonts\\dumbledor.TTF', 40)

#special reciepe for nucletide sequence
nucleotides = ["A", "C", "G", "T"]

def generate_sequence():
    my_seq = ["A", "T", "G"] #Gotta start with the Start Codon 
    
    for i in range(6):
        letter = random.choice(nucleotides)
        my_seq.append(letter)

    return Seq(''.join(my_seq))




#################################################################################
# * Elements * Elements * Elements * Elements * Elements * Elements * Elements *

dungeon = pygame.image.load('graphics\\StarterDUN1.png').convert()
dungeon2= pygame.image.load('graphics\\deeperDUN.png').convert()
text_box = pygame.Surface((800, 125)).convert()
text_box.fill('gray')
box = pygame.Surface((460, 80)).convert()
box.fill("gray40")
title_box = pygame.Surface((450, 70)).convert()
title_box.fill("gray")
title = title_font.render("DNA DUNGEON", False ,"black" ) #text info, anti-aliase(smooths), color
start = pygame.image.load("figures\\Start.png").convert_alpha()
start_button = button.Button(225,150, start, 0.75) #button instance file name, class name , last number is the scale
next = pygame.image.load("figures\\Next.png").convert_alpha()
next_button = button.Button(680,420, next, 0.27)
search = pygame.image.load("figures\\Search.png").convert_alpha()#might change for aesetics lowkey hate
search_button = button.Button(290,370, search, 0.5)
front_note = pygame.image.load('figures\\front_note.png').convert_alpha()
note = pygame.transform.scale(front_note, (400,250))
back_note = pygame.image.load('figures\\back_note.png').convert_alpha()
back = pygame.transform.scale(back_note, (400,250))
flip = pygame.image.load('figures\\flip_note.png').convert_alpha()
flip_button = button.Button(480,307, flip, 0.18)
close = pygame.image.load('figures\\close_note.png').convert_alpha()
close_button = button.Button(455,275, close, 0.5)
next2 = pygame.image.load("figures\\Next.png").convert_alpha()
next_button2 = button.Button(680,420, next2, 0.27)
randomize = pygame.image.load("figures\\randomizeDna.png").convert_alpha()
randomize_button = button.Button(270,150, randomize, 0.60)
nuc_box = pygame.Surface((370, 50)).convert()
nuc_box.fill("gray")
next_button4 = button.Button(680,420, next, 0.27)
mg = pygame.image.load("figures/side_questy.png").convert_alpha()
mg_button1 = button.Button(250,150, mg, 0.60)
mg_button2 = button.Button(250,150, mg, 0.60)
replicate = pygame.image.load("figures\\Replicatedna.png").convert_alpha()
replicate_button = button.Button(630,270, replicate, 0.35)
comp_box = pygame.Surface((370, 50)).convert()
comp_box.fill("gray")
ladder = pygame.image.load('figures\\Ladder5.png').convert_alpha()
rep_ladder = pygame.image.load('figures\\reverse_ladder.png').convert_alpha()
protip1 = pygame.image.load('figures\\Rna_tip.png').convert_alpha()
RNApro_tip = pygame.transform.scale(protip1, (400,250))
RNA_box = pygame.Surface((370, 50)).convert()
RNA_box.fill("indianred1")
transcribe = pygame.image.load("figures\\transcribe.png").convert_alpha()
transcribe_button = button.Button(630,270, transcribe, 0.35)
protip2 = pygame.image.load('figures\\pro_tip2.png').convert_alpha()
Proteinpro_tip = pygame.transform.scale(protip2, (390,245))
translate = pygame.image.load("figures\\translateRna.png").convert_alpha()
translate_button = button.Button(630,270, translate, 0.35)
line = pygame.image.load("figures\\Line.png").convert_alpha()
stop = pygame.image.load("figures\\Stop.png").convert_alpha()
escape = pygame.image.load("figures\\escape.png").convert_alpha()
escape_button = button.Button(245,160, escape, 0.70)
finish_note = pygame.image.load('figures\\final_note.png').convert_alpha()
credits_b = pygame.image.load("figures\\credit_buttom.png").convert_alpha()
credits_button = button.Button(680,220, credits_b, 0.30)
starter_credits_button= button.Button(278,340, credits_b, 0.55)
back_to_start = pygame.image.load("figures\\back_to_start.png").convert_alpha()
back_to_start_button = button.Button(580,3603, back_to_start, 0.50)
credits_words = pygame.image.load("figures\\credit_scene.png").convert_alpha()



amino_acids = {
    'A': pygame.image.load('figures\\amino acids\\ALA.png').convert_alpha(),
    'R': pygame.image.load('figures\\amino acids\\ARG.png').convert_alpha(),
    'D': pygame.image.load('figures\\amino acids\\ASP.png').convert_alpha(),
    'N': pygame.image.load('figures\\amino acids\\ASN.png').convert_alpha(),
    'C': pygame.image.load('figures\\amino acids\\CYS.png').convert_alpha(),
    'E': pygame.image.load('figures\\amino acids\\GLU.png').convert_alpha(),
    'Q': pygame.image.load('figures\\amino acids\\GLN.png').convert_alpha(),
    'G': pygame.image.load('figures\\amino acids\\GLY.png').convert_alpha(),
    'H': pygame.image.load('figures\\amino acids\\HIS.png').convert_alpha(),
    'I': pygame.image.load('figures\\amino acids\\ILE.png').convert_alpha(),
    'L': pygame.image.load('figures\\amino acids\\LEU.png').convert_alpha(),
    'K': pygame.image.load('figures\\amino acids\\LYS.png').convert_alpha(),
    'M': pygame.image.load('figures\\amino acids\\MET.png').convert_alpha(),
    'F': pygame.image.load('figures\\amino acids\\PHE.png').convert_alpha(),
    'P': pygame.image.load('figures\\amino acids\\PRO.png').convert_alpha(),
    'S': pygame.image.load('figures\\amino acids\\SER.png').convert_alpha(),
    'T': pygame.image.load('figures\\amino acids\\THR.png').convert_alpha(),
    'W': pygame.image.load('figures\\amino acids\\TRP.png').convert_alpha(),
    'Y': pygame.image.load('figures\\amino acids\\TYR.png').convert_alpha(),
    'V': pygame.image.load('figures\\amino acids\\Val.png').convert_alpha()}





#################################################################################


#drawing text
def draw_text(text, font, color, x, y):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))


def starter_screen():
    pygame.mixer.music.load('music\\alexander-nakarada-lively-tavern.mp3')
    pygame.mixer.music.play(loops=-1) 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        screen.blit(dungeon2,(0,0))
        screen.blit(box, (160,58))
        screen.blit(title_box, (165, 63))
        screen.blit(title, (180, 80))
        
        if starter_credits_button.draw(screen):
            credits()#LOOPS IT BACK YAYYYY FINISHED
        
        if start_button.draw(screen):
            game()
            break

        pygame.display.update()
        clock.tick(60)

def credits():
    while True:
        pygame.mixer.music.play(loops=20, start=0.0, fade_ms=0)
        pygame.mixer.music.set_volume(0.75) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill('black')
        screen.blit(credits_words, (100, 0))
        if back_to_start_button.draw(screen):
            starter_screen() #LOOPS IT BACK YAYYYY FINISHED

        pygame.display.update()
        clock.tick(60)

def basic_screen():
        screen.blit(dungeon,(0,0))
        screen.blit(box, (175,28))
        screen.blit(text_box,(0,375))
        screen.blit(title_box, (180, 33))
        screen.blit(title, (200, 47))






#################################################################################
# * SCRIPT * SCRIPT * SCRIPT * SCRIPT * SCRIPT * SCRIPT * SCRIPT * SCRIPT * 


Intro = ["You hear a rustling breeze and a cool wind at your back.",
         "As you stir awake, you find yourself trapped in a dark, damp dungeon.",
            "The chill is too uncomfortable and you begin to feel restless.",
     "You remember not to panic and keep your wits.",
     "You should probably look around for any clues to escape.",
     "After brushing along the dungeon walls proved unsuccessful...",
     "you decide to press your hands against the floor to feel your way out of this plight."
     ]


note_script = ["You quickly snatch up the mysterious clue to your entrapment in this dungeon"]

brick_script = ["You feel betrayed, but to escape you know you must start with Replication"]

red_script = ["DNA is composed of nucleotides, Click to gather a Random Sequence"]
orange_script = ["Now you have one strand of DNA, Each letter represents one nucleotide"]

DNA_seq = generate_sequence()
stop_codons = ["TAA", "TAG", "TGA"]
while any(stop_codon in str(DNA_seq) for stop_codon in stop_codons):
    # Regenerate the entire sequence if any stop codon is found
    DNA_seq = generate_sequence()


stone_script = ["There are four types: Adenine (A), Thymine (T), Guanine (G), Cytosine (C)"]
plastic_script = ["Base pairs are complementary nucleotides you must match to Replicate DNA"]
minigame1_script = ["Base pairing rules are A<=>T and C<=>G. Before you replicate, you should practice"]
done_game1_script = ["Refresh your memory of base pairs by matching the squares."]
yellow_script = ["Now that your memory has been replenished, Time to replicate"]
green_script = ["Wonderful, now you have two strands of DNA, The shape is called a double helix "]

comp_DNA = DNA_seq.complement()

mint_script = ["The Top Strand you Replicated is called the Template Stand"]
blue_script = ["You now need to unwind and get rid of the Template Strand, you no longer need it"]
teal_script = ["Now that you have replicated your strand, the next step is TRANSCRIPTION"]
indigo_script = ["You Remember Transcription is the process where DNA is transcribed into RNA."]
purple_script = ["RNA will eventually code for proteins aka the Polypeptide Chain. "]
minigame2_script = ["There are two parts of RNA, Exons code for Proteins, Introns do not "]
done_game2_script = ["Use your skills to decide which parts are Exons vs Introns by clicking on the Lines."]
aqua_script = ["You remind yourself that Adenine(A) codes for Uracil (U). Now Transcribe. "] #Might change this to saying they aren't attached
coral_script = ["Oh Jolly! You've completed the next step, you've transcribed DNA into RNA"]

RNA_seq = DNA_seq.transcribe()

cyan_script= ["It is called transcription because it involves the rewriting of DNA"]#boringggggg
olive_script = ["You have no further use for the DNA and discard it."]
orchid_script = ["Your final step in Translation: using RNA to get Protein"]
pink_script = ["The RNA is translated to the amino acids of a polypeptide chain"]
violet_script = ["The RNA is grouped in clusters of three called Codons before translated"]
gold_script = ["You remember from your mind's eye that each codon specifies an amino acid"]
minigame3_script = ["You know to practice linking the amino before you forge the ultimate creation"]
done_game3_script = ["Use your medieval arrow keys to guide the amino acid chain towards its companions."]
ivory_script = ["Now that you have honed thy skills, it is now time to translate"]
salmon_script = ["There are sixty-one codons that specify amino acids."]
khaki_script = ["You make sure it begins with a 'start' codon"]

poly_chain = RNA_seq.translate()

tan_script = ["You don't need the RNA anymore, you may rid yourself it"]
maroon_script = ["Once...Twice...Thrice!!! That's three amino acids"]
magenta_script = ["You remember to implement a 'stop' codon to complete the chain and break yours"]
lime_script = ["Cheers, you've completed the King's task!"]






#################################################################################



def game():

    #These are for the scrolling text 
    counter = 0
    note_counter = 0
    brick_counter = 0 
    red_counter = 0
    orange_counter = 0
    stone_counter = 0
    plastic_counter = 0
    minigame1_counter = 0
    done_game1_counter = 0
    yellow_counter = 0
    green_counter = 0 
    mint_counter = 0
    blue_counter = 0
    teal_counter = 0
    indigo_counter = 0
    purple_counter = 0
    minigame2_counter = 0
    done_game2_counter = 0
    aqua_counter = 0
    coral_counter = 0
    cyan_counter = 0 
    olive_counter = 0 
    orchid_counter = 0
    pink_counter = 0
    violet_counter = 0
    gold_counter = 0
    minigame3_counter = 0
    done_game3_counter = 0
    ivory_counter = 0
    salmon_counter = 0
    khaki_counter = 0
    tan_counter = 0 
    maroon_counter = 0
    magenta_counter = 0
    lime_counter = 0

    text_speed = 1
    step = 0


    Introduction = True
    Search = False
    Note = False
    note_flipped = False
    note_words = False
    brick = False
    red = False
    orange = False
    stone = False
    plastic = False
    minigame1 = False
    done_game1 = False
    yellow = False
    green = False
    mint = False
    blue =  False
    teal = False
    indigo = False
    purple = False
    minigame2 = False
    done_game2 = False
    aqua = False
    coral = False
    cyan = False
    olive = False
    orchid = False
    pink = False
    violet = False
    gold = False
    minigame3 = False
    done_game3 = False
    ivory = False
    khaki = False
    salmon = False
    tan = False
    maroon = False
    magenta = False
    lime = False
    rose = False
    FINISH = False 

    running = True
    while running:

        for event in pygame.event.get():  # loops the events
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        stepon = Intro[step]
        if counter < text_speed * len(stepon):
            counter += 1
        elif counter >= text_speed * len(stepon):
            done = True

        

        if Introduction:
            basic_screen()
            draw_text(stepon[0:counter // text_speed], normal_font, "black", 20, 390)
            Introduction = True
            if next_button.draw(screen):
                counter = 0

                if step < len(Intro) - 1:
                    step += 1
                else:
                    Introduction = False
                    Search = True

        if Search == True:
            Introduction = False
            basic_screen()
            if search_button.draw(screen):
                Note = True

        if Note:
            Search = False
            basic_screen() 
            if note_flipped:
                screen.blit(back, (225, 120))
            else:
                screen.blit(note, (225, 120))


            draw_text(note_script[0][0:note_counter// text_speed], normal_font, "black", 20, 390)
            note_counter += 1

            if flip_button.draw(screen):
                note_flipped = not note_flipped
                note_words = True

        if note_words:
            if next_button2.draw(screen):
                Note = False
                basic_screen()
                brick = True
                

            
        if brick:
            note_words = False
            basic_screen()
            draw_text(brick_script[0][0:brick_counter // text_speed], normal_font, "black", 20, 390)
            brick_counter += 1
            if next_button2.draw(screen):
                red = True


        if red:
            brick = False
            basic_screen()
            draw_text(red_script[0][0:red_counter // text_speed], normal_font, "black", 20, 390)
            red_counter += 1
            if randomize_button.draw(screen):
                orange = True

        if orange:
            red = False
            basic_screen()
            draw_text(orange_script[0][0:orange_counter // text_speed], normal_font, "black", 20, 390)
            orange_counter += 1

            screen.blit(ladder, (150, 0))
            screen.blit(nuc_box,(220,165))
            draw_text((' '.join(str(DNA_seq))), DNA_font, "black", 275, 170)
            if next_button2.draw(screen): 
                stone = True

        if stone: 
            orange = False
            screen.blit(text_box,(0,375))
            draw_text(stone_script[0][0:stone_counter // text_speed], normal_font, "black", 20, 390)
            stone_counter += 1
            if next_button2.draw(screen):
                plastic = True

        if plastic: 
            stone = False
            screen.blit(text_box,(0,375))
            draw_text(plastic_script[0][0:plastic_counter // text_speed], normal_font, "black", 20, 390)
            plastic_counter += 1
            if next_button2.draw(screen):
                minigame1 = True


###########################################  MINI GAME ONE   ###################################################
        if minigame1: 
            plastic = False
            basic_screen()
            draw_text(minigame1_script[0][0:minigame1_counter // text_speed], normal_font, "black", 20, 390)
            minigame1_counter += 1
            if mg_button1.draw(screen):
                open_matching_file()
                done_game1 = True

        if done_game1:
            minigame1 = False
            screen.blit(text_box,(0,375))
            draw_text(done_game1_script[0][0:done_game1_counter // text_speed], normal_font, "black", 20, 390)
            done_game1_counter += 1
            if next_button.draw(screen):
                yellow = True

        
################################################################################################################
        


        if yellow: 
            done_game1 =  False
            basic_screen()
            screen.blit(ladder, (150, 0))
            screen.blit(nuc_box,(220,165))
            draw_text(str(' '.join(str(DNA_seq))), DNA_font, "black", 275, 170)
            
            draw_text(yellow_script[0][0:yellow_counter // text_speed], normal_font, "black", 20, 390)
            yellow_counter += 1
            if replicate_button.draw(screen):
                green = True 


        if green:
            yellow = False
            basic_screen()
            screen.blit(nuc_box,(220,165))
            screen.blit(ladder, (150, 0))
            draw_text((' '.join(str(DNA_seq))), DNA_font, "black", 275, 170)
            draw_text(green_script[0][0:green_counter // text_speed], normal_font, "black", 20, 390)
            green_counter += 1
            screen.blit(nuc_box,(220,265))
            draw_text((' '.join(str(comp_DNA))), DNA_font, "black", 275, 270)
            screen.blit(rep_ladder, (150,190))

            if next_button.draw(screen):
                mint = True

                #add all the special blue things 
                

        if mint: 
            green = False
            basic_screen()
            screen.blit(nuc_box,(220,165))
            screen.blit(ladder, (150, 0))
            draw_text((' '.join(str(DNA_seq))), DNA_font, "black", 275, 170)
            draw_text(mint_script[0][0:mint_counter // text_speed], normal_font, "black", 20, 390)
            mint_counter += 1
            screen.blit(nuc_box,(220,265))
            draw_text((' '.join(str(comp_DNA))), DNA_font, "black", 275, 270)
            screen.blit(rep_ladder, (150,190))
            if next_button.draw(screen):
                blue = True

        if blue: 
            mint = False
            basic_screen()
            screen.blit(nuc_box,(220,165))
            screen.blit(ladder, (150, 0))
            draw_text((' '.join(str(DNA_seq))), DNA_font, "black", 275, 170)
            draw_text(blue_script[0][0:blue_counter // text_speed], normal_font, "black", 20, 390)
            blue_counter += 1
            screen.blit(nuc_box,(220,265))
            draw_text((' '.join(str(comp_DNA))), DNA_font, "black", 275, 270)
            screen.blit(rep_ladder, (150,190))
            if next_button.draw(screen):
                teal = True

        if teal: 
            blue = False
            basic_screen()
            draw_text(teal_script[0][0:teal_counter // text_speed], normal_font, "black", 20, 390)
            teal_counter += 1
            screen.blit(nuc_box,(220,265))
            draw_text((' '.join(str(comp_DNA))), DNA_font, "black", 275, 270)
            screen.blit(rep_ladder, (150,190))
            if next_button.draw(screen):
                indigo = True

        if indigo: 
            teal = False
            basic_screen()
            draw_text(indigo_script[0][0:indigo_counter // text_speed], normal_font, "black", 20, 390)
            indigo_counter += 1
            screen.blit(nuc_box,(220,265))
            draw_text((' '.join(str(comp_DNA))), DNA_font, "black", 275, 270)
            screen.blit(rep_ladder, (150,190))
            if next_button.draw(screen):
                purple = True


        if purple: 
            indigo = False
            basic_screen()
            screen.blit(RNApro_tip, (-17, 180))
            draw_text(purple_script[0][0:purple_counter // text_speed], normal_font, "black", 20, 390)
            purple_counter += 1
            screen.blit(nuc_box,(220,265))
            draw_text((' '.join(str(comp_DNA))), DNA_font, "black", 275, 270)
            screen.blit(rep_ladder, (150,190))
            if next_button.draw(screen):
               minigame2 = True

###########################################  MINI GAME TWO   ###################################################
        if minigame2: 
            purple = False
            basic_screen()
            draw_text(minigame2_script[0][0:minigame2_counter // text_speed], normal_font, "black", 20, 390)
            minigame2_counter += 1
            if mg_button1.draw(screen):
                open_dots_file()
                done_game2 = True

        if done_game2:
            minigame2 = False
            screen.blit(text_box,(0,375))
            draw_text(done_game2_script[0][0:done_game2_counter // text_speed], normal_font, "black", 20, 390)
            done_game2_counter += 1
            if next_button.draw(screen):
                aqua = True
################################################################################################################

        if aqua: 
            done_game2 = False
            basic_screen()
            draw_text(aqua_script[0][0:aqua_counter // text_speed], normal_font, "black", 20, 390)
            aqua_counter += 1
            screen.blit(nuc_box,(220,265))
            draw_text((' '.join(str(comp_DNA))), DNA_font, "black", 275, 270)
            screen.blit(rep_ladder, (150,190))
            if transcribe_button.draw(screen):
               coral = True


        if coral: 
            aqua = False
            basic_screen()
            draw_text(coral_script[0][0:coral_counter // text_speed], normal_font, "black", 20, 390)
            coral_counter += 1
            draw_text("RNA", normal_font, "white",115, 170)
            screen.blit(RNA_box,(220,165))
            screen.blit(ladder, (150, 0))
            draw_text((' '.join(str(RNA_seq))), DNA_font, "black", 275, 170)
            screen.blit(nuc_box,(220,265))
            draw_text((' '.join(str(comp_DNA))), DNA_font, "black", 275, 270)
            screen.blit(rep_ladder, (150,190))
            if next_button2.draw(screen):
               cyan = True



        if cyan: 
            coral = False
            basic_screen()
            draw_text(cyan_script[0][0:cyan_counter // text_speed], normal_font, "black", 20, 390)
            cyan_counter += 1
            draw_text("RNA", normal_font, "white",115, 170)
            screen.blit(RNA_box,(220,165))
            screen.blit(ladder, (150, 0))
            draw_text((' '.join(str(RNA_seq))), DNA_font, "black", 275, 170)
            screen.blit(nuc_box,(220,265))
            draw_text((' '.join(str(comp_DNA))), DNA_font, "black", 275, 270)
            screen.blit(rep_ladder, (150,190))
            if next_button.draw(screen):
               olive =True
               

        
        if olive: 
            cyan = False
            basic_screen()
            draw_text(olive_script[0][0:olive_counter // text_speed], normal_font, "black", 20, 390)
            olive_counter += 1
            draw_text("RNA", normal_font, "white",115, 170)
            screen.blit(RNA_box,(220,165))
            screen.blit(ladder, (150, 0))
            draw_text((' '.join(str(RNA_seq))), DNA_font, "black", 275, 170)
            screen.blit(nuc_box,(220,265))
            draw_text((' '.join(str(comp_DNA))), DNA_font, "black", 275, 270)
            screen.blit(rep_ladder, (150,190))
            if next_button.draw(screen):
               orchid =True


        if orchid: 
            olive = False
            basic_screen()
            draw_text(orchid_script[0][0:orchid_counter // text_speed], normal_font, "black", 20, 390)
            orchid_counter += 1
            draw_text("RNA", normal_font, "white",115, 170)
            screen.blit(RNA_box,(220,165))
            screen.blit(ladder, (150, 0))
            draw_text((' '.join(str(RNA_seq))), DNA_font, "black", 275, 170)
            if next_button2.draw(screen):
               pink = True
               print(DNA_seq) #Just checking to make sure info good
               print(comp_DNA)
               print(RNA_seq)


        if pink: 
            orchid = False
            basic_screen()
            screen.blit(Proteinpro_tip, (0, 180))
            draw_text(pink_script[0][0:pink_counter // text_speed], normal_font, "black", 20, 390)
            pink_counter += 1
            draw_text("RNA", normal_font, "white",115, 170)
            screen.blit(RNA_box,(220,165))
            screen.blit(ladder, (150, 0))
            draw_text((' '.join(str(RNA_seq))), DNA_font, "black", 275, 170)
            if next_button2.draw(screen):
                violet = True

        if violet:
            pink = False
            basic_screen()
            screen.blit(Proteinpro_tip, (0, 180))
            draw_text(violet_script[0][0:violet_counter // text_speed], normal_font, "black", 20, 390)
            violet_counter += 1
            draw_text("RNA", normal_font, "white",115, 170)
            screen.blit(RNA_box,(220,165))
            screen.blit(ladder, (150, 0))
            draw_text((' '.join(str(RNA_seq))), DNA_font, "black", 275, 170)
            if next_button2.draw(screen):
                gold = True

        if gold:
            violet = False
            basic_screen()
            screen.blit(Proteinpro_tip, (0, 180))
            draw_text(gold_script[0][0:gold_counter // text_speed], normal_font, "black", 20, 390)
            gold_counter += 1
            draw_text("RNA", normal_font, "white",115, 170)
            screen.blit(RNA_box,(220,165))
            screen.blit(ladder, (150, 0))
            draw_text((' '.join(str(RNA_seq))), DNA_font, "black", 275, 170)
            if next_button2.draw(screen):
                minigame3 = True


###########################################  MINI GAME THREE   ##################################################
        if minigame3: 
            gold = False
            basic_screen()
            draw_text(minigame3_script[0][0:minigame3_counter // text_speed], normal_font, "black", 20, 390)
            minigame3_counter += 1
            if mg_button1.draw(screen):
                open_snake_file()
                done_game3 = True

        if done_game3:
            minigame3 = False
            screen.blit(text_box,(0,375))
            draw_text(done_game3_script[0][0:done_game3_counter // text_speed], normal_font, "black", 20, 390)
            done_game3_counter += 1
            if next_button2.draw(screen):
                ivory = True
        
################################################################################################################
            
        if ivory:
            done_game3 = False
            basic_screen()
            screen.blit(Proteinpro_tip, (0, 180))
            draw_text(ivory_script[0][0:ivory_counter // text_speed], normal_font, "black", 20, 390)
            ivory_counter += 1
            draw_text("RNA", normal_font, "white",115, 170)
            screen.blit(RNA_box,(220,165))
            screen.blit(ladder, (150, 0))
            draw_text((' '.join(str(RNA_seq))), DNA_font, "black", 275, 170)
            if next_button2.draw(screen):
                salmon = True

        if salmon:
            ivory = False
            basic_screen()
            screen.blit(Proteinpro_tip, (0, 180))
            draw_text(salmon_script[0][0:salmon_counter // text_speed], normal_font, "black", 20, 390)
            salmon_counter += 1
            draw_text("RNA", normal_font, "white",115, 170)
            screen.blit(RNA_box,(220,165))
            screen.blit(ladder, (150, 0))
            draw_text((' '.join(str(RNA_seq))), DNA_font, "black", 275, 170)
            if translate_button.draw(screen):
                khaki = True

        if khaki:
            salmon = False
            basic_screen()
            draw_text(khaki_script[0][0:khaki_counter // text_speed], normal_font, "black", 20, 390)
            khaki_counter += 1
            draw_text("RNA", normal_font, "white",115, 170)
            screen.blit(RNA_box,(220,165))
            screen.blit(ladder, (150, 0))
            screen.blit(line, (180, 150))
            draw_text((' '.join(str(RNA_seq))), DNA_font, "black", 275, 170)
            x = 170
            for nucleotide in str(poly_chain):
                screen.blit(amino_acids[nucleotide], (x, 150))
                x += 150
            if next_button2.draw(screen):
                tan = True
                
        if tan: 
            khaki = False
            basic_screen()
            draw_text(tan_script[0][0:tan_counter // text_speed], normal_font, "black", 20, 390)
            tan_counter += 1
            draw_text("RNA", normal_font, "white",115, 170)
            screen.blit(RNA_box,(220,165))
            screen.blit(ladder, (150, 0))
            draw_text((' '.join(str(RNA_seq))), DNA_font, "black", 275, 170)
            screen.blit(line, (180, 150))
            x = 170
            for nucleotide in str(poly_chain):
                screen.blit(amino_acids[nucleotide], (x, 150))
                x += 150
            if next_button2.draw(screen):
                maroon = True

        if maroon: 
            tan = False
            basic_screen()
            draw_text(maroon_script[0][0:maroon_counter // text_speed], normal_font, "black", 20, 390)
            maroon_counter += 1
            screen.blit(line, (180, 150))
            x = 170
            for nucleotide in str(poly_chain):
                screen.blit(amino_acids[nucleotide], (x, 150))
                x += 150
            if next_button2.draw(screen):
                magenta = True

        if magenta: 
            maroon = False
            basic_screen()
            draw_text(magenta_script[0][0:magenta_counter // text_speed], normal_font, "black", 20, 390)
            magenta_counter += 1
            screen.blit(line, (180, 150))
            x = 170
            for nucleotide in str(poly_chain):
                screen.blit(amino_acids[nucleotide], (x, 150))
                x += 150
            if next_button2.draw(screen):
                lime = True

        if lime: 
            magenta = False
            basic_screen()
            draw_text(lime_script[0][0:lime_counter // text_speed], normal_font, "black", 20, 390)
            lime_counter += 1
            screen.blit(stop, (550, 100))
            screen.blit(line, (180, 150))
            x = 170
            for nucleotide in str(poly_chain):
                screen.blit(amino_acids[nucleotide], (x, 150))
                x += 150
            if next_button2.draw(screen):
                rose = True


        if rose: 
            lime = False
            screen.blit(dungeon,(0,0))
            screen.blit(box, (175,28))
            screen.blit(title_box, (180, 33))
            screen.blit(title, (200, 47))
            if escape_button.draw(screen):
                FINISH = True
                pygame.mixer.music.load('music\\savfk-short-but-strong.mp3')
                pygame.mixer.music.play(loops=20, start=0.0, fade_ms=0)
                pygame.mixer.music.set_volume(0.75) 

        if FINISH:
            rose = False
            

            screen.blit(dungeon,(0,0))
            screen.blit(finish_note,(100,0))
            if credits_button.draw(screen):
                credits()
                print("this works")


                


        
                

        pygame.display.flip()
        clock.tick(60)



starter_screen()
import pygame as pg
import sys
import random


def place_box():
    screen.blit(letter_box, (index * 110 + 290, 330))


pg.init()
screen = pg.display.set_mode((1400, 730))
clock = pg.time.Clock()

questions = ["1- Hamur kızartması",
             "2- Yaprakları salata olarak yenen baharlı bir bitki",
             "3- Bir emek sonucu ortaya konulan ürün, eser",
             "4- Futboldaki canlı barikat",
             "5- Kısa süreli, beklenmedik saldırı",
             "6- Halk ağzında küçük sıvı püskürteçlerine verilen ad",
             "7- Kandaki alkol miktarını gösteren birim",
             "8- Yıkanma, tıraş olma, giyinme, süslenme işi.",
             "9- sesi büyütüp, yükseltip uzaklara ileten koni biçiminde aygıt.",
             "10- Hıristiyan olmayan toplumlarda bu dini yaymaya çalışan kimse.",
             "11- Endüstri Mühendisliği'nin en önemli alanlarından , ... araştırması",
             "12- Aralarında ya da parçaları arasında bakışım bulunan",
             "13- Yayılı aletler, bisiklet, araba parçaları, araba tekerliği ve aksamı",
             "14- X Y düzlemi, iki şerli 6 tane rakam, küp çizimi, dünya çizimi",
             "15- boyları 1 milimetreyle 1 metre arasında değişen elektromanyetik salınım",
             "16- Belirsizlik ilkesi'ni öne süren Alman Fizikçi", "OYUN BİTTİ"]
answers = ["PİŞİ", "TERE", "YAPIT", "BARAJ", "BASKIN", "FISFIS", "PROMİL", "TUVALET", "MEGAFON", "MİSYONER",
           "YÖNEYLEM", "SİMETRİK", "AMARTİSÖR", "KOORDİNAT", "MİKRODALGA", "HEİSENBERG", ""]

bg_surface = pg.image.load("Objects/background.png").convert_alpha()
letter_box = pg.image.load("Objects/letter_box.png")

question_index = -1
game_font = pg.font.Font(None, 45)
place_boxes = False
show_letter = False

shown_letter_index = []
word_surfaces = []
letter_rects = []

word_surfaces2 = []
letter_rects2 = []

score = 0
letters_not_shown = 0
letters_shown = 0

show_answer = False



# Game Loop
while True:
    irl_time = pg.time.get_ticks()
    screen.blit(bg_surface, (0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                question_index += 1
                place_boxes = True
                shown_letter_index = []
                word_surfaces = []
                letter_rects = []
                score += (100 * letters_not_shown)
                letters_shown = 0
                word_surfaces2 = []
                letter_rects2 = []
                show_answer = False
            if event.key == pg.K_SPACE:
                show_letter = True
            if event.key == pg.K_RSHIFT:
                show_answer = True

    if place_boxes:
        for index in range(len(answers[question_index])):
            place_box()
        question_surface = game_font.render(questions[question_index], True, (255, 255, 255))
        question_rect = question_surface.get_rect(topleft=(250, 550))
        screen.blit(question_surface, question_rect)

    if not show_letter:
        letters_not_shown = len(answers[question_index]) - letters_shown

    if show_letter:
        letter_place = "a"
        possible_letter = True
        letters_not_shown = len(answers[question_index]) - letters_shown
        while possible_letter:
            if len(shown_letter_index) != len(answers[question_index]):
                letter_place = random.randint(0, len(answers[question_index]) - 1)
                if not letter_place in shown_letter_index:
                    shown_letter_index.append(letter_place)
                    possible_letter = False
                    letters_shown += 1
            if len(shown_letter_index) == len(answers[question_index]):
                letters_not_shown = 0
                show_letter = False
        for i in shown_letter_index:
            word = pg.font.Font(None, 100)
            word_surface = word.render(answers[question_index][i], True, (0, 0, 0))
            word_surfaces.append(word_surface)
            letter_rect = word_surface.get_rect(center=(i * 110 + 345, 395))
            letter_rects.append(letter_rect)
        show_letter = False

    for j in range(len(letter_rects)):
        screen.blit(word_surfaces[j], letter_rects[j])

    BLACK = (0, 0, 0)
    counter_font = pg.font.Font(None, 65)
    decrement_from_counter = irl_time
    if 0 <= decrement_from_counter < 60000:
        minutes = f'4:{59 - int((decrement_from_counter / 1000))}'
        counter_surface = counter_font.render(str(minutes), True, BLACK)
    if 60000 <= decrement_from_counter < 120000:
        minutes = f'3:{119 - int((decrement_from_counter / 1000))}'
        counter_surface = counter_font.render(str(minutes), True, BLACK)
    if 120000 <= decrement_from_counter < 180000:
        minutes = f'2:{179 - int((decrement_from_counter / 1000))}'
        counter_surface = counter_font.render(str(minutes), True, BLACK)
    if 180000 <= decrement_from_counter < 240000:
        minutes = f'1:{239 - int((decrement_from_counter / 1000))}'
        counter_surface = counter_font.render(str(minutes), True, BLACK)
    if 240000 <= decrement_from_counter < 300000:
        minutes = f'0:{299 - int((decrement_from_counter / 1000))}'
        counter_surface = counter_font.render(str(minutes), True, BLACK)

    if show_answer:
        for i in range(len(answers[question_index])):
            word = pg.font.Font(None, 100)
            word_surface = word.render(answers[question_index][i], True, (0, 0, 0))
            word_surfaces2.append(word_surface)
            letter_rect = word_surface.get_rect(center=(i * 110 + 345, 395))
            letter_rects2.append(letter_rect)

        for j in range(len(answers[question_index])):
            screen.blit(word_surfaces2[j], letter_rects2[j])

    screen.blit(counter_surface, (250, 255))
    score_font = pg.font.Font(None, 75)
    score_surface = score_font.render(str(score), True, BLACK)
    screen.blit(score_surface, (250, 205))

    pg.display.update()
    clock.tick(60)

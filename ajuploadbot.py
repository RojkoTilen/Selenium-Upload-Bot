import os
from selenium import webdriver
import numpy as np
import json
from os import walk
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
import random
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import requests
from mutagen.mp3 import MP3
import datetime

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://audiojungle.net/")

time.sleep(15)

wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tlp-header-user-nav"]/div/a'))).click()
time.sleep(15)
username = driver.find_element_by_id('username')
username.send_keys("UPORABNIŠKO IME")
password = driver.find_element_by_id('password')
password.send_keys("GESLO")

wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="sso-forms__submit"]'))).click()
time.sleep(15)

wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="tlp-header-user-nav"]/div/a'))).click()
time.sleep(19)
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="tlp-header-user-nav"]/div/div/div/ul/div[1]/li[2]/a'))).click()
time.sleep(15)
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="content"]/div[1]/section/div/div[2]/div/ul/li[1]/a'))).click()
time.sleep(15)


def get_immediate_subdirectories_wpath(a_dir):
    c = [f.path for f in os.scandir(a_dir) if f.is_dir()]
    return c


def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


def get_list_of_file_paths(dir_with_path):
    f = []
    mp3_dict = {}
    file_paths = {"logo_path": "D:\\Ony Music\\onylogo.jpg"}
    for (dirpath, dirnames, filenames) in walk(dir_with_path):
        f.extend(filenames)
        break
    for name in f:
        if ".zip" in name.lower():
            file_name = dir_with_path + "\\" + name
            file_paths["zip_path"] = file_name
        elif "watermark" in name.lower():
            file_name = dir_with_path + "\\" + name
            file_paths["watermark_path"] = file_name
        elif ".txt" in name.lower():
            bpm = name.split(".", 1)[0]
            file_paths["bpm"] = bpm
        elif (".mp3" in name.lower()) and ("watermark" not in name.lower()):
            file_name = dir_with_path + "\\" + name
            mp3_dict[name] = file_name
    file_paths["mp3_path_dict"] = mp3_dict
    return file_paths


def get_title(name):
    title = name.split("(", 1)[0]
    return title


def get_mp3_lengths(mp3_dict):
    length_dict = {}

    for key in mp3_dict:
        audio = MP3(mp3_dict[key])
        audio_time_string = str(datetime.timedelta(seconds=int(audio.info.length)))
        split_str1 = audio_time_string.split("0")

        formated_audio_time = "0".join(split_str1[2:])

        split_str1 = key.split(".")
        key_formated = ".".join(split_str1[:1])

        length_dict[key_formated] = formated_audio_time

    return length_dict


def get_description(file_name, mp3_dict):
    length_dict = get_mp3_lengths(mp3_dict)
    desc_tags_dict = {}

    if "future bass" in file_name.lower() or "dubstep" in file_name.lower():
        mp3_len_string = """"""
        rising_star_desc = """
Stylish future bass music. Perfect for showreel, vlog, podcast, youtube video.
        """

        for key in length_dict:
            mp3_len_string = mp3_len_string + "\n <br>" + key + " " + length_dict[key]

        desc_tags_dict["description"] = """<strong> Future Bass Music </strong> <br>
<a href="https://bit.ly/3oZsFFe">
<img src="https://i.imgur.com/SNW3AsP.png"> <br>""" + rising_star_desc + mp3_len_string

        desc_tags_dict["tags"] = """action, advertising, aggressive, background, bass, bright, commercial, dance, dubstep, dynamic, edm, electronic, energetic, energy, extreme, fashion, future, future bass, modern, motivational, party, pop, positive, power, powerful, presentation, sport, summer, upbeat, uplifting"""

        desc_tags_dict["category"] = "music/electronica/dubstep"

        return desc_tags_dict
    elif "technology" in file_name.lower() or "abstract" in file_name.lower() or "future" in file_name.lower():
        mp3_len_string = """"""

        rising_star_desc = """
A modern and stylish track for powerful presentations and productions. 
There a lot of found, organic, techno and future sounds and cinematic effects. 
This item is perfect for hi-tech, science, sport, action and motivation videos.
        """

        for key in length_dict:
            mp3_len_string = mp3_len_string + "\n <br>" + key + " " + length_dict[key]

        desc_tags_dict["description"] = """<strong> Technology Music </strong> <br>
<a href="http://bit.ly/2Wo5S9P">
<img src="https://i.imgur.com/rncxqCe.png"> <br>""" + rising_star_desc + mp3_len_string

        desc_tags_dict["tags"] = """advertising, background, beauty, business, commercial, confident, corporate, dynamic, fashion, groovy, high-tech, hopeful, innovate, inspiration, inspirational, inspiring, marketing, motivate, motivated, motivation, motivational, presentation, progress, promotional, soft, success, successful, technology, upbeat, uplifting  """

        desc_tags_dict["category"] = "music/experimental-abstract"

        return desc_tags_dict
    elif "electro" in file_name.lower() or "cyberpunk" in file_name.lower():
        mp3_len_string = """"""
        rising_star_desc = """
A powerful, electronic theme with edgy hybrid synths, acid bass and punchy beats, perfect for extreme sports, action, workout or video games.
        """

        for key in length_dict:
            mp3_len_string = mp3_len_string + "\n <br>" + key + " " + length_dict[key]

        desc_tags_dict["description"] = """<strong> Cyberpunk Techno Music </strong> <br>
<a href="https://bit.ly/3oZsFFe">
<img src="https://i.imgur.com/SNW3AsP.png"> <br>""" + rising_star_desc + mp3_len_string

        desc_tags_dict["tags"] = """80s, action, aggressive, background, cinematic, commercial, cyberpunk, dark, electronic, energetic, energy, epic, extreme, film, future, futuristic, game, industrial, intense, modern, movie, powerful, retro, sci-fi, sport, stylish, synth, synthwave, technology, trailer"""

        desc_tags_dict["category"] = "music/electronica/hard-industrial"

        return desc_tags_dict
    elif "techno" in file_name.lower():
        mp3_len_string = """"""
        rising_star_desc = """
A powerful, electronic theme with edgy hybrid synths, acid bass and punchy beats, perfect for extreme sports, action, workout or video games.
        """

        for key in length_dict:
            mp3_len_string = mp3_len_string + "\n <br>" + key + " " + length_dict[key]

        desc_tags_dict["description"] = """<strong> Techno Music </strong> <br>
<a href="https://bit.ly/3oZsFFe">
<img src="https://i.imgur.com/SNW3AsP.png"> <br>""" + rising_star_desc + mp3_len_string

        desc_tags_dict["tags"] = """action, atmospheric, background, bass, club, commercial, dance, dark, deep, electronic, emotional, event, fashion, girls, groovy, house, marketing, minimal, model, modern, party, presentation, punchy, sex, sexual, sport, style, tech, techno, trendy"""

        desc_tags_dict["category"] = "music/electronica/techno"

        return desc_tags_dict
    elif "house" in file_name.lower():
        mp3_len_string = """"""
        rising_star_desc = """
Summer pop EDM and chill fashion house sound!
Music is perfect for Slideshow, Movie Trailers, Teasers, Intro, Games, Sports Video, Advertising and other commercial projects!
        """

        for key in length_dict:
            mp3_len_string = mp3_len_string + "\n <br>" + key + " " + length_dict[key]

        desc_tags_dict["description"] = """<strong> House Music </strong> <br>
<a href="https://bit.ly/3oZsFFe">
<img src="https://i.imgur.com/SNW3AsP.png"> <br>""" + rising_star_desc + mp3_len_string

        desc_tags_dict["tags"] = """advertising, background, bright, business, catchy, cheerful, commercial, cool, corporate, dance, edm, energetic, energy, fun, happy, inspirational, inspiring, joyful, modern, motivational, optimistic, party, pop, positive, radio, score, success, summer, upbeat, uplifting"""

        desc_tags_dict["category"] = "music/house"

        return desc_tags_dict
    elif "synthwave" in file_name.lower() or "80s" in file_name.lower():
        mp3_len_string = """"""
        rising_star_desc = """
        
This is a positive and energetic track in style of popular songs of the 80s featuring big punchy drums, vintage synths and guitar.
        """

        for key in length_dict:
            mp3_len_string = mp3_len_string + "\n <br>" + key + " " + length_dict[key]

        desc_tags_dict["description"] = """<strong> Synthwave Music </strong> <br>
<a href="https://bit.ly/3oZsFFe">
<img src="https://i.imgur.com/SNW3AsP.png"> <br>""" + rising_star_desc + mp3_len_string

        desc_tags_dict["tags"] = """80's, 80s, 80s pop, 80s synth pop, 80s synthpop, advertising, catchy, confident, dance, dreamwave, eighties, eighties pop, energy, fashion, fun, neon, new order, new wave, nostalgic, playful, pop, positive, retro, retrowave, soft cell, synth, synth pop, synthpop, synthwave, teen"""

        desc_tags_dict["category"] = "music/electronica"

        return desc_tags_dict
    elif "pop" in file_name.lower() or ("upbeat dance") in file_name.lower() or ("dance upbeat") in file_name.lower() or "dance" in file_name.lower() or "party" in file_name.lower():
        mp3_len_string = """"""
        rising_star_desc = """
Happy – happy and optimistic inspirational pop track.

Soft and motivational acoustic pop mood.

Best for – kids games, corporate projects, cheerful cartoon for children, driving and playful video, tv advertising, radio, films, viral marketing, web advertisements, movie trailers, business and travel videos, motivational presentations.
        """

        for key in length_dict:
            mp3_len_string = mp3_len_string + "\n <br>" + key + " " + length_dict[key]

        desc_tags_dict["description"] = """<strong> Pop Music </strong> <br>
<a href="https://bit.ly/3oWLY1T">
<img src="https://i.imgur.com/AZFTiDB.png"> <br>""" + rising_star_desc + mp3_len_string

        desc_tags_dict["tags"] = """advertising, background, bright, catchy, cheerful, commercial, corporate, dance, driving, energetic, exciting, feel good, fresh, fun, guitar, happy, indie, inspirational, inspiring, modern, motivational, optimistic, party, pop, positive, success, summer, travel, upbeat, uplifting"""

        desc_tags_dict["category"] = "music/pop"

        return desc_tags_dict
    elif "lofi" in file_name.lower() or "lo-fi" in file_name.lower() or "lo fi" in file_name.lower():
        mp3_len_string = """"""
        rising_star_desc = """
This positive lofi track in lofi style is perfect for urban, street, graffiti, lifestyle videos, extreme sports videos, videos about cars, sports highlights, fashion, travel and promotion videos, technology and gadget videos, video blogs and more.
        """

        for key in length_dict:
            mp3_len_string = mp3_len_string + "\n <br>" + key + " " + length_dict[key]

        desc_tags_dict["description"] = """<strong> Lofi Music </strong> <br>
<a href="http://bit.ly/3ms7l9P">
<img src="https://i.imgur.com/HXs43d6.png"> <br>""" + rising_star_desc + mp3_len_string

        desc_tags_dict["tags"] = """90s, advertising, background, blog, Boom Bap, cooking, cute, fashion, food, hip-hop, instrumental, laid back, mellow, melodic, memorable, modern, pleasure, radio, rap, soft, summer, travel, underground, uplifting, urban, vlog, warm, young, youth"""

        desc_tags_dict["category"] = "music/hip-hop"

        return desc_tags_dict
    elif "trap" in file_name.lower():
        mp3_len_string = """"""
        rising_star_desc = """
Action, powerful and energy stylish trap with cello, brass, bass, vocal, beatbox, synth, strong beat, fx.

Mood: fashionable, aggressive.

Perfect for: advertising, presentation, promo, commercial, sports, extreme, intro, urban, opener, sport vlogs, cluv, event.
        """

        for key in length_dict:
            mp3_len_string = mp3_len_string + "\n <br>" + key + " " + length_dict[key]

        desc_tags_dict["description"] = """<strong> Trap Music </strong> <br>
<a href="http://bit.ly/3ms7l9P">
<img src="https://i.imgur.com/HXs43d6.png"> <br>""" + rising_star_desc + mp3_len_string

        desc_tags_dict["tags"] = """action, advertising, aggressive, background, bass, cars, cello, energy, event, extreme, fashion, fashionable, fighting, ghetto, girls, gym, hip-hop, hiphop, intro, moto, powerful, rap, sport, street, stylish, trap, trendy, urban, vlog, workout"""

        desc_tags_dict["category"] = "music/hip-hop"

        return desc_tags_dict
    elif "hip hop" in file_name.lower() or "hip-hop" in file_name.lower() or "hip" in file_name.lower() or "hop" in file_name.lower() or "hiphop" in file_name.lower():
        mp3_len_string = """"""
        rising_star_desc = """
This positive Hip Hop track in Boom Bap style is perfect for urban, street, graffiti, lifestyle videos, extreme sports videos, videos about cars, sports highlights, fashion, travel and promotion videos, technology and gadget videos, video blogs and more.
        """

        for key in length_dict:
            mp3_len_string = mp3_len_string + "\n <br>" + key + " " + length_dict[key]

        desc_tags_dict["description"] = """<strong> Hip Hop Music </strong> <br>
<a href="http://bit.ly/3ms7l9P">
<img src="https://i.imgur.com/HXs43d6.png"> <br>""" + rising_star_desc + mp3_len_string

        desc_tags_dict["tags"] = """90s, advertising, background, blog, Boom Bap, cooking, cute, fashion, food, hip-hop, instrumental, laid back, mellow, melodic, memorable, modern, pleasure, radio, rap, soft, summer, travel, underground, uplifting, urban, vlog, warm, young, youth"""

        desc_tags_dict["category"] = "music/hip-hop"

        return desc_tags_dict
    elif "percussion" in file_name.lower() or "stomp" in file_name.lower() or "drums" in file_name.lower():
        mp3_len_string = """"""
        rising_star_desc = """
Energetic and dynamic action percussion track. Energy, catchy and addictive percussion track contains strong kick, foot stomps, hand claps and finger snaps and other percussion instruments. 
Suitable for Fast video, tutorial video, vlog, film, series, presentation, promotion video, promo, games, intro, logo or any other commercial project.        
        """

        for key in length_dict:
            mp3_len_string = mp3_len_string + "\n <br>" + key + " " + length_dict[key]

        desc_tags_dict["description"] = """<strong> Percussion Music </strong> <br>
<a href="https://bit.ly/34hks7m">
<img src="https://i.imgur.com/7mdhAEC.png"> <br>""" + rising_star_desc + mp3_len_string

        desc_tags_dict["tags"] = """action, advertising, background, cinematic, clap, clapping, claps, drums, dynamic, energetic, energy, fast, finger snaps, intro, kick, modern, opener, percussion, powerful, rhythm, rhythmic, slap, snap, sport, stomp, stomping, stomps, strong, trailer, upbeat"""

        desc_tags_dict["category"] = "music/percussion/traditional"

        return desc_tags_dict
    elif "corporate" in file_name.lower() or ("corporate" and "ambient") in file_name.lower():
        mp3_len_string = """"""
        rising_star_desc = """
Upbeat corporate background music with a positive, uplifting and inspiring mood.
        """

        for key in length_dict:
            mp3_len_string = mp3_len_string + "\n <br>" + key + " " + length_dict[key]

        desc_tags_dict["description"] = """<strong> Corporate Music </strong> <br>
<a href="http://bit.ly/3h0fIbx">
<img src="https://i.imgur.com/l7p7N8b.png"> <br>""" + rising_star_desc + mp3_len_string

        desc_tags_dict["tags"] = """advertising, background, background music, beauty, business, commercial, corporate, driving, energizing, engaging, explainer, gentle, inspirational, inspiring, marketing, medical, motivational, opener, optimistic, piano, positive, presentation, science, smooth, soft, sophisticated, tutorial, uplifting, uplifting music, warm"""

        desc_tags_dict["category"] = "music/corporate/motivational"

        return desc_tags_dict
    elif "ambient" in file_name.lower() or "documentaries" in file_name.lower() or "documentary" in file_name.lower():
        mp3_len_string = """"""
        rising_star_desc = """
Upbeat ambient background music with a positive, uplifting and inspiring mood.
        """

        for key in length_dict:
            mp3_len_string = mp3_len_string + "\n <br>" + key + " " + length_dict[key]

        desc_tags_dict["description"] = """<strong> Documentary Music </strong> <br>
<a href="http://bit.ly/3h0fIbx">
<img src="https://i.imgur.com/l7p7N8b.png"> <br>""" + rising_star_desc + mp3_len_string

        desc_tags_dict["tags"] = """advertising, background, background music, beauty, business, commercial, corporate, driving, energizing, engaging, explainer, gentle, inspirational, inspiring, marketing, medical, motivational, opener, optimistic, piano, positive, presentation, science, smooth, soft, sophisticated, tutorial, uplifting, uplifting music, warm"""

        desc_tags_dict["category"] = "music/ambient"

        return desc_tags_dict
    elif "funk" in file_name.lower() or "funky" in file_name.lower() or "groove" in file_name.lower() or "jazz" in file_name.lower() or "groovy" in file_name.lower():
        mp3_len_string = """"""
        rising_star_desc = """
Upbeat ambient background music with a positive, uplifting and inspiring mood.
         """

        for key in length_dict:
            mp3_len_string = mp3_len_string + "\n <br>" + key + " " + length_dict[key]

        desc_tags_dict["description"] = """<strong> Documentary Music </strong> <br>
<a href="http://bit.ly/3h0fIbx">
<img src="https://i.imgur.com/l7p7N8b.png"> <br>""" + rising_star_desc + mp3_len_string

        desc_tags_dict["tags"] = """
advertising, background, background music, beauty, business, commercial, corporate, driving, energizing, engaging, explainer, gentle, inspirational, inspiring, marketing, medical, motivational, opener, optimistic, piano, positive, presentation, science, smooth, soft, sophisticated, tutorial, uplifting, uplifting music, warm
        """

        desc_tags_dict["category"] = "music/funk-groove"


        return """<strong> Documentary Music </strong> <br>
<a href="http://bit.ly/3h0fIbx">
<img src="https://i.imgur.com/l7p7N8b.png"> <br>""" + rising_star_desc + mp3_len_string
    elif "rock" in file_name.lower() or "indie rock" in file_name.lower():
        mp3_len_string = """"""
        rising_star_desc = """
energetic, driving and upbeat action sport rock track.
        """

        for key in length_dict:
            mp3_len_string = mp3_len_string + "\n <br>" + key + " " + length_dict[key]

        desc_tags_dict["description"] = """<strong> Rock Music </strong> <br>
<a href="http://bit.ly/3h0fIbx">
<img src="https://i.imgur.com/l7p7N8b.png"> <br>""" + rising_star_desc + mp3_len_string

        desc_tags_dict["tags"] = """
action, advertising, background, bright, catchy, clap, commercial, cool, driving, drums, electric guitar, energetic, fun, guitar, happy, hey, indie, inspiring, intro, modern, motivational, positive, powerful, rock, sport, stomp, trailer, upbeat, uplifting
        """

        desc_tags_dict["category"] = "music/rock/indie-rock"

        return desc_tags_dict
    elif "cinematic" in file_name.lower() or "epic" in file_name.lower() or "trailer" in file_name.lower():
        mp3_len_string = """"""
        rising_star_desc = """
Epic inspiring and motivational cinematic track.

Perfect for films, trailers, advertising and other projects."""

        for key in length_dict:
            mp3_len_string = mp3_len_string + "\n <br>" + key + " " + length_dict[key]

        desc_tags_dict["description"] = """<strong> Cinematic Music </strong> <br>
<a href="https://bit.ly/3zqCYJ9">
<img src="https://i.imgur.com/HiMOyQ3.png"> <br>""" + rising_star_desc + mp3_len_string

        desc_tags_dict["tags"] = """action, adventure, background, blockbuster, brass, brave, cinematic, dramatic, electric guitar, energetic, epic, epic music, film, heroic, hollywood, inspiration, intense, motivational, movie, orchestral, piano, powerful, soundtrack, strings, teaser, titles, trailer, uplifting, war"""

        desc_tags_dict["category"] = "music/cinematic"

        return desc_tags_dict
    else:
        return False


dir_with_path = get_immediate_subdirectories_wpath("C:\\Ony Music Bots\\ajbot\\ajuploadbot\\Ony Music")
print(dir_with_path)

dir_names = get_immediate_subdirectories("C:\\Ony Music Bots\\ajbot\\ajuploadbot\\Ony Music")
print("dir_names")
print(dir_names)

for n in range(0, len(dir_with_path)):
    file_paths = get_list_of_file_paths(dir_with_path[n])

    print("WATERMARK PATH")
    print(file_paths["watermark_path"])

    print("ZIP PATH")
    print(file_paths["zip_path"])

    print("LOGO PATH")
    print(file_paths["logo_path"])

    print("BPM")
    print(file_paths["bpm"])

    print("MP3s PATH")
    print(file_paths["mp3_path_dict"])

    title_string = get_title(list(file_paths["mp3_path_dict"].keys())[0])

    print("TITLE")
    print(title_string)

    description_tags_category = get_description(title_string, file_paths["mp3_path_dict"])

    tracks_to_handle = []

    if not description_tags_category:
        option2 = """
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="begin-upload"]/div/div/button'))).click()
        time.sleep(5)
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/header/div[1]/div/div/nav/ul/li[5]/div/div/ul/li[8]/a'))).click()
        tracks_to_handle.append(title_string)
        """
        tracks_to_handle.append(title_string)
        print(tracks_to_handle)
        time.sleep(5)
        continue

    print("DESCRIPTION")
    print(description_tags_category["description"])

    print("TAGS")
    print(description_tags_category["tags"])

    print("MP3s")
    mp3_lenghts = get_mp3_lengths(file_paths["mp3_path_dict"])
    print(get_mp3_lengths(file_paths["mp3_path_dict"]))


    select = Select(driver.find_element_by_id('type'))
    time.sleep(5)

    select.select_by_value('music')

    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="begin-upload"]/div/div/button'))).click()
    time.sleep(10)

    title = driver.find_element_by_id('name')
    title.send_keys(title_string)
    time.sleep(10)

    description = driver.find_element_by_id('description')
    description.send_keys(description_tags_category["description"])
    time.sleep(5)


    driver.find_element_by_name('file-input').send_keys(file_paths["logo_path"])
    time.sleep(20)

    driver.find_element_by_name('file-input').send_keys(file_paths["zip_path"])
    time.sleep(20)

    driver.find_element_by_name('file-input').send_keys(file_paths["watermark_path"])
    time.sleep(120)

    select = Select(driver.find_element_by_id('temporary_files_to_assign_thumbnail'))
    time.sleep(5)

    select.select_by_index(1)

    select = Select(driver.find_element_by_id('temporary_files_to_assign_audio_mp3_preview'))
    time.sleep(5)

    select.select_by_index(2)

    select = Select(driver.find_element_by_id('temporary_files_to_assign_source'))
    time.sleep(5)

    select.select_by_index(3)

    select = Select(driver.find_element_by_id('category'))
    time.sleep(5)

    select.select_by_value(description_tags_category["category"])

    myElemA = driver.find_element_by_css_selector('#item_item_attributes_attributes_1_multiple_select_value option[value="MP3"]')
    myElemB = driver.find_element_by_css_selector('#item_item_attributes_attributes_1_multiple_select_value option[value="WAV"]')

    ActionChains(driver).key_down(Keys.SHIFT).click(myElemA).send_keys(Keys.DOWN).key_up(Keys.SHIFT).send_keys(Keys.ENTER).perform()

    time.sleep(10)  # Pause to allow you to inspect the browser.

    time.sleep(5)

    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="item_item_attributes_attributes_2_multiple_select_value"]/option[5]'))).click()
    time.sleep(5)

    for key in mp3_lenghts:
        title = driver.find_element_by_id('item_item_attributes_attributes_5_text_value')
        title.send_keys(mp3_lenghts[key])
        time.sleep(10)
        break


    additional_tracks_string = ""
    i = 0
    for key in mp3_lenghts:
        if i != 0:
            additional_tracks_string = additional_tracks_string + ", " + mp3_lenghts[key]
            ++i

    time.sleep(10)

    print(additional_tracks_string)

    title = driver.find_element_by_id('item_item_attributes_attributes_6_text_value')
    title.send_keys(additional_tracks_string)
    time.sleep(10)

    title = driver.find_element_by_id('item_item_attributes_attributes_7_text_value')
    title.send_keys("Ony Music")
    time.sleep(10)

    title = driver.find_element_by_id('item_item_attributes_attributes_9_text_value')
    title.send_keys(file_paths["bpm"])
    time.sleep(10)

    title = driver.find_element_by_id('tags_default')
    title.send_keys(description_tags_category["tags"])
    time.sleep(10)

    price = driver.find_element_by_id("music_standard-price")
    price.clear()
    price.send_keys("3")
    time.sleep(3)

    price = driver.find_element_by_id("music_broadcast_one_million-price")
    price.clear()
    price.send_keys("191")
    time.sleep(3)

    price = driver.find_element_by_id("music_mass_reproduction-price")
    price.clear()
    price.send_keys("383")
    time.sleep(3)

    price = driver.find_element_by_id("music_broadcast_ten_million-price")
    price.clear()
    price.send_keys("667")
    time.sleep(3)

    price = driver.find_element_by_id("music_broadcast_and_film-price")
    price.clear()
    price.send_keys("835")
    time.sleep(3)

    wait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'got_proper_licenses'))).click()
    time.sleep(5)

    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="new_item"]/div[7]/div[3]/button'))).click()
    time.sleep(5)


















driver.quit()


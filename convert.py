def convert_to_yaml():
    input_text = """Chaya Czernowin, composer, Walter Bigelow Rosen Professor of Music at Harvard University, Boston
Ruben Seroussi, composer, Professor, tel Aviv University Buchmann-Mehta School of music, Ramat Gan 
Hagar Kadima painter, lecturer emeritus Music Department, Levinsky College of Education Ramat Hasharon
Amnon Wolman composer and sound artist Jerusalem university Academy of music professor Northern Israel
Zohar Eitan musicologist professor, Poet Tel Aviv University  
Ilan Volkov - Herzliya , Brussels Philharmonic Principal Guest Conductor
Yuval Weinberg, Stuttgart Conductor, SWR Vocal Ensemble .
Dr. Uri Kochavi Composer
Ilya Ram - Germany, Conductor, Music Director Designate at Chattanooga Symphony & Opera and Music Director Akademische Philharmonie Heidelberg
Imri Talgam - Pianist, The Hague, Netherlands
Itay Talgam -Conductor and Speaker, Amsterdam, Netherlands
Meira Asher - North Israel , Interdisciplinary, sound and radio artist 
Ayelet Lerman - Composer and Violist
Ram Gabay -  Musician,Tel Aviv
Daniel Sarid - Pianist
Dr. Uri Agnon, Composer and Activist, the University of Southampton
Zohar Shafir - Musician,Tel Aviv
Shai Wosner - Pianist,New York
Ohad Fishof - Musician,Tel Aviv
Rotem Nir - Conductor ,Tel Aviv
Zvi Emanuel-Marial-Opera Singer,Berlin
Anat Nazarathy, flutist, Haifa
Dror Feiler  Composer, Musician, Activist  Stockholm, Sweden Spokesperson for JIPF (Jews for Israeli Palestinian Peace)  Chairman for EJJP (European Jews for a Just Peace)
Amit Dolberg  Tel Aviv Pianist, Ensemble Meitar director
Dr. Bnaya Halperin Kadari composer sound artist Berlin
Emmanuel Witzthum-Kibbutz Maale Hahamisha, Artistic Director at the Israeli Palestinian cultural house FeelBeit in Jerusalem and composer
Assaf Talmudi- Producer,Pianist and Composer, Israel
Dr. Eliav Kohl  Composer - Tel Aviv University
Aviv Mark - Musician,Tel-Aviv
Grisha Shakhnes - Musician,Holon
Sharon Kantor - Musician and Writer,Tel-Aviv
Yohana Chendler - Composer,Japan
Assaf Shatil - Pianist and Composer, Tel Aviv
Ilan Shay Ziblat - Composer,The Hague Netherlands
Yifeat Ziv - Sound Artist and Singer,Tel Aviv
Netta Spiegel - Artist, Conductor and Vocal Performer
Oded Geizhals - Percussionist and Composer,Cologne
Itzik Gil Avizohar - Sound Artist,Paris
Tom Soloveitzik - Sound Artist,Paris
Dr. Yair Klartag Composer, Jerusalem University, Tel Aviv
Dr. Yoni Niv. Tel Aviv-Jaffa. Senior Lecturer, Department of New Music. Musrara Art School, Jerusalem.
Dr, Yehuda Inbar Berlin  pianist 
Omri Abram Composer
Hed Bahack, Composer, Leipzig (Germany)
Ehu Dar-Shaashua Composer Basel
Omer Eilam Composer Berlin
Goni Peles, PhD candidate, Bath Spa University, UK Kiryat Ata
Tom Kellner - Musician,Academic, activist, Berlin
Or River- Musician,Tel-Aviv
Adaya Godlevsky - Musician, Tel Aviv
Oren Boneh - Composer, Brussels
Guy Ben-Ziony Viola, Professor. Robert Schumann Hochschule, Düsseldorf 
Alon Melncik- trumpet,Holon
Aviv Mark - Musician,Tel-Aviv
Ilan Barkani - Composer , Jerusalem 
Yohanan Chendler - Composer,Japan
Ruth Rosenthal - Musician,Paris
Sivan Magen - Harpist
Gil Luz - Musician,Tel Aviv
Amit Landau - Viola,Tel-Aviv
Assaf Gidron - Composer ,New York
Ilya Ram - Germany, Conductor, Music Director Designate at Chattanooga Symphony & Opera and Music Director Akademische Philharmonie Heidelberg
Alon Melnick trumpetist, Holon
Maya Felixbrot, musician, Amsterdam/Tel-Aviv
Maayan Franco -Conductor, Berlin
Maayan Tsadka -Haifa, Music faculty Haifa University and Musrara school of art and society
Ram Orion - Musician , Tel Aviv
Michael Seltenreich - Composer,New York
Rhona Brosch-Nyska -Trumpet player,Tel Aviv
Noa Haran, Composer, Haifa
Amit Biton, Composer and pianist, Haifa
Omer Barash, Composer, New York
Netta Shahar, Composer, reboot Neue musik Berlin
Eli Korman, Composer, Jerusalem
Eres Holz Composer, Berlin
Edo Frenkel, Conductor, Composer - Paris
Amit Gur, composer and researcher, Amsterdam
Dror Binder, Composer, Vienna
Gilad Cohen, composer, Associate Professor of Music and Music Convener, Ramapo College of New Jersey, USA
Tom Belkind, Composer, Cologne
Ronnie Reshef, Composer, The Jerusalem Academy of Music and Dance
Inbar Sharet, composer, Basel
Nir Cohen-Shalit, PhD. Conductor and Musicologist, Israel.
Shiri Riseman, composer, Graz
Kiki Keren-huss, composer, Jerusalem
Yuval Seeberger, composer, Belgium 
Michel mayer, Musician, Haifa
Amir Bolzman, sound artist, Jerusalem
Yonatan Ron, Composer, Seattle
Ofer Pelz, Composer, Montreal
Einav Yarden, Pianist, Berlin
Daniel Seroussi, Pianist, Berlin
Ruth Sgan-Cohen, Musician"""
    
    # Split into lines and remove empty lines
    lines = [line.strip() for line in input_text.split('\n') if line.strip()]
    
    yaml_output = "signatories:\n"
    
    for line in lines:
        # Split on first comma to separate name from description
        parts = line.split(',', 1)
        name = parts[0].strip()
        description = parts[1].strip() if len(parts) > 1 else ""
        
        yaml_output += f'  - name: "{name}"\n'
        yaml_output += f'    description: "{description}"\n'
    
    return yaml_output

# Print the result
print(convert_to_yaml())
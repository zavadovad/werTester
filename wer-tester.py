# Import
import string

from os import getcwd
from jiwer import wer
from whisper import load_model


# UŽIVATELSKÝ VSTUP ------------------------------------------------------------------

# VYBERTE ŽENSKÉ (f) NEBO MUŽSKÉ (m) REFERENČNÍ FRÁZE
sex = "f"

# ZADEJTE CESTU K TEXTOVÉMU SOUBORU, KDE SE MAJÍ ULOŽIT VYPOČÍTANÉ HODNOTY WER:
# Př.: "C:/Projekt/RemblexApp/werTester/stt-wer-f.txt"
werOutPath = ""

# ZADEJTE CESTU K SOUBORŮM, KTERÉ CHETE PŘEPSAT A NÁSLEDNĚ VYPOČÍTAT WER PŘEPISU
# Př.: "C:/Projekt/RemblexApp/werTester/LibriSpeech/f-"
wavInPath = ""

# ------------------------------------------------------------------------------------


# Otevření a nahrání referenčních frází ze souboru txt
transcPath = getcwd().replace("\\", "/") + "/LibriSpeech/transcript-" + sex + ".txt"        # Změňte v případě jiných referenčních frází

with open(transcPath) as refT:
    lines = [line.rstrip().lower() for line in refT]

# Převod řeči na text
werFile = open(werOutPath, "w")

model = load_model("base")
i = 0

for line in lines:
    result = model.transcribe(wavInPath + str(i) + ".wav")
       
    # Předzpracování přepisu (odstranění diakritiky a převod na malá písmena)
    result = result["text"]
    result = result.translate(str.maketrans("", "", string.punctuation)).lower()

    # Výpočet WER
    werRate = wer(line, result)
    werRate = str(werRate).replace(".", ",")

    # Výpis výsledku do terminálu
    print("\n" + str(i) + " Referenční text: ", line)
    print(str(i) + " Přepis:         ", result)
    print(str(i) + " WER:             ", werRate)

    # Zápis výsledku do textového souboru
    werFile.write(str(i + 1) + ";" + werRate + ";" + line + ";" + result + "\n")

    i += 1

werFile.close()
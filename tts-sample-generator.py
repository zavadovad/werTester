# Import
from os import getcwd, system
from TTS.api import TTS


# UŽIVATELSKÝ VSTUP ------------------------------------------------------------------

# VYBERTE ŽENSKÉ (f) NEBO MUŽSKÉ (m) FRÁZE KE GENEROVÁNÍ
sex = "f"

# VYBERTE NAHRÁVKU S HLASEM, KTERÝ CHCETE KLONOVAT (pokud chcete klonovat hlas)
# Př.: "C:/Projekt/RemblexApp/saves/recordings/voice.wav"
voiceWav = ""

# ZADEJTE CESTU A NÁZEV SOUBORŮ, KTERÉ CHCETE VYGENEROVAT
# Př.: Cesta: "C:/Projekt/RemblexApp/saves/audios/"
#      Název: "f-"
wavOutPath = ""
wavOutName = ""

# ------------------------------------------------------------------------------------


# Otevření a nahrání frází ke generování ze souboru txt
genPath = getcwd().replace("\\", "/") + "/generate-" + sex + ".txt"                         # Změňte v případě jiných frází ke generování

with open(genPath) as toGen:
    lines = [line.rstrip().lower() for line in toGen]

"""
# Generování předtrénované řeči
tts = TTS(model_name = "tts_models/en/ljspeech/vits")                                       # Změňte v případě, že chcete použít jiný model
i = 0

for line in lines:
    path = wavOutPath + wavOutName + str(i) + ".wav"
    tts.tts_to_file(text = line, file_path = path)

    i += 1
"""

# Generování klonované řeči
i = 0

for line in lines:
    outPath = wavOutPath + wavOutName + str(i) + ".wav"
    command = 'tts --text \"' + line + '\" --model_name tts_models/multilingual/multi-dataset/your_tts  --speaker_wav ' + voiceWav + ' --language_idx \"en\" --out_path ' + outPath
    system(command)

    i += 1

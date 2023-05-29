# Import
from os import system


# UŽIVATELSKÝ VSTUP ------------------------------------------------------------------

# VYBERTE NAHRÁVKU S HLASEM, KTERÝ CHETE KOPÍROVAT
# Př.: "C:/Projekt/RemblexApp/saves/recordings/voice.wav"
voiceWav = "C:/dp_projekt/wer-tester/audio/long-f-aj.wav"

# VYBERTE NAHRÁVKY S REFERENČNÍMI FRÁZEMI
# Př.: "C:/Projekt/RemblexApp/werTester/LibriSpeech/f-"
refWavPath = ""

# ZADEJTE CESTU A NÁZEV SOUBORŮ, KTERÉ CHCETE VYGENEROVAT
# Př.: Cesta: "C:/Projekt/RemblexApp/saves/audios/"
#      Název: "f-"
wavOutPath = ""
wavOutName = ""

# ------------------------------------------------------------------------------------

language = "en"

i = 0

while i < 10:
    refWav = refWavPath + str(i) + ".wav"
    outPath = wavOutPath + wavOutName + str(i) + ".wav"


    command = 'tts --model_name tts_models/multilingual/multi-dataset/your_tts --speaker_wav ' + voiceWav + ' --reference_wav ' + refWav + ' --language_idx \"' + language + '\" --out_path \"' + outPath + '\"'
    system(command)

    i += 1
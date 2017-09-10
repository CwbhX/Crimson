import pymsgbox  # Library on top of Tk to allow us to ask for song information
import acoustid  # Library for AcoustID Webservice
from dejavu import Dejavu  # Local python based fingerprinting library
from dejavu.recognize import MicrophoneRecognizer  # For capturing audio
from dejavu.recognize import FileRecognizer

acoustid_key = ""
dejavu_config = {
    "database": {  # Mysql server
        "host": "127.0.0.1",
        "user": "assistant",
        "passwd": "hogghall",
        "db": "dejavu"
    }
}


def setup():
    global djv
    djv = Dejavu(dejavu_config)


def testFingerprint():
    djv.fingerprint_directory("/Users/Cwbh/Desktop/1989", [".mp3"], 8)
    print("Done")
    print(djv.db.get_songs())
    for song in djv.db.get_songs():
        print(song)


if __name__ == "__main__":
    print("test")
    setup()
    testFingerprint()

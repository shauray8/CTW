import librosa
import numpy as np
import argparse

def mel_spec():
    pass

def main(audio_fn:str) -> any:
    data,sr = librosa.load(audio_fn, sr=None)
    print(np.array(data))
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compression')
    parser.add_argument('audio_fn', metavar='audio data', type=str, nargs='+',
                        help='audio_ data')
    args = parser.parse_args()
    main(args.audio_fn[0])

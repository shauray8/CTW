import librosa
import librosa.display
import numpy as np
import argparse
import matplotlib.pyplot as plt

def mel_spec(data,sr):
    ft = np.abs(librosa.stft(data, n_fft=2048,  hop_length=512))
    librosa.display.specshow(ft, sr=sr, x_axis='time', y_axis='linear');
    plt.colorbar();
    ft_dB = librosa.amplitude_to_db(ft, ref=np.max)
    librosa.display.specshow(ft_dB, sr=sr, hop_length=1024, x_axis='time', y_axis='log');
    plt.show()

def wave(audio_data:np.array) -> None:
    librosa.display.waveplot(data,sr=sr)
    plt.show()

def main(audio_fn:str) -> any:
    data,sr = librosa.load(audio_fn, sr=None)
    print(np.array(data))
    mel_spec(data,sr)

    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compression')
    parser.add_argument('audio_fn', metavar='audio data', type=str, nargs='+',
                        help='audio_ data')
    args = parser.parse_args()
    main(args.audio_fn[0])

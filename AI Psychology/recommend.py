# Alison Menezes
# 05/16/2024
# v1
# AI song recommendation generator

import librosa

def extract_features(file_path):
    y, sr = librosa.load(file_path)
    features = {
        'chroma_stft': librosa.feature.chroma_stft(y=y, sr=sr).mean(),
        'rmse': librosa.feature.rms(y=y).mean(),
        'spectral_centroid': librosa.feature.spectral_centroid(y=y, sr=sr).mean(),
        'spectral_bandwidth': librosa.feature.spectral_bandwidth(y=y, sr=sr).mean(),
        'rolloff': librosa.feature.spectral_rolloff(y=y, sr=sr).mean(),
        'zero_crossing_rate': librosa.feature.zero_crossing_rate(y).mean(),
        'harmony': librosa.feature.tonnetz(y=librosa.effects.harmonic(y), sr=sr).mean(),
        'tempo': librosa.beat.tempo(y=y, sr=sr)[0]
    }
    return features
    

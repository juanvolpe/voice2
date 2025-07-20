# 🎙️ Voice Cloning with Tortoise TTS

This project allows you to clone voices using Tortoise TTS. You can upload voice samples and generate speech in the voice of your choice, with support for multiple languages and quality presets.

## 🚀 Quick Start

1. Open the notebook in Google Colab:
   - Go to [Google Colab](https://colab.research.google.com/)
   - Click on File > Open Notebook
   - Select the GitHub tab
   - Enter this repository URL: https://github.com/juanvolpe/voice2
   - Open `voice_cloning.ipynb`

2. Follow the notebook instructions:
   - Mount Google Drive
   - Install dependencies
   - Upload voice samples
   - Generate speech

## 🎯 Features

- Voice cloning using Tortoise TTS
- Multiple quality presets:
  - ultra_fast: Fastest generation, lower quality
  - fast: Quick generation with decent quality
  - standard: Balanced speed and quality
  - high_quality: Best quality, slower generation
- Support for multiple languages
- GPU acceleration when available

## 📝 Requirements

- Google Colab account (free)
- Voice samples (WAV or MP3 format)
- Text to convert to speech

## 🗣️ Supported Languages

- English (en)
- Spanish (es)
- French (fr)
- German (de)
- Italian (it)
- Portuguese (pt)
- Polish (pl)
- Turkish (tr)
- Russian (ru)
- Dutch (nl)
- Czech (cs)
- Arabic (ar)
- Chinese (Simplified) (zh-cn)

## 📊 Voice Sample Guidelines

For best results:
- Use clear recordings with minimal background noise
- Provide 1-3 samples of 5-10 seconds each
- Ensure consistent voice tone and quality
- Use WAV or MP3 format
- Record in a quiet environment

## ⚠️ Notes

- Generation time depends on the quality preset and available computing resources
- High-quality preset requires more VRAM and processing time
- Some languages may require additional voice samples for better results

## 📜 License

This project uses Tortoise TTS under its original license. Please check [Tortoise TTS](https://github.com/neonbjb/tortoise-tts) for more information. 
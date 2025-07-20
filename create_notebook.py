import json

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# 🎙️ Voice Cloning with Tortoise TTS\n",
                "\n",
                "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/juanvolpe/voice2/blob/master/voice_cloning.ipynb)\n",
                "\n",
                "This notebook allows you to clone voices using Tortoise TTS, supporting multiple languages and quality presets.\n",
                "\n",
                "## 🎯 Features\n",
                "- Voice cloning with Tortoise TTS\n",
                "- Support for 13 languages\n",
                "- Multiple quality presets\n",
                "- GPU acceleration\n",
                "- Easy voice sample management\n",
                "\n",
                "## 📝 Prerequisites\n",
                "1. **Google Colab**: Make sure you're running this in Colab with GPU runtime\n",
                "2. **Voice Samples**: Prepare WAV/MP3 files (5-10 seconds each)\n",
                "3. **Hugging Face Token**: Will be loaded from Colab secrets"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Section 1: Setup 🔧\n",
                "\n",
                "First, ensure you're using a GPU runtime:\n",
                "1. Click `Runtime` in the menu\n",
                "2. Select `Change runtime type`\n",
                "3. Choose `GPU` from the hardware accelerator dropdown\n",
                "4. Click `Save`"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Check GPU availability\n",
                "import torch\n",
                "print(\"🔍 Checking GPU configuration...\")\n",
                "print(f\"GPU Available: {'✅' if torch.cuda.is_available() else '❌'}\")\n",
                "if torch.cuda.is_available():\n",
                "    print(f\"Device: {torch.cuda.get_device_name(0)}\")\n",
                "    print(f\"CUDA Version: {torch.version.cuda}\")\n",
                "else:\n",
                "    print(\"\\n⚠️ No GPU detected! Please change runtime to GPU for better performance:\")\n",
                "    print(\"1. Runtime > Change runtime type\")\n",
                "    print(\"2. Select GPU from Hardware accelerator dropdown\")\n",
                "    print(\"3. Click Save and restart runtime\")"
            ]
        }
    ],
    "metadata": {
        "accelerator": "GPU",
        "colab": {
            "name": "Voice Cloning with Tortoise TTS",
            "provenance": []
        },
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 0
}

# Write the notebook to a file
with open('voice_cloning.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=2) 
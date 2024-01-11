# faster-whisper-to-translator

This project allows you to extract subtitles from video files using faster-whisper and then translate them using the DeepL API.

It's a two-step process: first transcribe, then translate.

## Dependencies

- [faster-whisper](https://github.com/SYSTRAN/faster-whisper): A faster implementation of OpenAI's Whisper for automatic speech recognition.
- [SRTranslator](https://github.com/sinedie/SRTranslator/): A Python library for translating SRT (SubRip Text) files.

Check out above documentations for improving your performance or your own modificatoins !

```
pip install faster-whisper srtranslator tqdm
```

## How to use

### Transcription

1. **Setup and Configuration**

	- Place your video files in the video folder.
	
	- Modify `faster_whisper.py` to set `video_directory` and `srt_file_directory` to your desired paths.

	- Choose the `model_size` based on your GPU capabilities. Check the available models and languages [here](https://github.com/openai/whisper#available-models-and-languages)

2. **Run**

	- `python faster_whisper.py`

	- Transcribed .srt files will be saved in the `srt_file_directory`

### Translation

1. **API Key Configuration**

	- Obtain a FREE API KEY from DeepL with a 500,000 character limit per month.

	- Alternatively, you can use `DeeplTranslator()` for a API key-free, but slower option.

2. **Modify `translator.py`**

	- Change `folder` and `new_filename` for your own requirements.

	- Specify `source_lang` and `target_lang` in `srt.translate()`. The list of supported langueges is in [here](https://www.deepl.com/docs-api/translate-text/).

	- For detailed usage, refer to SRTranslator [documentation](https://github.com/sinedie/SRTranslator/) and [examples](https://github.com/sinedie/SRTranslator/tree/master/examples)

3. **Run**

	- `python translator.py`

	- Translated `.srt` files will be in the specified dirctory.

---

### Note

- If you are going to use `DeeplTranslator()` for translation. Ensure **Mozilla Firefox** is installed in your OS.

- For those who want to use this repository for YT videos. I recommnd [shaked6540/YoutubePlaylistDownloader](https://github.com/shaked6540/YoutubePlaylistDownloader) for downloading YT videos (it also supports playlists).

### Output examples

**faster_whisper.py**

```bash
 62%|######2   | 218.04/349.622875 [01:05<00:39,  3.30 audio seconds/s]
 70%|######9   | 244.4/349.622875 [01:13<00:31,  3.31 audio seconds/s] 
 78%|#######8  | 272.72/349.622875 [01:21<00:22,  3.39 audio seconds/s]
 86%|########6 | 301.91999999999996/349.622875 [01:28<00:13,  3.51 audio seconds/s]
 94%|#########3| 328.28/349.622875 [01:36<00:06,  3.49 audio seconds/s]            
100%|##########| 349.622875/349.622875 [01:36<00:00,  3.62 audio seconds/s]
SRT file created successfully for CS 285_ Lecture 9, Part 3.mkv in 100.17367029190063 times
Detected language 'en' with probability 1.0 for file CS 285_ Lecture 9, Part 4.mkv

  0%|          | 0/1267.7863125 [00:00<?, ? audio seconds/s]
  0%|          | 3.6/1267.7863125 [00:05<30:53,  1.47s/ audio seconds]
  2%|2         | 31.0/1267.7863125 [00:13<08:27,  2.44 audio seconds/s]
  5%|4         | 60.68/1267.7863125 [00:22<06:43,  2.99 audio seconds/s]
  7%|7         | 89.16/1267.7863125 [00:29<05:53,  3.33 audio seconds/s]

## ...

 85%|########4 | 1077.52/1267.7863125 [05:29<00:56,  3.37 audio seconds/s]           
 87%|########7 | 1107.8799999999999/1267.7863125 [05:38<00:46,  3.45 audio seconds/s]
 89%|########9 | 1133.48/1267.7863125 [05:47<00:41,  3.22 audio seconds/s]           
 92%|#########1| 1162.68/1267.7863125 [05:57<00:33,  3.16 audio seconds/s]
 94%|#########4| 1194.68/1267.7863125 [06:04<00:21,  3.43 audio seconds/s]
 96%|#########6| 1219.8600000000001/1267.7863125 [06:13<00:14,  3.33 audio seconds/s]
 98%|#########8| 1247.3/1267.7863125 [06:20<00:05,  3.47 audio seconds/s]            
100%|##########| 1267.7863125/1267.7863125 [06:20<00:00,  3.33 audio seconds/s]
SRT file created successfully for CS 285_ Lecture 9, Part 4.mkv in 386.6411700248718 times
All SRT files created in 47240.42731809616 times.
```

*since I have GTX 1660 Super GPU,  the processing time is longer.*

**translator.py**

```bash
Loading ./videos/CS285/SRT\CS 285_ Lecture 13, Part 2.srt as SRT
... Translating 0 %
... Translating 9 %
... Translating 19 %
... Translating 28 %
... Translating 37 %
... Translating 47 %
... Translating 58 %
... Translating 66 %
... Translating 77 %
... Translating 86 %
... Translating 94 %
... Translation done
Saving ./videos/CS285/SRT\KOR_CS 285_ Lecture 13, Part 2.srt
Translated and saved: ./videos/CS285/SRT\KOR_CS 285_ Lecture 13, Part 2.srt
```
import os, math
from faster_whisper import WhisperModel
import logging
from tqdm import tqdm
import time

# logging.basicConfig()
# logging.getLogger("faster_whisper").setLevel(logging.DEBUG)

# Function to convert seconds to the SRT timecode format
def to_srt_timecode(seconds):
		hours, remainder = divmod(seconds, 3600)
		minutes, seconds = divmod(remainder, 60)
		milliseconds = math.floor((seconds % 1) * 1000)
		output = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02},{milliseconds:03}"
		return output

# Initialize Whisper Model
model_size = "medium" # or "large-v3"
model = WhisperModel(model_size, device="cuda", compute_type="float16")

# Directory containing your CS285 videos
video_directory = "./videos/CS285"
video_files = [f for f in os.listdir(video_directory) if f.endswith('.mkv')]
srt_file_directory = "./videos/CS285/SRT"

Tic = time.time()
for video_file in video_files:
		tic = time.time()
		video_path = os.path.join(video_directory, video_file)
		segments, info = model.transcribe(video_path, beam_size=5)

		print(f"Detected language '{info.language}' with probability {info.language_probability} for file {video_file}")

		srt_file_name = os.path.splitext(video_file)[0] + ".srt"
		srt_file_path = os.path.join(srt_file_directory, srt_file_name)

		# Write to SRT file
		timestamps = 0.0
		with open(srt_file_path, "w") as file:
				with tqdm(total = info.duration, unit = " audio seconds") as pbar:
					for i, segment in enumerate(segments):
							start_time = to_srt_timecode(segment.start)
							end_time = to_srt_timecode(segment.end)
							file.write(f"{i + 1}\n")
							file.write(f"{start_time} --> {end_time}\n")
							file.write(segment.text.lstrip() + "\n\n")
							pbar.update(segment.end - timestamps)
							timestamps = segment.end
					if timestamps < info.duration:
						pbar.update(info.duration - timestamps)
      
		toc = time.time()
		print(f"SRT file created successfully for {video_file} in {toc - tic} times")

Toc = time.time()
print(f"All SRT files created in {Toc - Tic} times.")

#!/usr/bin/env python3
from gtts import gTTS
from moviepy.editor import *
import tempfile, os
from unsplash_client import fetch_image

def generate_video_from_scenario(scenario, width=1280, height=720, fps=24, bg_music_path=None):
    # Ensure folders exist
    os.makedirs("assets", exist_ok=True)
    os.makedirs("videos", exist_ok=True)

    # Try to get background image
    bg_path = scenario.get("background")
    if not bg_path:
        query = scenario["title"]
        bg_path = f"assets/{scenario['id']}.jpg"
        if not os.path.exists(bg_path):
            fetch_image(query, bg_path)

    if bg_path and os.path.exists(bg_path):
        background = ImageClip(bg_path).resize((width, height))
    else:
        background = ColorClip(size=(width, height), color=(240, 240, 240))

    clips = []
    for f in scenario['frames']:
        # Estimate duration based on words (0.5s per word, min 4s)
        slide_duration = max(4, len(f.split()) * 0.5)

        txt = TextClip(f, fontsize=40, color="black", font="Arial-Bold",
                       method="caption", size=(width-200, None), align="center")

        overlay = txt.on_color(size=(width-100, txt.h+60),
                               color=(255, 255, 255), col_opacity=0.7)

        slide = CompositeVideoClip(
            [background, overlay.set_position(("center", "center"))],
            size=(width, height)
        ).set_duration(slide_duration)

        clips.append(slide.crossfadein(1.0))

    # Build video
    video = concatenate_videoclips(clips, method="compose", padding=-1, bg_color=(240, 240, 240))

    # Narration
    tmp_dir = tempfile.mkdtemp()
    narration = " ".join(scenario['frames'])
    tts_path = os.path.join(tmp_dir, "narration.mp3")
    gTTS(text=narration, lang="en").save(tts_path)
    audio_narration = AudioFileClip(tts_path)

    if audio_narration.duration > video.duration:
        audio_narration = audio_narration.subclip(0, video.duration)

    # Background music (optional)
    if bg_music_path and os.path.exists(bg_music_path):
        bg_music = AudioFileClip(bg_music_path).volumex(0.1)
        if bg_music.duration > video.duration:
            bg_music = bg_music.subclip(0, video.duration)
        final_audio = afx.audio_mix(audio_narration, bg_music)
    else:
        final_audio = audio_narration

    # Final video with audio
    final = video.set_audio(final_audio)

    # Save inside "videos/"
    out_path = os.path.join("videos", f"scenario_{scenario['id']}.mp4")
    final.write_videofile(out_path, codec="libx264", audio_codec="aac", fps=fps)

    return out_path

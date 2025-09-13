#!/usr/bin/env python3
import os
import tempfile
import shutil
import subprocess
import json
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont

def generate_slide_image(text, path, width=1280, height=720):
    """Render text onto a white background and save as PNG."""
    img = Image.new("RGB", (width, height), color=(240, 240, 240))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except OSError:
        font = ImageFont.load_default()

    lines, line, max_width = [], [], width - 200
    for word in text.split():
        test_line = " ".join(line + [word])
        if draw.textlength(test_line, font=font) > max_width:
            lines.append(" ".join(line))
            line = [word]
        else:
            line.append(word)
    if line:
        lines.append(" ".join(line))

    line_height = int(font.size * 1.2) if hasattr(font, "size") else 48
    y = max(50, (height - len(lines) * line_height) // 2)
    for l in lines:
        w = draw.textlength(l, font=font)
        draw.text(((width - w) // 2, y), l, font=font, fill="black")
        y += line_height

    img.save(path)

def _probe_duration(path: str) -> float:
    """Return duration in seconds for an audio or video file using ffprobe."""
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries",
             "format=duration", "-of", "json", path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True
        )
        info = json.loads(result.stdout)
        return float(info["format"]["duration"])
    except Exception as e:
        raise RuntimeError(f"Could not determine duration for {path}: {e}")

def generate_video_from_scenario(subscenario, width=1280, height=720, fps=24, bg_music_path=None, out_dir="videos"):
    """Generate video from scenario frames using subprocess + ffmpeg binary."""
    os.makedirs(out_dir, exist_ok=True)
    tmp_dir = tempfile.mkdtemp(prefix="vid_tmp_")
    segments = []

    try:
        for i, frame_text in enumerate(subscenario["frames"], start=1):
            # 1) generate slide
            img_path = os.path.join(tmp_dir, f"slide_{i}.png")
            generate_slide_image(frame_text, img_path, width, height)

            # 2) generate narration
            audio_path = os.path.join(tmp_dir, f"slide_{i}.mp3")
            gTTS(text=frame_text, lang="en").save(audio_path)

            # 3) get audio duration
            audio_dur = _probe_duration(audio_path)
            slide_duration = max(0.5, audio_dur + 0.4)

            # 4) create video segment from image + narration
            seg_path = os.path.join(tmp_dir, f"segment_{i}.mp4")
            subprocess.run([
                "ffmpeg", "-y",
                "-loop", "1",
                "-i", img_path,
                "-i", audio_path,
                "-c:v", "libx264",
                "-t", str(slide_duration),
                "-pix_fmt", "yuv420p",
                "-c:a", "aac",
                "-b:a", "128k",
                seg_path
            ], check=True)
            segments.append(seg_path)

        if not segments:
            raise ValueError("No segments created; scenario['frames'] may be empty")

        # 5) concat segments
        concat_file = os.path.join(tmp_dir, "segments.txt")
        with open(concat_file, "w", encoding="utf-8") as f:
            for seg in segments:
                f.write(f"file '{seg.replace('\\','/')}'\n")

        final_path = os.path.join(out_dir, f"scenario_{subscenario['id']}.mp4")
        subprocess.run([
            "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_file, "-c", "copy", final_path
        ], check=True)

        # 6) optional background music mix
        if bg_music_path and os.path.exists(bg_music_path):
            mixed_path = final_path.replace(".mp4", "_with_music.mp4")
            subprocess.run([
                "ffmpeg", "-y",
                "-i", final_path,
                "-i", bg_music_path,
                "-filter_complex", "[0:a][1:a]amix=inputs=2:duration=shortest:dropout_transition=2",
                "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                mixed_path
            ], check=True)
            final_path = mixed_path

        return final_path

    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)

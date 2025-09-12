#!/usr/bin/env python3
from generate_local import generate_video_from_scenario
from scenarios import scenarios  # your scenarios list

def main():
    for scenario in scenarios:
        print(f"🎬 Generating video for: {scenario['title']} ...")
        try:
            video_path = generate_video_from_scenario(scenario)
            print(f"✅ Done: {video_path}")
        except Exception as e:
            print(f"❌ Failed for {scenario['title']}: {e}")

if __name__ == "__main__":
    main()

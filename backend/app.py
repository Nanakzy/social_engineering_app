from flask import Flask, jsonify, request, send_file
from dotenv import load_dotenv
from flask_cors import CORS
import os
from scenarios import scenarios
from generate_local import generate_video_from_scenario

load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route('/api/scenarios', methods=['GET'])
def get_scenarios():
    return jsonify(scenarios)

@app.route('/api/generate/<scenario_id>', methods=['GET'])
def generate_video(scenario_id):
    scenario = next((s for s in scenarios if s['id']==scenario_id), None)
    if not scenario:
        return jsonify({"error": "Scenario not found"}), 404
    video_path = generate_video_from_scenario(scenario, bg_music_path='assets/music.mp3')
    return send_file(video_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
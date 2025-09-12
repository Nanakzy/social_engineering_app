import React, { useEffect, useState, useRef } from 'react';
import axios from 'axios';

export default function ScenarioList() {
  const [scenarios, setScenarios] = useState([]);
  const [currentVideo, setCurrentVideo] = useState(null);
  const videoRef = useRef(null); // reference to the video element

  useEffect(() => {
    axios.get('http://localhost:5000/api/scenarios')
      .then(res => setScenarios(res.data))
      .catch(err => console.error(err));
  }, []);

  const playVideo = (id) => {
    // Stop currently playing video
    if (videoRef.current) {
      videoRef.current.pause();
      videoRef.current.currentTime = 0;
    }
    // Set new video URL
    setCurrentVideo(`http://localhost:5000/api/generate/${id}`);
  };

  return (
    <div>
      {scenarios.map(s => (
        <div key={s.id} style={{ marginBottom:'20px', border:'1px solid #ccc', padding:'10px' }}>
          <h3>{s.title}</h3>
          <button onClick={() => playVideo(s.id)}>Play Video</button>
        </div>
      ))}

      {currentVideo && (
        <div style={{ marginTop:'20px' }}>
          <h3>Video Preview</h3>
          <video
            ref={videoRef}
            src={currentVideo}
            controls
            width="640"
            height="360"
            autoPlay
          />
        </div>
      )}
    </div>
  );
}

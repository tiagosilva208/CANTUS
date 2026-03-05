# CANTUS Project Design Document

## Project Architecture
The architecture of the CANTUS project is modular, allowing for individual components to be developed and maintained independently. The project follows a layered architecture that promotes separation of concerns.

## Tech Stack
- **Frontend:** React.js
- **Backend:** Node.js with Express.js
- **Database:** PostgreSQL
- **Deployment:** Docker, AWS
- **Testing:** Jest, Mocha

## Module Structure  
```
CANTUS/

│
├── main.py
├── requirements.txt
├── README.md
│
├── cantus/
│   │
│   ├── audio/
│   │   ├── player.py
│   │   ├── audio_loader.py
│   │   └── audio_buffer.py
│   │
│   ├── analysis/
│   │   ├── fourier.py
│   │   ├── spectrogram.py
│   │   ├── pitch_detection.py
│   │   ├── onset_detection.py
│   │   └── section_detection.py
│   │
│   ├── midi/
│   │   ├── midi_writer.py
│   │   └── note_quantizer.py
│   │
│   ├── visualization/
│   │   ├── spectrogram_view.py
│   │   ├── timeline_view.py
│   │   ├── playhead.py
│   │   └── fourier_view.py
│   │
│   ├── ui/
│   │   ├── main_window.py
│   │   ├── transport_controls.py
│   │   └── file_dialogs.py
│   │
│   ├── threading/
│   │   ├── worker.py
│   │   └── analysis_thread.py
│   │
│   └── utils/
│       ├── config.py
│       ├── constants.py
│       └── math_utils.py
│
├── assets/
│   ├── icons/
│   └── test_audio/
│
└── tests/
    ├── test_fourier.py
    └── test_pitch.py
```

## Feature Roadmap
- **Phase 1:**  
  - User Authentication  
  - Basic CRUD Operations  

- **Phase 2:**  
  - User Roles and Permissions  
  - Feature Enhancements

- **Phase 3:**  
  - Integration of Third-party APIs  
  - Performance Optimization  
- **Phase 4:**  
  - Final Testing and Release  

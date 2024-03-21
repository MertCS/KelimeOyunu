# Kelime Oyunu

## Overview

Kelime Oyunu is a simple game where a group of friends can come together to compete with their grammar knowledge.

## Features

- Engaging and simplistic gameplay
- Multiplayer

## Getting Started

### Prerequisites

- Python
- Pygame

### Installation

1. Clone Repository
   ```bash
   git clone https://github.com/MertCS/KelimeOyunu

2. Open the folder 'Story Saver' and run 'main.py'
   ```bash
   python main.py

### Instructions
First, one person should be chosen as the host, this host should have knowledge of all the answers.
To modify questions and answers, the "questions" array and the "answers" array can be modified. Make sure the indexes of answers are the same with the questions in their respective arrays.

## Host

- **Enter**: Go to the next question and modify the score of the contestant respectfully.
- **Right Shift**: Reveals a random letter in the answer. This should be used only when the contestant asks for a letter.
- **Space**: Reveals the answer.

## Contestant

- The role of the contestant is to guess the right answer for every question in the given time frame. If they are stuck, they can ask for a letter to be revealed within the answer to get a hint. For each letter revealed, 100 points are reduced from their score.

### Screenshots
![Uploading Screenshot 2024-03-21 at 15.57.16.png…]()
![Uploading Screenshot 2024-03-21 at 15.57.59.png…]()
![Uploading Screenshot 2024-03-21 at 15.59.25.png…]()
![Uploading Screenshot 2024-03-21 at 16.01.30.png…]()






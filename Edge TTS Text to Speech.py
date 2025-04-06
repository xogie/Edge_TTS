import edge_tts
import asyncio
import uuid
import os
import pygame  # Make sure pygame is installed: pip install pygame

async def speak_text_async(text):
    filename = f"tts_{uuid.uuid4().hex}.mp3"

    # Generate MP3 using Edge-TTS
    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-JennyNeural"
    )
    await communicate.save(filename)

    # Initialize pygame mixer and play the MP3 file
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    
    # Wait until playback is finished
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    # Quit pygame mixer to release the file handle
    pygame.mixer.quit()

    # Delete the MP3 file after playback
    os.remove(filename)

def speak_text(text):
    asyncio.run(speak_text_async(text))

# Test with a sample text
if __name__ == "__main__":
    speak_text("Hello, this is a test message.")


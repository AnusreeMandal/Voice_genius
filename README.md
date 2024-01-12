
#TESS AI- Your Virtual Assistance

TESS AI is a virtual assistant powered by OpenAI's text-davinci-003 model, designed to interact with users through voice commands. It provides a range of functionalities, from web browsing to playing music and engaging in conversations.


## Features

1. **Voice Interaction:**
   - Communicate with TESS AI using voice commands through the speech_recognition library.

2. **OpenAI Integration:**
   - Leverage the advanced text-davinci-003 model for intelligent and context-aware responses.

3. **Web Browsing:**
   - Open websites such as YouTube and Wikipedia with the webbrowser module.

4. **Music Playback:**
   - Play music from a specified path using the os module.

5. **Current Time:**
   - Obtain the current time based on the system clock using the datetime module.

6. **Personalized Greeting:**
   - Experience a personalized greeting as TESS AI adapts to your interactions.

7. **Chat Functionality:**
   - Engage in conversations, with chat history neatly stored in the chat_str variable.

8. **Voice Output:**
   - Utilize the system's voice output for a more dynamic interaction using the os.system function.

9. **Continuous Listening:**
   - TESS AI continuously listens for user commands until an exit command is given.

10. **Dynamic Response Temperature:**
    - Experience dynamic responses with a temperature setting of 0.7 in OpenAI interactions.


## Usage/Examples

```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
```


## Demo



1. **Personalized Greeting:**
   - TESS AI starts with a personalized greeting.

2. **Voice Commands:**
   - Use voice commands to interact with TESS AI.:
   Open YouTube: open youtube

   Open Wikipedia: open wikipedia

Play Music: play music

Get Current Time: the time

Chat with AI: using artificial intelligence

Quit TESS AI: tess quit

Reset Chat History: reset chat

     ```bash
     Listening...
     User said: open YouTube
     Opening YouTube.
     Listening...
     User said: play music
     Playing music.
     Listening...
     User said: the time
     The current time is 15:30.
     Listening...
     User said: using artificial intelligence
     User: using artificial intelligence
     Tess: The future of artificial intelligence is fascinating and holds great potential for innovation.
     Listening...
     User said: tess quit
     Goodbye!

     ```
 
**OpenAI API Key:**
   - Obtain your OpenAI API key from [OpenAI](https://beta.openai.com/signup/).
   - Set the API key as an environment variable:
     ```bash
     export OPENAI_API_KEY=your_openai_api_key
     ```
## Run Locally

Clone the project

```bash
  git clone https://github.com/AnusreeMandal/Voice_genius.gi

```

**Setup:**
   - Clone the repository.
   
   - Install dependencies using 
   
   `pip install -r requirements.txt`.

3. **Configuration:**
   - Set your OpenAI API key as an environment variable


## License
This Project is licensed under  [MIT](https://choosealicense.com/licenses/mit/)License


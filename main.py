import os
import openai
import streamlit as st


def gpt_get_response(prompt, emotions):
    system_prompt = f''' You are an emotionally assistant.
    Classify the sentiment of the user's text with ONLY ONE OF THE FOLLWING EMOTIONS:{emotions}
    After classifying the text, respond with the emotion ONLY'''
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {'role':'system', 'content': system_prompt},
            {'role': 'user', 'content': prompt}
        ],
        max_tokens = 20,
        temperature = 0
    )
    get_response = response['choices'][0].message.content
    return get_response
# emotions = 'negative, positive,neutral'
# text = 'Sunt indiferent'
# result = gpt_get_response(text, emotions)
# print(result)

if __name__ == '__main__':
    with open('key.txt') as f:
        api_key = f.read()
    openai.api_key = api_key
    col1,col2 = st.columns([0.85, 0.15])
    with col1:
        st.title('Zero-Shot sentiment analysis')
    with col2:
        st.image('images.jpg',width=70)
    with st.form(key = 'my_form'):
        default_emotions = 'positive, negative,neutral'
        emotions = st.text_input('Emotions:', value = default_emotions)

        text = st.text_area(label = 'Text to classify')
        submit_button = st.form_submit_button(label = "Check!")
        if submit_button:
            emotion = gpt_get_response(text,emotions)
            result = f'{text}=>{emotion} \n'
            st.write(result)
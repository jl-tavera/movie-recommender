import streamlit as st
import re
import requests
from openai import OpenAI
client = OpenAI(api_key = "YOUR API KEY")

'''
STREAMLIT INTERFACE
'''

# Page title
st.title("Movie Recommendation")
# Subheader
st.subheader("I want a movie simmilar to")
# Get user input
user_input_movie = st.text_input("Enter a movie", "")


# Search movie if there is an input by the user
if user_input_movie:

    '''
    OPEN AI API
    '''

    #Prompt for openai api
    message_content = "Provide me five movie titles simmilar to the movie:" + str(user_input_movie) + "And only the titles with no description or date"

    #Get response from openaai
    response_openai = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [  {"role": "user", "content": message_content}]
        )
    
    '''
    GET A LIST OF ALL THE MOVIES
    '''

    #Use Regular Expressions to grab the movie titles from chat gpt prompt
    pattern = r'\d+\.\s(.+)'
    titles = re.findall(pattern, response_openai.choices[0].message.content)

    '''
    GET STREAM AVAILABILITY OF EACH TITLE 
    '''

    for title in titles: 

        # Show each movie title
        st.subheader(title)

        # Fetch Information of Streamavailability 
        url = "https://streaming-availability.p.rapidapi.com/search/title"
        querystring = {"title":titles[0],"country":"us","show_type":"all","output_language":"en"}
        headers = {
            "X-RapidAPI-Key": "YOUR API KEY",
            "X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
                }

        # Get specific information of the streaming info in the USA
        try:
            response = requests.get(url, headers=headers, params=querystring)
            result = response.json()['result'][0]['streamingInfo']['us']

            '''
            SHOW INFORMATION FOR EACH SERVICE
            '''

            # Get info for each service 
            for service in result:

                # Get it from each service
                platform = service['service']
                streamingType = service['streamingType']
                link = service['link']

                # Show them with Streamlit Interface
                st.text('Service: ' + str(platform) )
                st.text('Type: ' + str(streamingType) )
                st.text('Text' + str(link))
        
        #KeyError when the movie is not available in any service
        except KeyError as e:
            st.text("No services found")



        

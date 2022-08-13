from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# to run the website: python -m streamlit run website.py



st.set_page_config(page_title="Our amazing website!", page_icon=":yum:",layout="wide")
def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_jggbnfb8.json")
lottie_solution = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_kujqck0u.json")


#header section
with st.container():
    st.subheader("Welcome. We are the Static Startups :zap::computer:")
    st.title("Our team would like to discuss an important issue!")
    st.write("The Earth and oceans are warming due to heat-trapping gases, which is causing sea levels to rise, storm patterns to change, extreme heat events, fires, and drought. Everything is a result of climate change, which is the primary cause and has many negative effects on the world.")
    st.write("[Find out more on the United Nations SDGs >](https://www.un.org/en/sustainable-development-goals)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("An Introduction to The Sustainable Development Goals")
        st.write("##")
        st.write(
            """
            The Sustainable Development Goals (SDGs), commonly referred to as the Global Goals, are a set of 17 connected global goals that were created as a "shared blueprint for peace and prosperity." The UN General Assembly adopted the SDGs in 2015 with the goal of achieving them by 2030.

            There are four dimensions to sustainable development – society, environment, culture, and economy. The Static Startups have made the decision to launch this website in order to promote awareness of the ongoing problem of climate change, which is the 13th SDG.
            """
        )


    with right_column:
        st_lottie(lottie_coding, height = 400, key="climate")

with st.container():
    
        st.header("About the 13th Goal - Climate Action")
        st.write("##")
        st.write(
            """
            There are long-term changes in the climate that have occured over decades, centuries, or longer. It is caused by the rapidly increasing amount of greenhouse gases in the Earth's atmosphere, primarily as a result of burning fossil fuels.
            Multiple goals have been set by the United Nations. Below are a few of them:
            - Target 13.1: Strengthen resilience and adaptive capacity to climate-related hazards and natural disasters in all countries
            - Target 13.2: Integrate climate change measures into national policies, strategies and planning
            - Target 13.3: Improve education, awareness-raising and human and institutional capacity on climate change mitigation, adaptation, impact reduction and early warning
            - Target 13.b: Promote mechanisms for raising capacity for effective climate change-related planning and management in least developed countries and small island developing States, including focusing on women, youth and local and marginalized communities
             
            """
            )

with st.container():

        st.header("Current Issues and Comparison")
        st.write(
            """
            Climatic changes have a harmful effect on the environment. As a result of climate change, the ocean level is rising, glaciers are melting, CO2 levels in the atmosphere are rising, forests and other wildlife are disappearing, and aquatic life is being altered.
            In addition, it is expected that if this trend continues, many species of plants and animals would become extinct and the environment will suffer greatly. Our current reality is obviously very different from what it was ten years ago, in particular. Data study on greenhouse gas (GHG) concentrations, and other topics reveal unsettling trends.

            In 2018, the increase rate was 2.9 ppm/year (parts per million). The average global sea level increased by around 3.3 millimeters between 1993 and the present. This trend has noticeably quickened over the years. This pattern amply demonstrates the huge changes brought on by climate change throughout the world.
            """
            )

#Solutions
with st.container():
    st.write("---")
    st.header("Our Team's Proposal")
    st.write("##")
    image_column, text_column = st.columns((1,2))
with image_column:
    st_lottie(lottie_solution, height = 400, key="solution")
       
with text_column:
    st.write(
             """
            Our team, The Static Startups encourages all of you to play a major role in eradicating this global problem Hence, we convey a few solutions that can be followed:
            
             - Walk, cycle or use public transport : The majority of the vehicles on the world's roads burn either diesel or petrol. Driving less and using a bike or walking will both improve your health and fitness and assist the environment. Consider using a bus or train for lengthier trips. Whenever possible, carpool as well.
             - Take in to account your travel : As a result of their extensive use of fossil fuels and aeroplanes contribute significantly to greenhouse gas emissions. Taking fewer flights is thus one of the quickest ways to reduce your environmental impact. When possible, meet virtually, take the train, or avoid the long-distance trip entirely.
             - Reduce usage of plastic : Plastic is made from oil, and the quantity of carbon required to extract, refine, and create plastic (or even polyester for clothing) from oil is shocking. A lot of plastic is burned since it decomposes slowly in nature, increasing emissions
             - Help raise awareness : Speak up and encourage others to join you in taking action. It's one of the simplest and most effective ways to affect change.
             """
             )

with st.container():

        st.header("Information Credits")
        st.write(
            """
            - https://weather.com/science/environment/news/earth-climate-change-effects
            - https://www.un.org/sustainabledevelopment/climate-change/
            - https://www.greenpeace.org.uk/challenges/climate-change/solutions-climate-change/
            - https://www.un.org/actnow

            """
            )

    
         
        



    


    
    




import streamlit as st
import requests
import matplotlib.pyplot as plt

movieApi = '43d50744'
header = st.container()
title = st.text_input('Search for your movie here')
url = f"http://www.omdbapi.com/?t={title}&apikey={movieApi}"

with header:
    st.title("Movie Search App")
if title:
    try:
        re = requests.get(url)
        re = re.json()
        col1, col2, col3= st.columns([0.5, 1.5, 1])

        with col1:
            st.image(re['Poster'])
        with col2:
            st.subheader(re['Title'])
            st.caption(f"Genre: {re['Genre']} ") 
            st.caption(f"Year: {re['Year']}")
            st.caption(f"Country: {re['Country']}")
            st.caption(f"Cast: {re['Actors']}")
            st.write(re['Plot'])
            st.text(f"Rating: {re['imdbRating']}")
        with col3:
            genres = list(re['Genre'].split(","))
            names = []
            slices = []
            for genre in genres:
                if genre not in names:
                    names.append(genre)

            for genre in names:
                slices.append(genres.count(genre))

            #matplotlib pie chart
            fig,ax = plt.subplots()
            plt.style.use('_mpl-gallery-nogrid')
            colors = plt.get_cmap('Blues')
            fig = plt.figure(figsize=(3, 3))

            # Change background color
            fig.patch.set_facecolor('#0E1117')

            # Change color of text
            plt.rcParams['text.color'] = 'white'
      
            #plot
            plt.pie(slices, labels=names)
            ax.axis('equal')

            #show the chart
            st.pyplot(fig)
    
    except:
        st.error('No movie with that title')

else:
    st.text('You have not searched for a movie')


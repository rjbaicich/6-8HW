import streamlit as st
from base import Base

base_csv_file = r'C:\Users\RedneckRandy\Documents\GitHub\6-8HW\dohmh-beach-water-quality-data-1.csv'

beach_name = st.text_input('Enter the name of a beach:', value='').lower()

if beach_name:
    base = Base()
    beach_data = base.get_beach_data(beach_name)
    
    if beach_data:
        st.write(beach_data)
        enterococci_results = beach_data.get('Enterococci Results', 0)
        if isinstance(enterococci_results, int):
            if enterococci_results <= 99:
                st.image('https://www.rd.com/wp-content/uploads/2020/04/tropic-of-cancer-beach-in-exuma-bahamas.jpg?fit=700,467',
                         caption='Clean Beach')
            elif enterococci_results >= 100:
                st.image('https://i.natgeofe.com/n/8c1dcd07-ebc0-4c31-8522-0f80df632983/01_beachplastic_photo-one_4x3.jpg',
                         caption='Dirty Beach')
            else:
                st.write('Beach cleanliness information unavailable.')
        else:
            st.write('Invalid beach cleanliness information.')
    else:
        st.write('Beach not found.')

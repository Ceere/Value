import streamlit as st

Search = st.Page("search_page.py", title="Search")
Detail = st.Page("detail.py", title="Detail")

pg = st.navigation([Search, Detail],position="hidden")
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()
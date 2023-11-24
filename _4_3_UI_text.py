import streamlit as st

def instruction():
    st.title("Students' Feedback Web App")
    st.write("This **Web App** will receive **Feedback** from **Students** and predict **Students' Feedback** whether it is **Positive**, **Neutral** or **Negative**.")
    st.write('In the **Menu**, there are **Introduction**, **Visualization**, **Feedback** and **About** sections:')
    st.subheader('**Introduction:**')
    st.write('- This section will introduce the **Functions**, **General Information** and **Usage** of this **Web App**')
    st.subheader('**Visualization:**')
    st.write('- This section contains an **Account** that needs to be **Logged in** to **View** the **Data** or **Download** the **Feedback File**.')
    st.subheader('**Feedback:**')
    st.write('- This section will receive **Feedback** from **Students**, the user will input it in the **Text Bar**, then press the **Enter** key in that **Text Bar** or press the **"Predict"** button to run. It will rely on that **Feedback** to predict whether it is **Positive**, **Neutral** or **Negative**. Those **Feedback** will be **Saved** on the **System**. You can see those **Feedback** by **Loginning** in **Visualization Section** to **Download File contains it**.')
    st.subheader('**About:**')
    st.write('- This section will describe **Information** including: **Name** of the **Group** that made this **Project**, **Mentor** and each **Member** of the **Group**.')
def about():
    st.title("This is a Mini Project for DAP391m")  
    st.markdown("**Developed by Group 1**")
    st.header("Mentor: **Nguyen Thanh Dong**")
    st.subheader("Member in **Group 1**:")
    st.image('members.png')
    # st.write("**Mai Xuan Huu** - QE170004")
    # st.write("**Tran Thong Nhat** - QE170005")
    # st.write("**Le Huy Hoan** - QE170006")
    # st.write("**Dang Thi Le Chi** - QE170156")    
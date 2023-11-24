import time
import streamlit as st
import base64

from _1_3_visualization import draw_distribution, draw_wordcloud

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def log_in():
    global login_form, email, password, submit, file_feedback, username, choice_sentiment,choice_topic
    st.title("Data Visualization")
    # Create an empty container
    login_form = st.empty()
    success = st.empty()
    
    # Insert a form in the container
    with login_form.form('login'):
        st.markdown("#### Enter your credentials")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
    try:
        with open('account.txt','r',encoding='utf-8') as file_account:
            pass    
    except:
        with open('account.txt','w+',encoding='utf-8') as file_account:
            file_account.write(f"huumxqe170004@fpt.edu.vn maixuanhuu123 Mai_Xuan_Huu\n")
            file_account.write(f"nhatttqe170005@fpt.edu.vn tranthongnhat123 Tran_Thong_Nhat\n")
            file_account.write(f"hoanlhqe170006@fpt.edu.vn lehuyhoan123 Le_Huy_Hoan\n")
            file_account.write(f"thangtqqe170008@fpt.edu.vn truongquyetthang123 Truong_Quyet_Thang\n")
            file_account.write(f"lamhtqe170013@fpt.edu.vn hoangthanhlam123 Hoang_Thanh_Lam\n")
            file_account.write(f"baohtqe170017@fpt.edu.vn hotonbao123 Ho_Ton_Bao\n")
            file_account.write(f"dongdgqe170049@fpt.edu.vn diepgiadong123 Diep_Gia_Dong\n")
            file_account.write(f"datttqe170053@fpt.edu.vn trantiendat123 Tran_Tien_Dat\n")
            file_account.write(f"anndqe170066@fpt.edu.vn ngodinhan123 Ngo_Dinh_An\n")
            file_account.write(f"tienttqe170069@fpt.edu.vn truongtrongtien123 Truong_Trong_Tien\n")
            file_account.write(f"hungpqqe170078@fpt.edu.vn phamquochung123 Pham_Quoc_Hung\n")
            file_account.write(f"trungpqqe170085@fpt.edu.vn phanquoctrung123 Phan_Quoc_Trung\n")
            file_account.write(f"trungtpqe170090@fpt.edu.vn truongphuoctrung123 Truong_Phuoc_Trung\n")
            file_account.write(f"duydtqe170105@fpt.edu.vn duongthanhduy123 Duong_Thanh_Duy\n")
            file_account.write(f"datntqe170110@fpt.edu.vn nguyenthanhdat123 Nguyen_Thanh_Dat\n")
            file_account.write(f"chidtlqe170156@fpt.edu.vn dangthilechi123 Dang_Thi_Le_Chi\n")
            file_account.write(f"kietntqe170224@fpt.edu.vn nguyentankiet123 Nguyen_Tan_Kiet\n")
            file_account.write(f"a b c\n")
    if submit:
        try:
            with open('account.txt','r',encoding='utf-8') as file_account:
                pass    
        except:
            with open('account.txt','w+',encoding='utf-8') as file_account:
                file_account.write(f"huumxqe170004@fpt.edu.vn maixuanhuu123 Mai_Xuan_Huu\n")
                file_account.write(f"nhatttqe170005@fpt.edu.vn tranthongnhat123 Tran_Thong_Nhat\n")
                file_account.write(f"hoanlhqe170006@fpt.edu.vn lehuyhoan123 Le_Huy_Hoan\n")
                file_account.write(f"thangtqqe170008@fpt.edu.vn truongquyetthang123 Truong_Quyet_Thang\n")
                file_account.write(f"lamhtqe170013@fpt.edu.vn hoangthanhlam123 Hoang_Thanh_Lam\n")
                file_account.write(f"baohtqe170017@fpt.edu.vn hotonbao123 Ho_Ton_Bao\n")
                file_account.write(f"dongdgqe170049@fpt.edu.vn diepgiadong123 Diep_Gia_Dong\n")
                file_account.write(f"datttqe170053@fpt.edu.vn trantiendat123 Tran_Tien_Dat\n")
                file_account.write(f"anndqe170066@fpt.edu.vn ngodinhan123 Ngo_Dinh_An\n")
                file_account.write(f"tienttqe170069@fpt.edu.vn truongtrongtien123 Truong_Trong_Tien\n")
                file_account.write(f"hungpqqe170078@fpt.edu.vn phamquochung123 Pham_Quoc_Hung\n")
                file_account.write(f"trungpqqe170085@fpt.edu.vn phanquoctrung123 Phan_Quoc_Trung\n")
                file_account.write(f"trungtpqe170090@fpt.edu.vn truongphuoctrung123 Truong_Phuoc_Trung\n")
                file_account.write(f"duydtqe170105@fpt.edu.vn duongthanhduy123 Duong_Thanh_Duy\n")
                file_account.write(f"datntqe170110@fpt.edu.vn nguyenthanhdat123 Nguyen_Thanh_Dat\n")
                file_account.write(f"chidtlqe170156@fpt.edu.vn dangthilechi123 Dang_Thi_Le_Chi\n")
                file_account.write(f"kietntqe170224@fpt.edu.vn nguyentankiet123 Nguyen_Tan_Kiet\n")
                file_account.write(f"a b c\n")
        finally:
            with open('account.txt','r',encoding='utf-8') as file_account:
                list_account = []
                for i in file_account:
                    list_account.append(i.split())
        
        if len(email.split()) == 0 and len(password) == 0:
            st.error("Please Input **Email** and **Password** !")
        elif len(email.split()) == 0:
            st.error("Please Input **Email** !")
        elif len(password) == 0:
            st.error("Please Input **Password** !")
        else:
            correct_email = False
            correct_password = False
            for i in list_account:
                if email == i[0]:
                    correct_email = True
                if password == i[1]:
                    correct_password = True
                if correct_email == True and correct_password == True:                   
                    username = i[2]
                    username = username.replace('_',' ')

                    login_form.empty()
                    success.success("Login Successful.")
                    with st.spinner("Loading..."):
                        time.sleep(2)
                    success.empty()
                    st.subheader(f"Hello {username}")
                    # View data (code thêm)
                    choice_sentiment = st.selectbox('Choose Sentiment', [None,'Positive','Neutral','Negative'],on_change=refresh_logged_page)
                    choice_topic = st.selectbox('Choose Topic', [None,'Lecturer','Training Program','Facility','Others'],on_change=refresh_logged_page)
                    view = st.button("View Data",on_click=view_data)
                    with open('feedback.txt',encoding='utf-8') as file_feedback:
                        st.download_button(
                            label = "Download File Feedback",
                            data = file_feedback,
                            file_name = "feedback.txt",on_click=refresh_logged_page,
                        )
                    st.button("Log out", on_click=log_out)
                    break
                else:
                    if i == list_account[-1]:
                        st.error("Login Failed.")       

def log_out():
    set_background('background.png')
    menu = ["Introduction","Visualization","Feedback","About"]
    choice = st.sidebar.selectbox("Menu",menu)  
    log_in()
    st.stop()

def refresh_logged_page():
    set_background('background.png')
    menu = ["Introduction","Visualization","Feedback","About"]
    choice = st.sidebar.selectbox("Menu",menu)
    st.title("Data Visualization")
    st.subheader(f"Hello {username}")
    # View data (code thêm)
    choice_sentiment = st.selectbox('Choose Sentiment', [None,'Positive','Neutral','Negative',],on_change=refresh_logged_page)
    choice_topic = st.selectbox('Choose Topic', [None,'Lecturer','Training Program','Facility','Others'],on_change=refresh_logged_page)
    view = st.button("View Data",on_click=view_data)
    with open('feedback.txt',encoding='utf-8') as file_feedback:
        st.download_button(
            label = "Download File Feedback",
            data = file_feedback,
            file_name = "feedback.txt",on_click=refresh_logged_page,
        )
    st.button("Log out", on_click=log_out)
    st.stop()

def view_data():
    set_background('background.png')
    menu = ["Introduction","Visualization","Feedback","About"]
    choice = st.sidebar.selectbox("Menu",menu)
    st.title("Data Visualization")
    st.subheader(f"Hello {username}")
    # View data (code thêm)
    choice_sentiment = st.selectbox('Choose Sentiment', [None,'Positive','Neutral','Negative',],on_change=refresh_logged_page)
    choice_topic = st.selectbox('Choose Topic', [None,'Lecturer','Training Program','Facility','Others'],on_change=refresh_logged_page)
    if choice_sentiment == None and choice_topic == None:
        pass
    else:
        histogram = draw_distribution(sentiment = choice_sentiment, topic = choice_topic)
        st.pyplot(histogram)
    wordcloud = draw_wordcloud(sentiment = choice_sentiment, topic = choice_topic)
    wordcloud.to_file('wordcloud.png')
    st.image('wordcloud.png')

    view = st.button("View Data",on_click=view_data)
    with open('feedback.txt',encoding='utf-8') as file_feedback:
        st.download_button(
            label = "Download File Feedback",
            data = file_feedback,
            file_name = "feedback.txt",on_click=refresh_logged_page,
        )
    st.button("Log out", on_click=log_out)
    st.stop()
from utils.Chatbot_web_text_video import *
import streamlit as st


def main():
    st.set_page_config("Chat PDF")
    st.header("Chat with PDF, WEB and Video using Gemini💁")

    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")
    with st.sidebar:
        web_url = st.text_input("Insert web link:")
        if st.button("Submit"):
            with st.spinner("Processing..."):
                raw_text = fetch_data_from_web(web_url)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")
    with st.sidebar:
        uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])
        if st.button("Submit_Button"):
            if uploaded_file is not None:
                with st.spinner("Processing..."):
                    # Save the uploaded video file to a temporary location
                    video_file_path = save_uploaded_video(uploaded_file)
                    
                    # Pass the video file path to the processing function
                    # Assuming video_to_text() is a placeholder for your actual processing function
                    video_file = video_to_text(video_file_path)
                    text_chunks = get_text_chunks(video_file)
                    get_vector_store(text_chunks)
                    st.success("Done")



if __name__ == "__main__":
    main()
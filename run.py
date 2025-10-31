import streamlit as st
from streamlit_option_menu import option_menu
import time  
import os 
from textsummarizer.pipeline.prediction import PredictionPipeline

with st.sidebar:
    page = option_menu("📘 Text Summarization", 
                       ["Home", "Train Model", "Predict", "Settings"], 
                       icons=["house", "cpu", "file-text", "gear"],  
                       default_index=0)

if page == "Home":
    
    st.title("📘 Text Summarization App")
    st.markdown("""
    Welcome to the **Text Summarization App**! This tool helps you generate concise summaries from lengthy paragraphs, making it easy to extract key insights. Here’s what you can do:
    - **Train** a custom summarization model.
    - **Generate summaries** for any large block of text.
    - **Adjust settings** to customize your experience.

    **Get started** by selecting an option from the sidebar. Enjoy streamlined summarization!
    """)

elif page == "Train Model":
    st.header("Train the Model")
    st.write("Click the button below to start training the model.")
    

    if st.button("Start Training"):
        progress_bar = st.progress(0)
        status_text = st.empty()  
        
        try:
            # Simulate a training process by updating the progress bar
            for percent_complete in range(0, 101, 10):
                time.sleep(0.3)  # Simulate time taken for each step
                progress_bar.progress(percent_complete)
                status_text.text(f"Training progress: {percent_complete}%")
            
            # Execute the actual training script
            os.system("python main.py")
            status_text.text("Training complete!")
            st.success("Training successful!")
            
        except Exception as e:
            status_text.text("An error occurred!")
            st.error(f"Error during training: {e}")
        finally:
            progress_bar.empty()  # Remove the progress bar after completion

# Section 2: Predict
elif page == "Predict":
    st.header("Predict Text Summarization")
    st.write("Enter the text you want to summarize and click **Summarize Text**.")
    
    # Text input area for prediction
    user_input = st.text_area("Enter text to summarize:", height=100)
    
    # Button to perform prediction
    if st.button("Summarize Text"):
        if user_input.strip():
            # Initialize the progress bar for prediction
            progress_bar = st.progress(0)
            status_text = st.empty()  # For status messages
            
            try:
                # Slower progress bar for summarizing text
                for percent_complete in range(0, 101, 10):  # Increased steps for smoother progression
                    time.sleep(0.5)  # Slower time interval for each step
                    progress_bar.progress(percent_complete)
                    status_text.text(f"Summarizing text... {percent_complete}%")
                
                # Generate the summary using PredictionPipeline
                predictor = PredictionPipeline()
                summary = predictor.predict(user_input)
                
                st.success("Summarization successful!")
                st.write("**Summary:**")
                st.write(summary)
                
            except Exception as e:
                status_text.text("An error occurred!")
                st.error(f"Error during summarization: {e}")
            finally:
                progress_bar.empty()  # Remove the progress bar after completion
        else:
            st.warning("Please enter some text to summarize.")

# Section 3: Settings
elif page == "Settings":
    st.header("Settings")
    st.write("This section can be used to adjust settings or version of model.")
    st.write("Model Information: Text Summarization v1.0")
    # st.write("Developer: TEAM RAR")
    # st.write("Description: This app summarizes text using a custom-trained NLP model.")

# Footer with copyright and developer info, fixed at the bottom
st.markdown("""
    <style>
    /* Fixed footer at the bottom of the page */
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f9f9f9;
        text-align: center;
        padding: 10px 0;
        font-size: 12px;
        color: #333;
        box-shadow: 0px -1px 5px rgba(0, 0, 0, 0.1);
        z-index: 1000;
    }
    .footer a {
        text-decoration: none;
        margin: 0 15px;
        display: inline-block;
    }
    .footer-icons img {
        width: 20px;
        height: 20px;
        transition: transform 0.3s ease, opacity 0.3s ease;
        opacity: 0.8;
    }
    .footer-icons img:hover {
        transform: scale(1.2);
        opacity: 1;
    }
    </style>

    <div class="footer">
        &copy; 2024 Text Summarization App. All Rights Reserved.<br>
        Developed by <strong>Rudra Prasad Panda</strong><br>
        <div class="footer-icons">
            <a href="https://github.com/RudraPrasadPanda1234" target="_blank">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub">
            </a>
            <a href="https://www.linkedin.com/in/rudraprpanda/" target="_blank">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" alt="LinkedIn">
            </a>
        </div>
    </div>
""", unsafe_allow_html=True)

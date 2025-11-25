import streamlit as st
import google.generativeai as genai
from PIL import Image
import time
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables (for local development)
load_dotenv()

# Get API key from multiple sources
def get_api_key():
    # Try Streamlit secrets first (for deployment)
    try:
        if hasattr(st, 'secrets') and 'GOOGLE_API_KEY' in st.secrets:
            return st.secrets['GOOGLE_API_KEY']
    except:
        pass

    # Try environment variables (for local development)
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key:
        return api_key

    # Return None if not found
    return None

# Configure API key
API_KEY = get_api_key()
if not API_KEY:
    st.error("❌ API Key not found! Please set GOOGLE_API_KEY in:")
    st.markdown("""
    - **Local development**: Set in `.env` file or `.streamlit/secrets.toml`
    - **Streamlit Cloud**: Set in Secrets section of your app settings
    """)
    st.stop()
genai.configure(api_key=API_KEY)

# Page configuration
st.set_page_config(
    page_title="AI Image Analyzer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced styling
def load_css():
    st.markdown("""
    <style>
        .main-header {
            text-align: center;
            padding: 2rem 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px;
            margin-bottom: 2rem;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }

        .main-header h1 {
            color: white;
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            font-weight: 700;
        }

        .main-header p {
            color: rgba(255,255,255,0.9);
            font-size: 1.1rem;
            margin: 0;
        }

        .upload-container {
            background: white;
            padding: 0.1rem;
            border-radius: 15px;
            border: 2px dashed #e0e0e0;
            transition: all 0.3s ease;
            margin-bottom: 2rem;
        }

        .upload-container:hover {
            border-color: #667eea;
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.1);
        }

        .prompt-container {
            background: #f8f9fa;
            padding: 0.1rem;
            border-radius: 15px;
            border: 2px dashed #e0e0e0;
            margin-bottom: 1.5rem;
        }

        .response-container {
            background: white;
            padding: 0.2rem;
            border-radius: 15px;
            border-left: 5px solid #667eea;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .sidebar-content {
            padding: 1rem;
        }

        .feature-card {
            background: white;
            padding: 0.1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }

        .success-message {
            background: #d4edda;
            color: #155724;
            padding: 1rem;
            border-radius: 10px;
            border-left: 4px solid #28a745;
        }

        .error-message {
            background: #f8d7da;
            color: #721c24;
            padding: 1rem;
            border-radius: 10px;
            border-left: 4px solid #dc3545;
        }

        /* Hide default Streamlit elements */
        .stDeployButton {
            display: none;
        }

        /* Custom button styling */
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 0.75rem 2rem;
            font-weight: 600;
            border-radius: 10px;
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
        }

        /* Custom input styling */
        .stTextInput > div > div > input {
            border-radius: 10px;
            border: 2px solid #e0e0e0;
            padding: 0.75rem;
        }

        .stTextInput > div > div > input:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
    </style>
    """, unsafe_allow_html=True)

# Load custom CSS
load_css()

# Header with gradient background
st.markdown("""
<div class="main-header">
    <h1>🤖 AI Image Analyzer</h1>
    <p>Upload an image and ask anything about it using advanced AI technology</p>
</div>
""", unsafe_allow_html=True)

# Sidebar for additional features
with st.sidebar:
    # st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)

    # App Information
    st.markdown('<h3>📊 App Information</h3>', unsafe_allow_html=True)
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown("**Model:** Google Gemini 2.5 Flash")
    st.markdown("**Version:** 1.0.0")
    st.markdown(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}")
    st.markdown('</div>', unsafe_allow_html=True)

    # Features
    st.markdown('<h3>✨ Features</h3>', unsafe_allow_html=True)
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown("🖼️ **Multiple Formats** - JPG, JPEG, PNG")
    st.markdown("🔍 **Detailed Analysis** - Comprehensive image understanding")
    st.markdown("⚡ **Fast Response** - Quick AI processing")
    st.markdown("🎯 **Accurate Results** - High-quality analysis")
    st.markdown('</div>', unsafe_allow_html=True)

    # Tips
    st.markdown('<h3>💡 Tips</h3>', unsafe_allow_html=True)
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown("• Use clear, high-quality images")
    st.markdown("• Ask specific questions")
    st.markdown("• Try different types of queries")
    st.markdown("• Be patient while processing")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    # Upload Section
    st.markdown('<div class="upload-container">', unsafe_allow_html=True)
    st.markdown("### 📤 Upload Image")

    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=["jpg", "jpeg", "png"],
        help="Supported formats: JPG, JPEG, PNG (Max 10MB)"
    )

    if uploaded_file is not None:
        # Display uploaded image with caption
        image = Image.open(uploaded_file)

        # Get image info
        img_size = f"{image.width}x{image.height}"
        img_format = image.format

        st.success(f"✅ Image uploaded successfully!")
        st.info(f"**Details:** {img_format} • {img_size} pixels")

        # Display image
        st.image(
            image,
            caption=f"📸 Uploaded Image ({img_format}, {img_size})",
            use_container_width=True,
            output_format="auto"
        )

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # Prompt Section
    st.markdown('<div class="prompt-container">', unsafe_allow_html=True)
    st.markdown("### 💬 Ask About Your Image")

    # Sample prompts
    sample_prompts = [
        "What's in this image?",
        "Describe the main objects",
        "What colors are dominant?",
        "Is there text in this image?",
        "What's the mood of this picture?"
    ]

    selected_prompt = st.selectbox(
        "💡 Quick prompts (optional):",
        ["Custom question..."] + sample_prompts
    )

    if selected_prompt != "Custom question...":
        prompt = st.text_input(
            "Your question:",
            value=selected_prompt,
            help="Ask anything about the uploaded image"
        )
    else:
        prompt = st.text_input(
            "Your question:",
            placeholder="e.g., What objects do you see in this image?",
            help="Ask anything about the uploaded image"
        )

    st.markdown('</div>', unsafe_allow_html=True)

    # Analysis Button
    if st.button("🔍 Analyze Image", use_container_width=True, type="primary"):
        if uploaded_file is None:
            st.markdown("""
            <div class="error-message">
                <strong>❌ Please upload an image first!</strong><br>
                You need to upload an image before analyzing it.
            </div>
            """, unsafe_allow_html=True)
        elif not prompt.strip():
            st.markdown("""
            <div class="error-message">
                <strong>❌ Please enter a question!</strong><br>
                You need to ask something about the image.
            </div>
            """, unsafe_allow_html=True)
        else:
            # Show processing indicator
            with st.spinner('🤖 AI is analyzing your image...'):
                try:
                    # Generate content
                    model = genai.GenerativeModel("gemini-2.5-flash")
                    response = model.generate_content([prompt, image])

                    # Show success message
                    st.markdown("""
                    <div class="success-message">
                        <strong>✅ Analysis Complete!</strong><br>
                        Here's what the AI found:
                    </div>
                    """, unsafe_allow_html=True)

                    # Display response
                    st.markdown('<div class="response-container">', unsafe_allow_html=True)
                    st.markdown("### 📋 AI Response")
                    st.markdown(response.text)
                    st.markdown('</div>', unsafe_allow_html=True)

                except Exception as e:
                    st.markdown(f"""
                    <div class="error-message">
                        <strong>❌ Error occurred!</strong><br>
                        {str(e)}
                    </div>
                    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
# st.markdown(
#     """
#     <div style='text-align: center; color: #666; padding: 1rem;'>
#         Made with ❤️ using Streamlit • Powered by Google Gemini AI
#     </div>
#     """,
#     unsafe_allow_html=True
# )

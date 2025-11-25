# Tech Stack Documentation

## 📋 Project Overview

**AI Image Analyzer** is a web-based application that allows users to upload images and ask questions about them using advanced AI technology powered by Google's Gemini AI model.

## 🛠️ Technology Stack

### **Backend & Core Framework**
- **Python 3.12.4** - Primary programming language
- **Streamlit** - Web framework for building ML/AI applications
  - Version: Latest
  - Used for creating the web interface, handling file uploads, and managing user interactions

### **AI/ML Integration**
- **Google Generative AI (Gemini 2.5 Flash)** - AI model for image analysis
  - Model: `gemini-2.5-flash`
  - Purpose: Advanced image understanding and natural language processing
  - Library: `google-generativeai`

### **Image Processing**
- **Pillow (PIL)** - Python Imaging Library
  - Used for image manipulation and processing
  - Handles image format validation and metadata extraction

### **Environment Management**
- **python-dotenv** - Environment variable management
  - Used for managing API keys and configuration

### **Frontend & Styling**
- **HTML5 & CSS3** - Custom styling via Streamlit's HTML components
  - Responsive design with gradients and animations
  - Custom CSS classes for UI components

### **Development Tools**
- **LocalTunnel** (Node.js package) - Local development tunneling
  - Version: ^2.0.2
  - Used for exposing local development server to public URLs

## 📦 Dependencies

### Python Dependencies (requirements.txt)
```
google-generativeai
streamlit
python-dotenv
```

### Node.js Dependencies (package.json)
```json
{
  "dependencies": {
    "localtunnel": "^2.0.2"
  }
}
```

## 🏗️ Architecture Overview

### **Application Structure**
```
Image_Analyzer/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── package.json          # Node.js dependencies (LocalTunnel)
├── package-lock.json     # NPM lock file
└── node_modules/         # Node.js packages
```

### **Key Components**

1. **Main Application (app.py:1-306)**
   - Streamlit web interface
   - Image upload and processing
   - AI model integration
   - Custom CSS styling

2. **API Integration (app.py:8-9, 271-272)**
   - Google Generative AI configuration
   - Model initialization and content generation

3. **User Interface (app.py:20-139, 142-305)**
   - Responsive design with custom CSS
   - Two-column layout for upload and prompt
   - Interactive sidebar with app information

## 🔧 Configuration

### **API Configuration**
- Google Gemini AI API key configured in `app.py:8`
- Model: `gemini-2.5-flash`
- API endpoints handled by `google-generativeai` library

### **Streamlit Configuration**
- Page title: "AI Image Analyzer"
- Layout: Wide
- Initial sidebar state: Expanded
- Custom emoji favicon: 🤖

## 🚀 Deployment & Development

### **Local Development**
1. **Python Environment Setup**
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```

2. **LocalTunnel Setup** (for public URL)
   ```bash
   npm install
   npx localtunnel --port 8501
   ```

### **Supported Image Formats**
- JPG/JPEG
- PNG
- Maximum file size: 10MB

## 🎨 Frontend Features

### **Custom Styling**
- Gradient backgrounds and buttons
- Animated hover effects
- Responsive card layouts
- Custom error and success messages
- Professional color scheme (purple/blue gradient theme)

### **UI Components**
- File upload area with drag-and-drop support
- Interactive prompt input with sample questions
- Real-time image preview with metadata display
- Sidebar with app information and tips

## 🔒 Security Considerations

### **API Key Management**
- API key is currently hardcoded in the main application file
- **Recommendation**: Move to environment variables using python-dotenv

### **File Upload Security**
- File type validation (JPG, JPEG, PNG only)
- File size limitation (10MB)
- **Note**: No server-side file persistence (images processed in memory)

## 📊 Performance Characteristics

### **Processing Flow**
1. Image upload and validation
2. Image processing with Pillow
3. API request to Google Gemini
4. Response formatting and display

### **Optimizations**
- In-memory image processing (no disk I/O)
- Responsive UI with loading indicators
- Efficient error handling and user feedback

## 🔄 API Integration Details

### **Google Gemini AI**
- **Model**: Gemini 2.5 Flash
- **Capabilities**: Image analysis, natural language understanding
- **Usage**: Multi-modal input (image + text prompt)
- **Response**: Text-based analysis and insights

## 🛡️ Error Handling

### **Application-Level Errors**
- File upload validation
- API key authentication
- Network connectivity issues
- Model response errors

### **User Experience**
- Custom error messages with CSS styling
- Success confirmations for completed operations
- Loading states during processing

---

## 📝 Development Notes

- **Python Version**: 3.12.4
- **Primary Language**: Python with JavaScript for LocalTunnel
- **Design Pattern**: Streamlit's functional approach
- **State Management**: Streamlit's built-in session state
- **Styling Approach**: Inline CSS with custom classes

## 🔮 Future Enhancements

### **Potential Improvements**
1. Environment variable management for API keys
2. Image persistence and history
3. Batch image processing
4. Additional AI model options
5. User authentication and session management
6. Docker containerization for deployment
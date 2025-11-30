"""
Gradio UI for History-Data Collaboration System
Run this file to launch the interactive web interface
"""

import gradio as gr
from src.collaboration_system import HistoryDataCollaborationSystem
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Verify API key is set
if not os.getenv('OPENAI_API_KEY'):
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please set it in your .env file")

# Initialize the system
print("🚀 Initializing History-Data Collaboration System...")
system = HistoryDataCollaborationSystem()
print("✅ System ready!\n")


def process_query(query: str, timeout: int) -> str:
    """
    Process user query through the multi-agent system
    
    Args:
        query: User's historical question
        timeout: Maximum time in seconds for processing
        
    Returns:
        str: Final answer from the collaboration system
    """
    if not query or query.strip() == "":
        return "⚠️ Please enter a question or task."
    
    try:
        result = system.process_query(query, timeout=timeout)
        return result
    except Exception as e:
        return f"❌ Error: {str(e)}\n\nPlease try again or reduce the timeout value."


# Create the Gradio interface
demo = gr.Interface(
    fn=process_query,
    inputs=[
        gr.Textbox(
            label="Your Historical Question", 
            placeholder="Ask anything... (e.g., 'How did urbanization rates in Europe compare to those in North America during the Industrial Revolution?')",
            lines=4
        ),
        gr.Slider(
            minimum=30, 
            maximum=300, 
            value=120, 
            step=10,
            label="Timeout (seconds)",
            info="Maximum time for agents to collaborate"
        )
    ],
    outputs=gr.Textbox(
        label="Answer", 
        lines=20
    ),
    title="🏛️ History-Data Collaboration System",
    description="""
    **Ask complex historical questions and watch AI agents collaborate to find answers!**
    
    ### How it works:
    1. 🏛️ **History Research Agent** gathers historical context and qualitative insights
    2. 📊 **Data Analysis Agent** identifies data needs and analyzes quantitative patterns
    3. 🎯 **Synthesis** combines all insights into a comprehensive answer
    
    *Built with LangChain and OpenAI for exploring multi-agent AI systems*
    """,
    examples=[
        [
            "How did urbanization rates in Europe compare to those in North America during the Industrial Revolution, and what were the main factors influencing these trends?",
            120
        ],
        [
            "What were the economic impacts of the Silk Road on medieval trade patterns, and how did it influence cultural exchange?",
            120
        ],
        [
            "Analyze the correlation between technological advancement and societal change during the Renaissance period.",
            100
        ],
        [
            "Compare the population growth rates of major civilizations during the Bronze Age and identify key factors.",
            120
        ]
    ],
   
    article="""
    ---
    
    ### 🎓 About This Project
    
    This multi-agent system demonstrates advanced AI collaboration patterns:
    - **State Management**: Agents share context across workflow steps
    - **Specialized Roles**: Each agent has unique expertise and skills
    - **Workflow Orchestration**: Structured 5-step process for comprehensive answers
    - **Error Handling**: Robust timeout and exception management
    
    **Technologies:** LangChain, OpenAI GPT-4, Python, Gradio
    
    **GitHub:** [View Source Code](#)
    
    ---
    *Built for exploring Adobe's Gen AI Platform capabilities*
    """
)


if __name__ == "__main__":
    # Launch the app
    print("="*80)
    print("🌐 Launching History-Data Collaboration System UI...")
    print("="*80)
    print("📝 Make sure your .env file has OPENAI_API_KEY set")
    print("🌐 The app will open in your browser automatically")
    print("🔗 A public shareable link will be generated")
    print("="*80)
    print()
    
    demo.launch(
        share=True,          # Creates public link you can share
        server_name="0.0.0.0",  # Allow external connections
        server_port=7860,    # Default Gradio port
        show_error=True      # Show detailed errors in UI
    )
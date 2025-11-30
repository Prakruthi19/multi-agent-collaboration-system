# History-Data Collaboration System

> An intelligent multi-agent system that combines historical research with data analysis to answer complex questions about historical trends and patterns.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)](https://github.com/langchain-ai/langchain)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Overview

This project implements a sophisticated multi-agent collaboration system where specialized AI agents work together to answer complex historical questions that require both qualitative historical knowledge and quantitative data analysis. It demonstrates advanced agent orchestration and workflow management.

### Key Features

- **Multi-agent orchestration** with specialized roles (Historical Research & Data Analysis)
- **State management** for context sharing between agents
- **LangChain integration** for LLM orchestration
- **Timeout handling** for long-running processes
- **Error recovery** and robust exception handling
- **Jupyter notebook** for interactive exploration

## 🏗️ Architecture

```
User Question
      ↓
Historical Research Agent
   (Gathers context & qualitative insights)
      ↓
Data Analysis Agent
   (Processes quantitative patterns)
      ↓
Synthesis & Final Answer
```

### How It Works

1. **Historical Research Agent**: Gathers historical context, events, and qualitative information
2. **Data Analysis Agent**: Analyzes quantitative data, trends, and statistical patterns
3. **Collaboration**: Agents share context and insights to generate comprehensive answers
4. **Synthesis**: Combined insights are synthesized into a coherent final answer

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Git (for cloning)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/history-data-collaboration.git
cd history-data-collaboration

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your-openai-api-key-here
```

### Running the System

#### Option 1: Jupyter Notebook (Recommended)

```bash
jupyter notebook multi_agent_notebook.ipynb
```

Run the cells to see the agents collaborate in real-time!

#### Option 2: Python Script

```python
from src.collaboration_system import HistoryDataCollaborationSystem

# Initialize the system
system = HistoryDataCollaborationSystem()

# Ask a complex question
question = """
How did urbanization rates in Europe compare to those in 
North America during the Industrial Revolution, and what 
were the main factors influencing these trends?
"""

# Get the answer
result = system.solve(question)
print(result)
```

## 📊 Example Questions

Try asking questions like:

- "How did urbanization rates in Europe compare to those in North America during the Industrial Revolution, and what were the main factors influencing these trends?"
- "What were the economic impacts of the Silk Road on medieval trade patterns?"
- "Compare the population growth rates of major civilizations during the Bronze Age"
- "Analyze the correlation between technological advancement and societal change during the Renaissance"

## 🧠 Technical Implementation

### Agent Architecture

The system uses a base `Agent` class with specialized implementations:

```python
class HistoryDataCollaborationSystem:
    def __init__(self):
        self.history_agent = HistoryResearchAgent()
        self.data_agent = DataAnalysisAgent()
    
    def solve(self, question: str) -> str:
        # Historical research phase
        historical_context = self.history_agent.process(question)
        
        # Data analysis phase
        data_insights = self.data_agent.process(question, historical_context)
        
        # Synthesis
        return self.synthesize(historical_context, data_insights)
```

### Key Components

- **Base Agent Class**: Defines common agent interface and LLM interaction
- **HistoryResearchAgent**: Specializes in historical context and qualitative analysis
- **DataAnalysisAgent**: Specializes in quantitative data and statistical patterns
- **Collaboration System**: Orchestrates agent interaction and context management

### State Management

Agents maintain and share context through a structured state object:

```python
{
    "question": "Original user question",
    "historical_context": "Research findings",
    "data_insights": "Analytical findings",
    "confidence": 0.85
}
```

## 📁 Project Structure

```
history-data-collaboration/
├── multi_agent_notebook.ipynb    # Main Jupyter notebook
├── src/
│   ├── __init__.py
│   └── collaboration_system.py   # Core system classes
├── .env                          # API keys (not in repo)
├── .env.example                  # Template for .env
├── requirements.txt              # Python dependencies
├── README.md                     # This file
└── LICENSE                       # MIT License
```

## 🛠️ Technologies Used

- **LangChain**: Agent framework and LLM orchestration
- **OpenAI GPT-4**: Language model for reasoning and analysis
- **Python 3.8+**: Core programming language
- **python-dotenv**: Environment variable management
- **Jupyter**: Interactive development and demonstration

## 📝 Usage Examples

### Basic Usage

```python
from src.collaboration_system import HistoryDataCollaborationSystem

system = HistoryDataCollaborationSystem()
result = system.solve("Your historical question here")
print(result)
```

### With Custom Configuration

```python
system = HistoryDataCollaborationSystem(
    model_name="gpt-4",
    temperature=0.7,
    timeout=120
)

result = system.solve(
    question="Complex historical question",
    include_sources=True
)
```

## 🎓 Key Learning Concepts

This project demonstrates:

- **Multi-agent collaboration patterns**
- **State management across agent boundaries**
- **Context propagation and enrichment**
- **LLM orchestration with LangChain**
- **Error handling in async workflows**
- **Timeout management for long-running processes**

## 🔧 Configuration Options

Customize system behavior in your code:

```python
CONFIG = {
    "model": "gpt-4",           # LLM model to use
    "temperature": 0.7,         # Response creativity
    "timeout": 120,             # Max processing time (seconds)
    "max_retries": 3,           # Retry failed operations
    "verbose": True             # Print debug information
}
```

## 📈 Future Enhancements

- [ ] Add vector database integration for historical facts
- [ ] Implement agent memory for conversation continuity
- [ ] Add more specialized agents (Geographic, Economic, etc.)
- [ ] Include data visualization for quantitative insights
- [ ] Add source citation and fact verification
- [ ] Implement LangGraph for more complex workflows

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Built with ❤️ for exploring multi-agent AI systems**

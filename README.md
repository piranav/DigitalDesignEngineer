# GPT Digital Design Engineer

This is a GitHub repository for the `app.py` code, which implements a GPT-based digital design engineer. It uses the LangChain library to interact with OpenAI's language model and perform various natural language processing tasks.

## Prerequisites

Before running the code, make sure you have the following:

- Python 3.6 or higher installed
- OpenAI API key (available from OpenAI) assigned to the `OPENAI_API_KEY` environment variable

## Installation

To run the code, follow these steps:

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/your-username/your-repo.git
   ```

2. Change into the repository's directory:

   ```shell
   cd your-repo
   ```

3. Install the required dependencies using pip:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the `app.py` script:

```shell
streamlit run app.py
```

Once the application is running, you can interact with it through a web-based interface provided by Streamlit. The interface allows you to input prompts and receive responses from the GPT-based digital design engineer.

## Code Overview

The `app.py` script starts by importing the necessary dependencies and modules. It sets the OpenAI API key by assigning it to the `OPENAI_API_KEY` environment variable.

The script then creates an instance of the OpenAI LLM (Language Learning Model) and initializes an OpenAIEmbeddings object. It also creates a PyPDFLoader object and loads a PDF document named "DDGuide.pdf." The pages of the document are split and stored in a Chroma vector database named "designdesigner."

A VectorStoreInfo object is created, providing information about the vector store, such as its name and description. This object is used to create a VectorStoreToolkit, which converts the document store into a LangChain toolkit.

The script sets up the Streamlit application by using `st.title` to display a title and `st.text_input` to create a text input box for user prompts. When a prompt is entered, the agent_executor runs the prompt through the GPT model, and the response is displayed using `st.write`.

Additionally, the script includes an expandable section labelled "Document Similarity Search." It performs a similarity search on the vector store based on the user prompt and displays the most relevant page's content.

## License

This project is licensed under the [MIT License](LICENSE).

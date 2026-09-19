\# GFC Financial Analysis Chatbot



A rule-based financial analysis chatbot prototype developed as part of the BCG GenAI Consulting job simulation.



\## Project Overview



This project demonstrates how structured financial data can be integrated into a conversational web application.



The chatbot provides financial analysis for three companies:



\* Microsoft

\* Tesla

\* Apple



The dataset covers fiscal years:



\* 2023

\* 2024

\* 2025



The underlying dataset stores financial figures in USD millions. The chatbot converts these values to USD billions when presenting results to users.



\## Project Objectives



The chatbot was designed to demonstrate:



\* Financial data retrieval

\* Financial metric identification

\* Year-over-year growth analysis

\* Financial comparisons

\* Highest-revenue identification

\* Conversation state management

\* Rule-based query handling

\* Error handling

\* Web-based interaction through Flask



\## Features



\### Financial Data Retrieval



The chatbot can answer questions about:



\* Total Revenue

\* Net Income

\* Total Assets

\* Total Liabilities

\* Operating Cash Flow



\### Growth Analysis



The chatbot can calculate year-over-year percentage changes for supported financial metrics.



It can also calculate the overall percentage change between 2023 and 2025.



\### Financial Comparisons



Users can compare financial metrics between two years.



Example:



> Compare Apple's revenue in 2024 and 2025.



The chatbot returns the values for both years and calculates the absolute and percentage change.



\### Highest Revenue



The chatbot can identify the company with the highest revenue for a selected year.



Example:



> What was the highest revenue in 2025?



\### Conversation State



The chatbot uses Flask session management to remember relevant information from previous questions, including:



\* Company

\* Financial metric

\* Year



This allows contextual follow-up questions.



Example:



> What was Microsoft's revenue in 2025?



Followed by:



> What about 2024?



The chatbot uses the previous company and metric context to answer the follow-up question.



\### Error Handling



Unsupported or unrelated questions receive a clear response explaining the financial topics supported by the chatbot.



The chatbot does not attempt to answer questions outside its defined financial-analysis scope.



\## Technology Stack



\* Python

\* Flask

\* Pandas

\* HTML

\* CSS

\* JavaScript

\* CSV



\## Architecture



The application follows a simple web-based architecture:



```text

User

&#x20; |

&#x20; v

Web Interface

(index.html + CSS + JavaScript)

&#x20; |

&#x20; v

Flask Application

(app.py)

&#x20; |

&#x20; +----------------------+

&#x20; |                      |

&#x20; v                      v

Query Processing       Session State

&#x20; |

&#x20; v

Pandas Data Retrieval

&#x20; |

&#x20; v

financial\_data.csv

&#x20; |

&#x20; v

Financial Response

&#x20; |

&#x20; v

Web Interface

```



\## How It Works



The chatbot follows a rule-based approach.



1\. The user submits a financial question through the web interface.

2\. JavaScript sends the question to the Flask `/chat` endpoint.

3\. Flask receives and validates the request.

4\. The application identifies the company, year, and financial metric.

5\. Pandas retrieves the relevant financial data from the CSV file.

6\. The application performs calculations when required.

7\. A natural-language response is generated.

8\. The response is returned to the browser as JSON.

9\. Flask session management preserves relevant conversation context for follow-up questions.



\## Supported Companies



The chatbot currently supports:



\* Microsoft

\* Tesla

\* Apple



\## Supported Financial Metrics



The chatbot currently supports:



\* Total Revenue

\* Net Income

\* Total Assets

\* Total Liabilities

\* Operating Cash Flow



\## Supported Years



The dataset currently covers:



\* 2023

\* 2024

\* 2025



\## Example Queries



Users can ask questions such as:



```text

What was Microsoft's revenue in 2025?



What was Tesla's net income in 2024?



How did Microsoft's net income change?



Compare Apple's revenue in 2024 and 2025.



What was the highest revenue in 2025?



What about 2024?

```



\## Example Responses



\### Direct Financial Lookup



Question:



```text

What was Tesla's net income in 2024?

```



Example response:



```text

Tesla's net income in 2024 was $7.15 billion.

```



\### Financial Comparison



Question:



```text

Compare Apple's revenue in 2024 and 2025.

```



Example response:



```text

Apple's revenue changed from $391.04 billion in 2024 to $416.16 billion in 2025. That represents an increase of $25.13 billion, or 6.43%.

```



\### Growth Analysis



Question:



```text

How did Microsoft's net income change?

```



Example response:



```text

From 2023 to 2025, Microsoft's net income increased by 40.73%. It changed from $72.36 billion to $101.83 billion.

```



\### Conversation Context



Initial question:



```text

What was Microsoft's revenue in 2025?

```



Follow-up:



```text

What about 2024?

```



The chatbot remembers Microsoft and revenue from the previous question and returns the 2024 value.



\## Project Structure



```text

GFC\_Financial\_Chatbot/

â”‚

â”œâ”€â”€ app.py

â”œâ”€â”€ financial\_data.csv

â”œâ”€â”€ requirements.txt

â”œâ”€â”€ README.md

â”‚

â”œâ”€â”€ templates/

â”‚   â””â”€â”€ index.html

â”‚

â””â”€â”€ static/

&#x20;   â””â”€â”€ style.css

```



\## Files and Their Purpose



\### app.py



Contains the Flask application, chatbot logic, financial-data retrieval functions, growth calculations, session management, and API routes.



\### financial\_data.csv



Contains the structured financial dataset for Microsoft, Tesla, and Apple covering 2023-2025.



\### index.html



Provides the chatbot web interface.



\### style.css



Provides the visual styling for the chatbot interface.



\### requirements.txt



Lists the Python packages required to run the application.



\### README.md



Provides project documentation, setup instructions, architecture information, testing information, limitations, and future improvements.



\## Data



The financial dataset contains manually structured financial information for Microsoft, Tesla, and Apple covering fiscal years 2023-2025.



The dataset includes:



\* Total Revenue

\* Net Income

\* Total Assets

\* Total Liabilities

\* Operating Cash Flow



The financial data was prepared during Task 1 of the BCG GenAI Consulting simulation.



For consistency across companies, Apple's reported total net sales are represented as Total Revenue in the dataset.



\## Data Units



The original dataset stores financial figures in USD millions.



For example:



```text

Microsoft 2025 Revenue

281,724 USD million

```



The chatbot converts these values into billions when presenting responses:



```text

$281.72 billion

```



\## Rule-Based Query Processing



The chatbot uses predefined rules rather than a large language model.



The application identifies:



\* Company names

\* Years

\* Financial metrics

\* Growth-related questions

\* Comparison requests

\* Highest-revenue requests

\* Follow-up questions



This approach provides predictable responses for the supported financial queries.



\## Running the Application



\### 1. Open the project directory



Open PowerShell and navigate to the chatbot directory:



```powershell

cd "C:\\Users\\ADMIN\\BCG\_GFC\_Financial\_Analysis\\GFC\_Financial\_Chatbot"

```



\### 2. Install the required packages



Run:



```powershell

pip install -r requirements.txt

```



\### 3. Start the Flask application



Run:



```powershell

python app.py

```



The Flask development server should start locally.



\### 4. Open the chatbot



Open a web browser and go to:



```text

http://127.0.0.1:5000

```



\### 5. Stop the application



Return to the PowerShell window running Flask and press:



```text

Ctrl + C

```



\## Requirements



The application requires:



\* Python 3.x

\* Flask 3.1.3

\* Pandas 3.0.5

\* A modern web browser



The required Python packages are listed in `requirements.txt`.



\## Testing



The chatbot was tested using several categories of financial queries.



\### Test 1: Direct Financial Lookup



Question:



```text

What was Tesla's net income in 2024?

```



Expected result:



```text

Tesla's net income in 2024 was $7.15 billion.

```



\### Test 2: Financial Comparison



Question:



```text

Compare Apple's revenue in 2024 and 2025.

```



Expected result includes:



```text

$391.04 billion

$416.16 billion

6.43% increase

```



\### Test 3: Growth Analysis



Question:



```text

How did Microsoft's net income change?

```



Expected result includes:



```text

40.73%

```



representing the change between 2023 and 2025.



\### Test 4: Highest Revenue



Question:



```text

What was the highest revenue in 2025?

```



Expected result identifies Apple and reports approximately:



```text

$416.16 billion

```



\### Test 5: Conversation State



Initial question:



```text

What was Microsoft's revenue in 2025?

```



Follow-up:



```text

What about 2024?

```



The chatbot successfully uses the previous company and metric context to answer the follow-up question.



\### Test 6: Error Handling



Example unsupported question:



```text

What is the weather today?

```



The chatbot responds by explaining that it is a financial analysis assistant and lists the supported financial topics.



\## Limitations



This is an educational prototype designed around a controlled financial dataset.



The chatbot:



\* Does not provide live financial-market data.

\* Does not connect to external financial APIs.

\* Supports only Microsoft, Tesla, and Apple.

\* Supports only the 2023-2025 dataset.

\* Uses predefined rule-based intent detection.

\* Does not use a large language model.

\* May not understand financial questions outside its predefined patterns.

\* Should not be used as a substitute for professional financial advice.



\## Future Improvements



Potential improvements include:



\* Integration with live financial-data APIs.

\* Natural-language processing using a large language model.

\* Retrieval-augmented generation (RAG).

\* More advanced intent detection.

\* Financial charts and interactive visualizations.

\* Additional companies and financial metrics.

\* More sophisticated conversation memory.

\* Automated financial-data updates.

\* Authentication and user management.

\* Cloud deployment.

\* Automated testing.

\* Improved security and production configuration.



\## Educational Context



This project was developed as part of a simulated consulting project focused on applying data analysis and GenAI-related concepts to a financial-services use case.



The chatbot demonstrates how structured financial data and rule-based conversational logic can be combined into a simple web application.



\## Disclaimer



This project is an educational prototype created for a simulated consulting exercise.



The information provided by the chatbot is based on the included dataset and is intended for demonstration and learning purposes only.



The chatbot does not provide financial, investment, tax, accounting, or legal advice.





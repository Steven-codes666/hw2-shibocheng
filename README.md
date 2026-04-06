# GenAI Workflow Assignment

## Business Workflow
Customer Support Response Generation

## User
Customer service agents in e-commerce platforms who handle customer inquiries and complaints.

## Input
Customer messages, including:
- complaints (e.g., delayed orders)
- refund requests
- product issues
- general inquiries

## Output
A clear, professional, and empathetic response that:
- acknowledges the user's issue
- maintains a polite and calm tone
- provides a solution or next step
- avoids making unsupported assumptions

## Value
- Improves response efficiency by reducing manual writing time
- Ensures consistent tone and service quality
- Enhances customer satisfaction through better communication
- Supports scalable customer service operations

## Notes
This workflow is inspired by real-world AI customer service systems and focuses on improving both efficiency and user experience.


## How to Run

1. Install the required package:
```bash
pip install google-genai
````

2. Set your Gemini API key:

Mac / Linux:

```bash
export GEMINI_API_KEY="your_api_key_here"
```

Windows (PowerShell):

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

3. Run the application:

```bash
python app.py
```

4. Enter a customer message when prompted.

The program will:

* generate a customer support response
* print the result in the terminal
* save the output to `output.txt`

# GenAI Workflow Report

## Business Use Case

This project explores a customer support response generation workflow for e-commerce platforms. The primary user is a customer service agent who handles large volumes of written communication, including complaints, refund requests, delivery issues, and general inquiries.

The system takes a customer message as input and generates a professional, empathetic, and structured response. The goal is not to replace human agents, but to assist them in drafting consistent and high-quality replies.

This workflow is valuable because customer support is highly repetitive but requires careful tone control and clarity. Automating the first draft of responses can improve efficiency, reduce response time, and ensure consistent service quality across different agents.

---

## Model Choice

This project uses the Gemini API (gemini-2.5-flash) via Google AI Studio.

The model was selected for three main reasons:
- it provides fast response times suitable for interactive workflows  
- it is cost-efficient for repeated evaluation and iteration  
- it performs reliably on general natural language generation tasks  

I did not conduct a full multi-model benchmark. However, during early testing, I observed that simpler or smaller prompts often led to inconsistent tone and weaker handling of ambiguous inputs. This motivated the focus on prompt design rather than model switching.

---

## Baseline vs Final Design

The baseline system used a minimal prompt:

"You are a customer support agent. Write a polite response."

This version produced responses that were generally polite but lacked structure and consistency. Based on testing with the evaluation set:

- In the *angry customer case*, the model sometimes failed to show sufficient empathy  
- In the *missing information case*, it often made assumptions instead of asking clarifying questions  
- In the *customs-related case*, it occasionally generated unsupported explanations  

These issues indicated that the baseline prompt did not provide enough constraints or guidance.

After two iterations, the final system prompt introduced:

- explicit tone requirements (polite, empathetic, clear, professional)  
- structured behavioral rules (acknowledge the issue, provide next steps)  
- safety constraints (avoid unsupported claims, ask clarifying questions, escalate when necessary)  

The improvements were observable across the same evaluation set:

- In emotional scenarios, responses became more empathetic and aligned with expected customer service tone  
- In edge cases, the model began asking for missing information instead of guessing  
- In high-risk scenarios, the model avoided hallucination and responded more cautiously  

This demonstrates that prompt iteration, even without changing the model, significantly improved both response quality and reliability.

---

## Limitations and Failure Cases

Despite these improvements, the prototype still has important limitations.

First, the system has no access to real customer data, such as order status or logistics information. As a result, it cannot provide factual resolutions and must rely on generic guidance.

Second, in ambiguous cases, the model may produce responses that are overly cautious or still somewhat generic. While this reduces risk, it may also reduce usefulness in certain situations.

Third, the model does not have true situational awareness. For example, in policy-related or logistics-related questions (such as customs issues), it may still require human intervention to ensure correctness.

These limitations indicate that the system is not suitable for fully autonomous deployment.

---

## Deployment Recommendation

I would recommend deploying this workflow only under a human-in-the-loop framework.

The system is well-suited for:
- generating first-draft responses  
- assisting agents in handling repetitive inquiries  
- improving consistency in tone and communication quality  

However, it should not be used as a fully automated customer-facing system. Human review is necessary for:
- complex or high-risk cases  
- policy or logistics-related issues  
- situations requiring access to real backend data  

With proper oversight, this workflow can significantly improve efficiency while maintaining service quality. Without such controls, there is a risk of incorrect or misleading responses.

---

## Conclusion

This project demonstrates that prompt engineering plays a critical role in shaping LLM behavior in real-world workflows. Even with a fixed model, structured prompt iteration can meaningfully improve performance, reliability, and safety.

However, the results also highlight that LLM-based systems still require careful integration with human processes. The most effective use of this workflow is as an assistive tool rather than a fully automated solution.

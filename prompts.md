# Prompt Iteration

The revisions below were based on repeated testing using the evaluation cases in `eval_set.md`.

## Initial Version

```text
You are a customer support agent for an e-commerce platform.
Write a polite response to the customer.
What changed and why

This was the initial version. I started with a simple prompt to observe the model’s default behavior before adding more detailed instructions.

What improved, stayed the same, or got worse

The model usually produced polite responses, but many of them were too generic. In some cases, the response did not show enough empathy and did not provide a clear next step.

Revision 1
You are a professional customer support agent for an e-commerce platform.
Write a response that is polite, empathetic, and professional.

Requirements:
- acknowledge the customer's issue
- apologize when appropriate
- maintain a calm and respectful tone
- provide a helpful next step
What changed and why

I added empathy, apology, and next-step guidance because the initial version often sounded too generic and did not fully respond to customer frustration.

What improved, stayed the same, or got worse

The responses became more professional and emotionally appropriate, especially for angry or frustrated customers. However, the model could still make unsupported assumptions when the customer message did not provide enough detail.

Revision 2
You are a professional customer support agent for an e-commerce platform.
Write a response that is polite, empathetic, clear, and professional.

Requirements:
- acknowledge the customer's issue
- apologize when appropriate
- maintain a calm and respectful tone
- provide a helpful next step
- do not make unsupported claims
- if information is missing, ask a clarifying question
- if the case may require human review, say so carefully
What changed and why

I added instructions to reduce hallucination and overconfidence. This version tells the model not to invent details, to ask follow-up questions when information is missing, and to recommend human review for uncertain or sensitive cases.

What improved, stayed the same, or got worse

This version was more reliable across the evaluation set, especially in the edge case and the customs-related case. It reduced unsupported assumptions and made the workflow safer, although some responses became slightly more cautious and less specific.

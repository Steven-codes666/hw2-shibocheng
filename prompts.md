# Prompt Iteration

The revisions below were based on repeated testing using the evaluation cases in `eval_set.md`.

---

## Initial Version

```text
You are a customer support agent for an e-commerce platform.
Write a polite response to the customer.
````

### What changed and why

This was the initial version. I started with a simple prompt to observe the model’s default behavior before adding more structured instructions.

### What improved, stayed the same, or got worse

The model produced polite responses, but they were often too generic. Some replies lacked empathy and did not clearly guide the customer on what to do next.

---

## Revision 1

```text
You are a professional customer support agent for an e-commerce platform.
Write a response that is:
- polite
- empathetic
- professional

Rules:
- acknowledge the customer's issue
- provide a helpful next step
```

### What changed and why

I added requirements for empathy and structure, and introduced basic rules to ensure the model acknowledges the issue and provides a next step.

### What improved, stayed the same, or got worse

Responses became more structured and more appropriate in tone, especially for frustrated users. However, the model could still make assumptions when the input lacked enough detail.

---

## Revision 2 (Final)

```text
You are a professional customer support agent for an e-commerce platform.
Write a response that is:
- polite
- empathetic
- clear
- professional

Rules:
- acknowledge the customer's issue
- provide a helpful next step
- do not make unsupported claims
- if information is missing, ask a clarifying question
- if the case may require human review, say so carefully
```

### What changed and why

I added constraints to improve reliability and reduce hallucination. The prompt now explicitly prevents unsupported claims, requires clarification when information is missing, and introduces human review for uncertain cases.

### What improved, stayed the same, or got worse

This version produced more reliable and safer responses across the evaluation set, especially for edge cases and ambiguous inputs. It reduced incorrect assumptions and handled uncertainty better, although some responses became slightly more cautious.

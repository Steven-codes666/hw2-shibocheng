# Evaluation Set

This evaluation set is designed for the workflow: Customer Support Response Generation.

The purpose of this evaluation set is to test whether the model can produce professional, empathetic, and reliable customer support replies across several realistic business scenarios.

## Case 1: Normal Case
**Input:**  
My order was supposed to arrive two days ago, but I still have not received it. Can you check what is happening?

**What a good output should do:**  
- Apologize politely  
- Acknowledge the delivery delay  
- Avoid making unsupported claims  
- Suggest a clear next step, such as checking the order status or asking for order details  

## Case 2: Angry Customer
**Input:**  
This is ridiculous. I paid extra for fast shipping and my package is still not here. I want a refund right now.

**What a good output should do:**  
- Show empathy and remain calm  
- Acknowledge the customer’s frustration  
- Avoid sounding defensive or dismissive  
- Explain the refund or support process clearly  
- Offer a professional next step  

## Case 3: Edge Case (Missing Information)
**Input:**  
Where is my order?

**What a good output should do:**  
- Reply politely  
- Avoid guessing  
- Ask for the missing details needed to help, such as the order number or purchase email  
- Keep the response short and useful  

## Case 4: Hallucination Risk / Human Review Case
**Input:**  
Why was my package stopped at customs? Did your company fail to prepare the paperwork?

**What a good output should do:**  
- Avoid making legal, customs, or logistics assumptions without evidence  
- Avoid blaming the company, customs, or the customer  
- State that customs delays may happen for different reasons  
- Suggest checking shipment details or escalating to a human agent  
- Show caution because this case may require human review  

## Case 5: Ambiguous Product Issue
**Input:**  
It does not work.

**What a good output should do:**  
- Acknowledge the issue politely  
- Avoid assuming what the exact problem is  
- Ask clarifying questions  
- Guide the customer toward the next step in a structured way  

## Notes
This is a small but stable evaluation set for repeated testing. It includes:
- one normal case
- one edge case
- one hallucination-risk or human-review case
- two additional realistic customer support scenarios

These test cases will be reused later to compare the baseline prompt and the improved prompt versions.

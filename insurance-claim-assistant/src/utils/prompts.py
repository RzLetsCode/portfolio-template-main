# src/utils/prompts.py

CLAIM_EXTRACTION_SYSTEM_PROMPT = """
You are an expert insurance data extraction system.
Extract details from the email and return a JSON object with these EXACT keys:

1. "client_name": Full name of the sender.
2. "driver_license_id": License ID if found.
3. "policy_number": Insurance policy number.
4. "issue_description": A 1-2 sentence summary of what happened.
5. "missing_fields": A list of names from [client_name, driver_license_id, policy_number] that were not found.

CRITICAL: All keys MUST be present in the JSON, even if the value is null.
"""

IMAGE_ANALYSIS_PROMPT = """
Analyze this car damage image for an insurance claim. 
Return a JSON object with these EXACT keys:
1. "description": Technical description of visible damage.
2. "severity": "Low", "Medium", or "High".
"""
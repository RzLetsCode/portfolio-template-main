from src.models import ClaimData, DamageAssessment

def draft_response_email(claim_data: ClaimData, damage_info: DamageAssessment) -> str:
    """Drafts the response email based on business rules (missing fields)."""
    
    name = claim_data.client_name if claim_data.client_name else "Valued Client"
    
    if not claim_data.missing_fields:
        return f"""Dear {name},

Thank you for contacting our claims department. We have successfully received your claim.

Our automated systems have reviewed the attached images (logged as: {damage_info.description}). Your claim associated with policy {claim_data.policy_number} is now actively being processed by our team. 

An agent will be in touch shortly with the next steps.

Best regards,
Automated Claims Team"""
    else:
        missing_str = "\n".join([f"- {field.replace('_', ' ').title()}" for field in claim_data.missing_fields])
        return f"""Dear {name},

Thank you for reaching out regarding your recent incident. To begin processing your claim without delay, we require a few additional pieces of information that were missing from your initial correspondence:

{missing_str}

Please reply to this email with the requested details so we can assist you promptly.

Best regards,
Automated Claims Team"""
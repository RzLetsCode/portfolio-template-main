import json
from openai import AzureOpenAI
from src.config import settings
from src.models import ClaimData, DamageAssessment
from src.utils.prompts import CLAIM_EXTRACTION_SYSTEM_PROMPT, IMAGE_ANALYSIS_PROMPT

class AzureAIEngine:
    def __init__(self, api_key: str = None, endpoint: str = None):
        # Allow UI to override .env for demo purposes
        self.client = AzureOpenAI(
            api_key=api_key or settings.AZURE_OPENAI_API_KEY,
            api_version=settings.AZURE_OPENAI_API_VERSION,
            azure_endpoint=endpoint or settings.AZURE_OPENAI_ENDPOINT
        )
        self.deployment_name = settings.AZURE_OPENAI_DEPLOYMENT_NAME

    def extract_text_data(self, email_text: str) -> ClaimData:
        try:
            # SAFETY INJECTION: Appending "Return JSON" to ensure API compliance
            system_instructions = f"{CLAIM_EXTRACTION_SYSTEM_PROMPT}\n\nReturn the output in JSON format."
            
            response = self.client.chat.completions.create(
                model=self.deployment_name,
                messages=[
                    {"role": "system", "content": system_instructions},
                    {"role": "user", "content": f"Email Content:\n{email_text}"}
                ],
                response_format={"type": "json_object"} 
            )
            data = json.loads(response.choices[0].message.content)
            return ClaimData(**data)
        except Exception as e:
            # Raising more descriptive errors is better for enterprise debugging
            raise Exception(f"LLM Extraction Failure: {str(e)}")

    def analyze_image(self, base64_image: str) -> DamageAssessment:
        try:
            # SAFETY INJECTION: Explicit JSON instruction for multimodal calls
            user_instruction = f"{IMAGE_ANALYSIS_PROMPT}\n\nReturn the assessment in JSON format."

            response = self.client.chat.completions.create(
                model=self.deployment_name,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": user_instruction},
                            {
                                "type": "image_url", 
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}",
                                    "detail": "high" # Ensures high-res analysis for car damage
                                }
                            }
                        ]
                    }
                ],
                response_format={"type": "json_object"},
                max_tokens=500 # Slightly increased for detailed descriptions
            )
            data = json.loads(response.choices[0].message.content)
            return DamageAssessment(**data)
        except Exception as e:
            raise Exception(f"LLM Vision Failure: {str(e)}")
from google import genai

def generate_learning_path(goal: str, api_key: str) -> str:
    client = genai.Client(api_key="AQ.Ab8RN6JKNSZkqcIB_qTqHbsnPG3o8ScaON7ivzty-NGy45jucA")

    prompt = f"""
Create a detailed personalized learning roadmap.

Goal:
{goal}

Include:

1. Day-by-day breakdown
2. Topics to cover each day
3. Recommended resources
4. Milestones
5. Motivation tips

Format using markdown headings and bullet points.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
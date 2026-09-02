from openai import OpenAI

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

response = client.chat.completions.create(
    model="z-ai/glm-5.2",
    messages=[{"role": "user", "content": "Say hello"}]
)

print(response.choices[0].message.content)
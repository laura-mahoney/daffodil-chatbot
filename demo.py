# from openai import OpenAI
#
# response = OpenAI.images.generate(
#     prompt="Duck with glasses",
#     n=1,
#     size="1024x1024"
# )
#
# print(response)

from openai import OpenAI

openai = OpenAI(
    api_key="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"
)

user_input = "Cat laying with dog"

response = openai.images.generate(
    prompt=user_input,
    n=1,
    size="512x512"
)

image_url = response.data[0].url
print(image_url)

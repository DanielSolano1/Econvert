import together
import base64
together.api_key = "2b084736a3bc9b659361dead521119d5bc00d5f8f3ad5c71e40f9ca5c14d25fd"

# prompt = "Story"
# # generate response
# for token in together.Complete.create_streaming(prompt=prompt):
#     print(token, end="", flush=True)
# print("\n")
# # print(response)


# generate image 
# response = together.Image.create(prompt="Space robots")

# save the first image
# image = response["output"]["choices"][0]
# with open("spacerobots.png", "wb") as f:
#     f.write(base64.b64decode(image["image_base64"]))
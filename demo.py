from biasModel import BiasModel

# Create an instance of the BiasModel class
model = BiasModel()

# Test the classify_string function
model.classify_string("This is a test comment.")

# Accept new input
# while True:
#     user_input = input("Enter comment to test its toxicity (or 'quit' to exit): ")
#     if user_input.lower() == 'quit':
#         break
#     else:
#         model.classify_string(user_input)

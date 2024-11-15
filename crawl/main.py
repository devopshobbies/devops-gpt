from content_parser import WebContentParser

url = "https://developer.hashicorp.com/terraform/intro"

# Create an instance of the parser
parser = WebContentParser(url)

# Get parsed data
data = parser.get_data()


print(data)
# # Print the results
# for idx, section in enumerate(data, start=1):
#     print(f"Section {idx}:")
#     for key, value in section.items():
#         print(f"  {key}: {value}")
#     print("-" * 40)

